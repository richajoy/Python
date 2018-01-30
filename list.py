def list_numb(numbers):
    for i in numbers:
        if 1 <= i <= 20:
            print(i)

list_numb([1, 2, 4, 8, 16, 32, 64])



def enrollment_stats():
    user_option = input("Do you want to enter univ details? Enter 'yes' or 'no':  ")
    if user_option == "yes":
        user_number_of_univ = int(input("How many universities do you need to make the entries? "))
        universities = []
        for univ in range(user_number_of_univ):
            user_univ_option = input("Enter the name of the university: ")
            user_total_enrolled_students = int(input("Enter the total number of enrolled students: "))
            annual_tut_fees = int(input("Enter the annual tution fees: "))
            universities.append([user_univ_option, user_total_enrolled_students, annual_tut_fees])
            print(universities)
            continue
        student_enroll = []
        tution_fees = []
        for enroll in universities:
            student_enroll.append(enroll[1])
            tution_fees.append(enroll[2])
        return student_enroll, tution_fees
    else:
        print("Thanks! No details entered")
        exit(1)


def mean():
    mean_tot = enrollment_stats()[0]
    total_mean = mean_tot[0] + mean_tot[1]
    print("student mean is {}".format(total_mean))

def medium():
    medium_tot = enrollment_stats()[1]
    total_medium = medium_tot[0] + medium_tot[1]
    print("tution median is {}".format(total_medium))

mean()
medium()



