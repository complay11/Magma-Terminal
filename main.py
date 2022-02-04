print("Starting...") #Program booting
print("Importing libs...")
import random
import time
import sys
import os
import ctypes
import threading
print("Defining terminal functions...")
def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin
print("Defining variables...")
exclusiveMode = False
space = str(" "*10)
print("Done!")
time.sleep(0.03)
os.system('title Magma Terminal v1.2.0')
print("===============================================")
print("Magma Terminal 1.2.0 loaded succesfully!")
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
        print("reboot - reboots program")
        print("showProjectTemplate - shows what project template has inside")
        print("setPath - activates path targeted mode")
        print("installLibaries - install libaries for exclusive commands (requires python)")
        print("reinstallLibs - uninstalls and installs libs ")
        print("activateExclusiveMode - activates exclusive mode (libs need to be installed)")
        print("loadMod - loads mod .py file")
        print("======================================================================")
        print("Exclusive Commands:")
        print("startServer - create remote server (for best efficiency and no bugs, use hamachi or radmin VPN)")
        print("startClient - connect to remote server (for best efficiency and no bugs, use hamachi or radmin VPN)")
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
    elif cmd == "loadMod":
        try:
            import MagmaTerminalAPI
        except:
            print("Cannot find mod!")
    elif cmd == 'installLibaries':
        if isAdmin():
            os.system('cls')
            print("Installing libs in 3")
            time.sleep(1)
            os.system('cls')
            print("Installing libs in 2")
            time.sleep(1)
            os.system('cls')
            print("Installing libs in 1")
            time.sleep(1)
            os.system('cls')
            os.system('pip install sockets')
            os.system("pip install PySimpleGUI")
            sys.exit()
        else:
            print("Please run program as administrator to continue...")
            time.sleep(3)
            sys.exit()
    elif cmd == "activateExclusiveMode":
        print("Activating exclusive mode...")
        os.system('cls')
        try:
            import socket
            import PySimpleGUI as sg
            exclusiveMode = True
            print("Imported succesful!")
        except:
            print("Error! Cannot import!")
    elif cmd == "reinstallLibs":
        if isAdmin():
            try:
                print("Uninstalling libs...")
                os.system("pip remove socket")
                os.system("pip remove PySimpleGUI")
                os.system("cls")
                print("Installing libs...")
                os.system("pip install socket")
                os.system("pip install PySimpleGUI")
                os.system("cls")
            except:
                print("Error! Cannot reinstall!")
        else:
            print("Please run program as administrator to continue...")
            time.sleep(3)
            sys.exit()
    elif cmd == "startUIMode":
        if exclusiveMode == True:
            output = ['Started succesfully!']   

            layout = [[sg.Text('Enter command')],
                     [sg.Listbox(output, key='-LIST-')],      
                     [[sg.InputText(key='-IN-')],      
                     [sg.Button('Run'), sg.Button('Exit')]]]    

            window = sg.Window('Magma Terminal EXPERIMENTAL UI Mode', layout)    
            
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    sys.exit()
                if event == "Run":
                    output.append(values['-IN-'])
                    
        else:  
            print("Activate exclusive mode!")
    elif cmd == "startServer":
        if exclusiveMode == True:
            HEADER = 64
            PORT = 5050
            SERVER = socket.gethostbyname(socket.gethostname())
            ADDR = (SERVER, PORT)
            FORMAT = 'utf-8'
            DISCONNECT_MESSAGE = "!DISCONNECT"
            serverShutdown = False

            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(ADDR)
            def handle_client(conn, addr):
                print(f"[NEW CONNECTION] {addr} connected.")

                connected = True
                while connected:
                    msg_length = conn.recv(HEADER).decode(FORMAT)
                    if msg_length:
                        
                        msg_length = int(msg_length)
                        msg = conn.recv(msg_length).decode(FORMAT)
                        if msg == DISCONNECT_MESSAGE:
                            connected = False
                        if msg == "setPath":
                            while msg != "setPath":
                                pathNow = msg
                        if msg == "dir":
                            allFiles = os.listdir(pathNow)
                            filesNumber = allFiles.count
                            conn.send(allFiles).encode(2048)
                            for i in allFiles:
                                filePath = pathNow + "/" + i
                                fileSize = os.path.getsize(filePath)
                                fileName, fileType = os.path.splitext(i)
                                print(fileName + "   ", end='')
                                print(fileType + "   ", end='')
                                print(fileSize)
                    print(f"[{addr}] {msg}")
                conn.close()

            def start():
                server.listen()
                print(f"[LISTENING] Server is listening on {SERVER}")
                while True:
                    if serverShutdown == True:
                        print("Shutting down...")
                        sys.exit()
                    conn, addr, = server.accept()
                    thread = threading.Thread(target=handle_client, args=(conn, addr))
                    thread.start()
                    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            
            print("===================CONSOLE===========================")
            print("[STARTING] server is starting...")
            start()
        else:
            print("Enable exclusive mode!")
    elif cmd == "startClient":
        if exclusiveMode == True:
            HEADER = 64
            PORT = 5050
            FORMAT = 'utf-8'
            DISCONNECT_MESSAGE = "!DISCONNECT"
            SERVER = input("Enter server IP: ")
            ADDR = (SERVER, PORT)

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            
            def send(msg):
                message = msg.encode(FORMAT)
                msg_length = len(message)
                send_length = str(msg_length).encode(FORMAT)
                send_length += b' ' * (HEADER - len(send_length))
                client.send(send_length)
                client.send(message)

            while True:
                messageToSend = input("Enter message: ")
                if messageToSend == "!DISCONNECT":
                    send(messageToSend)
                    sys.exit()
                if messageToSend == "!CMD":
                    cmdCommand = input("Enter CMD Command: ")
                    send("cmd")
                    time.sleep(2)
                    send(messageToSend)
                if messageToSend == "dir":
                    filesNumber = client.recv(2048).decode(FORMAT)
                    for i in range(filesNumber):
                        print(client.recv(2048).decode(FORMAT))
                else:
                    send(messageToSend)
                    os.system('cls')

        else:
            print("Enable exclusive mode!")
    elif cmd == "reboot":
        os.system('start Rebootal.bat')
        sys.exit()
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
                print("WARNING! If you chosen system folder or disk, this can damage your PC!")
                decision = input("(Y/N)")
                if decision != 'Y':
                    sys.exit()
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
                for i in allFiles:
                    filePath = pathNow + "/" + i
                    fileSize = os.path.getsize(filePath)
                    fileName, fileType = os.path.splitext(i)
                    print(fileName + "   ", end='')
                    print(fileType + "   ", end='')
                    print(fileSize)


    elif cmd == "exit":
        print("Exiting...")
        sys.exit()
    else:
        print('Command not found!') #Command not found script
