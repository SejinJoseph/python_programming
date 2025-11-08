import subprocess as sp
count=0

while True:
    sp.Popen("cmd.exe")
    sp.Popen("notepad.exe")
    sp.Popen("python.exe")
    count+=1
    if count==1000:
        break
    else:
        print("dammit bloody brat stop.....")
    