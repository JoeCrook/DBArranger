from Functions.Misc import checkAnother, createFile, findFile
from Functions.NewSuper import createSuper
from Functions.FindTag import findTag
from Functions.SelectSection import selectSection
from Functions.Tesys import createTesys


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

        print(createTesys(createFile(True), tesysList))

    # Loops if the given function doesn't exist/isn't recognised
    else:
        print("Functions: \"Find Tag\", \"Select Section\", \"Super\", \"Tesys\"")
        findFunction(
            input("Function type required: ").lower().replace(" ", ""))
    return


# Gathers which function is wanted, and runs the function to find/start it
findFunction(input(
    "Function type required (\"Find Tag\", \"Select Section\", \"Super\" or \"Tesys\"): ").lower().replace(" ", ""))

# Loops until the user states otherwise
while checkAnother("function") == True:
    findFunction(input(
        "Function type required (\"Find Tag\", \"Select Section\", \"Super\" or \"Tesys\"): ").lower().replace(" ", ""))
