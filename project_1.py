import csv

def write_into_csv(info_list):
    with open('student_details.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["NAME", "AGE", "CONTACT NO.", "E-MAIL ADDRESS"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_number = 1

while(condition):
    student_details = input("Enter student details for student #{} in the following format (Name Age Contact No. E-mail Address):\n".format(student_number))
    #split
    student_details_list = student_details.split(' ')
    print("\nThe entered details are - \nName: {}\nAge: {}\nContact_No.: {}\nE-mail_Address: {}"
    .format(student_details_list[0], student_details_list[1], student_details_list[2], student_details_list[3]))

    choice_check = input(" Are the given details correct?(yes/no): ")


    if choice_check == "yes":
        write_into_csv(student_details_list)

    condition_check = input("Enter(yes/no) if you want to enter the details of another student: ")
    if condition_check == "yes":
       condition = True
       student_number = student_number + 1
    elif condition_check == "no":
       condition = False

    elif choice_check == "no":
       print("\nPlease re-enter the details!")
