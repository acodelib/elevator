__author__ = 'Andrei'
from random import *

#===========================Customer class=====================================================================================================================
class Customer(object):
    def __init__(self,SomeName,MaxFloors:'int',CurrentFloor:'int'):
        '''
        Customer will receive a name at instantiation: This Could be either a number or int (index);
        MaxFloors and urrentFloor will be passed by environment (Building)
        '''
        self.Name        = ''
        self.Destination = ''
        self.Location    = ''
        self.Name        = SomeName
#check if passed arguments are of valid types -- useful for only when Customer is used outside of a building:
        try:
            self.Destination = randint(0,int(MaxFloors)) #Customer decides it's own destination (and not the building for him)
        except ValueError:
            self.Destination = randint(0,120)
            print("Error trapped and solved: Destination of Customer can be only a valid Integer; Random values were assigned for instance (Customer {})".format(self.Name))
        try:
            self.Location = int(CurrentFloor)
        except ValueError:
            self.Location = randint(0,120)
            print("Error trapped and solved: Current floor Location of Customer can be only a valid Integer; Random values were assigned for instance (Customer {})".format(self.Name))
    def __str__(self):
        self.__Printable = '{} is sitting at floor {} and wants to reach floor {}'.format(self.Name,self.Location,self.Destination)
        return self.__Printable
#===============================================================================================================================================================


class Elevator(object):
    pass

class Building(object):
    pass


if __name__=='__main__' :
    P = Customer('Charlie',15,6)
    print(P)