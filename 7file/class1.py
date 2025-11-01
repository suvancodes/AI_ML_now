# read file in one time

# with open('file.txt',mode='r') as file:
#     content = file.read()
#     print(content)          


# # read file in line by line 

# with open('file.txt', mode='r') as file:
#     for line in file:
#         print(line.strip())         # .strip() remove new line 

# write in a file
# it overwrite in file it is not good process

# with open('file.txt','w') as file:
#     file.write('nano is chutya')

# good process 

# with open('file.txt','a',) as file:
#     file.write('tanmay is bokachoda')

# write in a file line by line

# line = ['1st line\n','2nd line\n','3rd line\n']
# with open('file.txt','w') as file:
#     file.writelines(line)


# copy a content form a file to other

# with open('file.txt','r') as file:
#     con = file.read()
    
# with open('example.txt','w') as w_file:
#     w_file.write(con)

        # reading and writing
        
# with open('file/example.txt', 'w+') as file:

#     file.write('hello world i am 1st\n')
#     file.write('hey i am subho , i am 2nd\n')
#             # to read the file move the cursor to the first line 
#     file.seek(0)
#     read = file.read()
#     print(read)