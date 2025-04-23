
class car:
    color = "red"
    model = "BMW"

    #method to display car details
    def drive():
        print("The car is driving") 

my_car = car() # create an instance of the car class
my_car.drive() # call the drive method
# print(my_car.color) # access the color attribute

# self is just like a pointer which refers to the instance of the class the method is in
# refers to the instance of the class and is used to access and methods within the class.