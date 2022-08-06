from getfile import *
from readlicense import *
from fetchlicense import *
import pdb

list=get_file("/home/drumil/Downloads/travelwebsite")
licenses_1a=fetchlicense(list,"license.txt")

unlicensed = []
for m in licenses_1a:
    if(licenses_1a[m] == "none"):
        unlicensed.append(m)
    else:
        # print(m)
        # print(licenses_1a[m])

        pass
licenses_1c=[]

licenses_1b=fetchlicense(unlicensed,"readme.md")
for m in licenses_1b:
    if(licenses_1b[m] is None):
        licenses_1b[m]="none"

for m in licenses_1b:
    if(licenses_1b[m]=="none"):
        licenses_1b[m]=readlicense(m)

for m in licenses_1b:
    if(licenses_1b[m]!=""):
        # print(m)
        # print(licenses_1b[m])
        pass
    else:
        licenses_1c.append(m)

for m in licenses_1c:
    print(m)
#uncomment line 34 for licenses which are mentioned in a non standard format
#uncomment line 19 for licenses which are mentioned in a standard format
