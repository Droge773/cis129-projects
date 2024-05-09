with open("grades.txt", "r") as f:
    data = [int(x) for x in f.read().split()]
    print(data)
    print("There are ", len(data), " grades\n")
    print("The sum of the grades is ", sum(data))
    print("The average of the grades is ", sum(data)/len(data))
