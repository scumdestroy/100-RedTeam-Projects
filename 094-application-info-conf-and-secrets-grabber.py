# A script that gathers a list of all installed applications on a Window's computer and saves it onto a text file
# While checking these application folders for executables, note an hardcoded passwords, API keys, usernames, e-mail addresses, IP addresses on readable, non-binary files
# Look for any files with extensions like .yaml. .toml, .conf, .cfg and many more that I discovered while researching for this script

import os
import subprocess
import re

# create a blank file for recording data

with open('applications-info.txt', 'w') as f:
    f.write('Results of application information gathering: \n\n')
    f.write('Home directory:' os. path. expanduser('~'))
    
# get a list of all installed applications on the computer

installed_applications = subprocess.check_output(['ls', '/Applications']).decode('utf-8').split('\n')

# iterate through the list of installed applications and check for any files with extensions like .yaml, .toml, .conf or .cfg

for application in installed_applications:
    if application:
        for root, dirs, files in os.walk('/Applications/' + application):
            for file in files:
                if file.endswith(('.yaml', '.toml', '.conf', '.cnf', '.config', '.ini', '.cfg', '.json', '.prof', '.pro', '.reg', '.net', '.dbc', '.rdp', '.scf', '.sql', '.ora', '.htaccess', '.global', '.ecf', '.vrf', '.vmc', '.set', '.con', '.lic', '.autoconf', '.vcl' )):
                    with open(os.path.join(root, file), 'r') as f:
                        for line in f:
                            f.write(line)
                            f.write('\n')
                            
# check for any hardcoded passwords, API keys, usernames, e-mail addresses, IP addresses on readable, non-binary files

for application in installed_applications:
    if application:
        for root, dirs, files in os.walk('/Applications/' + application):
            for file in files:
                if file.endswith('.yaml', '.toml', '.conf', '.cnf', '.config', '.ini', '.cfg', '.json', '.prof', '.pro', '.reg', '.net', '.dbc', '.rdp', '.scf', '.sql', '.ora', '.htaccess', '.global', '.ecf', '.vrf', '.vmc', '.set', '.con', '.lic', '.autoconf', '.vcl', '.txt', '.rtf', '.md', '.xml'):
                    with open(os.path.join(root, file), 'r') as f:
                        for line in f:
                            if re.search(r'password|api|key|username|email|ip', line, re.I):
                                f.write(line)
                                f.write('\n')








