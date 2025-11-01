    # Inheritance
# class car:
#     def __init__(self,name,window):
#         self.name = name
#         self.window = window
#         pass
#     def drive(self):
#         print(f"{self.name} car is running")
        
        
#                 # Inherit form car       
# class bmw(car):
#     def __init__(self, name, window,price):
#         super().__init__(name, window)                  #here we mainly Inherit
#         self.price = price
    
#     def pri(self):
#         print(self.price)
    


# car1 = car('bmw',4)
# bmw1 = bmw('bmw123',4,100000000) 
# bmw1.pri()
# bmw1.drive()
# car1.drive()


                    # multiple Inherit -> when a class Inherit more then one base class 

# class car:
#     def __init__(self,name,window):
#         self.name = name
#         self.window = window
#         pass
#     def drive(self):
#         print(f"{self.name} car is running")
        
        
# class car2:
#     def __init__(self,door,color):
#         self.door = door
#         self.color = color
#         pass
        
        
#                 # Inherit form car       
# class bmw(car,car2):
#     def __init__(self, name, window,door,color,price):
#         car.__init__(self,name, window)                  #here we mainly Inherit
#         car2.__init__(self,door, color)                  #here we mainly Inherit
#         self.price = price
    
#     def pri(self):
#         print(self.price)
    


# Create a class Device, inherited by Computer, which is further inherited by Laptop
# . Add methods and attributes in each level and print them from the Laptop object

# car1 = car('bmw',4)
# bmw1 = bmw('bmw123',4,4,'red',100000) 
# bmw1.pri()
# bmw1.drive()
# car1.drive()
# print(bmw1.name)
# print(bmw1.window)
# print(bmw1.door)
# print(bmw1.color)
# print(bmw1.price)


# class devise:
#     def __init__(self,ram,rom):
#         self.ram = ram
#         self.rom = rom
#         pass
    
# class computer(devise):
#     def __init__(self,ram,rom,w_no,key_no):
#         devise.__init__(self,ram,rom)
#         self.w_no = w_no
#         self.key_no = key_no
#         pass
    
# class laptop(computer):
#     def __init__(self,ram,rom,w_no,key_no,brand_name):
#         computer.__init__(self,ram,rom,w_no,key_no)
#         self.brand_name = brand_name
#         pass
    
# mac = laptop('16gb','512gb',1,1,'macbook pro')

# print(mac.__dict__)


