from subprocess import check_output
import subprocess

x = check_output('systeminfo', stderr=subprocess.STDOUT)

n = open('infowindows14.txt', 'wb')
n.write(x)
print("info capturada")
n.close()

