print("Starting...") #Program booting
print("Importing libs...")
import random
import time
import sys
import os
print("Done!")
print("===============================================")
print("Magma Terminal 1.1.0 loaded succesfully!")
print("For help, type 'help'.")
print("===============================================")


while True: #Main loop
    cmd = input("Enter command: ") #Getting and executing command
    if cmd == "echo":
        param = input("Enter parameter: ")
        print(param)
    elif cmd == "help":
        print("Normal commands:")
        print("======================================================================")
        print("exit - exits program")
        print("echo - prints message")
        print("help - shows this message")
        print("showProjectTemplate - shows what project template has inside")
        print("setPath - activates path targeted mode")
        print("======================================================================")
        print("Path targeted commands:")
        print("======================================================================")
        print("createProject - creates project from template in directory")
        print("deleteFiles - deletes all files in directory")
        print("createProject - creates folder")
        print("dir - shows files in directory")
        print("======================================================================")
    elif cmd == "showProjectTemplate":
        print("Basic project template has:")
        print("=============================")
        print("File 'main.py'")
        print("Folder 'assets'")
        print("=============================")
    elif cmd == "setPath":
        param = input("Enter target folder: ")
        pathNow = param
        print("Path target mode enabled!")
        print("Type 'exit' to enter normal mode.")
        while True:
            cmd = input(pathNow + ": ") #Path targeted mode
            if cmd == "exit":
                break
            if cmd == "createProject":
                projectName = input("Enter project name: ")
                dirName = pathNow + "/" + projectName
                os.mkdir(dirName)
                dirName = dirName + "/" + "assets"
                os.mkdir(dirName)
                dirName = pathNow + "/" + projectName
                open(dirName + "/main.py", 'w')
                print("Project created succesfully!")
            elif cmd == "deleteFiles": 
                allFiles = os.listdir(pathNow)
                for i in allFiles:
                    name, extension = os.path.splitext(i)
                    if extension == "":
                        os.rmdir(pathNow + "/" + i)
                        print("Deleted " + i)
                    else:
                        os.remove(pathNow + "/" + i)
                        print("Deleted " + i)
            elif cmd == "createFolder":
                folderName = input("Enter name: ")
                dirName = pathNow + "/" + folderName
                os.mkdir(dirName)
            elif cmd == "dir":
                allFiles = os.listdir(pathNow)
                print(allFiles)


    elif cmd == "exit":
        print("Exiting...")
        sys.exit()
    else:
        print('Command not found!') #Command not found script
