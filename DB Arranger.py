from csv import writer, reader
from Functions.NewSuper import createSuper
from Functions.FindTag import findTag
from Functions.SelectSection import selectSection
from Functions.Misc import findFile, createFile


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

    elif functionCheck in ["super"]:

        print(createSuper())

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
        print("Functions: \"Find Tag\", \"Select Section\", \"Super\", \"Tesys\"")
        findFunction(
            input("Function type required: ").lower().replace(" ", ""))
    return


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
        return "Set(s) of tags created"


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
    "Function type required (\"Find Tag\", \"Select Section\", \"Super\" or \"Tesys\"): ").lower().replace(" ", ""))

# Loops until the user states otherwise
while checkAnother("function") == True:
    findFunction(input(
        "Function type required (\"Find Tag\", \"Select Section\", \"Super\" or \"Tesys\"): ").lower().replace(" ", ""))
