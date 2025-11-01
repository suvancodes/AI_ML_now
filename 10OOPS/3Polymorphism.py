        # Polymorphism
        
# base class 
# class animal:
#     # mathod
#     def speak(self):
#         return 'sound of the animal'
    
# derived class 
 
# class dog:
#     def speak(self):
#         return 'woof!'

# class cat:
#     def speak(self):
#         return 'meow!'
    
    
# # function that demonstrates Polymorphism

# def animal_speak(animal):
#     print(animal.speak())
    
# dog1=dog()
# cat1 = cat()
# print(dog1.speak())
# print(cat1.speak())

# animal_speak(dog)


# class shape:
#     def area(self):
#         print('area')
        
# class ractangle:
#     def __init__(self,height,weight):
#         self.height = height
#         self.weight = weight
#         pass
#     def area(self):
#         return f"area is : {self.height*self.weight}"
    
    
# class squre:
#     def __init__(self,side):
#         self.side = side
#         pass
#     def area(self):
#         return f"area is : {self.side **2}"

# rec = ractangle(12,10)
# sq = squre(10)

# print(rec.area())
# print(sq.area())


                    #polymorphism with abstract base classes
                    
                    
# from abc import ABC , abstractmethod                 
                 
   
# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
    
# class car(vehicle):
#     def start():
#         return 'car is started'
# class bike(vehicle):
#     def start():
#         return 'bike is started'
    
    
# car1 = car()
# bike1 = bike()

# print(car.start())
# print(bike.start())


