
def checkNone(value):
    if value!=None:
        return True
    else:
        return False

def RetriveDat(filePath):
    if checkNone(filePath):
        collected = []
        with open(filePath, "r") as file:
            for line in file:
                print(line)
                collected.append(line)
        return collected
#print(RetriveDat('Report'))