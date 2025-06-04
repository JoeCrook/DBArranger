from csv import writer, reader
from Functions.Misc import findFile, checkAnother, createFile


def findTag():
    """Finds a given tag in a database, and optionally saves it to a file"""
    fileName = findFile()
    newFileName = createFile(True)
    moreTags = True
    tagList = []
    while moreTags == True:
        requiredTag = input("Tag to search for: ").lower()
        if requiredTag.startswith(":"):
            requiredTag = requiredTag[1:]
        else:
            tagList += [requiredTag]
        moreTags = checkAnother("tag")
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
                # If the first cell (the "tag") in the row contains the given tagList, increments the tag count, prints the whole row, and writes it to the output file if enabled)
                for tag in tagList:
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
