import csv
import sys

student_data = []

with open('input.csv', mode = 'r') as file:
	csvFile = csv.reader(file)
	for lines in csvFile:
		student_data.append(lines)

output_data = [["","",sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7]]
	,["","","Day","Date","AM/PM","Group","Lead Advisor","Organizer","Prepared By"]
	,["Lineup", "", "Last Name", "First Name", "Student ID", "Major", "Major Change", "Advisor","Cancelled"]]

del student_data[0]

cancelled_students = []

i = 1
for student in student_data:

	if student[3] == "Yes":
		cancelled_students.append(student)
		del student_data[i-1]

	else:
		lastName = student[0].split(", ")[0]
		firstName = student[0].split(", ")[1]

		output_data.append(["",i,lastName,firstName,student[1],student[2],"","",student[3]])
		i+=1

while i < 16:
	output_data.append(["",i])
	i+=1

for student in cancelled_students:
	lastName = student[0].split(", ")[0]
	firstName = student[0].split(", ")[1]
	output_data.append(["","",lastName,firstName,student[1],student[2],"","",student[3]])



with open('output.csv','w',newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(output_data)