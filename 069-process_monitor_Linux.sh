#!/bin/sh

# This script gets a list of running processes and saves them to a text file
# then it sends this list to an e-mail
# it also checks periodically and if there are any interesting changes, it will send another e-mail
# it does all of this in the background, without opening a window

# This script is meant to be run from a cron job, like this:    
# */5 * * * * /home/username/bin/monitor_processes.sh

mkdir /tmp/.process_monitor
cd /tmp/.process_monitor

top -b -n 1 > top.txt
ps -ef > ps.txt
diff top.txt top.txt.old > top_diff.txt
diff ps.txt ps.txt.old > ps_diff.txt

# change "processfarmer@abyssmail.com" to your receiving mail address of choice
# the abyssmail.com is a temporary e-mail openly accessible through the getnada.com platform

if [ -s top_diff.txt ] || [ -s ps_diff.txt ]
then
    echo "USER: " $whoami "\n" > process_info.txt
    ip a >> process_info.txt
    echo "TOP DIFF\n\n" >> process_info.txt
    cat top_diff.txt >> process_info.txt
    echo "PS DIFF\n\n" >> process_info.txt
    cat ps_diff.txt >> process_info.txt

    cat process_info.txt | mail -s "Process Monitor" processfarmer@abyssmail.com
fi  
mv top.txt top.txt.old
mv ps.txt ps.txt.old
rm top_diff.txt ps_diff.txt
rm process_info.txt
