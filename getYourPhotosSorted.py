import shutil
from os import stat, listdir, path, makedirs
from datetime import datetime


def whenWasThePhotoTaken(pathTOThePhoto):
    theDate = stat(pathTOThePhoto).st_birthtime
    # the stat function retrieves the status of a file
    # it has a lot of attributes that talk about different aspects
    # of the file like st_size which extracts the size of the file
    # and may more.
    # But for now we only need the date of creation of the file
    # which we can access using st_birthtime

    theDateFormat = datetime.fromtimestamp(theDate).strftime('%B %d, %Y')
    # B gets a month's full name, the others are pretty straight forward
    # to understand

    return (theDateFormat)


def sortThemAll(pathTotheFolder):

    if not path.exists(pathTotheFolder):
        print ("You led me the wrong path.")
        print ("All these bad things are happening because of you.")


    for aFile in listdir(pathTotheFolder):
        theFilePath = path.join(pathTotheFolder, aFile)

        if path.isdir(theFilePath):
            continue

        theFileDate = whenWasThePhotoTaken(theFilePath)
        theFolderName = "Photos from {}".format(theFileDate)
        dateFolder = path.join(pathTotheFolder, theFolderName)

        if not path.exists(dateFolder):
            makedirs(dateFolder, exist_ok=True)

        if path.exists(dateFolder):
            shutil.move(theFilePath, path.join(dateFolder, aFile))

    print ("The Operation was successful.")
    print ("All the infinty stones have been collected.")
    print ("You can rest now.")


if __name__ == "__main__":
    theFolderToBeSorted = '/Users/Neftalem/Documents/Photos off my phone/To be deleted'
    sortThemAll(theFolderToBeSorted)
