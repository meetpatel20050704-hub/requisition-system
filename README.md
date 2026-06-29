# Requisition System

## Project Overview

The Requisition System is a Python application that has been created as a part of the Software Development Project assessment. This project aims to make the requisition request creation and management process easy and convenient in an organisation. Staff can submit requisitions, and enter the details of staff and the cost of the required items. The system automatically calculates the total amount, automatically approves the requisition if it passes or sends it for the manager's approval and stores all the information about the requisition for future reference. The project illustrates the use of Object Oriented Programming concepts, and offers a simple and easy-to-use console application.

---

## Project Objectives

The key aims of this project are to:

* Write Python program to create a requisition management system.
* Use object-oriented programming (OOP) concepts.
* Automatically calculate the total requisition cost.
* Approve/reject requisitions according to the business rules.
* Permit manager to react to pending requisitions.
* Display all requisition records, and summary statistics.

---

## System Features

The application has some handy options for efficient requisition management. Automatically assigned unique identification numbers to each requisition are. Users can add the date, staff ID, staff name, item details and the prices of items. The system sums up all the requisitions and automatically accepts the requests that do not exceed a total of $500. Requests for items that cost $500 or more will be held in queue until a manager can look at them. The Manager has the authority to either approve, reject or leave a requisition pending. The program will also create an approval reference number for approved requisitions, and produce an overview summary of all requisitions, along with a summary of the statistics.

---

## How the System Works

At the initial start of the program, the user will be asked to provide the necessary information such as date, staff member ID and staff member name. The user can then enter one or more of the items required to make up a requisition with its separate price. When all items are entered the program works out the amount of the requisition.

If the total comes to less than **$500** an approval reference number is automatically generated and the requisition is approved. The total cost is the total sum of the requisitioned items.Total cost is the sum of the items that were requisitioned - if the total cost is $500 or more the requisition status is set to Pending and a later prompt asks the manager for a decision. Once the requisitions are processed, the system will show each requisition, and provide new statistics of the number of approved, pending and rejected requests.

---

## Object-Oriented Programming

This project is designed based on the object oriented programming concepts. Each staff member's requisition is represented by a single class named "Requisition". All the necessary data is stored in the class such as requisition Id, Date, Staffs, Total Amount, approval/Rejection and Approval Ref Id. Various techniques have been developed in class to accomplish these types of actions: adding a requisition, approving a requisition, responding to pending requisitions, and displaying a requisition's details and/or generating statistics. This design helps to maintain the code structure, reusability and organization.

---

## Approval Process

The approvals for a requisition are based on a simple business rule:

Any Requisition for an amount of less than $500 will be automatically accepted.
The total of all requisitions ranging from $500 and above are represented as Pending.
Managers will be able to change the status to:

  * Approved
  * Not Approved
  * Pending

When a requisition is approved, the system will automatically create an approval reference number with the staff ID and last three digits of the requisition ID.

---

## Technologies Used

The following technologies were used with this project:

* Python 3
* Visual Studio Code
* Git
* GitHub

---

## Running the Program

To run the program:

Install Python 3 into computer.
3. In Visual Studio Code, ensure that the file on the left side is selected.4. Make sure that the file on the left is highlighted in Visual Studio Code.
3. Open up the built-in terminal.
5. Run the python script.
6. Go through the instructions in the terminal to make and run requisitions.

---

## Testing

The application has been verified with various requisition scenarios, to ensure that all functions of the program work properly. The automatic approval, pending requisitions, manager responses, approval reference generation, displaying the requisition information and generating the requisition statistics are all included in testing. Various input values were fed to check the program for correct processing of both approved and pending requisitions.

---

## Future Improvements

The assessment system in place meets the requirements but there are a number of enhancements that may be made to the system in the next iteration. These include creating a database or file to store the data of what requisitions are needed, creating a graphical user interface (GUI), enabling users to edit or delete requisitions, better input validation, and detailed reports for management.

---

## Conclusion

The Requisition System is a successful demonstration of how the concepts of Object Oriented Programming can be applied to Python, to solve a real business problem. The system automates the process of approving requisitions, keeps a proper record of the requisitions and offers informative statistical data. In general, the project has enhanced the programming abilities of the students in terms of designing classes, implementing methods, interacting with users and programming practices.

---

## Author

**Meet Patel**

Assessment 2: Software Development Project (SDP)