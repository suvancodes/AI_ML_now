# encapsulation and abstraction. 

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age            
#         pass
    
# def get_name(person):
#         return person.name
# p = person('subho',18)
# print(get_name(p))

# example of privet variable -> we can't use this outside this class (obj an derived class) 

# class person:
#     def __init__(self,name,age,classes):
#         self.__age = age            # this is the syntax of privet variable
#         self.__name = name          #privet variable
#         pass
#         self.classes = classes      ##public variable
    

# p = person('subho',18,'3rd sam')



# example of protected variable -> we can't use it outside the same class and derived class

# class person:
#     def __init__(self,name,age,classes):
#         self._age = age            # this is the syntax of protected variable
#         self._name = name          #protected variable
#         pass
#         self.classes = classes      ##public variable
        
# class man:
#     def __init__(self,name,age,classes):
#         person.__init__(self,name,age,classes)
        
#         pass   

# p = man('subho',18,'3rd sam')
# print(p.__dict__)


# getter and setter mathod 

# class person:
#     def __init__(self,name,age,classes):
#         self.__age = age            # this is the syntax of privet variable
#         self.__name = name          #privet variable
#         self.classes = classes      ##public variable
#         pass
#     # getter mathod-> here we can get the value of privet variable
#     def get_name(self):
#         return self.__name
    
#     # setter mathod-> here we can change the value of privet variable
#     def change_name(self,name):
#         self.__name = name
#         return self.__name
    
        
    
    

# p = person('subho',18,'3rd sam')

# print(p.get_name())
# print(p.change_name('nano'))



