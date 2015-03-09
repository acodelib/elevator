__author__ = 'Andrei'
from random import *

#===========================Customer class=====================================================================================================================
class Customer(object):
    #---------------------------------------------------------------------------------
    def __init__(self,SomeName,MaxFloors:'int'):
        '''
        Customer will receive a name at instantiation: This Could be either a number or int (index);
        MaxFloors will be passed by environment (Building)
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
    def __init__(self,PendingCalls:'List'):    
        '''
         Elevator receives total floor numbers and initial pending calls from the building         
        '''
        self.Capacity            = 0
        self.PendingCalls        = []
        self.Passengers          = []
        self.DestinationsQueue   = []
#===============================================================================================================================================================
class Building(object):
    def __init__(self,CustomersNo:'int',MaxFloors:'int'):
        pass     
if __name__=='__main__' :
    P = Customer('Charlie',15)
    print(P)
