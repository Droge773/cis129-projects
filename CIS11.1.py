print("Enter any number of grades you would like\nWhen you're done, press enter to finish")
with open('grades.txt', mode='w') as grades:
    gTemp = 1
    while gTemp != "":
        gTemp = input()
        gTemp2 = gTemp + "\n"
        grades.write(gTemp2)
        
