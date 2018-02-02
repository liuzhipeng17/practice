
import subprocess
with open('subprocess.txt','wb') as log:
    with subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE) as proc:
        log.write(proc.stdout.read())

