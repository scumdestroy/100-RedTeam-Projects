#!/bin/bash

# List SUID binaries
echo "SUID Binaries:"
find / -perm /4000 -type f -exec ls -l {} \;

# List processes running as root
echo "Processes Running as Root:"
ps -ef | grep "^root"

# List capabilities
echo "Capabilities:"
getcap -r / 2>/dev/null

# Check for cleartext passwords in files
echo "Cleartext Passwords in Files:"
grep -Rl "password" / 2>/dev/null

# List sudo binaries
echo "Sudo Binaries:"
which sudo

# Check fstab permissions
echo "Fstab Permissions:"
ls -l /etc/fstab

# List writable folders in PATH
echo "Writable Folders in PATH:"
echo $PATH | tr ':' '\n' | xargs -I {} sh -c 'echo {}; [ -w {} ] && echo "Writable" || echo "Not writable"'

# List interesting cron jobs
echo "Interesting Cron Jobs:"
ls -l /etc/cron*

# List users with shell access
echo "Users with Shell Access:"
cut -d: -f1 /etc/passwd | while read user; do
    user_shell=$(awk -F: -v u=$user '$1 == u {print $NF}' /etc/passwd)
    if [[ -n "$user_shell" && "$user_shell" != "/usr/sbin/nologin" ]]; then
        echo "$user"
    fi
done

# List groups
echo "Groups:"
getent group
