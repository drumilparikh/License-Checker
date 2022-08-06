from pathlib import Path
import os


def get_file(input):
    p=Path(input)

    unique=set()
    my_list=[]
    new_list=[]
    for file in list(p.glob('**/*.js')):
        new_list.append(str(file))

    return new_list
        # print(list(p.glob('**/*.css')))
    # for m in list(p.glob('**/*.js')):
    #     # print(m)
    #     pass
# print(get_file("/home/drumil/Downloads/travelwebsite"))
