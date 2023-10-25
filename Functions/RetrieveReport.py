def RetriveDat(filePath):
    collected = []
    with open(filePath, "r") as file:
        for line in file:
            print(line)
            collected.append(line)
    return collected
#print(RetriveDat('Report'))