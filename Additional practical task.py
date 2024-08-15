grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
student = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_student = sorted(student)
print(sorted_student)
grades0 = sum(grades[0]) / len(grades[0])
grades1 = sum(grades[1]) / len(grades[1])
grades2 = sum(grades[2]) / len(grades[2])
grades3 = sum(grades[3]) / len(grades[3])
grades4 = sum(grades[4]) / len(grades[4])
print(grades0, grades1, grades2, grades3, grades4)
academic_performance = {sorted_student[0]: grades0, sorted_student[1]: grades1, sorted_student[2]: grades2, sorted_student[3]: grades3, sorted_student[4]: grades4}
print(academic_performance)