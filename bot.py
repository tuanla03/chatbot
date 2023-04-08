import pyttsx3
import speech_recognition
from datetime import date, datetime
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio) 
    except:
        you = ""
    print("You:" + you)
    if you == '':
        robot_brain = "I can't hear you, please try again."
    elif you == "hello":
        robot_brain = "Hi there!"
    elif you == "how are you":
        robot_brain = "i'm doing good, and you!"
    elif you == "what is today":
        today = date.today()
        robot_brain = today.strftime('%B %d, %Y')
    elif you == "what time is it":
        now = datetime.now()
        robot_brain = now.strftime('%H hours %M minutes %S seconds')       
    elif "bye" in you:
        robot_brain = "See you again!"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    