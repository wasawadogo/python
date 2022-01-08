class Vehicle:
    make_model = ""
    color = ""
    fuelType = ""
    options = []

    
    def __init__(self,make_model,color,fuelType):
        self.make_model = make_model
        self.color = color
        self.fuelType = fuelType
        self.options = []


    def getEngineSize(self):
        pass


    def getModel(self):
        return self.make_model


    def getColor(self):
        return self.color


    def getFuelType(self):
        return self.fuelType




class Car(Vehicle):
    engineSize = 0
    numberDoors = 0


    def __init__(self,make_model,color,fuelType,engineSize,numberDoors):
        Vehicle.__init__(self,make_model,color,fuelType)
        self.engineSize = engineSize
        self.numberDoors = numberDoors


    def getEngineSize(self):
        return self.engineSize


    def getNumDoors(self):
        return self.numberDoors


class Pickup(Vehicle):
    cabStyle = ""
    bedLength = 0


    def __init__(self,make_model,color,fuelType,cabStyle,bedLength):
        Vehicle.__init__(self,make_model,color,fuelType)
        self.cabStyle = cabStyle
        self.bedLength = bedLength


    def getCabStyle(self):
        return self.cabStyle


    def getBedLength(self):
        return self.bedLength





def createCar(option_list):
    makeModel = input("Enter the model of the car : ")
    color = input("Enter the color of the Car: ")
    fuelType = input("Enter the fuel type of the car: ")
    engineSize = input("Enter the engine size: ")
    numDoors = input("Enter the number of doors: ")


    obj = Car(makeModel,color,fuelType,engineSize,numDoors)


    print("Please enter the extra features one by one and type done to end")
    print("Choices are : ",option_list)
    while(True):
        choice = input()
        if(choice=="done"):
            break
        elif(choice in option_list):
            obj.options.append(choice)
        else:
            print("Enter the correct features")
    return obj



def printCar(car_object):
    for i in car_object:
        print("model : ",i.getModel())
        print("Color : ",i.getColor())
        print("Fuel Type : ",i.getFuelType())
        print("Engine Size : ",i.getEngineSize())
        print("Number of doors : ",i.getNumDoors())
        print("Some of the extra features are- ",i.options)


        print("-----------------------------------------------")



def createPickup(option_list):
    makeModel = input("Enter the model of the Pickup : ")
    color = input("Enter the color of the Pickup: ")
    fuelType = input("Enter the fuel type of the Pickup: ")
    cabStyle = input("Enter the CabStyle: ")
    bedLength = input("Enter the bedLength: ")


    obj = Pickup(makeModel,color,fuelType,cabStyle,bedLength)


    print("Please enter the extra features one by one and type done to end")
    print("Choices are : ",option_list)
    while(True):
        choice = input()
        if(choice=="done"):
            break


        elif(choice in option_list):
            obj.options.append(choice)
        else:
            print("enter the correct features ")
    return obj





def printPickup(pickup_object):
    for i in pickup_object:
        print("model : ",i.getModel())
        print("Color : ",i.getColor())
        print("Fuel Type : ",i.getFuelType())
        print("Cab Style : ",i.getCabStyle())
        print("Bed length : ",i.getBedLength())
        print("Some of the extra features are- ",i.options)


        print("------------------------------------------------")






if __name__=="__main__":
    car_object = []
    pickup_object = []
    option_list = ["power_mirrors","power_locks","remote_start","backup_camera","Bluetooth","cruise_control","Dual_Front_Airbags","Central_Locking"]
    while(True):
        print("Press 1 for Car \nPress 2 for Pickup \nPress any other number to exit")
        choice = int(input())


        if(choice == 1):
            obj = createCar(option_list)
            car_object.append(obj)
        elif(choice==2):
            obj = createPickup(option_list)
            pickup_object.append(obj)
        else:
            break




    print("The details of cars in garage is ")
    printCar(car_object)


    print("************************************************")
    print("The details of pickup in garage is : ")
    printPickup(pickup_object)