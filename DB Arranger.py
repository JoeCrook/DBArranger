import csv
import os.path

# Finds the function required, and gathers/passes the information needed to run
def findFunction(functionCheck):
    # Function that finds a given tag in a database, and optionally saves it to a file
    if functionCheck in ["findtag", "ft"]:
        moreTags = True
        tagList = []
        while moreTags == True:
            requiredTag = input("Tag to search for: ").lower()
            if requiredTag.startswith(":"):
                requiredTag = requiredTag[1:]
            else:
                tagList += [requiredTag]
            moreTags = checkAnother("tag")

        print(findTag(createFile(), tagList))
    
    # Function that selects a certain section of tags, and saves them only to a file
    elif functionCheck in ["selectsection", "selsec", "ss"]:
        # Discovers which section is required
        moreSections = True
        sections = []
        while moreSections == True:
            sections.append(input("Which section to keep: ").lower())
            moreSections = checkAnother("section")
            
        print(selectSection(createFile(), sections))
    
    # Loops if the given function doesn't exist/isn't recognised
    else:
        print("Functions: \"Find Tag\", \"Select Section\"")
        findFunction(input("Function type required: ").lower().replace(" ",""))
    
    return


# Function that finds a given tag in a database, and optionally saves it to a file
def findTag(newFileName, requiredTag):
    tagCount = 0
    # Opens the given base file
    with open(fileName+".csv", newline='') as DBInput:
        # If an output file is required, creates one and prepares to write to it
        if newFileName != "":
            DBOutput = open(newFileName+".csv", "w", newline = "")
            DBWriter = csv.writer(DBOutput)
        DBReader = csv.reader(DBInput, delimiter=',')
        # Reads the given base file row by row
        for row in DBReader:
            if row[0].lower().startswith(":mode="):
                if newFileName != "":
                        DBWriter.writerow(row)
                continue
            # If the first cell (the "tag") in the row contains the given requiredTag, increments the tag count, prints the whole row, and writes it to the output file if enabled)
            for tag in requiredTag:
                if tag in row[0].lower():
                    if headerWritten == False:
                        if newFileName != "":
                            DBWriter.writerow(currentHeader)
                        headerWritten = True
                    tagCount += 1
                    print(', '.join(row))
                    if newFileName != "":
                        DBWriter.writerow(row)
                # If the row is a section header, and an output file is required, write the row to the output file
                elif row[0].lower().startswith(":"):
                    headerWritten = False
                    currentHeader = row
    
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


# Function that selects a certain section of tags, and saves them only to a file
def selectSection(newFileName, sections):
    correctSection = False
    with open(fileName+".csv", newline="") as DBInput:
        DBReader = csv.reader(DBInput, delimiter=',')
        with open(newFileName+".csv", "w", newline = "") as DBOutput:
            if newFileName != "":
                DBWriter = csv.writer(DBOutput)
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


# Asks if an output file is required, and generates the name if so
def createFile():
    fileLoop = True
    while fileLoop == True:
        fileReqd = input("Create new file for discovered files? ").lower()
        if fileReqd in ["y", "ye", "yes", "1"]:
            fileLoop = False
            # If file required, gets the name
            newFileName = input("Name of new file: ")
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


# Checks if more than one input is required
def checkAnother(type):
    moreInputs = input("Another "+type+"? ").lower().replace(" ","")
    if moreInputs in ["y", "ye", "yes", "1"]:
        return True
    elif moreInputs in ["n", "no", "0"]:
        moreInputs = False
    else:
        print("Error: \"Yes\" or \"No\" answer required")
        return checkAnother(type)


# Loops until the user states otherwise
loop = True
while loop == True:
    fileLoop = True
    while fileLoop == True:
        # Gathers the name of the csv file to be checked
        fileName = input("Name of the CSV file: ").lower()
        if fileName.endswith(".csv"):
            fileName = fileName[:-4]
        # Loops asking for the file name if the given one doesn't exist
        if not os.path.isfile(fileName+".csv"):
            print("File doesn't exist!")
        else:
            fileLoop = False


    # Gathers which function is wanted, and runs the function to find/start it
    findFunction(input("Function type required: ").lower().replace(" ",""))

    # Determines if a loop is needed for another function
    loop = input("Run another function? ")
    if loop in ["y", "ye", "yes", "1"]:
        loop = True
    elif loop in ["n", "no", "0"]:
        loop = False
    else:
        print("Error: Expected answer \"yes\" or \"no\"")