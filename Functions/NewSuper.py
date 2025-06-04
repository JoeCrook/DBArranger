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
        if self.Type.endswith("_lototo"):
            self.LOTOTO = True
        else:
            self.LOTOTO = False


def createSuper():
    """Creates a new Super supertag"""
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
    rowCount = rowCount + 1

    # Opens the output file and preps to write to it
    with open(newFileName+".csv", "w", newline="") as SuperOutput:
        SuperWriter = writer(SuperOutput)
        SuperWriter.writerow([":mode=ask"])

        # Writes all the IODisc tags
        SuperWriter.writerow([":IODisc", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "InitialDisc", "OffMsg", "OnMsg", "AlarmState", "AlarmPri",
                              "Dconversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "DSCAlarmDisable", "DSCAlarmInhibitor", "SymbolicName"])
        for i in range(rowCount):
            newSuperLoop(SuperWriter, NewSupers, i, "iodisc")

        # Writes all the MemoryInt tags
        SuperWriter.writerow([":MemoryInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinValue", "MaxValue", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue",
                              "MinorDevAlarmPri", "MajorDevAlarmState", "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName", "LocalTag"])
        for i in range(rowCount):
            newSuperLoop(SuperWriter, NewSupers, i, "memint")
            if NewSupers[i].LOTOTO:
                SuperWriter.writerow([NewSupers[i].Name+"\LOTOTOHMIW", NewSupers[i].Group, NewSupers[i].Comment+" - LOTOTO Word", "No", "No", "0", "No", "No", "0", "0", "", "1", "0", "65535", "0", "1", "Off", "0", "1",
                                      "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            SuperWriter.writerow([NewSupers[i].Name+"\Precision", NewSupers[i].Group, NewSupers[i].Comment+" - Precision", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "9999", "0", "1", "Off", "0", "1",
                                  "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
            SuperWriter.writerow([NewSupers[i].Name+"\AccessLevel", NewSupers[i].Group, NewSupers[i].Comment+" - AccessLevel", "No", "No", "0", "No", "No", "0", "0", "", "900", "0", "9999", "0", "1", "Off", "0",
                                  "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])

        # Writes all the IOInt tags
        SuperWriter.writerow([":IOInt", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                              "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName"])
        for i in range(rowCount):
            newSuperLoop(SuperWriter, NewSupers, i, "ioint")

        # Writes all the IOReal tags
        SuperWriter.writerow([":IOReal", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority", "RetentiveValue", "RetentiveAlarmParameters", "AlarmValueDeadband", "AlarmDevDeadband", "EngUnits", "InitialValue", "MinEU", "MaxEU", "Deadband", "LogDeadband", "LoLoAlarmState", "LoLoAlarmValue", "LoLoAlarmPri", "LoAlarmState", "LoAlarmValue", "LoAlarmPri", "HiAlarmState", "HiAlarmValue", "HiAlarmPri", "HiHiAlarmState", "HiHiAlarmValue", "HiHiAlarmPri", "MinorDevAlarmState", "MinorDevAlarmValue", "MinorDevAlarmPri", "MajorDevAlarmState",
                              "MajorDevAlarmValue", "MajorDevAlarmPri", "DevTarget", "ROCAlarmState", "ROCAlarmValue", "ROCAlarmPri", "ROCTimeBase", "MinRaw", "MaxRaw", "Conversion", "AccessName", "ItemUseTagname", "ItemName", "ReadOnly", "AlarmComment", "AlarmAckModel", "LoLoAlarmDisable", "LoAlarmDisable", "HiAlarmDisable", "HiHiAlarmDisable", "MinDevAlarmDisable", "MajDevAlarmDisable", "RocAlarmDisable", "LoLoAlarmInhibitor", "LoAlarmInhibitor", "HiAlarmInhibitor", "HiHiAlarmInhibitor", "MinDevAlarmInhibitor", "MajDevAlarmInhibitor", "RocAlarmInhibitor", "SymbolicName"])
        for i in range(rowCount):
            newSuperLoop(SuperWriter, NewSupers, i, "ioreal")

        # Writes all the MemoryMessage tags
        SuperWriter.writerow([":MemoryMsg", "Group", "Comment", "Logged", "EventLogged", "EventLoggingPriority",
                              "RetentiveValue", "MaxLength", "InitialMessage", "AlarmComment", "SymbolicName", "LocalTag"])
        for i in range(rowCount):
            SuperWriter.writerow([NewSupers[i].Name+"\OBJ", NewSupers[i].Group, NewSupers[i].Comment,
                                 "No", "No", "0", "No", "131", NewSupers[i].Type.upper(), "", "", "No"])

        return "Created " + str(rowCount) + " new Supertag(s) and saved to the file " + newFileName + ".csv"


def newSuperLoop(SuperWriter, NewSupers, i, section):
    if NewSupers[i].Type.startswith(("op_di_", "op_do_")):
        createDx(SuperWriter, NewSupers, i, section)
    elif NewSupers[i].Type.startswith(("op_m_", "op_mr_", "op_mv_")):
        createMx(SuperWriter, NewSupers, i, section)
    elif NewSupers[i].Type.startswith(("op_mf_")):
        createMF(SuperWriter, NewSupers, i, section)
    elif NewSupers[i].Type.startswith(("op_fv1_", "op_fv2_")):
        createFV1(SuperWriter, NewSupers, i, section)
    elif NewSupers[i].Type.startswith(("op_pmc_")):
        createPMC(SuperWriter, NewSupers, i, section)
    elif NewSupers[i].Type.startswith(("op_ai_")):
        createAI(SuperWriter, NewSupers, i, section)


def createDx(SuperWriter, NewSupers, i, section):
    """Creates a new DI or DO supertag"""
    # Writes all the rows required
    if section == "iodisc":
        SuperWriter.writerow([NewSupers[i].Name+"\DIW", NewSupers[i].Group, NewSupers[i].Comment+" - Digital Input Warning", "No", "Yes", "1", "No", "Off", "", "", "On", "3",
                              "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.09", "No", NewSupers[i].Comment+" - Digital Input Warning", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GI", NewSupers[i].Group, NewSupers[i].Comment+" - General Inhibit", "No", "No", "0", "No", "Off", "", "", "None", "1",
                              "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.STW.02", "No", NewSupers[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GA", NewSupers[i].Group, NewSupers[i].Comment+" - General Alarm", "No", "No", "0", "No", "Off", "", "", "None",
                              "1", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".GA", "No", NewSupers[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DIA", NewSupers[i].Group, NewSupers[i].Comment+" - Digital Input Alarm", "No", "Yes", "1", "No", "Off", "", "", "On", "3",
                              "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.08", "No", NewSupers[i].Comment+" - Digital Input Alarm", "0", "0", "", "", "No"])
    elif section == "ioint":
        SuperWriter.writerow([NewSupers[i].Name+"\HMICMDW", NewSupers[i].Group, NewSupers[i].Comment+" - HMICMDW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMISTW", NewSupers[i].Group, NewSupers[i].Comment+" - HMISTW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMIHMIW", NewSupers[i].Group, NewSupers[i].Comment+" - HMIHMIW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICUSW", NewSupers[i].Group, NewSupers[i].Comment+" - HMICUSW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICFGW", NewSupers[i].Group, NewSupers[i].Comment+" - HMICFGW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMIFIELDW", NewSupers[i].Group, NewSupers[i].Comment+" - HMIFIELDW", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                             "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        if NewSupers[i].Type in ["op_do_10"]:
            SuperWriter.writerow([NewSupers[i].Name+"\MAINTHMIW", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Word", "No", "No", "0", "No", "No", "0", "0", " ", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                                 "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
    elif section == "ioreal" and NewSupers[i].Type in ["op_do_10"]:
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPESP", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Operating Time Setpoint", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.OPE_SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPETOT", NewSupers[i].Group, NewSupers[i].Comment+" - Total Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.OPE_TOT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPE", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.OPE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])


def createMx(SuperWriter, NewSupers, i, section):
    """Creates a new M_10 supertag"""
    if section == "iodisc":
        SuperWriter.writerow([NewSupers[i].Name+"\GI", NewSupers[i].Group, NewSupers[i].Comment+" - General Inhibit", "No", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.09", "No", NewSupers[i].Comment+" - General Inhibit", "0", "0", "", ""])
        SuperWriter.writerow([NewSupers[i].Name+"\OLA", NewSupers[i].Group, NewSupers[i].Comment+" - Overload Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.9", "No", NewSupers[i].Comment+" - Overload Alarm", "0", "0", "", ""])
        SuperWriter.writerow([NewSupers[i].Name+"\GEE", NewSupers[i].Group, NewSupers[i].Comment+" - Equipment Energize", "Yes", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.STW.3", "No", NewSupers[i].Comment+" - Equipment Energize", "0", "0", "", ""])
        SuperWriter.writerow([NewSupers[i].Name+"\GA", NewSupers[i].Group, NewSupers[i].Comment+" - General Alarm", "Yes", "Yes", "3", "No", "Off", "", "", "None",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".GA", "No", NewSupers[i].Comment+" - General Alarm", "0", "0", "", ""])
        SuperWriter.writerow([NewSupers[i].Name+"\CIA", NewSupers[i].Group, NewSupers[i].Comment+" - Isolated", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.11", "No", NewSupers[i].Comment+" - Isolated", "0", "0", "", ""])
        SuperWriter.writerow([NewSupers[i].Name+"\CBA", NewSupers[i].Group, NewSupers[i].Comment+" - Tripped", "No", "No", "0", "No", "Off", "", "",
                              "On", "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.8", "No", NewSupers[i].Comment+" - Tripped", "0", "0"])
        if NewSupers[i].Type in ["op_m_10", "op_mr_10", "op_m_10_lototo"]:
            SuperWriter.writerow([NewSupers[i].Name+"\CRA", NewSupers[i].Group, NewSupers[i].Comment+" - Run Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                  "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.10", "No", NewSupers[i].Comment+" - Run Alarm", "0", "0", "", ""])
            SuperWriter.writerow([NewSupers[i].Name+"\BPA", NewSupers[i].Group, NewSupers[i].Comment+" - Stop Button", "No", "No", "0", "No", "Off", "", "", "On",
                                  "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.12", "No", NewSupers[i].Comment+" - Stop Button", "0", "0", "", ""])
        elif NewSupers[i].Type in ["op_mv_10"]:
            SuperWriter.writerow([NewSupers[i].Name+"\RUNA", NewSupers[i].Group, NewSupers[i].Comment+" - Run Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                  "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.10", "No", NewSupers[i].Comment+" - Run Alarm", "0", "0", "", ""])
            SuperWriter.writerow([NewSupers[i].Name+"\ZSCA", NewSupers[i].Group, NewSupers[i].Comment+" - Limit Switch Close Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                  "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.12", "No", NewSupers[i].Comment+" - Limit Switch Close Alarm", "0", "0", "", ""])
            SuperWriter.writerow([NewSupers[i].Name+"\ZSOA", NewSupers[i].Group, NewSupers[i].Comment+" - Limit Switch Open Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                                  "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.12", "No", NewSupers[i].Comment+" - Limit Switch Open Alarm", "0", "0", "", ""])

    elif section == "ioint":
        SuperWriter.writerow([NewSupers[i].Name+"\HMICFGW", NewSupers[i].Group, NewSupers[i].Comment+" - Config Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTHMIW", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMISTW", NewSupers[i].Group, NewSupers[i].Comment+" - Status Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMIHMIW", NewSupers[i].Group, NewSupers[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMIFIELDW", NewSupers[i].Group, NewSupers[i].Comment+" - Field Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICUSW", NewSupers[i].Group, NewSupers[i].Comment+" - Custom Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICMDW", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
    elif section == "ioreal":
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPESP", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Operating Time Setpoint", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.OPE_SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPETOT", NewSupers[i].Group, NewSupers[i].Comment+" - Total Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.OPE_TOT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPE", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.OPE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\IPV", NewSupers[i].Group, NewSupers[i].Comment+" - Current", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".IPV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])


def createMF(SuperWriter, NewSupers, i, section):
    if section == "iodisc":
        SuperWriter.writerow([NewSupers[i].Name+"\RUNA", NewSupers[i].Group, NewSupers[i].Comment+" - Run Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.10", "No", NewSupers[i].Comment+" - Run Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\RDYA", NewSupers[i].Group, NewSupers[i].Comment+" - Ready Status Alarm", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.9", "No", NewSupers[i].Comment+" - Ready Status Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GI", NewSupers[i].Group, NewSupers[i].Comment+" - General Inhibit", "Yes", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.STW.02", "No", NewSupers[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GEE", NewSupers[i].Group, NewSupers[i].Comment+" - Equipment Energize", "No", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.STW.3", "No", NewSupers[i].Comment+" - Equipment Energize", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GA", NewSupers[i].Group, NewSupers[i].Comment+" - General Alarm", "Yes", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.STW.05", "No", NewSupers[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\ERRA", NewSupers[i].Group, NewSupers[i].Comment+" - Error", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.13", "No", NewSupers[i].Comment+" - Error", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\CIA", NewSupers[i].Group, NewSupers[i].Comment+" - Isolated", "No", "No", "0", "No", "Off", "", "", "On", "3",
                              "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.11", "No", NewSupers[i].Comment+" - Isolated", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\CBA", NewSupers[i].Group, NewSupers[i].Comment+" - Tripped", "No", "No", "0", "No", "Off", "", "", "On",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.8", "No", NewSupers[i].Comment+" - Tripped", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\BPA", NewSupers[i].Group, NewSupers[i].Comment+" - Stop Button", "No", "No", "0", "No", "Off", "", "", "On", "3",
                              "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.12", "No", NewSupers[i].Comment+" - Stop Button", "0", "0", "", "", "No"])
    elif section == "ioint":
        SuperWriter.writerow([NewSupers[i].Name+"\HMICFGW", NewSupers[i].Group, NewSupers[i].Comment+" - Config Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTHMIW", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMISTW", NewSupers[i].Group, NewSupers[i].Comment+" - Status Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMIHMIW", NewSupers[i].Group, NewSupers[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMIFIELDW", NewSupers[i].Group, NewSupers[i].Comment+" - Field Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICUSW", NewSupers[i].Group, NewSupers[i].Comment+" - Custom Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICMDW", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
    elif section == "ioreal":
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPESP", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Operating Time Setpoint", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.OPE_SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPETOT", NewSupers[i].Group, NewSupers[i].Comment+" - Total Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.OPE_TOT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPE", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".MAINT.OPE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\AO", NewSupers[i].Group, NewSupers[i].Comment+" - Output", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".AO", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\JPV", NewSupers[i].Group, NewSupers[i].Comment+" - Power", "Yes", "No", "0", "No", "No", "0", "0", "kW", "0", "0", "35", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "35", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".JPV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\SPV", NewSupers[i].Group, NewSupers[i].Comment+" - Speed", "Yes", "No", "0", "No", "No", "0", "0", "rpm", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".SPV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\SPM", NewSupers[i].Group, NewSupers[i].Comment+" - Setpoint Manual", "Yes", "No", "0", "No", "No", "0", "0", "%", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".SPM", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\SP", NewSupers[i].Group, NewSupers[i].Comment+" - Setpoint", "Yes", "No", "0", "No", "No", "0", "0", "%", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\PV", NewSupers[i].Group, NewSupers[i].Comment+" - Process Value", "Yes", "No", "0", "No", "No", "0", "0", "%", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".PV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])


def createFV1(SuperWriter, NewSupers, i, section):
    if section == "iodisc":
        SuperWriter.writerow([NewSupers[i].Name+"\ZSOA", NewSupers[i].Group, NewSupers[i].Comment+" - Open Alarm", "Yes", "No", "0", "No", "Off", "", "", "On", "3", "Direct",
                              NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.13", "No", NewSupers[i].Comment+" - Open Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\ZSCA", NewSupers[i].Group, NewSupers[i].Comment+" - Close Alarm", "Yes", "No", "0", "No", "Off", "", "", "On", "3", "Direct",
                              NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.CMDW.12", "No", NewSupers[i].Comment+" - Close Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GI", NewSupers[i].Group, NewSupers[i].Comment+" - General Inhibit", "No", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.STW.02", "No", NewSupers[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GEE", NewSupers[i].Group, NewSupers[i].Comment+" - Equipment Energize", "Yes", "No", "0", "No", "Off", "",
                              "", "None", "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.STW.3", "No", NewSupers[i].Comment+" - Equipment Energize", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GA", NewSupers[i].Group, NewSupers[i].Comment+" - General Alarm", "No", "Yes", "3", "No", "Off", "", "",
                              "None", "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".HMI.STW.05", "No", NewSupers[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        if NewSupers[i].Type == "op_fv2_10":
            SuperWriter.writerow([NewSupers[i].Name+"\E1", NewSupers[i].Group, NewSupers[i].Comment+" - Energize Forward Output", "Yes", "No", "0",
                                 "No", "Off", "", "", "None", "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".E1", "No", "", "0", "0", "", "", "No"])
            SuperWriter.writerow([NewSupers[i].Name+"\E2", NewSupers[i].Group, NewSupers[i].Comment+" - Energize Reverse Output", "Yes", "No", "0",
                                 "No", "Off", "", "", "None", "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".E2", "No", "", "0", "0", "", "", "No"])
    elif section == "ioint":
        SuperWriter.writerow([NewSupers[i].Name+"\HMIHMIW", NewSupers[i].Group, NewSupers[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICFGW", NewSupers[i].Group, NewSupers[i].Comment+" - Config Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTHMIW", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".MAINT.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMISTW", NewSupers[i].Group, NewSupers[i].Comment+" - Status Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMIFIELDW", NewSupers[i].Group, NewSupers[i].Comment+" - Field Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICUSW", NewSupers[i].Group, NewSupers[i].Comment+" - Custom Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICMDW", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                              "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
    elif section == "ioreal":
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPETOT", NewSupers[i].Group, NewSupers[i].Comment+" - Total Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".MAINT.OPE_TOT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPESP", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Operating Time Setpoint", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".MAINT.OPE_SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MAINTOPE", NewSupers[i].Group, NewSupers[i].Comment+" - Maintenance Operating Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1",
                              "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".MAINT.OPE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])


def createPMC(SuperWriter, NewSupers, i, section):
    if section == "iodisc":
        SuperWriter.writerow([NewSupers[i].Name+"\GA", NewSupers[i].Group, NewSupers[i].Comment+" - General Alarm", "Yes", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".GA", "No", NewSupers[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GW", NewSupers[i].Group, NewSupers[i].Comment+" - General Warning", "Yes", "No", "0", "No", "Off", "", "", "None",
                              "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".GW", "No", NewSupers[i].Comment+" - General Warning", "0", "0", "", "", "No"])
    elif section == "ioint":
        SuperWriter.writerow([NewSupers[i].Name+"\CMD", NewSupers[i].Group, NewSupers[i].Comment+" - Command", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".CMD", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICFG", NewSupers[i].Group, NewSupers[i].Comment+" - Configuration", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMICFG", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\MODE", NewSupers[i].Group, NewSupers[i].Comment+" - Mode", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".MODE", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\SNO", NewSupers[i].Group, NewSupers[i].Comment+" - Sequence Step Number", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".S_NO", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\STAT", NewSupers[i].Group, NewSupers[i].Comment+" - Status", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".STAT", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
    elif section == "ioreal":
        SuperWriter.writerow([NewSupers[i].Name+"\STime", NewSupers[i].Group, NewSupers[i].Comment+" - Sequence Remaining Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                              "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].ItemName+".S_Time", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])


def createAI(SuperWriter, NewSupers, i, section):
    if section == "iodisc":
        SuperWriter.writerow([NewSupers[i].Name+"\GW", NewSupers[i].Group, NewSupers[i].Comment+" - General Warning", "Yes", "No", "3", "No", "Off", "0", "0",
                             "None", "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].Name+".GW", "No", NewSupers[i].Comment+" - General Warning", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\AH", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm High", "Yes", "No", "3", "No", "Off", "0", "0", "On",
                             "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.CMDW.09", "No", NewSupers[i].Comment+" - Alarm High", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\AL", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm Low", "Yes", "No", "3", "No", "Off", "0", "0", "On",
                             "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.CMDW.10", "No", NewSupers[i].Comment+" - Alarm Low", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GA", NewSupers[i].Group, NewSupers[i].Comment+" - General Alarm", "Yes", "Yes", "3", "No", "Off", "0", "0",
                             "None", "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].Name+".GA", "No", NewSupers[i].Comment+" - General Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GEE", NewSupers[i].Group, NewSupers[i].Comment+" - Equipment Energized", "Yes", "No", "3", "No", "Off", "0", "0", "None",
                             "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.STW.03", "No", NewSupers[i].Comment+" - Equipment Energized", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\GI", NewSupers[i].Group, NewSupers[i].Comment+" - General Inhibit", "No", "No", "3", "No", "Off", "0", "0", "None",
                             "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.STW.02", "No", NewSupers[i].Comment+" - General Inhibit", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\SQA", NewSupers[i].Group, NewSupers[i].Comment+" - Signal Quality Alarm", "Yes", "No", "3", "No", "Off", "0", "0", "On",
                             "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.CMDW.08", "No", NewSupers[i].Comment+" - Signal Quality Alarm", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\WH", NewSupers[i].Group, NewSupers[i].Comment+" - Warning High", "Yes", "No", "3", "No", "Off", "0", "0", "On",
                             "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.CMDW.11", "No", NewSupers[i].Comment+" - Warning High", "0", "0", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\WL", NewSupers[i].Group, NewSupers[i].Comment+" - Warning Low", "Yes", "No", "3", "No", "Off", "0", "0", "On",
                             "3", "Direct", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.CMDW.12", "No", NewSupers[i].Comment+" - Warning Low", "0", "0", "", "", "No"])
    elif section == "ioint":
        SuperWriter.writerow([NewSupers[i].Name+"\HMICFGW", NewSupers[i].Group, NewSupers[i].Comment+" - Config Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.CFGW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICMDW", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.CMDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMICUSW", NewSupers[i].Group, NewSupers[i].Comment+" - Custom Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.CUSW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMIFIELDW", NewSupers[i].Group, NewSupers[i].Comment+" - Field Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.FIELDW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMIHMIW", NewSupers[i].Group, NewSupers[i].Comment+" - Command Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.HMIW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\HMISTW", NewSupers[i].Group, NewSupers[i].Comment+" - Status Word", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "65535", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "65535", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".HMI.STW", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
    elif section == "ioreal":
        SuperWriter.writerow([NewSupers[i].Name+"\AI", NewSupers[i].Group, NewSupers[i].Comment+" - Process Value", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".AI", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGAHTIME", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm High Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.AH_TIME", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGALTIME", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm Low Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.AL_TIME", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGLAH", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm High Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.LAH", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGLAHD", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm High Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.LAHD", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGLAL", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm Low Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.LAL", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGLALD", NewSupers[i].Group, NewSupers[i].Comment+" - Alarm Low Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.LALD", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGLWH", NewSupers[i].Group, NewSupers[i].Comment+" - Warning High Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.LWH", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGLWHD", NewSupers[i].Group, NewSupers[i].Comment+" - Warning High Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.LWHD", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGLWL", NewSupers[i].Group, NewSupers[i].Comment+" - Warning Low Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.LWL", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGLWLD", NewSupers[i].Group, NewSupers[i].Comment+" - Warning Low Limit", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.LWLD", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGRH", NewSupers[i].Group, NewSupers[i].Comment+" - Range High", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.RH", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGRL", NewSupers[i].Group, NewSupers[i].Comment+" - Range Low", "No", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.RL", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGWHTIME", NewSupers[i].Group, NewSupers[i].Comment+" - Warning High Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off",
                             "0", "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.WH_TIME", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\DEVCFGWLTIME", NewSupers[i].Group, NewSupers[i].Comment+" - Warning Low Time", "No", "No", "0", "No", "No", "0", "0", "", "0", "-9999", "9999", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "-9999", "9999", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".DEVCFG.WL_TIME", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\PV", NewSupers[i].Group, NewSupers[i].Comment+" - Process Value", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".PV", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
        SuperWriter.writerow([NewSupers[i].Name+"\SP", NewSupers[i].Group, NewSupers[i].Comment+" - Setpoint", "Yes", "No", "0", "No", "No", "0", "0", "", "0", "0", "100", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0", "1", "Off", "0",
                             "1", "Off", "0", "1", "Off", "0", "1", "0", "Off", "0", "1", "Min", "0", "100", "Linear", NewSupers[i].AccessName, "No", NewSupers[i].Name+".SP", "No", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "", "", "", "", "", "No"])
