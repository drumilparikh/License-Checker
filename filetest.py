import re



def parsing(name):
    f = open(name,'r')
    count=0
    unique=set()
    my_list=[]
    while True:
        count += 1

        # Get next line from file
        line = f.readline()
        # if line is empty
        # end of file is reached
        if not line:
                break

        all_words=line.split()
        if(all_words!=[]):
            first_word=all_words[0]


            if(first_word=="<script"):
                temp = re.findall('"([^"]*)"', line)
                my_list.append(temp)


    return my_list
    f.close()

# print(parsing("/home/drumil/Downloads/travelwebsite/"))
