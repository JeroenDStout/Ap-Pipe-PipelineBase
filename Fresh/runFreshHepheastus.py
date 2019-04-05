import sys
import os
import subprocess
from subprocess import Popen, PIPE

os.chdir( "../../" )
print(os.getcwd())

hepPath = 'Code/HephaestusBase/.bin/win32/Release/Hephaestus Base.exe'
hepPathFull = '../' + hepPath;
arguments = [hepPathFull, "bootHepFresh.json", "-c:on", "-ping"]

print('Starting Hephaestus from\n ' + hepPath);

hepExists = os.path.isfile(hepPathFull)

if not hepExists:
    print('\n!! Cannot find hephaestus! Was it built?\n')
    input("Press Enter to continue...")
    sys.exit()

print('[%s]' % ', '.join(map(str, arguments)));

output,error = subprocess.Popen( Popen(arguments, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate() )