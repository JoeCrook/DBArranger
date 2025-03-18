# Updated 2024-05-12
# Added the ability to use an input file for NewDI

from csv import writer, reader
from os.path import isfile


class NewSuper:
    """A Class to store information about a new supertag"""

    def __init__(self, group, comment, accessName, itemName):
        self.Group = group
        self.Comment = comment
        self.AccessName = accessName
        self.ItemName = itemName
        self.Name = itemName


def findFile():
    """Finds the base CSV file and loops if not correct"""
    while True:
        # Gathers the name of the csv file to be checked
        fileName = input("Name of the input CSV file: ").lower()
        if fileName.endswith(".csv"):
            fileName = fileName[:-4]
        # Loops asking for the file name if the given one doesn't exist
        if not isfile(fileName + ".csv"):
            print("File doesn't exist!")
        else:
            break
    return fileName


def findFunction(functionCheck):
    """Finds the function required, and gathers/passes the information needed to run"""
    # Function that finds a given tag in a database, and optionally saves it to a file
    if functionCheck in ["findtag", "ft"]:
        fileName = findFile()
        moreTags = True
        tagList = []
        while moreTags == True:
            requiredTag = input("Tag to search for: ").lower()
            if requiredTag.startswith(":"):
                requiredTag = requiredTag[1:]
            else:
                tagList += [requiredTag]
            moreTags = checkAnother("tag")

        print(findTag(fileName, createFile(True), tagList))

    # Function that selects a certain section of tags, and saves them only to a file
    elif functionCheck in ["selectsection", "selsec", "ss"]:
        fileName = findFile()
        # Discovers which section is required
        moreSections = True
        sections = []
        while moreSections == True:
            sections.append(input("Which section to keep: ").lower())
            moreSections = checkAnother("section")

        print(selectSection(fileName, createFile(True), sections))

    # Function that creates a new DI supertag
    elif functionCheck in ["di"]:
        while True:
            # Determines if new tags are created using an input csv file, or via manual input
            inputFile = input("Use an input csv file?: (Y/N) ")
            if inputFile in ["y", "ye", "yes", "1", "true"]:
                print("Input file must have no headers, and have each new DI on it's own line, with info in the order: PLC Name, Comment, Group, AccessName")
                inputFile = True
                inputFileName = findFile()
                break
            elif inputFile in ["n", "no", "0", "false"]:
                inputFile = False
                break
            else:
                print("Error: Expected answer \"yes\" or \"no\"")
                continue

        if inputFile == False:
            # Checks how many new tags being created, and checks answer is given in a correct format
            while True:
                while True:
                    try:
                        newDINum = int(input("How many new tags needed: "))
                        break
                    except ValueError:
                        print("Answer must be an int")
                if newDINum > 0:
                    break
                else:
                    print("Answer must be 1 or more")

        # Creates the number of classes required and gathers required info
        newDIs = []
        if inputFile == True:
            # Uses an input file to gather the info
            newDINum = 0
            # Input file must have no headers, and have each new DI on it's own line, with info in the order: Item Name, Comment, Group, AccessName
            with open(inputFileName + ".csv", newline='', encoding='utf-8-sig') as DIInput:
                DIReader = reader(DIInput, delimiter=',')
                for row in DIReader:
                    newDINum += 1
                    newDIGroup = str(row[2])
                    newDIComment = str(row[1])
                    newDIAccessName = str(row[3])
                    newDIItemName = str(row[0])
                    newDIs.append(NewSuper(newDIGroup, newDIComment,
                                           newDIAccessName, newDIItemName))
        else:
            # Manually asks for all the required information
            for i in range(newDINum):
                newDIGroup = str(input("New DI #" + str(i + 1) + " Group: "))
                newDIComment = str(
                    input("New DI #" + str(i + 1) + " Comment: "))
                newDIAccessName = str(input(
                    "New DI #" + str(i + 1) + " AccessName: "))
                newDIItemName = str(
                    input("New DI #" + str(i + 1) + " ItemName: "))
                newDIs.append(NewSuper(newDIGroup, newDIComment,
                              newDIAccessName, newDIItemName))
        print(createDI(createFile(True), newDINum, newDIs))

    elif functionCheck in ["m_3"]:
        while True:
            # Determines if new tags are created using an input csv file, or via manual input
            inputFile = input("Use an input csv file?: (Y/N) ")
            if inputFile in ["y", "ye", "yes", "1", "true"]:
                print("Input file must have no headers, and have each new M_3 on it's own line, with info in the order: PLC Name, Comment, Group, AccessName")
                inputFile = True
                inputFileName = findFile()
                break
            elif inputFile in ["n", "no", "0", "false"]:
                inputFile = False
                break
            else:
                print("Error: Expected answer \"yes\" or \"no\"")
                continue

        if inputFile == False:
            # Checks how many new tags being created, and checks answer is given in a correct format
            while True:
                while True:
                    try:
                        newM_3Num = int(input("How many new tags needed: "))
                        break
                    except ValueError:
                        print("Answer must be an int")
                if newM_3Num > 0:
                    break
                else:
                    print("Answer must be 1 or more")

        # Creates the number of classes required and gathers required info
        NewM_3s = []
        if inputFile == True:
            # Uses an input file to gather the info
            newM_3Num = 0
            # Input file must have no headers, and have each new M_3 on it's own line, with info in the order: Item Name, Comment, Group, AccessName
            with open(inputFileName + ".csv", newline='', encoding='utf-8-sig') as M_3Input:
                M_3Reader = reader(M_3Input, delimiter=',')
                for row in M_3Reader:
                    newM_3Num += 1
                    newM_3Group = str(row[2])
                    newM_3Comment = str(row[1])
                    newM_3AccessName = str(row[3])
                    newM_3ItemName = str(row[0])
                    NewM_3s.append(NewSuper(newM_3Group, newM_3Comment,
                                            newM_3AccessName, newM_3ItemName))
        else:
            # Manually asks for all the required information
            for i in range(newM_3Num):
                newM_3Group = str(input("New M_3 #" + str(i + 1) + " Group: "))
                newM_3Comment = str(
                    input("New M_3 #" + str(i + 1) + " Comment: "))
                newM_3AccessName = str(input(
                    "New M_3 #" + str(i + 1) + " AccessName: "))
                newM_3ItemName = str(
                    input("New M_3 #" + str(i + 1) + " ItemName: "))
                NewM_3s.append(NewSuper(newM_3Group, newM_3Comment,
                                        newM_3AccessName, newM_3ItemName))
        print(createM_3(createFile(True), newM_3Num, NewM_3s))

    elif functionCheck in ["m_10"]:
        while True:
            # Determines if new tags are created using an input csv file, or via manual input
            inputFile = input("Use an input csv file?: (Y/N) ")
            if inputFile in ["y", "ye", "yes", "1", "true"]:
                print("Input file must have no headers, and have each new M_10 on it's own line, with info in the order: PLC Name, Comment, Group, AccessName")
                inputFile = True
                inputFileName = findFile()
                break
            elif inputFile in ["n", "no", "0", "false"]:
                inputFile = False
                break
            else:
                print("Error: Expected answer \"yes\" or \"no\"")
                continue

        if inputFile == False:
            # Checks how many new tags being created, and checks answer is given in a correct format
            while True:
                while True:
                    try:
                        newM_10Num = int(input("How many new tags needed: "))
                        break
                    except ValueError:
                        print("Answer must be an int")
                if newM_10Num > 0:
                    break
                else:
                    print("Answer must be 1 or more")

        # Creates the number of classes required and gathers required info
        NewM_10s = []
        if inputFile == True:
            # Uses an input file to gather the info
            newM_10Num = 0
            # Input file must have no headers, and have each new M_10 on it's own line, with info in the order: Item Name, Comment, Group, AccessName
            with open(inputFileName + ".csv", newline='', encoding='utf-8-sig') as M_10Input:
                M_10Reader = reader(M_10Input, delimiter=',')
                for row in M_10Reader:
                    newM_10Num += 1
                    newM_10Group = str(row[2])
                    newM_10Comment = str(row[1])
                    newM_10AccessName = str(row[3])
                    newM_10ItemName = str(row[0])
                    NewM_10s.append(NewSuper(newM_10Group, newM_10Comment,
                                             newM_10AccessName, newM_10ItemName))
        else:
            # Manually asks for all the required information
            for i in range(newM_10Num):
                newM_10Group = str(
                    input("New M_10 #" + str(i + 1) + " Group: "))
                newM_10Comment = str(
                    input("New M_10 #" + str(i + 1) + " Comment: "))
                newM_10AccessName = str(input(
                    "New M_10 #" + str(i + 1) + " AccessName: "))
                newM_10ItemName = str(
                    input("New M_10 #" + str(i + 1) + " ItemName: "))
                NewM_10s.append(NewSuper(newM_10Group, newM_10Comment,
                                         newM_10AccessName, newM_10ItemName))
        print(createM_10(createFile(True), newM_10Num, NewM_10s))

    elif functionCheck in ["mf_10"]:
        while True:
            # Determines if new tags are created using an input csv file, or via manual input
            inputFile = input("Use an input csv file?: (Y/N) ")
            if inputFile in ["y", "ye", "yes", "1", "true"]:
                print("Input file must have no headers, and have each new MF_10 on it's own line, with info in the order: PLC Name, Comment, Group, AccessName")
                inputFile = True
                inputFileName = findFile()
                break
            elif inputFile in ["n", "no", "0", "false"]:
                inputFile = False
                break
            else:
                print("Error: Expected answer \"yes\" or \"no\"")
                continue

        if inputFile == False:
            # Checks how many new tags being created, and checks answer is given in a correct format
            while True:
                while True:
                    try:
                        newMF_10Num = int(input("How many new tags needed: "))
                        break
                    except ValueError:
                        print("Answer must be an int")
                if newMF_10Num > 0:
                    break
                else:
                    print("Answer must be 1 or more")

        # Creates the number of classes required and gathers required info
        NewMF_10s = []
        if inputFile == True:
            # Uses an input file to gather the info
            newMF_10Num = 0
            # Input file must have no headers, and have each new MF_10 on it's own line, with info in the order: Item Name, Comment, Group, AccessName
            with open(inputFileName + ".csv", newline='', encoding='utf-8-sig') as MF_10Input:
                MF_10Reader = reader(MF_10Input, delimiter=',')
                for row in MF_10Reader:
                    newMF_10Num += 1
                    newMF_10Group = str(row[2])
                    newMF_10Comment = str(row[1])
                    newMF_10AccessName = str(row[3])
                    newMF_10ItemName = str(row[0])
                    NewMF_10s.append(NewSuper(newMF_10Group, newMF_10Comment,
                                              newMF_10AccessName, newMF_10ItemName))
        else:
            # Manually asks for all the required information
            for i in range(newMF_10Num):
                newMF_10Group = str(
                    input("New MF_10 #" + str(i + 1) + " Group: "))
                newMF_10Comment = str(
                    input("New MF_10 #" + str(i + 1) + " Comment: "))
                newMF_10AccessName = str(input(
                    "New MF_10 #" + str(i + 1) + " AccessName: "))
                newMF_10ItemName = str(
                    input("New MF_10 #" + str(i + 1) + " ItemName: "))
                NewMF_10s.append(NewSuper(newMF_10Group, newMF_10Comment,
                                          newMF_10AccessName, newMF_10ItemName))
        print(createMF_10(createFile(True), newMF_10Num, NewMF_10s))

    elif functionCheck in ["fv1_10p"]:
        while True:
            # Determines if new tags are created using an input csv file, or via manual input
            inputFile = input("Use an input csv file?: (Y/N) ")
            if inputFile in ["y", "ye", "yes", "1", "true"]:
                print("Input file must have no headers, and have each new FV1_10P on it's own line, with info in the order: PLC Name, Comment, Group, AccessName")
                inputFile = True
                inputFileName = findFile()
                break
            elif inputFile in ["n", "no", "0", "false"]:
                inputFile = False
                break
            else:
                print("Error: Expected answer \"yes\" or \"no\"")
                continue

        if inputFile == False:
            # Checks how many new tags being created, and checks answer is given in a correct format
            while True:
                while True:
                    try:
                        newFV1_10PNum = int(
                            input("How many new tags needed: "))
                        break
                    except ValueError:
                        print("Answer must be an int")
                if newFV1_10PNum > 0:
                    break
                else:
                    print("Answer must be 1 or more")

        # Creates the number of classes required and gathers required info
        NewFV1_10Ps = []
        if inputFile == True:
            # Uses an input file to gather the info
            newFV1_10PNum = 0
            # Input file must have no headers, and have each new FV1_10P on it's own line, with info in the order: Item Name, Comment, Group, AccessName
            with open(inputFileName + ".csv", newline='', encoding='utf-8-sig') as FV1_10PInput:
                FV1_10PReader = reader(FV1_10PInput, delimiter=',')
                for row in FV1_10PReader:
                    newFV1_10PNum += 1
                    newFV1_10PGroup = str(row[2])
                    newFV1_10PComment = str(row[1])
                    newFV1_10PAccessName = str(row[3])
                    newFV1_10PItemName = str(row[0])
                    NewFV1_10Ps.append(NewSuper(newFV1_10PGroup, newFV1_10PComment,
                                                newFV1_10PAccessName, newFV1_10PItemName))
        else:
            # Manually asks for all the required information
            for i in range(newFV1_10PNum):
                newFV1_10PGroup = str(
                    input("New FV1_10P #" + str(i + 1) + " Group: "))
                newFV1_10PComment = str(
                    input("New FV1_10P #" + str(i + 1) + " Comment: "))
                newFV1_10PAccessName = str(input(
                    "New FV1_10P #" + str(i + 1) + " AccessName: "))
                newFV1_10PItemName = str(
                    input("New FV1_10P #" + str(i + 1) + " ItemName: "))
                NewFV1_10Ps.append(NewSuper(newFV1_10PGroup, newFV1_10PComment,
                                            newFV1_10PAccessName, newFV1_10PItemName))
        print(createFV1_10P(createFile(True), newFV1_10PNum, NewFV1_10Ps))

    elif functionCheck in ["tesys"]:
        tesysLoop = True
        tesysList = []
        tesysNum = 1
        while tesysLoop == True:
            tesysListTemp = {}
            tesysListTemp["Tag"] = input("Tag #"+str(tesysNum)+": ")
            tesysListTemp["Comment"] = input("Comment #"+str(tesysNum)+": ")
            tesysListTemp["AccessName"] = input(
                "AccessName #"+str(tesysNum)+": ")
            tesysList.append(tesysListTemp)
            tesysNum += 1
            tesysLoop = checkAnother("set of tags")

        print(tesys(createFile(True), tesysList))

    # Loops if the given function doesn't exist/isn't recognised
    else:
        print("Functions: \"Find Tag\", \"Select Section\", \"DI\", \"M_3\", \"Tesys\"")
        findFunction(
            input("Function type required: ").lower().replace(" ", ""))
    return


def findTag(fileName, newFileName, requiredTag):
    """Finds a given tag in a database, and optionally saves it to a file"""
    tagCount = 0
    # Opens the given base file
    with open(fileName + ".csv", newline='') as DBInput:
        with open(newFileName + ".csv", "w", newline="") as DBOutput:
            DBWriter = writer(DBOutput)
            DBReader = reader(DBInput, delimiter=',')
            # Reads the given base file row by row
            for row in DBReader:
                if row[0].lower().startswith(":mode="):
                    DBWriter.writerow(row)
                # If the first cell (the "tag") in the row contains the given requiredTag, increments the tag count, prints the whole row, and writes it to the output file if enabled)
                for tag in requiredTag:
                    # If the row is a section header, and an output file is required, write the row to the output file
                    if row[0].lower().startswith(":"):
                        headerWritten = False
                        currentHeader = row
                    elif tag in row[0].lower():
                        if headerWritten == False:
                            DBWriter.writerow(currentHeader)
                            headerWritten = True
                        tagCount += 1
                        print(', '.join(row))
                        DBWriter.writerow(row)

    # Prints the amount of tags found in the console
    if tagCount > 0:
        if tagCount == 1:
            return str(tagCount)+" tag found. "
        else:
            return str(tagCount)+" tags found. "
    # Returns an error if no tags located in the file
    else:
        return "Error: Tag not found "


def selectSection(fileName, newFileName, sections):
    """Selects a certain section of tags, and saves them only to a file"""
    correctSection = False
    with open(fileName+".csv", newline="") as DBInput:
        DBReader = reader(DBInput, delimiter=',')
        with open(newFileName+".csv", "w", newline="") as DBOutput:
            if newFileName != "":
                DBWriter = writer(DBOutput)
            # Iterates through the input file, row by row
            for row in DBReader:
                # Checks if the row being looked at is the first one, if so saves that row to the top of the file
                if row[0].lower().startswith(":mode="):
                    if newFileName != "":
                        DBWriter.writerow(row)
                    else:
                        print(row)

                elif correctSection == True:
                    if row[0].lower().startswith(":"):
                        correctSection = False
                        if row[0].lower().startswith(":") and row[0][1:].lower() in sections:
                            correctSection = True
                            if newFileName != "":
                                DBWriter.writerow(row)
                            else:
                                print(row)
                        continue
                    else:
                        if newFileName != "":
                            DBWriter.writerow(row)
                        else:
                            print(row)

                # Checks if the row being looked at is the first one of the required section
                elif row[0].lower().startswith(":") and row[0][1:].lower() in sections:
                    correctSection = True
                    if newFileName != "":
                        DBWriter.writerow(row)
                    else:
                        print(row)

    # Gives a status message at the end of the function
    if newFileName != "":
        return "File created, saved as \""+newFileName+".csv\" "
    else:
        return "Finished searching"


def createDI(newFileName, newDINum, newDIs):
    """Creates a new DI supertag"""
    # Opens the output file and preps to write to it
    with open(newFileName+".csv", "w", newline="") as DIOutput:
        DIWriter = writer(DIOutput)
        # Writes all the rows required
        DIWriter.writerow([":mode=ask"])
        DIWriter.writerow([":IODisc", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "InitialDisc", "OffMsg", "OnMsg", "AlarmState", "AlarmPri",
                           "Dconversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "DSCAlarmDisable", "DSCAlarmInhibitor", "SymbolicName"])
        for i in range(newDINum):
            DIWriter.writerow([newDIs[i].Name+"\DIW", newDIs[i].Group, newDIs[i].Comment+" - Digital Input Warning", "No", "Yes", "1", "No", "Off", "", "", "On", "3",
                               "Direct", newDIs[i].AccessName, "No", newDIs[i].ItemName+".HMI.CMDW.09", "No", newDIs[i].Comment+" - Digital Input Warning", "0", "0", "", "", "No"])
            DIWriter.writerow([newDIs[i].Name+"\GI", newDIs[i].Group, newDIs[i].Comment+" - General Inhibit", "No", "No", "0", "No", "Off", "", "", "None", "1",
                               "Direct", newDIs[i].AccessName, "No", newDIs[i].ItemName+".HMI.STW.02", "No", newDIs[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
            DIWriter.writerow([newDIs[i].Name+"\GA", newDIs[i].Group, newDIs[i].Comment+" - General Alarm", "No", "No", "0", "No", "Off", "", "", "None",
                               "1", "Direct", newDIs[i].AccessName, "No", newDIs[i].ItemName+".GA", "No", newDIs[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
            DIWriter.writerow([newDIs[i].Name+"\DIA", newDIs[i].Group, newDIs[i].Comment+" - Digital Input Alarm", "No", "Yes", "1", "No", "Off", "", "", "On", "3",
                               "Direct", newDIs[i].AccessName, "No", newDIs[i].ItemName+".HMI.CMDW.08", "No", newDIs[i].Comment+" - Digital Input Alarm", "0", "0", "", "", "No"])
        DIWriter.writerow([":MemoryInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinValue", "MaxValue", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue",
                           "MinorDevAlarmPri", "MajorDevAlarmState", "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", "LocalTag"])
        for i in range(newDINum):
            DIWriter.writerow([newDIs[i].Name+"\Precision", newDIs[i].Group, newDIs[i].Comment+" - Precision", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "9999", "0", "1", "Off", "0", "1", "Off",
                               "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            DIWriter.writerow([newDIs[i].Name+"\AccessLevel", newDIs[i].Group, newDIs[i].Comment+" - AccessLevel", "No", "No", "0", "No", "No", "0", "0", "", "900", "0", "9999", "0", "1", "Off", "0", "1", "Off",
                               "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        DIWriter.writerow([":IOInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                           "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName"])
        for i in range(newDINum):
            DIWriter.writerow([newDIs[i].Name+"\HMICMDW", newDIs[i].Group, newDIs[i].Comment+" - HMICMDW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                               "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newDIs[i].AccessName, "No", newDIs[i].ItemName+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            DIWriter.writerow([newDIs[i].Name+"\HMISTW", newDIs[i].Group, newDIs[i].Comment+" - HMISTW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                               "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newDIs[i].AccessName, "No", newDIs[i].ItemName+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            DIWriter.writerow([newDIs[i].Name+"\HMIHMIW", newDIs[i].Group, newDIs[i].Comment+" - HMIHMIW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                               "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newDIs[i].AccessName, "No", newDIs[i].ItemName+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            DIWriter.writerow([newDIs[i].Name+"\HMICUSW", newDIs[i].Group, newDIs[i].Comment+" - HMICUSW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                               "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newDIs[i].AccessName, "No", newDIs[i].ItemName+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            DIWriter.writerow([newDIs[i].Name+"\HMICFGW", newDIs[i].Group, newDIs[i].Comment+" - HMICFGW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                               "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newDIs[i].AccessName, "No", newDIs[i].ItemName+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            DIWriter.writerow([newDIs[i].Name+"\HMIFIELDW", newDIs[i].Group, newDIs[i].Comment+" - HMIFIELDW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                               "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newDIs[i].AccessName, "No", newDIs[i].ItemName+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        DIWriter.writerow([":MemoryMsg", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority",
                           "RetentiveValue", "MaxLength", "InitialMessage", "AlarmComment", "SymbolicName", "LocalTag"])
        for i in range(newDINum):
            DIWriter.writerow([newDIs[i].Name+"\OBJ", newDIs[i].Group, newDIs[i].Comment +
                               " - OBJ", "No", "No", "0", "No", "131", "OP_DI_10", "", "", "No"])
        if newDINum > 1:
            DITemp = "s"
        else:
            DITemp = ""
        return "Created " + str(newDINum) + " new DI" + DITemp + " and saved to the file " + newFileName + ".csv"


def createM_3(newFileName, newM_3Num, newM_3s):
    """Creates a new M_3 supertag"""
    # Opens the output file and preps to write to it
    with open(newFileName+".csv", "w", newline="") as M_3Output:
        M_3Writer = writer(M_3Output)
        # Writes all the rows required
        M_3Writer.writerow([":mode=ask"])
        M_3Writer.writerow([":IODisc", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "InitialDisc", "OffMsg", "OnMsg", "AlarmState", "AlarmPri",
                           "Dconversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "DSCAlarmDisable", "DSCAlarmInhibitor", "SymbolicName"])
        for i in range(newM_3Num):
            M_3Writer.writerow([newM_3s[i].Name+"\OLA", newM_3s[i].Group, newM_3s[i].Comment+" - Overload Alarm", "Yes", "No", "0", "No", "Off", "", "", "On", "3",
                               "Direct", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.CMDW.09", "No", newM_3s[i].Comment+" - Overload Alarm", "0", "0", "", "", "No"])
            M_3Writer.writerow([newM_3s[i].Name+"\GEE", newM_3s[i].Group, newM_3s[i].Comment+" - Equipment Energized", "Yes", "No", "0", "No", "Off", "", "", "None", "3",
                               "Direct", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.STW.03", "No", newM_3s[i].Comment+" - Equipment Energized", "0", "0", "", "", "No"])
            M_3Writer.writerow([newM_3s[i].Name+"\GA", newM_3s[i].Group, newM_3s[i].Comment+" - General Alarm", "No", "Yes", "3", "No", "Off", "", "", "None", "3",
                               "Direct", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.STW.05", "No", newM_3s[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
            M_3Writer.writerow([newM_3s[i].Name+"\CRA", newM_3s[i].Group, newM_3s[i].Comment+" - Contactor Run Alarm", "Yes", "No", "0", "No", "Off", "", "", "On",
                               "3", "Direct", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.CMDW.10", "No", newM_3s[i].Comment+" - Contactor Run Alarm", "0", "0", "", "", "No"])
            M_3Writer.writerow([newM_3s[i].Name+"\CIA", newM_3s[i].Group, newM_3s[i].Comment+" - Isolated", "Yes", "No", "0", "No", "Off", "", "", "On",
                               "3", "Direct", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.CMDW.11", "No", newM_3s[i].Comment+" - Isolated", "0", "0", "", "", "No"])
            M_3Writer.writerow([newM_3s[i].Name+"\CBA", newM_3s[i].Group, newM_3s[i].Comment+" - Circuit Breaker Alarm", "Yes", "No", "0", "No", "Off", "", "", "On",
                               "3", "Direct", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.CMDW.08", "No", newM_3s[i].Comment+" - Circuit Breaker Alarm", "0", "0", "", "", "No"])
            M_3Writer.writerow([newM_3s[i].Name+"\BPA", newM_3s[i].Group, newM_3s[i].Comment+" - Push-Button Stop Alarm", "Yes", "No", "0", "No", "Off", "", "", "On",
                               "3", "Direct", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.CMDW.12", "No", newM_3s[i].Comment+" - Push-Button Stop Alarm", "0", "0", "", "", "No"])
        M_3Writer.writerow([":IOInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                           "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName"])
        for i in range(newM_3Num):
            M_3Writer.writerow([newM_3s[i].Name+"\HMISTW", newM_3s[i].Group, newM_3s[i].Comment+" - Status word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "0", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                               "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_3Writer.writerow([newM_3s[i].Name+"\HMIHMIW", newM_3s[i].Group, newM_3s[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "0", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                               "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_3Writer.writerow([newM_3s[i].Name+"\HMIFIELDW", newM_3s[i].Group, newM_3s[i].Comment+" - Field word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "0", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                               "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_3Writer.writerow([newM_3s[i].Name+"\HMICMDW", newM_3s[i].Group, newM_3s[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "0", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                               "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_3Writer.writerow([newM_3s[i].Name+"\HMICFGW", newM_3s[i].Group, newM_3s[i].Comment+" - Config word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "0", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                               "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        M_3Writer.writerow([":IOReal", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                           "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName"])
        for i in range(newM_3Num):
            M_3Writer.writerow([newM_3s[i].Name+"\IPV", newM_3s[i].Group, newM_3s[i].Comment+" - Motor Current", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "1", "0", "0.5", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                               "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "1", "Linear", newM_3s[i].AccessName, "No", newM_3s[i].ItemName+".IPV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        M_3Writer.writerow([":MemoryMsg", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority",
                           "RetentiveValue", "MaxLength", "InitialMessage", "AlarmComment", "SymbolicName", "LocalTag"])
        for i in range(newM_3Num):
            M_3Writer.writerow([newM_3s[i].Name+"\OBJ", newM_3s[i].Group, newM_3s[i].Comment +
                               " - Object", "No", "No", "0", "No", "131", "OP_M_3", "", "", "No"])
        if newM_3Num > 1:
            M_3Temp = "s"
        else:
            M_3Temp = ""
        return "Created " + str(newM_3Num) + " new M_3" + M_3Temp + " and saved to the file " + newFileName + ".csv"


def createM_10(newFileName, newM_10Num, newM_10s):
    """Creates a new M_10 supertag"""
    # Opens the output file and preps to write to it
    with open(newFileName+".csv", "w", newline="") as M_10Output:
        M_10Writer = writer(M_10Output)
        # Writes all the rows required
        M_10Writer.writerow([":mode=ask"])
        M_10Writer.writerow([":IODisc", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "InitialDisc", "OffMsg", "OnMsg", "AlarmState", "AlarmPri",
                             "Dconversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "DSCAlarmDisable", "DSCAlarmInhibitor", "SymbolicName"])
        for i in range(newM_10Num):
            M_10Writer.writerow([newM_10s[i].Name+"\GI", newM_10s[i].Group, newM_10s[i].Comment+" - General Inhibit", "No", "No", "0", "No", "Off", "", "", "None",
                                "3", "Direct", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.CMDW.09", "No", newM_10s[i].Comment+" - General Inhibit", "0", "0", "", ""])
            M_10Writer.writerow([newM_10s[i].Name+"\OLA", newM_10s[i].Group, newM_10s[i].Comment+" - Overload Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                "3", "Direct", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.CMDW.9", "No", newM_10s[i].Comment+" - Overload Alarm", "0", "0", "", ""])
            M_10Writer.writerow([newM_10s[i].Name+"\GEE", newM_10s[i].Group, newM_10s[i].Comment+" - Equipment Energize", "Yes", "No", "0", "No", "Off", "", "", "None",
                                "3", "Direct", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.STW.3", "No", newM_10s[i].Comment+" - Equipment Energize", "0", "0", "", ""])
            M_10Writer.writerow([newM_10s[i].Name+"\GA", newM_10s[i].Group, newM_10s[i].Comment+" - General Alarm", "Yes", "Yes", "3", "No", "Off", "", "", "None",
                                "3", "Direct", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.STW.05", "No", newM_10s[i].Comment+" - General Alarm", "0", "0", "", ""])
            M_10Writer.writerow([newM_10s[i].Name+"\CRA", newM_10s[i].Group, newM_10s[i].Comment+" - Run Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                "3", "Direct", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.CMDW.10", "No", newM_10s[i].Comment+" - Run Alarm", "0", "0", "", ""])
            M_10Writer.writerow([newM_10s[i].Name+"\CIA", newM_10s[i].Group, newM_10s[i].Comment+" - Isolated", "No", "No", "0", "No", "Off", "", "", "On",
                                "3", "Direct", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.CMDW.11", "No", newM_10s[i].Comment+" - Isolated", "0", "0", "", ""])
            M_10Writer.writerow([newM_10s[i].Name+"\CBA", newM_10s[i].Group, newM_10s[i].Comment+" - Tripped", "No", "No", "0", "No", "Off", "", "",
                                "On", "3", "Direct", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.CMDW.8", "No", newM_10s[i].Comment+" - Tripped", "0", "0"])
            M_10Writer.writerow([newM_10s[i].Name+"\BPA", newM_10s[i].Group, newM_10s[i].Comment+" - Stop Button", "No", "No", "0", "No", "Off", "", "", "On",
                                "3", "Direct", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.CMDW.12", "No", newM_10s[i].Comment+" - Stop Button", "0", "0", "", ""])
        M_10Writer.writerow([":MemoryInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinValue", "MaxValue", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue",
                            "MinorDevAlarmPri", "MajorDevAlarmState", "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", "LocalTag"])
        for i in range(newM_10Num):
            M_10Writer.writerow([newM_10s[i].Name+"\AccessLevel", newM_10s[i].Group, newM_10s[i].Comment+" - Access Level", "No", "No", "0", "No", "No", "0", "0", "", "5000", "0", "9999", "0", "1", "Off", "0", "1",
                                "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_10Writer.writerow([newM_10s[i].Name+"\Precision", newM_10s[i].Group, newM_10s[i].Comment+" - Precision", "No", "No", "0", "No", "No", "0", "0", "", "1", "0", "9999", "0", "1", "Off", "0", "1",
                                "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        M_10Writer.writerow([":IOInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                            "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", ""])
        for i in range(newM_10Num):
            M_10Writer.writerow([newM_10s[i].Name+"\HMICFGW", newM_10s[i].Group, newM_10s[i].Comment+" - Config Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_10Writer.writerow([newM_10s[i].Name+"\MAINTHMIW", newM_10s[i].Group, newM_10s[i].Comment+" - Maintenance Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".MAINT.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_10Writer.writerow([newM_10s[i].Name+"\HMISTW", newM_10s[i].Group, newM_10s[i].Comment+" - Status Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_10Writer.writerow([newM_10s[i].Name+"\HMIHMIW", newM_10s[i].Group, newM_10s[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_10Writer.writerow([newM_10s[i].Name+"\HMIFIELDW", newM_10s[i].Group, newM_10s[i].Comment+" - Field Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_10Writer.writerow([newM_10s[i].Name+"\HMICUSW", newM_10s[i].Group, newM_10s[i].Comment+" - Custom Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_10Writer.writerow([newM_10s[i].Name+"\HMICMDW", newM_10s[i].Group, newM_10s[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        M_10Writer.writerow([":IOReal", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                            "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", ""])
        for i in range(newM_10Num):
            M_10Writer.writerow([newM_10s[i].Name+"\MAINTOPESP", newM_10s[i].Group, newM_10s[i].Comment+" - Maintenance Operating Time Setpoint", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                                "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".MAINT.OPE_SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_10Writer.writerow([newM_10s[i].Name+"\MAINTOPETOT", newM_10s[i].Group, newM_10s[i].Comment+" - Total Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".MAINT.OPE_TOT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_10Writer.writerow([newM_10s[i].Name+"\MAINTOPE", newM_10s[i].Group, newM_10s[i].Comment+" - Maintenance Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                                "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".MAINT.OPE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            M_10Writer.writerow([newM_10s[i].Name+"\IPV", newM_10s[i].Group, newM_10s[i].Comment+" - Current", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newM_10s[i].AccessName, "No", newM_10s[i].ItemName+".IPV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        M_10Writer.writerow([":MemoryMsg", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority",
                             "RetentiveValue", "MaxLength", "InitialMessage", "AlarmComment", "SymbolicName", "LocalTag"])
        for i in range(newM_10Num):
            M_10Writer.writerow([newM_10s[i].Name+"\OBJ", newM_10s[i].Group, newM_10s[i].Comment +
                                " - Object", "No", "No", "0", "No", "131", "OP_M_10", "", "", "No"])
        if newM_10Num > 1:
            M_10Temp = "s"
        else:
            M_10Temp = ""
        return "Created " + str(newM_10Num) + " new M_10" + M_10Temp + " and saved to the file " + newFileName + ".csv"


def createMF_10(newFileName, newMF_10Num, newMF_10s):
    """Creates a new MF_10 supertag"""
    # Opens the output file and preps to write to it
    with open(newFileName+".csv", "w", newline="") as MF_10Output:
        MF_10Writer = writer(MF_10Output)
        # Writes all the rows required
        MF_10Writer.writerow([":mode=ask"])
        MF_10Writer.writerow([":IODisc", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "InitialDisc", "OffMsg", "OnMsg", "AlarmState", "AlarmPri",
                             "Dconversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "DSCAlarmDisable", "DSCAlarmInhibitor", "SymbolicName"])
        for i in range(newMF_10Num):
            MF_10Writer.writerow([newMF_10s[i].Name+"\RUNA", newMF_10s[i].Group, newMF_10s[i].Comment+" - Run Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                 "3", "Direct", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.CMDW.10", "No", newMF_10s[i].Comment+" - Run Alarm", "0", "0", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\RDYA", newMF_10s[i].Group, newMF_10s[i].Comment+" - Ready Status Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                 "3", "Direct", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.CMDW.9", "No", newMF_10s[i].Comment+" - Ready Status Alarm", "0", "0", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\GI", newMF_10s[i].Group, newMF_10s[i].Comment+" - General Inhibit", "Yes", "No", "0", "No", "Off", "", "", "None",
                                 "3", "Direct", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.STW.02", "No", newMF_10s[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\GEE", newMF_10s[i].Group, newMF_10s[i].Comment+" - Equipment Energize", "No", "No", "0", "No", "Off", "", "", "None",
                                 "3", "Direct", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.STW.3", "No", newMF_10s[i].Comment+" - Equipment Energize", "0", "0", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\GA", newMF_10s[i].Group, newMF_10s[i].Comment+" - General Alarm", "Yes", "No", "0", "No", "Off", "", "", "None",
                                 "3", "Direct", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.STW.05", "No", newMF_10s[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\ERRA", newMF_10s[i].Group, newMF_10s[i].Comment+" - Error", "No", "No", "0", "No", "Off", "", "", "On",
                                 "3", "Direct", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.CMDW.13", "No", newMF_10s[i].Comment+" - Error", "0", "0", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\CIA", newMF_10s[i].Group, newMF_10s[i].Comment+" - Isolated", "No", "No", "0", "No", "Off", "", "", "On", "3",
                                 "Direct", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.CMDW.11", "No", newMF_10s[i].Comment+" - Isolated", "0", "0", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\CBA", newMF_10s[i].Group, newMF_10s[i].Comment+" - Tripped", "No", "No", "0", "No", "Off", "", "", "On",
                                 "3", "Direct", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.CMDW.8", "No", newMF_10s[i].Comment+" - Tripped", "0", "0", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\BPA", newMF_10s[i].Group, newMF_10s[i].Comment+" - Stop Button", "No", "No", "0", "No", "Off", "", "", "On", "3",
                                 "Direct", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.CMDW.12", "No", newMF_10s[i].Comment+" - Stop Button", "0", "0", "", "", "No"])
        MF_10Writer.writerow([":MemoryInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinValue", "MaxValue", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue",
                              "MinorDevAlarmPri", "MajorDevAlarmState", "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", "LocalTag"])
        for i in range(newMF_10Num):
            MF_10Writer.writerow([newMF_10s[i].Name+"\AccessLevel", newMF_10s[i].Group, newMF_10s[i].Comment+" - Access Level", "No", "No", "0", "No", "No", "0", "0", "", "5000", "0", "9999", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\Precision", newMF_10s[i].Group, newMF_10s[i].Comment+" - Precision", "No", "No", "0", "No", "No", "0", "0", "", "1", "0", "9999", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        MF_10Writer.writerow([":IOInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                              "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", ""])
        for i in range(newMF_10Num):
            MF_10Writer.writerow([newMF_10s[i].Name+"\HMICFGW", newMF_10s[i].Group, newMF_10s[i].Comment+" - Config Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\MAINTHMIW", newMF_10s[i].Group, newMF_10s[i].Comment+" - Maintenance Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                  "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".MAINT.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\HMISTW", newMF_10s[i].Group, newMF_10s[i].Comment+" - Status Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\HMIHMIW", newMF_10s[i].Group, newMF_10s[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                  "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\HMIFIELDW", newMF_10s[i].Group, newMF_10s[i].Comment+" - Field Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\HMICUSW", newMF_10s[i].Group, newMF_10s[i].Comment+" - Custom Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\HMICMDW", newMF_10s[i].Group, newMF_10s[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        MF_10Writer.writerow([":IOReal", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                              "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", ""])
        for i in range(newMF_10Num):
            MF_10Writer.writerow([newMF_10s[i].Name+"\MAINTOPESP", newMF_10s[i].Group, newMF_10s[i].Comment+" - Maintenance Operating Time Setpoint", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                                  "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".MAINT.OPE_SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\MAINTOPETOT", newMF_10s[i].Group, newMF_10s[i].Comment+" - Total Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                  "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".MAINT.OPE_TOT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\MAINTOPE", newMF_10s[i].Group, newMF_10s[i].Comment+" - Maintenance Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                                  "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".MAINT.OPE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\AO", newMF_10s[i].Group, newMF_10s[i].Comment+" - Output", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                 "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".AO", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\JPV", newMF_10s[i].Group, newMF_10s[i].Comment+" - Power", "Yes", "No", "0", "No", "No", "0", "0", "kW", "0", "0", "35", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                 "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "35", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".JPV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\SPV", newMF_10s[i].Group, newMF_10s[i].Comment+" - Speed", "Yes", "No", "0", "No", "No", "0", "0", "rpm", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                 "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".SPV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\SPM", newMF_10s[i].Group, newMF_10s[i].Comment+" - Setpoint Manual", "Yes", "No", "0", "No", "No", "0", "0", "%", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                 "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".SPM", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\SP", newMF_10s[i].Group, newMF_10s[i].Comment+" - Setpoint", "Yes", "No", "0", "No", "No", "0", "0", "%", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                 "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            MF_10Writer.writerow([newMF_10s[i].Name+"\PV", newMF_10s[i].Group, newMF_10s[i].Comment+" - Process Value", "Yes", "No", "0", "No", "No", "0", "0", "%", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                 "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newMF_10s[i].AccessName, "No", newMF_10s[i].ItemName+".PV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        MF_10Writer.writerow([":MemoryMsg", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority",
                             "RetentiveValue", "MaxLength", "InitialMessage", "AlarmComment", "SymbolicName", "LocalTag"])
        for i in range(newMF_10Num):
            MF_10Writer.writerow([newMF_10s[i].Name+"\OBJ", newMF_10s[i].Group, newMF_10s[i].Comment +
                                  " - Object", "No", "No", "0", "No", "131", "OP_MF_10", "", "", "No"])
        if newMF_10Num > 1:
            MF_10Temp = "s"
        else:
            MF_10Temp = ""
        return "Created " + str(newMF_10Num) + " new MF_10" + MF_10Temp + " and saved to the file " + newFileName + ".csv"


def createFV1_10P(newFileName, newFV1_10PNum, newFV1_10Ps):
    """Creates a new FV1_10P supertag"""
    # Opens the output file and preps to write to it
    with open(newFileName+".csv", "w", newline="") as FV1_10POutput:
        FV1_10PWriter = writer(FV1_10POutput)
        # Writes all the rows required
        FV1_10PWriter.writerow([":mode=ask"])
        FV1_10PWriter.writerow([":IODisc", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "InitialDisc", "OffMsg", "OnMsg", "AlarmState", "AlarmPri",
                                "Dconversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "DSCAlarmDisable", "DSCAlarmInhibitor", "SymbolicName"])
        for i in range(newFV1_10PNum):
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\ZSOA", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Open Alarm", "Yes", "No", "0", "No", "Off", "", "", "On", "3", "Direct",
                                   newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].ItemName+".HMI.CMDW.13", "No", newFV1_10Ps[i].Comment+" - Open Alarm", "0", "0", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\ZSCA", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Close Alarm", "Yes", "No", "0", "No", "Off", "", "", "On", "3", "Direct",
                                   newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].ItemName+".HMI.CMDW.12", "No", newFV1_10Ps[i].Comment+" - Close Alarm", "0", "0", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\GI", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - General Inhibit", "No", "No", "0", "No", "Off", "", "", "None",
                                   "3", "Direct", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].ItemName+".HMI.STW.02", "No", newFV1_10Ps[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\GEE", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Equipment Energize", "Yes", "No", "0", "No", "Off", "",
                                   "", "None", "3", "Direct", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].ItemName+".HMI.STW.3", "No", newFV1_10Ps[i].Comment+" - Equipment Energize", "0", "0", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\GA", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - General Alarm", "No", "Yes", "3", "No", "Off", "", "",
                                   "None", "3", "Direct", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].ItemName+".HMI.STW.05", "No", newFV1_10Ps[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        FV1_10PWriter.writerow([":MemoryInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinValue", "MaxValue", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue",
                                "MinorDevAlarmPri", "MajorDevAlarmState", "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", "LocalTag"])
        for i in range(newFV1_10PNum):
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\Precision", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Precision", "No", "No", "0", "No", "No", "0", "0", "", "1", "0", "9999", "0", "1", "Off", "0",
                                   "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\AccessLevel", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Access Level", "No", "No", "0", "No", "No", "0", "0", "", "5000", "0", "9999", "0", "1", "Off",
                                   "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        FV1_10PWriter.writerow([":IOInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                                "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", ""])
        for i in range(newFV1_10PNum):
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\HMIHMIW", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                                   "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].Name+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\HMICFGW", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Config Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                   "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].Name+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\MAINTHMIW", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Maintenance Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                                   "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].Name+".MAINT.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\HMISTW", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Status Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                   "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].Name+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\HMIFIELDW", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Field Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                   "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].Name+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\HMICUSW", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Custom Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                   "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].Name+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\HMICMDW", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                   "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].Name+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        FV1_10PWriter.writerow([":IOReal", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                                "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", ""])
        for i in range(newFV1_10PNum):
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\MAINTOPETOT", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Total Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                                   "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].Name+".MAINT.OPE_TOT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\MAINTOPESP", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Maintenance Operating Time Setpoint", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                   "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].Name+".MAINT.OPE_SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\MAINTOPE", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment+" - Maintenance Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                   "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newFV1_10Ps[i].AccessName, "No", newFV1_10Ps[i].Name+".MAINT.OPE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        FV1_10PWriter.writerow([":MemoryMsg", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority",
                                "RetentiveValue", "MaxLength", "InitialMessage", "AlarmComment", "SymbolicName", "LocalTag"])
        for i in range(newFV1_10PNum):
            FV1_10PWriter.writerow([newFV1_10Ps[i].Name+"\OBJ", newFV1_10Ps[i].Group, newFV1_10Ps[i].Comment +
                                   " - Object", "No", "No", "0", "No", "131", "OP_FV1_10", "", "", "No"])
        if newFV1_10PNum > 1:
            FV1_10PTemp = "s"
        else:
            FV1_10PTemp = ""
        return "Created " + str(newFV1_10PNum) + " new FV1_10P" + FV1_10PTemp + " and saved to the file " + newFileName + ".csv"


def tesys(tesysFileName, tesysList):
    """Creates all the tags needed on SCADA from a Tesys unit"""
    with open(tesysFileName+".csv", "w", newline="") as tesysOutput:
        tesysWriter = writer(tesysOutput)
        tesysWriter.writerow([":mode=ask"])
        tesysWriter.writerow([":IODisc", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "InitialDisc", "OffMsg", "OnMsg", "AlarmState", "AlarmPri",
                              "Dconversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "DSCAlarmDisable", "DSCAlarmInhibitor", "SymbolicName"])
        for i in range(len(tesysList)):
            tesysWriter.writerow([tesysList[i]["Tag"]+"_ELI", "$System", tesysList[i]["Comment"]+" Isolator", "Yes", "No", "99", "No", "Off", "", "", "None", "99",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_ELI", "No", tesysList[i]["Comment"]+" Isolator", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_F1", "$System", tesysList[i]["Comment"]+" Tripped", "Yes", "No", "99", "No", "Off", "", "", "On", "1",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_F1", "No", tesysList[i]["Comment"]+" Tripped", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_F2", "$System", tesysList[i]["Comment"]+" Starter Off", "Yes", "No", "99", "No", "Off", "", "", "On", "1",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_F2", "No", tesysList[i]["Comment"]+" Starter Off", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_F3", "$System", tesysList[i]["Comment"]+" Isolated", "Yes", "No", "99", "No", "Off", "", "", "On", "1",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_F3", "No", tesysList[i]["Comment"]+" Isolated", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_F4", "$System", tesysList[i]["Comment"]+" Underload", "Yes", "No", "99", "No", "Off", "", "", "On", "1",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_F4", "No", tesysList[i]["Comment"]+" Underload", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_F5", "$System", tesysList[i]["Comment"]+" Run Fault", "Yes", "No", "99", "No", "Off", "", "", "On", "1",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_F5", "No", tesysList[i]["Comment"]+" Run Fault", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_F6", "$System", tesysList[i]["Comment"]+" Rotation Fault", "Yes", "No", "99", "No", "Off", "", "", "On", "1",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_F6", "No", tesysList[i]["Comment"]+" Rotation Fault", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_F7", "$System", tesysList[i]["Comment"]+" Handswitch Fault", "Yes", "No", "99", "No", "Off", "", "", "On", "1",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_F7", "No", tesysList[i]["Comment"]+" Handswitch Fault", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_GENERAL_F", "$System", tesysList[i]["Comment"]+" General Fault", "Yes", "Yes", "1", "No", "Off", "", "", "None", "99",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_GENERAL_F", "No", tesysList[i]["Comment"]+" General Fault", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_HS", "$System", tesysList[i]["Comment"]+" Handswitch", "Yes", "No", "99", "No", "Off", "", "", "None", "99",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_HS", "No", tesysList[i]["Comment"]+" Handswitch", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_MAINT_ST", "$System", tesysList[i]["Comment"]+" Maintenance Start", "No", "No", "99", "No", "Off", "", "", "None", "99",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_MAINT_ST", "No", tesysList[i]["Comment"]+" Maintenance Start", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_R", "$System", tesysList[i]["Comment"]+" Running", "Yes", "No", "99", "No", "Off", "", "", "None", "99",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_R", "No", tesysList[i]["Comment"]+" Running", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_RESET", "$System", tesysList[i]["Comment"]+" Reset Counts", "No", "No", "99", "No", "Off", "", "", "None", "99",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_RESET", "No", tesysList[i]["Comment"]+" Reset Counts", "0", "0", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_SSL", "$System", tesysList[i]["Comment"]+" Rotation Sensor", "Yes", "No", "99", "No", "Off", "", "", "None", "99",
                                  "Direct", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_SSL", "No", tesysList[i]["Comment"]+" Rotation Sensor", "0", "0", "", "", "No"])
        tesysWriter.writerow([":IOInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                              "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName"])
        for i in range(len(tesysList)):
            tesysWriter.writerow([tesysList[i]["Tag"]+"_CMND", "$System", tesysList[i]["Comment"]+" Command", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "0", "10", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "10", "Linear", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_CMND", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_FAULTS", "$System", tesysList[i]["Comment"]+" No. of Faults", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "32767", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "32767", "Linear", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_FAULTS", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_HOURS", "$System", tesysList[i]["Comment"]+" No. of Hours", "No", "No", "0", "No", "No", "0", "0", "Hours", "0", "0", "32767", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "32767", "Linear", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_HOURS", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_STARTS", "$System", tesysList[i]["Comment"]+" No. of Starts", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "32767", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "32767", "Linear", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_STARTS", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            tesysWriter.writerow([tesysList[i]["Tag"]+"_STAT", "$System", tesysList[i]["Comment"]+" Status", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "0", "10", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "10", "Linear", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_STAT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        tesysWriter.writerow([":IOReal", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                             "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName"])
        for i in range(len(tesysList)):
            tesysWriter.writerow([tesysList[i]["Tag"]+"_AC", "$System", tesysList[i]["Comment"]+" Actual Current", "Yes", "No", "0", "No", "No", "0", "0", "Amps", "0", "0", "200", "0", "0", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                                 "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "200", "Linear", tesysList[i]["AccessName"], "Yes", tesysList[i]["Tag"]+"_AC", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        if len(tesysList) == 1:
            return "Set of tags created"
        else:
            return "Sets of tags created"


def createFile(override):
    """Asks if an output file is required, and generates the name if so"""
    fileLoop = True
    while fileLoop == True:
        # Checks if a file is needed to be created without asking
        if override == False:
            fileReqd = input(
                "Create new file for discovered files? (Y/N) ").lower()
        else:
            fileReqd = "y"

        if fileReqd in ["y", "ye", "yes", "1", "true"] or override == True:
            fileLoop = False
            # If file required, gets the name
            newFileName = input("Name of the new file: ")
            if newFileName.lower().endswith(".csv"):
                return newFileName[:-4]
            else:
                return newFileName
        elif fileReqd in ["n", "no", "0", "false"]:
            # If not required, leaves the name blank
            fileLoop = False
            return ""
        else:
            print("Error: Expected answer \"yes\" or \"no\"")


def checkAnother(item):
    """Checks if more than one input is required"""
    moreInputs = input("Another "+item+"? (Y/N) ").lower().replace(" ", "")
    if moreInputs in ["y", "ye", "yes", "1", "true"]:
        return True
    elif moreInputs in ["n", "no", "0", "false"]:
        return False
    else:
        print("Error: \"Yes\" or \"No\" answer required")
        return checkAnother(item)


# Gathers which function is wanted, and runs the function to find/start it
findFunction(input(
    "Function type required (\"Find Tag\", \"Select Section\", \"DI\", \"M_3\", \"M_10\", \"FV1_10P\" or \"Tesys\"): ").lower().replace(" ", ""))

# Loops until the user states otherwise
while checkAnother("function") == True:
    findFunction(input(
        "Function type required (\"Find Tag\", \"Select Section\", \"DI\", \"M_3\", \"M_10\", \"FV1_10P\" or \"Tesys\"): ").lower().replace(" ", ""))
