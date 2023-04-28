import subprocess

# MySQL credentials
host = "localhost"  
port = "3306" 
username = "username"  
password = "password"  
database = "database_name" 

backup_dir = "/path/to/backup/dir"  
backup_name = "backup.sql"  

# Build the command
command = f"mysqldump -h {host} -P {port} -u {username} -p{password} {database} > {backup_dir}/{backup_name}"

# Execute the command
subprocess.call(command, shell=True)
