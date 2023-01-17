import os
import random

installed_apps = []

# add `ls` output to list
for app in os.system(f'ls /usr/bin/'):
    installed_apps.append(app)

# choose 25 random apps
target_apps = random.sample(installed_apps, 25)

# slap em on the desktop
for app in target_apps:
    os.system(f'ln -s /usr/bin/{app} ~/Desktop/{app}.desktop')
