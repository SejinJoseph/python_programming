import subprocess as stejin
i=0
while True:
    stejin.Popen("notepad.exe")
    stejin.Popen("cmd.exe")
    stejin.Popen("python.exe")
    stejin.Popen("chrome.exe")
    i=i+1
    if i==200:
        break
    else:
        print("bloody brat how dare you....")
