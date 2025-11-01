# def squar(n):
#     for i in range(n+1):
#         yield i*i

# iterate using for loop

# for i in squar(4):
#     print(i)
    
# iterate using next 
# sq = squar(3)
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))


# practial use -> reading learge file 

# def read_learge_file(file_path):
#     with open(file_path,'r') as file:
#         for line in file:
#             yield line
# for i in read_learge_file('advance_pyrthon/learge.txt'):
#     print(i.strip())


