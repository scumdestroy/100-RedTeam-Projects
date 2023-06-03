@echo off

reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\kbdhid\Parameters" /v CrashOnCtrlScroll /t REG_DWORD /d 1 /f

reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\i8042prt\Parameters" /v CrashOnCtrlScroll /t REG_DWORD /d 1 /f

%SendKeys% "^{SCROLLLOCK}"
%SendKeys% "^{SCROLLLOCK}"

: if the double scroll lock + ctrl combo above doesn't work, uncomment below and use instead
: start scrolllock.exe on
: start scrolllock.exe off
: start scrolllock.exe on
: start scrolllock.exe off

@end

: the system will trigger a KeBugCheck 
: and then show a 0xE2 error then, 
: display a bugcheck with a MANUALLY_INITIATED_CRASH message. 
