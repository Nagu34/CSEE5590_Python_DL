#5. Write a python program to create any one of the following management systems.
# b.Airline Booking Reservation System (e.g. classes Flight, Person, Employee, Passenger etc.)
# Prerequisites: a. Your code should have at least five classesb.
# Your code should have _init_ constructor in all the classesc.
# Your code should show inheritance at least onced.
# Your code should have one super calle.
# Use of self is requiredf. Use at least one private data member in your codeg.
# Use multiple Inheritance at least onceh.
#Create instances of all classes and show the relationship between them
#created first person class with passenger details
class Person():
    #constructor initialization
    def __init__(self, First_name, Last_name, Email_address, Phone_number, age, employee_Id):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Email_address = Email_address
        self.Phone_number = Phone_number
        self.age = age
        self.emplpoyee_Id = employee_Id

    def __employeeId__(self):
        print(" Employee ID", self.employee_Id)

    def nameprint(self):
        print(" First Nme and Last name :", self.First_name + " " + self.Last_name)

    def ageprint(self):
        print(" Age: ", self.age)

    def phonenumber(self):
        print(" Phone number: " + self.Phone_number)
#printing passenger details
    def PrintPassengerDetails(self):
        print(" First Name :" + self.First_name)
        print(" Last Name :" + self.Last_name)
        print(" Email Address :" + self.Email_address)
        print(" Phone number :" + self.Phone_number)
        print(" Age :" + self.age)
        print(" Employee Id :" + self.emplpoyee_Id)




#created flight details class
class Flight():
    def __init__(self, Flight_name, Flight_number, meals, Boarding_pass):
        self.Flight_number = Flight_number
        self.Flight_name = Flight_name
        self.Boarding_pass = Boarding_pass
        self.meals = meals

    def flightdetails(self):
        print(" Flight Name : ", self.Flight_name)
        print(" Flight Number : ", self.Flight_number)
        print("Boarding_pass :", self.Boarding_pass)
        print("Meal type : ", self.meals)


class Seatallotment():
    def __init__(self, seat_num, Row_num):
        self.seat_num = seat_num
        self.Row_num = Row_num

    def PrintSeatDetails(self):
        print(" Seat No.", self.seat_num)
        print(" Row Number", self.Row_num)

#booking confirmation class inherited from seatallotment class
class Booking_confirmation(Seatallotment):
    def __init__(self, DepartureDate, DepartureTime, ArrivalTime, Travel_Class, Source, destination, seat_num,Row_num,Booking_confirm):
        Seatallotment.__init__(self,seat_num,Row_num)
        self.Departuredate = DepartureDate
        self.DepartureTime = DepartureTime
        self.ArrivalTime = ArrivalTime
        self.destination = destination
        self.Travel_Class = Travel_Class
        self.Source = Source
        self.Booking_confirm=Booking_confirm



# passenger details class which is multilevel and multiple inherited class
class Passenger_details(Person, Flight, Booking_confirmation):
    def __init__(self, First_name, Last_name, Email_address, Phone_number, age, employee_Id,
                 Flight_name, Flight_number, meals, Boarding_pass,
                 DepartureDate, DepartureTime, ArrivalTime, Travel_Class, Source,
                 destination, seat_num, Row_num, Booking_confirm):
        #super call should be done inorder to access the multilevel class variables
        super().__init__(First_name, Last_name, Email_address, Phone_number, age, employee_Id)
#booking confirmation class variables can be accessed through this
        Booking_confirmation.__init__(self,DepartureDate, DepartureTime, ArrivalTime, Travel_Class, Source, destination,
                                      seat_num, Row_num,Booking_confirm)
        #flight class variables will be inherited
        Flight.__init__(self,Flight_name, Flight_number, meals, Boarding_pass)
#printing the travel details
    def printSOurceInfo(self):
        print(" Travel from where to : ", self.Source)
        print("Destination place : ", self.destination)
        print("Departure Date :" + self.Departuredate)
        print("Travel Class :" + self.Travel_Class)
        print("Departure Time :" + self.DepartureTime)
        print("Arrival Time :" + self.ArrivalTime)
        print("Booking Confirm:" + self.Booking_confirm)


#Booking = Booking_confirmation("02/23/2019", "3:00 AM", "4:00 PM", "Economy", "New york", "Amsterdam", "34", "B", "Booked")
#Booking.printSOurceInfo()
passenger = Passenger_details("bharat", "singla", "bharat12@gmail.com", "913654789", "25", "123", "Airbus", "A 456",
                              "Veg", "yes", "02/23/2019", "3:00 AM", "4:00 PM", "Economy", "New york", "Amsterdam", "34", "B", "yes")
print("-------------------Passenger Details---------------------------")
passenger.PrintPassengerDetails()
print("-------------------Flight Deatails------------------------------")
passenger.flightdetails()
print("-------------------Seat Details----------------------------------")
passenger.PrintSeatDetails()
print("------------------Travel Details----------------------------------")
passenger.printSOurceInfo()

