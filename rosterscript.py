import csv
import sys

# Input parameters
#
# Day of the week
# Date
# Your name
#
# EAB Columns
#
# Student Name
# ID
# Major
# Appointment Campaign Name
# Cancelled

student_data = []

with open('input.csv', mode = 'r') as file:
	csvFile = csv.reader(file)
	for lines in csvFile:
		student_data.append(lines)

del student_data[0]

hsci_output = [["","",sys.argv[1],sys.argv[2],"","HSCI","","Jo",sys.argv[3]]
	,["","","Day","Date","AM/PM","Group","Lead Advisor","Organizer","Prepared By"]
	,["Lineup", "", "Last Name", "First Name", "Student ID", "Major", "Major Change", "Advisor","Cancelled"]]
hsci_students = []
hsci_cancelled_students = []

kin_output = [["","",sys.argv[1],sys.argv[2],"","KIN","","Isa",sys.argv[3]]
	,["","","Day","Date","AM/PM","Group","Lead Advisor","Organizer","Prepared By"]
	,["Lineup", "", "Last Name", "First Name", "Student ID", "Major", "Major Change", "Advisor","Cancelled"]]
kin_students = []
kin_cancelled_students = []

cecs_output = [["","",sys.argv[1],sys.argv[2],"","CECS","","Cesar",sys.argv[3]]
	,["","","Day","Date","AM/PM","Group","Lead Advisor","Organizer","Prepared By"]
	,["Lineup", "", "Last Name", "First Name", "Student ID", "Major", "Major Change", "Advisor","Cancelled"]]
cecs_students = []
cecs_cancelled_students = []



for student in student_data:

	if student[3] == "FA25 GS HSCI Workshop":
		if student[4] == "No":
			hsci_students.append(student)
		else:
			hsci_cancelled_students.append(student)

	elif student[3] == "FA25 GS KIN Workshop":
		if student[4] == "No":
			kin_students.append(student)
		else:
			kin_cancelled_students.append(student)

	elif student[3] == "FA25 GS CECS Workshop":
		if student[4] == "No":
			cecs_students.append(student)
		else:
			cecs_cancelled_students.append(student)

	else:
		print("invalid workshop")

if len(hsci_students) != 0:
	i = 1
	for student in hsci_students:
		if student[0] != "" and student[0] != "Lineup":
			lastName = student[0].split(", ")[0]
			firstName = student[0].split(", ")[1]

			hsci_output.append(["",i,lastName,firstName,student[1],student[2],"","",student[4]])
			i+=1

	while i < 16:
		hsci_output.append(["",i])
		i+=1

	for student in hsci_cancelled_students:
		lastName = student[0].split(", ")[0]
		firstName = student[0].split(", ")[1]
		hsci_output.append(["","",lastName,firstName,student[1],student[2],"","",student[4]])

	date = sys.argv[2].split("/")
	date = ".".join(date)

	output_string = "3rd_Sem_WS_Roster_HSCI_" + date + ".csv"

	with open(output_string,'w',newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(hsci_output)



if len(kin_students) != 0:
	i = 1
	for student in kin_students:
		if student[0] != "" and student[0] != "Lineup":
			lastName = student[0].split(", ")[0]
			firstName = student[0].split(", ")[1]

			kin_output.append(["",i,lastName,firstName,student[1],student[2],"","",student[4]])
			i+=1

	while i < 16:
		kin_output.append(["",i])
		i+=1

	for student in kin_cancelled_students:
		lastName = student[0].split(", ")[0]
		firstName = student[0].split(", ")[1]
		kin_output.append(["","",lastName,firstName,student[1],student[2],"","",student[4]])

	date = sys.argv[2].split("/")
	date = ".".join(date)

	output_string = "3rd_Sem_WS_Roster_KIN_" + date + ".csv"

	with open(output_string,'w',newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(kin_output)

if len(cecs_students) != 0:
	i = 1
	for student in cecs_students:
		if student[0] != "" and student[0] != "Lineup":
			lastName = student[0].split(", ")[0]
			firstName = student[0].split(", ")[1]

			cecs_output.append(["",i,lastName,firstName,student[1],student[2],"","",student[4]])
			i+=1

	while i < 16:
		cecs_output.append(["",i])
		i+=1

	for student in cecs_cancelled_students:
		lastName = student[0].split(", ")[0]
		firstName = student[0].split(", ")[1]
		cecs_output.append(["","",lastName,firstName,student[1],student[2],"","",student[4]])

	date = sys.argv[2].split("/")
	date = ".".join(date)

	output_string = "3rd_Sem_WS_Roster_CECS" + date + ".csv"

	with open(output_string,'w',newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(cecs_output)