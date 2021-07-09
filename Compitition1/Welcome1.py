with open("welcome1.txt", "w") as outFile:
    with open("input.txt") as inFile:
        numLine = inFile.readline()
        for line in inFile:
            x = int(line.split()[0])
            y = int(line.split()[1])
            sum = x + y

            outFile.write(str(sum)+ "\n")


