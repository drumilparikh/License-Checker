from getfile import get_file
from readlicense import readlicense
from fetchlicense import fetchlicense

# NAME = input("Enter the project root directory")
NAME="/home/drumil/Downloads/travelwebsite"
filelist=get_file(NAME)

licenses_1a=fetchlicense(filelist,"license")


properlicenses= {}
unlicensed = []
for m in licenses_1a:
    if(licenses_1a[m] == "none"):
        unlicensed.append(m)
    else:
        properlicenses[m]=licenses_1a[m]


notlicensed=[]
improperlicenses={}
licenses_1b=fetchlicense(filelist,"readme")

for m in licenses_1b:
    if(licenses_1b[m]=="none"):
        licenses_1b[m]=readlicense(m)

for m in licenses_1b:
    if(licenses_1b[m]!=""):
        improperlicenses[m]=licenses_1b[m]
    else:
        if m not in properlicenses:
            notlicensed.append(m)

for m in properlicenses:
    print(m.removeprefix(NAME + "/"))
    print(properlicenses[m])
print("\n")
for m in improperlicenses:
    print(m.removeprefix(NAME + "/"))
    print(improperlicenses[m])
print("\n")
for m in notlicensed:
    print(m.removeprefix(NAME + "/"))
