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

#===========================Customer class======================================================================================================================
class Elevator(object):
    def __init__(self,ListOfElevatorCalls:'List'):    
        '''
         Elevator receives the initial list of Customer orders(that have pressed the UP or DOWN button to call the elevator)
        '''
        self.Capacity            = 0   # to simulate the Elevetaor's decision making of 'loading' more people or not due to capcity reasons
        self.WaitingList         = []
        self.Occupants           = []
        self.OrdersQue           = []  # Destinations of Occupants (Customers that have embarked)
        self.CurrDestination     = 0
        
        self.Capacity = randint(8,12) # gets a random capacity between 8 and 12
        self.WaitingList = ListOfElevatorCalls
    #---------------------------------------------------------------------------------
    def __str__(self):
        self.__Printable = 'Elevator with maximum capacity of {} has {} customers embarked and is currently heading towards floor {}'.format(self.Capacity,len(self.Occupants),self.CurrDestination)
        return self.__Printable
    ##---------------------------------------------------------------------------------
    def embarkCustomer(self,NewCustomer:'Customer'):
        self.__CustomerHandle = NewCustomer
        self.Occupants.append(self.__CustomerHandle.Name+':'+self.__CustomerHandle)
        self.OrdersList = self.__CustomerHandle.Destination
#===============================================================================================================================================================
class Building(object):
    def __init__(self,CustomersNo:'int',MaxFloors:'int'):
        '''
          At instantiation time several internal Lists and Dictionaries will be created:
          - Customers :
          - ElevatorCalls :
        '''
        self.TopFloor      = MaxFloors
        self.ElevatorCalls = []
        self.Customers     = []

        # generate customers
        for Idx in range(0,CustomersNo):
            LocalCustomer = new Customer(Idx,self.TopFloor)
            self.Customers.append(LocalCustomer) 
        # gather requests from all Customers in the building; 
        for Elem in self.Customers
            
            Elem.Direction
            
        
        self.MyElevator = Elevator

def main():
    P = Customer('Charlie',15)
    print(P)
    listOfCalls = list()
    El = Elevator(listOfCalls)
    print(El)
    
if __name__=='__main__' :
    main()
  
