class Requisition:
    def __init__(self, staff_id, staff_name):
        self.staff_id = staff_id
        self.staff_name = staff_name

    def display_staff(self):
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)


# Test Object
req = Requisition("FN19", "John Paul")
req.display_staff()