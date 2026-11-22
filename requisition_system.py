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


    def add_requisition(self, items):
        self.total = 0

        for item in items:
            self.total += item["cost"]

        return self.total

    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

        return self.status
    
    
    def manager_response(self, decision):
        if self.status == "Pending":
            if decision == "Approved":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
            elif decision == "Rejected":
                self.status = "Rejected"
                self.approval_reference = "Not available"

        return self.status


# Testing the class
date = input("Enter date: ")
staff_id = input("Enter staff ID: ")
staff_name = input("Enter staff name: ")

request = Requisition(date, staff_id, staff_name)

items = []

number_of_items = int(input("How many items do you want? "))

for i in range(number_of_items):
    item_name = input("Enter item name: ")
    item_cost = float(input("Enter item cost: "))

    items.append({"name": item_name, "cost": item_cost})

request.add_requisition(items)
request.approve_requisition()

print("Total Cost: $", request.total)


print("Requisition ID:", request.requisition_id)
print("Date:", request.date)
print("Staff ID:", request.staff_id)
print("Staff Name:", request.staff_name)
print("Status:", request.status)
print("Approval Reference:", request.approval_reference)

if request.status == "Pending":
    request.manager_response("Rejected")
    print("Manager Decision:", request.status)
    print("Approval Reference:", request.approval_reference)
