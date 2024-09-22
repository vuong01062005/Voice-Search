import speech_recognition
import pyttsx3
from datetime import date, datetime
import webbrowser as wb

def speak(robot_brain):
    robot_mouth.setProperty('voice', robot_mouth.getProperty('voices')[1].id)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    
def listen(audio):
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)
    return you

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ''
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        speak("I'm Listening")
        audio = robot_ear.listen(mic)
        
    print('Robot: ...')
        
    you = listen(audio)

    if you == '':
        robot_brain = "I can't here you, try again"
    elif 'hello' in you:
        robot_brain = "Hello Dinh Vuong"
    elif 'today' in you:
        today = date.today()
        robot_brain = today.strftime('%B %d, %Y')
    elif 'today' in you:
        now = datetime.now()
        robot_brain = now.strftime('%H hours %M minutes %S seconds')
    elif 'bye' in you:
        robot_brain = 'GoodBye'
        speak(robot_brain)
        break
    elif ('open google' in you) or ('google' in you):
        with speech_recognition.Microphone() as mic:
            print("What should I search boss")
            speak('What should I search boss')
            audio = robot_ear.listen(mic)
        search = listen(audio)
        search = search.lower()
        url = f'https://www.google.com/search?q={search}'
        wb.get().open(url)
        robot_brain = f'Here is your {search} on Google'
    elif ('open youtube' in you) or ('youtube' in you):
        with speech_recognition.Microphone() as mic:
            print("What should I search boss")
            speak('What should I search boss')
            audio = robot_ear.listen(mic)
        search = listen(audio)
        search = search.lower()
        url = f'https://www.youtube.com/search?q={search}'
        wb.get().open(url)
        robot_brain = f'Here is your {search} on Youtube'
    else:
        robot_brain = "I'm fine thank you and you"
        
    print(robot_brain)
    speak(robot_brain)