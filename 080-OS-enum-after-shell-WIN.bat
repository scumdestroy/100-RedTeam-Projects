@echo off


REM Run systeminfo command to gather system information
systeminfo > C:\temp\system_info_windows.txt

REM Check for plaintext credentials in files
echo Searching for plaintext credentials...
findstr /S /M /I /C:"password" "C:\*.txt" "C:\*.log"

REM Check for vulnerable backups of SAM and LSA files
echo Checking for vulnerable backups of SAM and LSA files...
if exist "C:\Windows\System32\config\SAM.bak" (
    echo SAM backup file found: C:\Windows\System32\config\SAM.bak
) else (
    echo SAM backup file not found
)
if exist "C:\Windows\System32\config\SYSTEM.bak" (
    echo SYSTEM backup file found: C:\Windows\System32\config\SYSTEM.bak
) else (
    echo SYSTEM backup file not found
)

REM Check antivirus status
echo Antivirus Status:
wmic /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get displayName, productState

REM Check firewall status
echo Firewall Status:
netsh advfirewall show allprofiles

REM Check UAC status
echo User Account Control (UAC) Status:
reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA


REM Describe current patches
echo Current Patches:
wmic qfe list brief

REM Describe services
echo Services:
wmic service get caption, name, startmode, state

REM Describe scheduled tasks
echo Scheduled Tasks:
schtasks /query /fo table

REM Describe user permissions
echo User Permissions:
whoami /all

REM Describe network configuration
echo Network Configuration:
ipconfig /all

REM Describe hosts file
echo Hosts File:
type %SystemRoot%\System32\drivers\etc\hosts

REM Describe ARP cache
echo ARP Cache:
arp -a

REM Describe WSUS settings
echo WSUS Settings:
reg query "HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate\AU"

REM Detect open ports
echo Open Ports:
netstat -ano

REM Detect interesting file permissions of binaries being executed
echo Interesting File Permissions of Executed Binaries:
icacls "%SystemRoot%\System32" /T /C /L /Q | findstr "(F)" | findstr /V /I "(N)"

REM Detect interesting file permissions of binaries run at startup
echo Interesting File Permissions of Binaries Run at Startup:
wmic startup get Caption, Command, User, Status, Location | findstr /V /I "C:\Windows\System32"

REM Check the AlwaysInstallElevated setting
echo AlwaysInstallElevated Setting:
reg query "HKCU\Software\Policies\Microsoft\Windows\Installer" /v AlwaysInstallElevated

REM Describe cached DNS entries
echo Cached DNS Entries:
ipconfig /displaydns

REM Describe mounted shares
echo Mounted Shares:
net use

REM Describe Windows Event Forwarding settings
echo Windows Event Forwarding Settings:
wevtutil get-subscriptions

REM Check LAPS installation status
echo LAPS Installation Status:
reg query "HKLM\SOFTWARE\Microsoft\LAPS" /s

pause
