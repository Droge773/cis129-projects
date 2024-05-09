import csv

with open("grades.csv", mode='w', newline='') as grades:
    inp = 1
    writer = csv.writer(grades)
    while inp == 1:
        print("(1) enter another entry\n(2) exit\n")
        inp = int(input())
        if inp != 1:
            break
        else:
            print("Student first name?")
            first = input()
            print("Student last name?")
            last = input()
            print("First grade?")
            test1 = input()
            print("Second grade?")
            test2 = input()
            print("Third grade?")
            test3 = input()
            writer.writerow([first, last, test1, test2, test3])
            
