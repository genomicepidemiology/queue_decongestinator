# queue_decongestinator

This script is made with the intention of having an easy way of cleaning up jobs stuck in the queue. It will take in the file that has all the output of the command "showq > queue_status.txt" and will print all the IDS of the jobs that satisfy the conditions for being discarded. These are hardcoded in the variables but can easily be changed.
IMPORTANT!!!!!!!!! Don't try to kill all the jobs at the same time or you might kill the server.

More detailed instructions on how to manage the queue and how to use this file can be found in the wiki: http://wiki.cge.dtu.dk:10090/x/DoHFAg
