class Requisition:
    counter = 10000
    all_requisitions = []

    def __init__(self, date, staff_id, staff_name):
        Requisition.counter += 1
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = Requisition.counter
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"