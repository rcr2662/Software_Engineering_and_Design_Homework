from asyncio import QueueEmpty


class HWSet:
    capacity = 0            #capacity of hw sets
    availability = 0        #available hw sets
    
    #This is the constructor for the class HWSet
    # initializing capacity and availability with input qty
    def __init__(self, qty):
        self.capacity = qty
        self.availability = qty

    #returns amount of available hw sets
    def get_availability(self):
        return self.availability

    #returns total capacity of hw sets
    def get_capacity(self):
        return self.capacity

    #returns how many hw sets are checked out
    def get_checkedout_qty(self):
        return self.capacity - self.availability

    #allows user to checkout qty hw sets. If qty
    #is larger than availability return error -1
    #else update availability
    def check_out(self, qty):
        if qty > self.availability:
            self.availability = 0
            return -1
        else:
            self.availability -= qty

    #allows user to check in hw sets, adding
    #qty to availability
    def check_in(self, qty):
        self.availability += qty
