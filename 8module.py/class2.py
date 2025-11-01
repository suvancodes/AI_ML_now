                # LIBRAY IN PYTHON 

            # first 
# import array
# # arr = array.array('typecode',[intitlazer])
# arr= array.array('i',[1,2,3,4])
# print(arr)

            # 2nd 
# import math as m
# print(m.sqrt(16))
# print(m.pi)


        # 3rd 
# import random as ran
# print(ran.randint(1,10))
# print(ran.choice(['subho','ankit','athar','rokey']))


        #4th
# import os           # it is use for file and directory access
# print(os.getcwd())          # get dir of current file
# # os.mkdir('test')        # creat a folder 
# os.rmdir('test')

    
    
                    # delete a folder

# import os

# folder = 'test'

# print(os.getcwd())  # Confirm current working directory

# if os.path.exists(folder):
#     os.rmdir(folder)
#     print(f"'{folder}' directory removed.")
# else:
#     print(f"'{folder}' directory does not exist.")


# high level opretion on file

# import shutil
# shutil.copyfile('s.txt','coppy.txt')


# import json
# data = {'nsme':'subho','age':19}

# json_str = json.dumps(data)                     # convart json data to string
# print(json_str)
# print(type(json_str))
# js = json.loads(json_str)                       # convart string data to json/dict
# print(js)
# print(type(js))    



# import csv

# with open('example.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['name', 'age'])
#     writer.writerow(['subho', '19'])
# with open('example.csv',mode='r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)



# from datetime import datetime , timedelta
# now = datetime.now()
# print(now)
# yes =now - timedelta(days=1)
# print(yes)


# import time 
# print(time.time())
# time.sleep(10)
# print(time.time())


# import re
# patten = r"\d+"
# patten1 = 'there'
# text = 'there are123 apple 1211'
# match = re.search(patten,text)                  ## Searches the string for first location where the pattern matches.
# print(match)
# print(match.group())

# print(re.match(patten1,text))                          ##Searches the string for first location where the pattern matches.

# print(re.findall(patten,text))                          ##Returns all non-overlapping matches as a list of strings.

# print(re.sub(r"\d", "*", "a1b2c3"))                        ## Replaces all occurrences of the pattern with repl.

