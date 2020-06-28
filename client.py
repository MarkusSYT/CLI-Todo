import socket
import sys

def Help():
    print("Hier kommen die Befehle noch rein. Bitte etwas Geduld ;)")

try:
    if(sys.argv[1] == '-l'):
        if(sys.argv[2] == '-new'):
            with open(".todosaves") as f:
                lines = f.readlines()
                file = open(".todosaves", "w")
                file.writelines(lines)
                file.write(sys.argv[3] + " [0]\n")
                try:
                    if(sys.argv[4] == '-d'):
                        file.write("\t" + sys.argv[5] + "\n")
                except:
                    print()
                file.close()
        elif(sys.argv[2] == '-close'):
            with open(".todosaves") as f:
                lines = f.readlines()
                i = 0
                for item in lines:
                    if(item == sys.argv[3] + ' [0]\n'):
                        lines[i] = lines[i][:-4]
                        lines[i] = lines[i] + "[1]\n"
                        break
                    i=i+1
                file = open(".todosaves", "w")
                file.writelines(lines)
                file.close()
        elif(sys.argv[2] == '-clear'):
            file = open(".todosaves", "w")
            file.write("")
            file.close()
        elif(sys.argv[2] == '-list'):
            with open(".todosaves") as f:
                lines = f.readlines()
                for item in lines:
                    print(item)
    elif(sys.argv[1] == '-c'):
        host = str(sys.argv[2])
        port = 4444
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(sys.argv[2].encode())
        #data = s.recv(1024)
        s.close()
    else:
        Help()
except:
    Help()

