# Assessment 2 - Purchase Requisition System

class Requisition:
    next_id = 10001

    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name

        self.requisition_id = Requisition.next_id
        Requisition.next_id += 1

        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"


# Testing the class
date = input("Enter date: ")
staff_id = input("Enter staff ID: ")
staff_name = input("Enter staff name: ")

request = Requisition(date, staff_id, staff_name)

print("Requisition ID:", request.requisition_id)
print("Date:", request.date)
print("Staff ID:", request.staff_id)
print("Staff Name:", request.staff_name)
print("Status:", request.status)
