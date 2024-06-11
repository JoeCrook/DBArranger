# Updated 2024-05-28

from csv import writer, reader
from os.path import isfile


class NewDI:
    """A Class to store information about a new DI supertag"""

    def __init__(self, group, comment, accessName, itemName):
        name = itemName.replace("_", "")
        self.Name = str(name)
        self.Group = str(group)
        self.Comment = str(comment)
        self.AccessName = str(accessName)
        self.ItemName = str(itemName)


def findFile():
    """Finds the base CSV file and loops if not correct"""
    while True:
        # Gathers the name of the csv file to be checked
        fileName = input("Name of the CSV file: ").lower()
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

        print(findTag(fileName, createFile(False), tagList))

    # Function that selects a certain section of tags, and saves them only to a file
    elif functionCheck in ["selectsection", "selsec", "ss"]:
        fileName = findFile()
        # Discovers which section is required
        moreSections = True
        sections = []
        while moreSections == True:
            sections.append(input("Which section to keep: ").lower())
            moreSections = checkAnother("section")

        print(selectSection(fileName, createFile(False), sections))

    # Function that creates a new DI supertag
    elif functionCheck in ["di"]:
        while True:
            inputFile = input("Use an input csv file?: ")
            if inputFile in ["y", "ye", "yes", "1"]:
                inputFile = True
                DIReader = reader(open(findFile()+".csv", "w", newline=""))
                break
            elif inputFile in ["n", "no", "0"]:
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
        for i in range(newDINum):
            newDIs.append(input("New DI #" + str(i + 1) + " Group: "), input("New DI #" + str(i + 1) + " Comment: "),
                          input("New DI #" + str(i + 1) + " AccessName: "), input("New DI #" + str(i + 1di) + " ItemName: "))

        createDI(createFile(True), newDINum, newDIs)

    # Loops if the given function doesn't exist/isn't recognised
    else:
        print("Functions: \"Find Tag\", \"Select Section\", \"DI\"")
        findFunction(
            input("Function type required: ").lower().replace(" ", ""))
    return


def findTag(fileName, newFileName, requiredTag):
    """Finds a given tag in a database, and optionally saves it to a file"""
    tagCount = 0
    # Opens the given base file
    with open(fileName + ".csv", newline='') as DBInput:
        # If an output file is required, creates one and prepares to write to it
        if newFileName != "":
            DBOutput = open(newFileName + ".csv", "w", newline="")
            DBWriter = writer(DBOutput)
        DBReader = reader(DBInput, delimiter=',')
        # Reads the given base file row by row
        for row in DBReader:
            if row[0].lower().startswith(":mode="):
                if newFileName != "":
                    DBWriter.writerow(row)
                continue
            # If the first cell (the "tag") in the row contains the given requiredTag, increments the tag count, prints the whole row, and writes it to the output file if enabled)
            for tag in requiredTag:
                # If the row is a section header, and an output file is required, write the row to the output file
                if row[0].lower().startswith(":"):
                    headerWritten = False
                    currentHeader = row
                elif tag in row[0].lower():
                    if headerWritten == False:
                        if newFileName != "":
                            DBWriter.writerow(currentHeader)
                        headerWritten = True
                    tagCount += 1
                    print(', '.join(row))
                    if newFileName != "":
                        DBWriter.writerow(row)

    # Closes the output file if used
    if newFileName != "":
        DBOutput.close()

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
    DIWriter = writer(open(newFileName+".csv", "w", newline=""))

    # Writes all the rows required
    DIWriter.writerow([":mode=ask"])
    DIWriter.writerow([":IODisc", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "InitialDisc", "OffMsg", "OnMsg", "AlarmState", "AlarmPri",
                      "Dconversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "DSCAlarmDisable", "DSCAlarmInhibitor", "SymbolicName"])
    for i in range(newDINum):
        DIWriter.writerow([newDIs[i].Name+"\DIW", newDIs[i].Group, newDIs[i].Comment+" - Digital Input Warning", "No", "Yes", "1", "No", "Off", "", "", "On", "1",
                          "Direct", newDIs[i].AccessName, "No", newDIs[i].ItemName+".HMI.CMDW.09", "No", newDIs[i].Comment+" - Digital Input Warning", "0", "0", "", "", "No"])
        DIWriter.writerow([newDIs[i].Name+"\GI", newDIs[i].Group, newDIs[i].Comment+" - General Inhibit", "No", "No", "0", "No", "Off", "", "", "None", "1",
                          "Direct", newDIs[i].AccessName, "No", newDIs[i].ItemName+".HMI.STW.02", "No", newDIs[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
        DIWriter.writerow([newDIs[i].Name+"\GA", newDIs[i].Group, newDIs[i].Comment+" - General Alarm", "No", "No", "0", "No", "Off", "", "", "None",
                          "1", "Direct", newDIs[i].AccessName, "No", newDIs[i].ItemName+".GA", "No", newDIs[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        DIWriter.writerow([newDIs[i].Name+"\DIA", newDIs[i].Group, newDIs[i].Comment+" - Digital Input Alarm", "No", "Yes", "1", "No", "Off", "", "", "On", "1",
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
    return


def createFile(override):
    """Asks if an output file is required, and generates the name if so"""
    fileLoop = True
    while fileLoop == True:
        # Checks if a file is needed to be created without asking
        if override == False:
            fileReqd = input("Create new file for discovered files? ").lower()
        else:
            fileReqd = "y"

        if fileReqd in ["y", "ye", "yes", "1"] or override == True:
            fileLoop = False
            # If file required, gets the name
            newFileName = input("Name of the new file: ")
            if newFileName.lower().endswith(".csv"):
                return newFileName[:-4]
            else:
                return newFileName
        elif fileReqd in ["n", "no", "0"]:
            # If not required, leaves the name blank
            fileLoop = False
            return ""
        else:
            print("Error: Expected answer \"yes\" or \"no\"")


def checkAnother(item):
    """Checks if more than one input is required"""
    moreInputs = input("Another "+item+"? ").lower().replace(" ", "")
    if moreInputs in ["y", "ye", "yes", "1"]:
        return True
    elif moreInputs in ["n", "no", "0"]:
        return False
    else:
        print("Error: \"Yes\" or \"No\" answer required")
        return checkAnother(item)


# Gathers which function is wanted, and runs the function to find/start it
findFunction(input(
    "Function type required (\"Find Tag\", \"Select Section\" or \"DI\"): ").lower().replace(" ", ""))

# Loops until the user states otherwise
while checkAnother("function") == True:
    findFunction(input(
        "Function type required (\"Find Tag\", \"Select Section\" or \"DI\"): ").lower().replace(" ", ""))
