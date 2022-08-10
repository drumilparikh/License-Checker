from getfile import *
from readlicense import *
from fetchlicense import *


name = input("Enter the project root directory")

list=get_file(name)
licenses_1a=fetchlicense(list,"license.txt")
properlicenses= {}
unlicensed = []
for m in licenses_1a:
    if(licenses_1a[m] == "none"):
        unlicensed.append(m)
    else:
        # print(m)
        # print(licenses_1a[m])
        properlicenses[m]=licenses_1a[m]

        pass


notlicensed=[]
improperlicenses={}
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
        improperlicenses[m]=licenses_1b[m]
        pass
    else:
        notlicensed.append(m)
print(properlicenses)
print("\n")
print("\n")
print(improperlicenses)
print("\n")
print("\n")
print(notlicensed)
