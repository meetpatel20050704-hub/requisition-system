# Class to manage all requisition-related information and operations
class Requisition:

    # Class variable used to generate unique requisition IDs
    requisition_counter = 10000

    # Stores all requisition objects created in the system
    all_requisitions = []

    # Constructor to initialize a new requisition
    def __init__(self):

        # Increase the requisition counter by 1
        Requisition.requisition_counter += 1

        # Assign the new requisition ID
        self.requisition_id = Requisition.requisition_counter

        print("\nRequisition ID:", self.requisition_id)

        # Get basic requisition details from the user
        self.date = input("Date: ")
        self.staff_id = input("Staff ID: ")
        self.staff_name = input("Staff Name: ")

        # Set default values
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

    # Method to add items to the requisition
    def add_requisition(self):

        # Keep asking for items until the user chooses to stop
        while True:

            item_name = input("Enter Item Name: ")
            item_price = float(input("Enter Item Price: $"))

            # Add item price to the total amount
            self.total += item_price

            choice = input("Add another item? (yes/no): ")

            if choice.lower() == "no":
                break

        # Check whether the requisition is approved automatically
        self.approve_requisition()

        # Save the requisition object in the class list
        Requisition.all_requisitions.append(self)

        # Return the total amount
        return self.total

    # Method to approve or keep the requisition pending
    def approve_requisition(self):

        # Automatically approve if the total is less than $500
        if self.total < 500:
            self.status = "Approved"

            # Generate an approval reference number
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]

        else:
            # Anything $500 or above requires manager approval
            self.status = "Pending"
            self.approval_reference = "Not available"

    # Manager responds to pending requisitions
    def respond_requisition(self):

        # Only pending requisitions can receive a response
        if self.status == "Pending":

            response = input(
                f"Manager response for Requisition {self.requisition_id} "
                "(Approved/Not approved/Pending): "
            )

            # Manager approves the requisition
            if response.lower() == "approved":

                self.status = "Approved"

                # Generate approval reference
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]

            # Manager rejects the requisition
            elif response.lower() == "not approved":

                self.status = "Not approved"
                self.approval_reference = "Not available"

            # Keep the requisition pending
            else:

                self.status = "Pending"
                self.approval_reference = "Not available"

    # Display one requisition
    def display_requisition(self):

        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $" + str(int(self.total)))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)
        print()

    # Display all requisitions saved in the system
    @classmethod
    def display_all_requisitions(cls):

        for requisition in cls.all_requisitions:
            requisition.display_requisition()

    # Display summary statistics for all requisitions
    @classmethod
    def requisition_statistics(cls):

        approved = 0
        pending = 0
        not_approved = 0

        # Count requisitions by their current status
        for requisition in cls.all_requisitions:

            if requisition.status == "Approved":
                approved += 1

            elif requisition.status == "Pending":
                pending += 1

            elif requisition.status == "Not approved":
                not_approved += 1

        # Display the statistics
        print("Displaying the Requisition Statistics")
        print("The total number of requisitions submitted:", len(cls.all_requisitions))
        print("The total number of approved requisitions:", approved)
        print("The total number of pending requisitions:", pending)
        print("The total number of not approved requisitions:", not_approved)
        print()


# Main function that controls the program
def main():

    # Keep creating requisitions until the user decides to stop
    while True:

        print("\nEnter Requisition Details")

        requisition = Requisition()
        requisition.add_requisition()

        another = input("\nDo you want to create another requisition? (yes/no): ")

        if another.lower() == "no":
            break

    # Display all requisitions entered
    print("\nPrinting Requisitions:\n")
    Requisition.display_all_requisitions()

    # Show statistics before manager responses
    print("Statistics:\n")
    Requisition.requisition_statistics()

    # Allow the manager to respond to pending requisitions
    print("\nManager Response Section\n")

    for requisition in Requisition.all_requisitions:

        if requisition.status == "Pending":
            requisition.respond_requisition()

    # Display the updated requisition list
    print("\nUpdated Requisition Summary\n")
    Requisition.display_all_requisitions()

    # Display updated statistics
    print("Updated Statistics\n")
    Requisition.requisition_statistics()


# Program starts running from here
if __name__ == "__main__":
    main()