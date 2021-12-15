import re
import urllib

message = ""
while message != "bye":
    message = input(">> ")
    message = re.sub('[^A-Za-z0-9]+', ' ', message).strip().lower()
    file = open("datafile.txt", "r")
    filedata = file.readlines()
    file.close()

    foundflag = False
    for line in filedata:
        question = re.sub('[^A-Za-z0-9]+', ' ', (line.split(","))[0]).strip()   # to ignore the special characters, remove newline character
        answer = (line.strip().split(","))[1]
        if question == message:
            print(answer)
            foundflag = True
            break

    if foundflag == False:
        newans = input ("Teach me the answer to this >> ")
        file = open("testfile.txt", "a")
        file.write("\n" + message + "," + newans)