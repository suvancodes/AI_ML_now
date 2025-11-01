# __str__ : it returns a string representation of an object.

# _init__	Constructor – initializes an object when created.
# __new__	Called before __init__; used to create and return a new instance (used rarely).
# __delattr__	Deletes an attribute from an object using del obj.attr.
# __setattr__	Automatically called when you set an attribute (obj.attr = value).
# __getattribute__	Called every time an attribute is accessed. Be careful — it overrides everything.
# __getstate__	Used with pickle to define what state to serialize.
# __reduce__, __reduce_ex__	Used to define how objects should be reduced to a serializable form (for pickling).
# __hash__	Returns the hash value for an object — used in sets and as dictionary keys.
# __eq__, __ne__, __lt__, __le__, __gt__, __ge__	Comparison operators: ==, !=, <, <=, >, >=.
# __str__	Defines the "informal" string representation (used by print() and str()).
# __repr__	Official string representation, used in debugging/logging.
# __format__	Custom string formatting using format(obj).
# __sizeof__	Returns the size of the object in bytes.
# __dir__	Defines what dir(obj) returns (list of attributes).
# __class__	Refers to the class of the object (built-in attribute).
# __dict__	A dictionary representing the object’s writable attributes.
# __doc__	The docstring of the class or method.
# __module__	Name of the module in which the class is defined.
# __weakref__	Used for garbage collection (support for weak references).
# __init_subclass__	Called when a class inherits from your class – useful for metaprogramming.
# __subclasshook__	Used by issubclass() to determine class hierarchy in ABCs.
# __static_attributes__	Not a standard dunder; likely internal/implementation-specific.
# __firstlineno__	Internal – line number of the first line in the class definition (used in debugging).

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         pass
    
#     def __str__(self):
#         return f"name : {self.name}, age: {self.age}"
    
#     def __repr__(self):
#         return f"person(name: {self.name} age: {self.age})"

# p = person('subho',18)
# print(p)
# print(repr(p))
    
# print(dir(p))



class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        pass
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        return Vector(self.x * other,self.y * other)
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    def __repr__(self):
        return f"vector({self.x},{self.y})"


v1 = Vector(2,3)
v2 = Vector(4,5)
print(v1+v2)
print(v1-v2)
print(v1*2)


