from csv import writer, reader
from Functions.Misc import findFile, createFile


class NewSuper:
    """A Class to store information about a new supertag"""

    def __init__(self, type, itemName, comment, group, accessName):
        self.Type = type.lower()
        self.ItemName = itemName
        self.Name = itemName
        self.Comment = comment
        self.Group = group
        self.AccessName = accessName


def createSuper(newFileName, rowCount, newSupers):
    print("Input file must have no headers, and have each new Super on it's own line, with info in the order: Supertag Type, PLC Name, Comment, Group, AccessName")
    # Creates the number of classes required and gathers required info
    NewSupers = []
    # Input file must have no headers, and have each new Super on it's own line, with info in the order: Supertag Type, Item Name, Comment, Group, AccessName
    with open(findFile() + ".csv", newline='', encoding='utf-8-sig') as SuperInput:
        SuperReader = reader(SuperInput, delimiter=',')
        next(SuperReader)
        for rowCount, row in enumerate(SuperReader):
            NewSupers.append(NewSuper(str(row[0]), str(
                row[1]), str(row[2]), str(row[3]), str(row[4])))

    newFileName = createFile(True)
    """Creates a new Super supertag"""
    # Opens the output file and preps to write to it
    with open(newFileName+".csv", "w", newline="") as SuperOutput:
        SuperWriter = writer(SuperOutput)
        SuperWriter.writerow([":mode=ask"])

        # Writes all the IODisc tags
        SuperWriter.writerow([":IODisc", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "InitialDisc", "OffMsg", "OnMsg", "AlarmState", "AlarmPri",
                              "Dconversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "DSCAlarmDisable", "DSCAlarmInhibitor", "SymbolicName"])
        for i in range(rowCount):
            newSuperLoop(SuperWriter, newSupers, i, "iodisc")

        # Writes all the MemoryInt tags
        SuperWriter.writerow([":MemoryInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinValue", "MaxValue", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue",
                              "MinorDevAlarmPri", "MajorDevAlarmState", "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", "LocalTag"])
        for i in range(rowCount):
            newSuperLoop(SuperWriter, newSupers, i, "memint")
            if newSupers[i].Type.endswith("_lototo"):
                SuperWriter.writerow([newSupers[i].Name+"\LOTOTOHMIW", newSupers[i].Group, newSupers[i].Comment+" - LOTOTO Word", "No", "No", "0", "No", "No", "0", "0", "", "1", "0", "65535", "0", "1", "Off", "0", "1",
                                      "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            SuperWriter.writerow([newSupers[i].Name+"\Precision", newSupers[i].Group, newSupers[i].Comment+" - Precision", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "9999", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            SuperWriter.writerow([newSupers[i].Name+"\AccessLevel", newSupers[i].Group, newSupers[i].Comment+" - AccessLevel", "No", "No", "0", "No", "No", "0", "0", "", "900", "0", "9999", "0", "1", "Off", "0",
                                  "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])

        # Writes all the IOInt tags
        SuperWriter.writerow([":IOInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                              "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName"])
        for i in range(rowCount):
            newSuperLoop(SuperWriter, newSupers, i, "ioint")

        # Writes all the IOReal tags
        SuperWriter.writerow([":IOReal", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                              "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName"])
        for i in range(rowCount):
            newSuperLoop(SuperWriter, newSupers, i, "ioreal")

        # Writes all the MemoryMessage tags
        SuperWriter.writerow([":MemoryMsg", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority",
                              "RetentiveValue", "MaxLength", "InitialMessage", "AlarmComment", "SymbolicName", "LocalTag"])
        for i in range(rowCount):
            SuperWriter.writerow([newSupers[i].Name+"\OBJ", newSupers[i].Group, newSupers[i].Comment,
                                 "No", "No", "0", "No", "131", newSupers[i].Type.upper(), "", "", "No"])

        return "Created " + str(rowCount) + " new Supertag(s) and saved to the file " + newFileName + ".csv"


def newSuperLoop(SuperWriter, newSupers, i, section):
    if newSupers[i].Type in ["op_di_3", "op_di_10"]:
        createDI(SuperWriter, newSupers, i, section)
    elif newSupers[i].Type in ["op_m_10", "op_m_10_lototo", "op_mr_10", "op_mv_10"]:
        createM_10(SuperWriter, newSupers, i, section)
    elif newSupers[i].Type == "op_mf_10":
        createMF_10(SuperWriter, newSupers, i, section)
    elif newSupers[i].Type in ["op_fv1_10", "op_fv2_10"]:
        createFV1_10P(SuperWriter, newSupers, i, section)
    elif newSupers[i].Type == "op_pmc_10":
        createPMC_10(SuperWriter, newSupers, i, section)
    elif newSupers[i].Type == "op_ai_10":
        createAI_10(SuperWriter, newSupers, i, section)


def createDI(SuperWriter, newSupers, i, section):
    """Creates a new DI supertag"""
    # Writes all the rows required
    if section == "iodisc":
        SuperWriter.writerow([newSupers[i].Name+"\DIW", newSupers[i].Group, newSupers[i].Comment+" - Digital Input Warning", "No", "Yes", "1", "No", "Off", "", "", "On", "3",
                              "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.09", "No", newSupers[i].Comment+" - Digital Input Warning", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GI", newSupers[i].Group, newSupers[i].Comment+" - General Inhibit", "No", "No", "0", "No", "Off", "", "", "None", "1",
                              "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.STW.02", "No", newSupers[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GA", newSupers[i].Group, newSupers[i].Comment+" - General Alarm", "No", "No", "0", "No", "Off", "", "", "None",
                              "1", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".GA", "No", newSupers[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DIA", newSupers[i].Group, newSupers[i].Comment+" - Digital Input Alarm", "No", "Yes", "1", "No", "Off", "", "", "On", "3",
                              "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.08", "No", newSupers[i].Comment+" - Digital Input Alarm", "0", "0", "", "", "No"])
    elif section == "ioint":
        SuperWriter.writerow([newSupers[i].Name+"\HMICMDW", newSupers[i].Group, newSupers[i].Comment+" - HMICMDW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMISTW", newSupers[i].Group, newSupers[i].Comment+" - HMISTW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMIHMIW", newSupers[i].Group, newSupers[i].Comment+" - HMIHMIW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICUSW", newSupers[i].Group, newSupers[i].Comment+" - HMICUSW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICFGW", newSupers[i].Group, newSupers[i].Comment+" - HMICFGW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMIFIELDW", newSupers[i].Group, newSupers[i].Comment+" - HMIFIELDW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])


def createM_10(SuperWriter, newSupers, i, section):
    """Creates a new M_10 supertag"""
    if section == "iodisc":
        SuperWriter.writerow([newSupers[i].Name+"\GI", newSupers[i].Group, newSupers[i].Comment+" - General Inhibit", "No", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.09", "No", newSupers[i].Comment+" - General Inhibit", "0", "0", "", ""])
        SuperWriter.writerow([newSupers[i].Name+"\OLA", newSupers[i].Group, newSupers[i].Comment+" - Overload Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.9", "No", newSupers[i].Comment+" - Overload Alarm", "0", "0", "", ""])
        SuperWriter.writerow([newSupers[i].Name+"\GEE", newSupers[i].Group, newSupers[i].Comment+" - Equipment Energize", "Yes", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.STW.3", "No", newSupers[i].Comment+" - Equipment Energize", "0", "0", "", ""])
        SuperWriter.writerow([newSupers[i].Name+"\GA", newSupers[i].Group, newSupers[i].Comment+" - General Alarm", "Yes", "Yes", "3", "No", "Off", "", "", "None",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".GA", "No", newSupers[i].Comment+" - General Alarm", "0", "0", "", ""])
        SuperWriter.writerow([newSupers[i].Name+"\CIA", newSupers[i].Group, newSupers[i].Comment+" - Isolated", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.11", "No", newSupers[i].Comment+" - Isolated", "0", "0", "", ""])
        SuperWriter.writerow([newSupers[i].Name+"\CBA", newSupers[i].Group, newSupers[i].Comment+" - Tripped", "No", "No", "0", "No", "Off", "", "",
                              "On", "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.8", "No", newSupers[i].Comment+" - Tripped", "0", "0"])
        if newSupers[i].Type in ["op_m_10", "op_mr_10", "op_m_10_lototo"]:
            SuperWriter.writerow([newSupers[i].Name+"\CRA", newSupers[i].Group, newSupers[i].Comment+" - Run Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                  "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.10", "No", newSupers[i].Comment+" - Run Alarm", "0", "0", "", ""])
            SuperWriter.writerow([newSupers[i].Name+"\BPA", newSupers[i].Group, newSupers[i].Comment+" - Stop Button", "No", "No", "0", "No", "Off", "", "", "On",
                                  "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.12", "No", newSupers[i].Comment+" - Stop Button", "0", "0", "", ""])
        elif newSupers[i].Type in ["op_mv_10"]:
            SuperWriter.writerow([newSupers[i].Name+"\RUNA", newSupers[i].Group, newSupers[i].Comment+" - Run Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                  "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.10", "No", newSupers[i].Comment+" - Run Alarm", "0", "0", "", ""])
            SuperWriter.writerow([newSupers[i].Name+"\ZSCA", newSupers[i].Group, newSupers[i].Comment+" - Limit Switch Close Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                  "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.12", "No", newSupers[i].Comment+" - Limit Switch Close Alarm", "0", "0", "", ""])
            SuperWriter.writerow([newSupers[i].Name+"\ZSOA", newSupers[i].Group, newSupers[i].Comment+" - Limit Switch Open Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                  "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.12", "No", newSupers[i].Comment+" - Limit Switch Open Alarm", "0", "0", "", ""])

    elif section == "ioint":
        SuperWriter.writerow([newSupers[i].Name+"\HMICFGW", newSupers[i].Group, newSupers[i].Comment+" - Config Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\MAINTHMIW", newSupers[i].Group, newSupers[i].Comment+" - Maintenance Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".MAINT.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMISTW", newSupers[i].Group, newSupers[i].Comment+" - Status Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMIHMIW", newSupers[i].Group, newSupers[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMIFIELDW", newSupers[i].Group, newSupers[i].Comment+" - Field Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICUSW", newSupers[i].Group, newSupers[i].Comment+" - Custom Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICMDW", newSupers[i].Group, newSupers[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
    elif section == "ioreal":
        SuperWriter.writerow([newSupers[i].Name+"\MAINTOPESP", newSupers[i].Group, newSupers[i].Comment+" - Maintenance Operating Time Setpoint", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".MAINT.OPE_SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\MAINTOPETOT", newSupers[i].Group, newSupers[i].Comment+" - Total Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".MAINT.OPE_TOT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\MAINTOPE", newSupers[i].Group, newSupers[i].Comment+" - Maintenance Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".MAINT.OPE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\IPV", newSupers[i].Group, newSupers[i].Comment+" - Current", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".IPV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])


def createMF_10(SuperWriter, newSupers, i, section):
    if section == "iodisc":
        SuperWriter.writerow([newSupers[i].Name+"\RUNA", newSupers[i].Group, newSupers[i].Comment+" - Run Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.10", "No", newSupers[i].Comment+" - Run Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\RDYA", newSupers[i].Group, newSupers[i].Comment+" - Ready Status Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.9", "No", newSupers[i].Comment+" - Ready Status Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GI", newSupers[i].Group, newSupers[i].Comment+" - General Inhibit", "Yes", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.STW.02", "No", newSupers[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GEE", newSupers[i].Group, newSupers[i].Comment+" - Equipment Energize", "No", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.STW.3", "No", newSupers[i].Comment+" - Equipment Energize", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GA", newSupers[i].Group, newSupers[i].Comment+" - General Alarm", "Yes", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.STW.05", "No", newSupers[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\ERRA", newSupers[i].Group, newSupers[i].Comment+" - Error", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.13", "No", newSupers[i].Comment+" - Error", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\CIA", newSupers[i].Group, newSupers[i].Comment+" - Isolated", "No", "No", "0", "No", "Off", "", "", "On", "3",
                              "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.11", "No", newSupers[i].Comment+" - Isolated", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\CBA", newSupers[i].Group, newSupers[i].Comment+" - Tripped", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.8", "No", newSupers[i].Comment+" - Tripped", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\BPA", newSupers[i].Group, newSupers[i].Comment+" - Stop Button", "No", "No", "0", "No", "Off", "", "", "On", "3",
                              "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.12", "No", newSupers[i].Comment+" - Stop Button", "0", "0", "", "", "No"])
    elif section == "ioint":
        SuperWriter.writerow([newSupers[i].Name+"\HMICFGW", newSupers[i].Group, newSupers[i].Comment+" - Config Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\MAINTHMIW", newSupers[i].Group, newSupers[i].Comment+" - Maintenance Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".MAINT.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMISTW", newSupers[i].Group, newSupers[i].Comment+" - Status Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMIHMIW", newSupers[i].Group, newSupers[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMIFIELDW", newSupers[i].Group, newSupers[i].Comment+" - Field Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICUSW", newSupers[i].Group, newSupers[i].Comment+" - Custom Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICMDW", newSupers[i].Group, newSupers[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
    elif section == "ioreal":
        SuperWriter.writerow([newSupers[i].Name+"\MAINTOPESP", newSupers[i].Group, newSupers[i].Comment+" - Maintenance Operating Time Setpoint", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".MAINT.OPE_SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\MAINTOPETOT", newSupers[i].Group, newSupers[i].Comment+" - Total Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".MAINT.OPE_TOT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\MAINTOPE", newSupers[i].Group, newSupers[i].Comment+" - Maintenance Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".MAINT.OPE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\AO", newSupers[i].Group, newSupers[i].Comment+" - Output", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".AO", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\JPV", newSupers[i].Group, newSupers[i].Comment+" - Power", "Yes", "No", "0", "No", "No", "0", "0", "kW", "0", "0", "35", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "35", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".JPV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\SPV", newSupers[i].Group, newSupers[i].Comment+" - Speed", "Yes", "No", "0", "No", "No", "0", "0", "rpm", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".SPV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\SPM", newSupers[i].Group, newSupers[i].Comment+" - Setpoint Manual", "Yes", "No", "0", "No", "No", "0", "0", "%", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".SPM", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\SP", newSupers[i].Group, newSupers[i].Comment+" - Setpoint", "Yes", "No", "0", "No", "No", "0", "0", "%", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\PV", newSupers[i].Group, newSupers[i].Comment+" - Process Value", "Yes", "No", "0", "No", "No", "0", "0", "%", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".PV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])


def createFV1_10P(SuperWriter, newSupers, i, section):
    if section == "iodisc":
        SuperWriter.writerow([newSupers[i].Name+"\ZSOA", newSupers[i].Group, newSupers[i].Comment+" - Open Alarm", "Yes", "No", "0", "No", "Off", "", "", "On", "3", "Direct",
                              newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.13", "No", newSupers[i].Comment+" - Open Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\ZSCA", newSupers[i].Group, newSupers[i].Comment+" - Close Alarm", "Yes", "No", "0", "No", "Off", "", "", "On", "3", "Direct",
                              newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.CMDW.12", "No", newSupers[i].Comment+" - Close Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GI", newSupers[i].Group, newSupers[i].Comment+" - General Inhibit", "No", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.STW.02", "No", newSupers[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GEE", newSupers[i].Group, newSupers[i].Comment+" - Equipment Energize", "Yes", "No", "0", "No", "Off", "",
                              "", "None", "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.STW.3", "No", newSupers[i].Comment+" - Equipment Energize", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GA", newSupers[i].Group, newSupers[i].Comment+" - General Alarm", "No", "Yes", "3", "No", "Off", "", "",
                              "None", "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".HMI.STW.05", "No", newSupers[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        if newSupers[i].Type == "op_fv2_10":
            SuperWriter.writerow([newSupers[i].Name+"\E1", newSupers[i].Group, newSupers[i].Comment+" - Energize Forward Output", "Yes", "No", "0",
                                 "No", "Off", "", "", "None", "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".E1", "No", "", "0", "0", "", "", "No"])
            SuperWriter.writerow([newSupers[i].Name+"\E2", newSupers[i].Group, newSupers[i].Comment+" - Energize Reverse Output", "Yes", "No", "0",
                                 "No", "Off", "", "", "None", "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".E2", "No", "", "0", "0", "", "", "No"])
    elif section == "ioint":
        SuperWriter.writerow([newSupers[i].Name+"\HMIHMIW", newSupers[i].Group, newSupers[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICFGW", newSupers[i].Group, newSupers[i].Comment+" - Config Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\MAINTHMIW", newSupers[i].Group, newSupers[i].Comment+" - Maintenance Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".MAINT.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMISTW", newSupers[i].Group, newSupers[i].Comment+" - Status Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMIFIELDW", newSupers[i].Group, newSupers[i].Comment+" - Field Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICUSW", newSupers[i].Group, newSupers[i].Comment+" - Custom Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICMDW", newSupers[i].Group, newSupers[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
    elif section == "ioreal":
        SuperWriter.writerow([newSupers[i].Name+"\MAINTOPETOT", newSupers[i].Group, newSupers[i].Comment+" - Total Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".MAINT.OPE_TOT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\MAINTOPESP", newSupers[i].Group, newSupers[i].Comment+" - Maintenance Operating Time Setpoint", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".MAINT.OPE_SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\MAINTOPE", newSupers[i].Group, newSupers[i].Comment+" - Maintenance Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".MAINT.OPE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])


def createPMC_10(SuperWriter, newSupers, i, section):
    if section == "iodisc":
        SuperWriter.writerow([newSupers[i].Name+"\GA", newSupers[i].Group, newSupers[i].Comment+" - General Alarm", "Yes", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".GA", "No", newSupers[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GW", newSupers[i].Group, newSupers[i].Comment+" - General Warning", "Yes", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].ItemName+".GW", "No", newSupers[i].Comment+" - General Warning", "0", "0", "", "", "No"])
    elif section == "ioint":
        SuperWriter.writerow([newSupers[i].Name+"\CMD", newSupers[i].Group, newSupers[i].Comment+" - Command", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".CMD", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICFG", newSupers[i].Group, newSupers[i].Comment+" - Configuration", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMICFG", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\MODE", newSupers[i].Group, newSupers[i].Comment+" - Mode", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".MODE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\SNO", newSupers[i].Group, newSupers[i].Comment+" - Sequence Step Number", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".S_NO", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\STAT", newSupers[i].Group, newSupers[i].Comment+" - Status", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".STAT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
    elif section == "ioreal":
        SuperWriter.writerow([newSupers[i].Name+"\STime", newSupers[i].Group, newSupers[i].Comment+" - Sequence Remaining Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].ItemName+".S_Time", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])


def createAI_10(SuperWriter, newSupers, i, section):
    if section == "iodisc":
        SuperWriter.writerow([newSupers[i].Name+"\GW", newSupers[i].Group, newSupers[i].Comment+" - General Warning", "Yes", "No", "3", "No", "Off", "0", "0",
                             "None", "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].Name+".GW", "No", newSupers[i].Comment+" - General Warning", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\AH", newSupers[i].Group, newSupers[i].Comment+" - Alarm High", "Yes", "No", "3", "No", "Off", "0", "0", "On",
                             "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.CMDW.09", "No", newSupers[i].Comment+" - Alarm High", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\AL", newSupers[i].Group, newSupers[i].Comment+" - Alarm Low", "Yes", "No", "3", "No", "Off", "0", "0", "On",
                             "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.CMDW.10", "No", newSupers[i].Comment+" - Alarm Low", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GA", newSupers[i].Group, newSupers[i].Comment+" - General Alarm", "Yes", "Yes", "3", "No", "Off", "0", "0",
                             "None", "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].Name+".GA", "No", newSupers[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GEE", newSupers[i].Group, newSupers[i].Comment+" - Equipment Energized", "Yes", "No", "3", "No", "Off", "0", "0", "None",
                             "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.STW.03", "No", newSupers[i].Comment+" - Equipment Energized", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\GI", newSupers[i].Group, newSupers[i].Comment+" - General Inhibit", "No", "No", "3", "No", "Off", "0", "0", "None",
                             "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.STW.02", "No", newSupers[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\SQA", newSupers[i].Group, newSupers[i].Comment+" - Signal Quality Alarm", "Yes", "No", "3", "No", "Off", "0", "0", "On",
                             "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.CMDW.08", "No", newSupers[i].Comment+" - Signal Quality Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\WH", newSupers[i].Group, newSupers[i].Comment+" - Warning High", "Yes", "No", "3", "No", "Off", "0", "0", "On",
                             "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.CMDW.11", "No", newSupers[i].Comment+" - Warning High", "0", "0", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\WL", newSupers[i].Group, newSupers[i].Comment+" - Warning Low", "Yes", "No", "3", "No", "Off", "0", "0", "On",
                             "3", "Direct", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.CMDW.12", "No", newSupers[i].Comment+" - Warning Low", "0", "0", "", "", "No"])
    elif section == "ioint":
        SuperWriter.writerow([newSupers[i].Name+"\HMICFGW", newSupers[i].Group, newSupers[i].Comment+" - Config Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICMDW", newSupers[i].Group, newSupers[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMICUSW", newSupers[i].Group, newSupers[i].Comment+" - Custom Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMIFIELDW", newSupers[i].Group, newSupers[i].Comment+" - Field Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMIHMIW", newSupers[i].Group, newSupers[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\HMISTW", newSupers[i].Group, newSupers[i].Comment+" - Status Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
    elif section == "ioreal":
        SuperWriter.writerow([newSupers[i].Name+"\AI", newSupers[i].Group, newSupers[i].Comment+" - Process Value", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".AI", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGAHTIME", newSupers[i].Group, newSupers[i].Comment+" - Alarm High Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.AH_TIME", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGALTIME", newSupers[i].Group, newSupers[i].Comment+" - Alarm Low Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.AL_TIME", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGLAH", newSupers[i].Group, newSupers[i].Comment+" - Alarm High Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.LAH", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGLAHD", newSupers[i].Group, newSupers[i].Comment+" - Alarm High Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.LAHD", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGLAL", newSupers[i].Group, newSupers[i].Comment+" - Alarm Low Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.LAL", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGLALD", newSupers[i].Group, newSupers[i].Comment+" - Alarm Low Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.LALD", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGLWH", newSupers[i].Group, newSupers[i].Comment+" - Warning High Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.LWH", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGLWHD", newSupers[i].Group, newSupers[i].Comment+" - Warning High Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.LWHD", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGLWL", newSupers[i].Group, newSupers[i].Comment+" - Warning Low Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.LWL", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGLWLD", newSupers[i].Group, newSupers[i].Comment+" - Warning Low Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.LWLD", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGRH", newSupers[i].Group, newSupers[i].Comment+" - Range High", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.RH", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGRL", newSupers[i].Group, newSupers[i].Comment+" - Range Low", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.RL", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGWHTIME", newSupers[i].Group, newSupers[i].Comment+" - Warning High Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.WH_TIME", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\DEVCFGWLTIME", newSupers[i].Group, newSupers[i].Comment+" - Warning Low Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".DEVCFG.WL_TIME", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\PV", newSupers[i].Group, newSupers[i].Comment+" - Process Value", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".PV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([newSupers[i].Name+"\SP", newSupers[i].Group, newSupers[i].Comment+" - Setpoint", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", newSupers[i].AccessName, "No", newSupers[i].Name+".SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
