#Overview of Class
class Car:
    total_car=0
    def __init__(self,brand,model):#whenever varibales starts with __ then it is a private varibales and what can be get by declaring method and accessing it via method
        self.__brand=brand
        self.model=model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand
    
    def fullName(self):
        return f"{self.__brand} {self.model}"

    def fulltype(self):
        return "Petrol Or Diesel"
# static method in python are declared using "@staticmethod" and staticmethod does not take self as an arguments and static methods are not accesed by objects in python
    def general_descriptions():
        return "Cars are used for the transport"
 
car=Car("Tata","Safari")
print(car.fullName())


#Inheritance Concept
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    
    def fulltype(self):
        return "Electric Charge"
    
new_car=ElectricCar("Tata","Safari","55KWH")
print(new_car.fulltype())
print(car.fulltype())
print(new_car.get_brand())
print(Car.total_car)
print(Car.general_descriptions())# static method and it is only acceseed by Class not by object
#property decorator is used to make variable read only..means we cant modify that variable .only reading that variable is possible
# "isinstance" method can be used to check whether obj is a istance of a particular class or not
print(isinstance(car,Car))
print(isinstance(new_car,Car))
print(isinstance(new_car,ElectricCar))

class Engine:
    def engine_info(self):
        return "This is a method of class Engine"

class Battery:
    def battery_info(self):
        return "This is a method of class Battery"

class EngineBatteryInfo(Engine,Battery):
    pass
new_obj=EngineBatteryInfo()
print(new_obj.battery_info())
print(new_obj.engine_info())