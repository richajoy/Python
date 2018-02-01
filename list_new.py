universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

# Function returning two lists: One with student enrollment values and other with tuition fees.

def enrollment_tuition(universities):
    enrollement_val = []
    tuition_val = []
    for i in universities:
        enrollement_val.append(i[1])
        tuition_val.append(i[2])
    return enrollement_val, tuition_val

# Define a mean() function from the above function as input.

def mean(list):
    list_len = len(list)
    mean_list = []
    for i in range(list_len):
        sub_list_len = len(list[i])
        total = 0
        for j in range(sub_list_len):
            total += int(list[i][j])
        mean = int(total / sub_list_len)
        mean_list.append(mean)
    return mean_list


def median(list):
    leng_of_list = len(list)
    median_list = []
    for k in range(leng_of_list):
        sorted_list = sorted(list[k])
        length_of_ind_list = len(sorted_list)
        if length_of_ind_list % 2:
            calc = (int(length_of_ind_list) - 1) / 2
            median_final = sorted_list[int(calc)]
        else:
            calc = (int(length_of_ind_list) + 1) / 2
            median_final = sorted_list[k][(int(length_of_ind_list) / 2)] + sorted_list[k][int(calc)]
        median_list.append(median_final)
    return median_list


total_final_calc = enrollment_tuition(universities)
total_student_tuition_lst = []
for l in range(len(total_final_calc)):
    student_total = 0
    for m in range(len(total_final_calc[l])):
        student_total += int(total_final_calc[l][m])
    total_student_tuition_lst.append(student_total)
print(3 * "*********")
print("Total students:", total_student_tuition_lst[0])
print("Total tuition: $", total_student_tuition_lst[1])
print("\n")
student_mean_list = mean(total_final_calc)
student_median_list = median(total_final_calc)
print("Student mean:", student_mean_list[0])
print("Student median:", student_median_list[0])
print("\n")
print("Tuition mean: $", student_mean_list[1])
print("Tuition median: $", student_median_list[1])
print(3 * "*********")




#        total = 0
#        for j in range(length_of_ind_list):
#            total += int(sorted_list[i][j])
#        if

#    if length_sorted_list % 2:
#        median_leng = (int(length_sorted_list) + 1) / 2.0
#    else:
#        median_leng = int(length_sorted_list) / 2
#        median_list_length = len(sorted_list[int(median_leng)])
#        total1 = 0
#        total2 = 0
#        for i in range(median_list_length):
#            total1 += total1 + sorted_list[int(median_leng)][i]
#            total2 += total2 + sorted_list[int(median_leng - 1)][i]
#        total = total1 + total2
#    print(total)



#    student_len = len(list[0])
#    tuition_len = len(list[1])
#    total_students = 0
#    total_tuition = 0
#    for j in range(student_len):
#        total_students += int(enroll_final[0][j])
#        if student_len == tuition_len:
#            total_tuition += int(enroll_final[1][j])
#        else:
#            for j in range(tuition_len):
#                total_tuition += int(enroll_final[1][j])
#    student_enroll_mean = total_students / student_len
#    tuition_mean = total_tuition / tuition_len

#    return student_enroll_mean, tuition_mean







