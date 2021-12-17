def gradingStudents(grades):
    grade = []
    for i in grades:
        if i <38:
            grade.append(i)
        else:
            num = i
            num1 =num%5
            num -=num1
            num +=5
            num2 = num - i
            if num2 < 3:
                i = num
            grade.append(i)
    return grade
