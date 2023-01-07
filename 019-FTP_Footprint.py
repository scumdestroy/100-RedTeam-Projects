## Note: Due to the lack of descriptions for each project in the original repo, I think that this challenge called "FTP User Footprint" was supposed to mean, a user enumeration tool.  This would've been easier and more logical than what I did here; a FTP Server Footprinting tool, but human minds do some wild things sometimes and end up in strange places.  Anyways, Thanks for reading!

import ftplib
import sys

if len(sys.argv) < 1:
    print("Usage: ftp-fingerprinter.py <SERVER_IP>")
    sys.exit()

ftp = ftplib.FTP()
ftp.connect(sys.argv[1], 21)

print("Banner accosted and smuggled...")
banner = ftp.getwelcome()

# Compare the banner to a list of known server banners
if 'SunOS 5.7' in banner:
    print('Server identified as: Solaris 7')
elif 'SunOS 4.1' in banner:
    print('Server identified as: SunOS 4.1.x')
elif 'Version 6.00LS' in banner:
    print('Server identified as: FreeBSD 4.x')
elif 'Version 6.00' in banner:
    print('Server identified as: FreeBSD 3.x')
elif 'NetBSD 1.5.x' in banner:
    print('Server identified as: NetBSD-ftpd 20010329')
elif 'Version 6.5/OpenBSD' in banner:
    print('Server identified as: OpenBSD')
elif '220 hostname FTP server ready' in banner:
    print('Server identified as: SGI IRIX 6.x')
elif 'Digital Unix Version 5.60' in banner:
    print('Server identified as: Compaq Tru64')
elif 'Version 1.1.214.6 ' in banner:
    print('Server identified as: HP-UX 11.x')    
elif 'Microsoft FTP Service (Version 4.0)' in banner:
    print('Server identified as: Windows NT 4.0')
elif 'Microsoft FTP Service (Version 5.0)' in banner:
    print('Server identified as: Windows 2000')
else:
    print('Server not found in database.\nServer banner was ' + str(banner))

ftp.quit()
