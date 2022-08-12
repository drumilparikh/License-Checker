from getfile import *
from readlicense import *
from fetchlicense import *
from pprint import pprint


def fetchlicense(list,file):

    licenses={}
    for x in list:
        licenses[x]="none"
    for str in list:
            x=str
            while(x!=""):
                if(x.rfind("/") == -1):
                    break
                x=x[:(x.rfind("/"))]
                if os.path.exists(x):
                    for path in os.listdir(x):
                        if os.path.isfile(os.path.join(x, path)):
                            if path.lower()==(file + ".md") or path.lower()==(file + ".txt") :
                                # pdb.set_trace()
                                licenses[str]= readlicense(x + "/" + path)
                                x=""
                                break
                else:
                    pass
    return licenses

# print(fetchlicense(['/home/drumil/Downloads/travelwebsite/tinymce_6.1.0_dev/tinymce/modules/tinymce/tools/modules/grunt-utils.js'],"readme.md"))
