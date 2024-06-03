#This script is made with the intention of having an easy way of cleaning up jobs stuck in the queue. It will take in the file that has all the 
#output of the command "showq > queue_status.txt" and will print all the IDS of the jobs that satisfy the conditions for being discarded. These
#are hardcoded in the variables but can easily be changed.
#IMPORTANT!!!!!!!!! Don't try to kill all the jobs at the same time or you might kill the server.

import re
#----------SETTINGS--------------------
#This next line opens the file that contains the output from the aforementioned "showq" command. Change as needed.
file= open('/home/people/s232520/queue_maintenance/queue_status.txt', 'r')
#state in which the process has to be to qualify for being discarded (Hold/Batchhold)
state= "BatchHold"
#the next two variables define the date before which we want to eliminate all jobs in the queue.
month= "Mar"
date = 31

#-------------------------------

lines = []
my_IDS= []

#This loop will start reading the file from the point where "blocked jobs" start.         
start_read= False  
for x in file:
    my_match= re.search("blocked", x)
    
    if my_match != None:
        start_read= True

    if start_read:
        my_line=[]
        prep= x.replace("\n", "")
        my_line.append(re.split("\t", prep))
    
        lines.append(my_line)
#We clean up the text from "blocked jobs" itself, empty lines, and the final lines of the file that do not jobIDs. 
lines= lines[3:]
lines= lines[:-5]
#print(lines)

#In this loop, the previously read lines are compared to 3 different criteria (matching_1 to 3), and we keep those that satisfy them.
for y in lines:
    my_str= y[0][0]
    matching_1= re.search(state, my_str)
    matching_2= re.search(month, my_str)
    the_date= (y[0][0][-11:-9])
    the_date= the_date.replace("\n", "")
    try:
        matching_3= int(the_date)<= date
    except:
        print("woopsie")
    date_match= (matching_2 != None and matching_3)
    if (matching_1 != None) and date_match:
        my_IDS.append(y[0][0][0:7])
        
file.close()

#print to screen with whitespaces (the IDs can be copy-pasted into the sudo canceljob #ID command directly)
str_ID= " ".join(my_IDS)
print(str_ID)
