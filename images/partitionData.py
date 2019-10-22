import glob
import os
import shutil

# Open the directory 


for i in range(17):

    temp = str(i)

    if i < 10: 
        temp = "0" + str(i) 

    path = "./" + temp

    fileList = os.listdir(path)
    trainPath = "train/" + temp
    validatePath = "validation/" + temp
    testPath = "test/" + temp

    lengthTrain = int(len(fileList) * .70)
    lengthValidation = int(len(fileList) * .10) + lengthTrain
    
    if not os.path.isdir(trainPath):
        os.mkdir(trainPath)
    if not os.path.isdir(validatePath):
        os.mkdir(validatePath)
    if not os.path.isdir(testPath):
        os.mkdir(testPath)

        

    counter = 0
    
    for filename in fileList:
        if counter <  lengthTrain:
            shutil.copyfile(path + "/" + filename, trainPath + "/" + filename)
        elif counter < lengthValidation:
            shutil.copyfile(path + "/" + filename, validatePath + "/" + filename)
        else:
            shutil.copyfile(path + "/" + filename, testPath + "/" + filename)
            

        counter = counter + 1

# Get the number of files in the directory

# Calculate 70, 20 , and 10 percent of that

# Store into vars that represent 70(train), 20(validaiton), 10(Test)

# move the corresponding number percentage into the right NEW folder
