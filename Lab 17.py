#This Program decodes a coded message.
#Created by: Chris Caponi

def get_data(fileName):
#Description: Opens the file, reads the coded message
#Parameters: The name of the file
#Return: The coded message 
    fileIn = open(fileName, "r")
    mCoded = (fileIn.read())

    return mCoded


def breakDown(mCoded):
#Description: Breaks down the code into substrings of 5 characters. Populates a list with each chunk (append).
#Parameters: The coded message
#Return: the list populated
    codeList = []
    n = 5
    for index in range(0, len(mCoded), n):
        codeList.append(mCoded[index : index + n])

    return codeList


def decodeMessage(codeList):
#Description: Extracts the 3rd character of each entry in the list and builds the decoded message letter by letter
#Parameters: The list
#Return: Decoded message
    for x in range(len(codeList)):
        mDecoded = print(codeList[x][2])

    return mDecoded

def main():
    fileName = input("What is the name of the file you want to open? ")
    coded = get_data(fileName)
    newList = breakDown(coded)
    cracked = decodeMessage(newList)
    print(cracked)

main()