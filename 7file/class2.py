import os
# make a folder using os 

# os.mkdir('example')

# listing file and directories
# lst = os.listdir('.')
# print(lst)

                # joining path 
                
# dir_name = 'folder'
# file_name = 'file.txt'
# full_path = os.path.join(dir_name,file_name)            # using this we canjoin two path
# print(full_path)


# chack a file present or not 

# path = 'example.txt'
# if os.path.exists(path):
#     print('exist')
# else:
#     print('not exist')

# test 2

# path = 'example.txt'
# if os.path.isfile(path):
#     print('it is a file')
# elif os.path.isdir(path):
#     print('it is a dir')
# else:
#     print('it is nothing')


# geting absolute path 

# relative_path = 'example.txt'
# absolute_path = os.path.abspath(relative_path)
# print(absolute_path)