#Everything in python is considered an object. Meaning everything is based off of a class, which is just a blueprint for objects
#The dir function will show all callabled methods for an object
a='string'
#print(dir(a))

#Creating a custom class
class Vehicle:
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        #Add some attributes
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        Stop the car
        :return:
        """
        return('%s braking') % self.vtype
    def drive(self):
        """
        Drive the car
        :return:
        """
        return('''I'm driving a %s %s!''') % (self.color, self.vtype)

class Car(Vehicle):
    """
    Sub classes inherit all attributes and methods from the main class
    You can overwrite them as well
    """
    def brake(self):
        """
        Override brake method
        :return:
        """
        return('The car class is braking slowly')

if __name__ == "__main__":
    car = Vehicle("blue", 5, 4, 'car')
    print(car.brake())
    print(car.drive())

    truck = Vehicle('red', 2, 4, 'truck')
    print(truck.brake())
    print(truck.drive())

    car2 = Car('yellow', 2, 4, 'car')
    print(car2.drive())
    print(car2.brake())