import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")
print("Welcome to Robo Speaker 1.2")
while True:
    x = input("Enter what you want to speack :")
    if x == "q":
        speak.Speak(" Byeeeeeee")
        break
    speak.Speak(x)
