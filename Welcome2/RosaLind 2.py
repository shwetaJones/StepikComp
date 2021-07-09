import itertools
import re
positions = []
with open("welcome1.txt", "w") as outFile:
    with open("input.txt") as inFile:
        numLine = int(inFile.readline())
        # for line1,line2 in itertools.zip_longest(*[inFile]*2):
        #     line1 = str(line1)
        #     line2 = str(line2)
        for i in range(numLine):
            line1 = str(inFile.readline())
            line1.rstrip("\n")
            line2 = str(inFile.readline())
            line2.strip("\n")
            print("line1:" + line1)
            print("line2:" + line2)
            # result = line1.find("TCAAATATC")
            # result = line1.find(line2)
            # print(result)

            # res = [i for i in range(len(line1)) if line1.startswith(str(line2), i)]
            # print(res)


