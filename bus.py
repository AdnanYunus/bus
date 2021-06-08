"""
Create a python class called ‘Bus’ which has conductor name, total seats, seats booked, bus unique registration number, driver name as their properties. Create member functions -
Constructor which takes registration_name, conductor_name, driver_name, total_seats, seats_booked.
print_bus_details  -> This function should print ALL details of the bus.
is_seat_available -> This function should return True if a seat available, if not return False.
book_seat(no_of_seats) -> This function should book a seats if seats available, else return message “Requested no of seats not available”.

"""

class Bus:
    def __init__(self,register_number,conductor_name,driver_name,total_seats,seats_booked):
        self.register_number=register_number
        self.conductor_name=conductor_name
        self.driver_name=driver_name
        self.total_seats=total_seats
        self.seats_booked=seats_booked

    def bus_details(self):
        print("register number"+self.register_number)
        print("conductor name:"+self.conductor_name)
        print("driver name:"+self.driver_name)
        print("total seats:"+self.total_seats)    
        print("seats booked:"+self.seats_booked)

    def is_seat_available(self):
        if self.total_seats > 0 :
            return True
        else:
            return False

    def book_seat(self,no_of_seats):
        if self.total_seats!=self.seats_booked:
            if no_of_seats<self.seats_booked:
                self.seats_booked-=no_of_seats 
                return "Seats booked successfully"
            else:
                return "Requested no of seats not available"
        else:
            return "Requested no of seats not available"   

obj = Bus("TN101", "Joe", "John", 25, 12)
print(obj.book_seat(1))
print(obj.book_seat(2))
print(obj.book_seat(21))

obj= Bus("TN102","Britto","Prince",100,100)
print(obj.book_seat(1))

