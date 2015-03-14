__author__ = 'Andrei'
from random import *

#===========================Customer class=====================================================================================================================
class Customer(object):
    #---------------------------------------------------------------------------------
    def __init__(self,SomeName,MaxFloors:'int'):
        '''
        Customer will receive a name at instantiation: This Could be either a number or int (index);
        MaxFloors will be passed by environment (Building); this is necessary for the customer to choose a destination within building's boundries
        '''
        self.Name        = ''
        self.Destination = 0
        self.Location    = 0
        self.Direction   = ''
        self.Name        = SomeName
        #check if passed arguments are of valid types -- useful for only when Customer is used outside of a building:
        try:
            self.Destination = randint(0,int(MaxFloors)) #Customer decides it's own destination (and not the building for him)
        except ValueError:
            self.Destination = randint(0,120)
            MaxFloors = 120
            print("Error trapped and solved: Destination of Customer can be only a valid Integer; Random values were assigned for instance (Customer {})".format(self.Name))
        try:
            self.Location = randint(0,int(MaxFloors)) #Customer decides what floor he will be waiting for the elevator
        except ValueError:            
            self.Location = randint(0,120)
            while self.Location == self.Destination:
                self.Location = randint(0,120)           
            print("Error trapped and solved: Current floor Location of Customer can be only a valid Integer; Random values were assigned for instance (Customer {})".format(self.Name))
        if self.Location < self.Destination:
            self.Direction = 'up'
        else:
            self.Direction = 'down'
    #---------------------------------------------------------------------------------
    def __str__(self):
        self.__Printable = '{} is sitting at floor {} and wants to reach floor {}, he is going {}'.format(self.Name,self.Location,self.Destination,self.Direction)
        return self.__Printable   
#===============================================================================================================================================================

#===========================Elevator class======================================================================================================================
class Elevator(object):
    def __init__(self,Building):
        '''
         Elevator needs to reside in a building. The current building is passed at instantiation
        '''
        self.Capacity            = 0   # to simulate the Elevetaor's decision making of 'loading' more people or not due to capcity reasons
        self.WaitingList         = []
        self.Occupants           = {}
        self.OrdersQueue         = []  # Destinations of Occupants (Customers that have embarked)
        self.CurrDestination     = 0
        self.ElevatorLocation    = 0
        self.CurrentFloor        = 0
        self.Building            = Building
        
        self.Capacity = randint(8,12) # gets a random capacity between 8 and 12
        self.CallsQue = self.Building.CallsQueue
    #---------------------------------------------------------------------------------
    def __str__(self):
        self.__Printable = 'Elevator with maximum capacity of {} has {} customers embarked and is currently heading towards floor {}'.format(self.Capacity,len(self.Occupants),self.CurrDestination)
        return self.__Printable
    ##---------------------------------------------------------------------------------
    def embarkNewOccupant(self,NewOccupant:'usually Customer'): #choosed emark as load wouldn't be nice on people
        '''
            Method defining how a customer or any other object can get in the lift
        '''
        self.__CustomerHandle = self.Building.Customers.pop(str(NewOccupant.Name)) #the customer becomes an occupants and is taken out of the Customers list
        self.Occupants[self.__CustomerHandle.Name] = self.__CustomerHandle    #customer gets in
        self.OrdersQueue = self.__CustomerHandle.Destination    # customer pushes panel with where he is going to
    #---------------------------------------------------------------------------------
    def debarkOccupant(self,Occupant:'usually Customer'):
        '''
        Defining how an occupant gets off the elevator:
            1.Occupants get written off the occupants list
            2.Their initial destination is erased from OrdersQueue
        '''
        self.Occupants.pop(Occupant.Name) #customer gets popped out the dictionary and thus from the building, ensuring he will not use the elevator again
        try:
            self.OrdersQueue.pop(Occupant.Destination)  #caring for situations where destination was writen off by a previous debarked
        except KeyError:
            pass
    #---------------------------------------------------------------------------------
    def movingRouting(self,Destination:'int'):
        '''
        Elevator will loop from current floor to destination, the passed param
        For each level it passes by it executes a floor routine
        '''
        if self.CurrentFloor < Destination:
            self.__MovingStep = 1
            self.Direction = 'up'
        else:
            self.__MovingStep = -1
            self.Direction = 'down'
        for floor in range(self.CurrentFloor,Destination,self.__MovingStep):
            if self.Direction == 'up':
                self.moveUp()
            else:
                self.moveDown()
            self.floorRoutine(self.CurrentFloor)
    #---------------------------------------------------------------------------------
    def floorRoutine(self,FloorNo):
        '''
        Implements the logic of stopping at a floor, opening doors so that:
            1. Occupants who where heading for this FloorNo will get of
            2. If there are customers on that level who are going in the same direction (up/down) they hop on the lift;
               Customers this become Occupants
            3. They input their desired floor destination (into the OrdersQueue)
        '''
        #check if anyone needs to get off
        for Name,Occ in self.Occupants:
            if Occ.Destination == FloorNo:
                self.debarkOccupant(Occ)    #and debark occupant
        #check if anyone needs to get on:
        for Name,Cust in self.Building.Customers.items():
            if Cust.Location == FloorNo and Cust.Direction == self.Direction:
                self.embarkNewOccupant(Cust)
    #---------------------------------------------------------------------------------
    def moveUp(self):
        '''
        Implements the 1 floor moving up for the elevator. Have put it in a method to simulate a thing that the elevator can do logic
        '''
        self.CurrentFloor += 1
    #---------------------------------------------------------------------------------
    def moveDown(self):
        '''
        Implements the 1 floor moving down.
        '''
        self.CurrentFloor -= 1

#===============================================================================================================================================================

#===========================BUILDING============================================================================================================================
class Building(object):
    def __init__(self):
        '''
          At instantiation time several internal Lists and Dictionaries will be created:
          - Customers :
          - CallsQue  :
        '''
        self.TopFloor      = 0
        self.CustomersNo   = 0
        self.CallsQueue    = []  #simulates outstanding calls made by customers for the elevator through each floor's panel
        self.Customers     = {}  #collection of all Customers in the building awaiting to be serviced by the elevator
        #get max floor and customers numbers with handling human error:
        while 1==1:
            try:
                self.TopFloor = int(input("Please set maximum floor numbers for the building: "))
            except ValueError:
                print("Error, the value needs to be numeric! ")
                continue
            else:
                break

        while 1==1:
            try:
                self.CustomersNo = int(input("Please set no of customers in the building: "))
            except ValueError:
                print("Error, the value needs to be numeric! ")
                continue
            else:
                break

        # generate customers
        for Idx in range(0,self.CustomersNo):
            LocalCustomer = Customer(Idx,self.TopFloor)
            self.Customers[str(LocalCustomer.Name)]=LocalCustomer

        #generate elevator calls ques. looping through Customers list and grabbing their Location
        for Name,Cust in self.Customers.items():
            if self.CallsQueue.count(Cust.Location) == 0:
                self.CallsQueue.append(Cust.Location)
        self.CallsQueue.sort() #sorting it so that elevator goest to the nearest call when starting the application (elevator will default as sitting on floor 0)

        # create elevator instance with passing list of
        self.MyElevator = Elevator(self)
    def startSimulator(self):
        self.MyElevator.movingRouting(6)
#=========================================================================================================
def main():
    bld = Building()
    bld.startSimulator()
    pass

if __name__=='__main__' :
    main()
  
