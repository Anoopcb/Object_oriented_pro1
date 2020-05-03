## Object Oriented programming

### this is just a style or way to write a code

# class, object(instance), method

l = [1, 2, 3, 4]

l.append(8)
print(l)


class Person:# make first capital letter for a class name
    def __init__(self, first_name, last_name, age):
        ##instance variables
        print("init method // constructor get called")
        self.first_name = first_name
        self.last_name = last_name

        self.age = age
p1 = Person("Anoop", "Singh", 37)
p2 = Person("Pi", "MitraSheoran", 2)
p3 = Person("Shalini", "Mitra", 39)

print(p1.first_name)
print(p2.first_name)
print(p3.first_name)


class Labtop:

    def __init__(self, brand_name, model_name, price ):
        #instance variables
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

        self.laptop_name = brand_name + " " +model_name

    def apply_discount(self, num):
        off_price = (num/100)*self.price
        return self.price - off_price




labtop1 = Labtop("hp", "aul14tx", 63000)
labtop2 = Labtop("iphone", "XR", 83000)
print(labtop1.model_name)
print(labtop1.laptop_name)
print(labtop1.apply_discount(10))
print(labtop2.apply_discount(10))




### instance methods
l1 = [1, 2, 3]
l.pop()

print(l1)
## all the functions which are defined in a class called methods of that class


class Person1:# make first capital letter for a class name
    def __init__(self, first_name, last_name, age):
        ##instance variables
        #print("init method // constructor get called")
        self.first_name = first_name
        self.last_name = last_name

        self.age = age
    def full_name(self):

        return f"{self.first_name} {self.last_name}"
    def is_above_18(self):
        return  self.age >18

p1 = Person1("Anoop", "Singh", 37)
p2 = Person1("Pi", "MitraSheoran", 2)
p3 = Person1("Shalini", "Mitra", 39)

print(p1.first_name)
print(p2.first_name)
print(p3.first_name)
print(p1.full_name())
print(p1.is_above_18())

print(p2.is_above_18())




## class variables

class Circle:
    pi = 3.14

    def __init__(self, radius):

        self.radius = radius
        #self.pi = pi## this class variable

    def calc_circumference(self):
        return 2*Circle.pi*self.radius

c = Circle(4)
c1 = Circle(5)

print(c.calc_circumference())







class Person2:# make first capital letter for a class name
    count_instance = 0


    def __init__(self, first_name, last_name, age):
        ##instance variables
        #print("init method // constructor get called")
        Person2.count_instance +=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p3 = Person2("Sandip", "Mitra", 63)
p4 = Person2("Sandip", "Mitra", 63)
print(Person2.count_instance)
