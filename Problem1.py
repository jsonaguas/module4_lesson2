class Vehicle:
    def __init__ (self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, owner):
        self.owner = owner


civic = Vehicle("XYZ456", "Car", "Bob")
print(civic.owner)

civic.update_owner("Steve")
print(civic.owner)

#Task 2
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant = 0

    def add_participant(self, participant):
        self.participant += participant 

    def get_participant (self):
        return self.participant

party = Event("Birthday", "12/12/2020")
party.add_participant(10)
print(party.get_participant())



