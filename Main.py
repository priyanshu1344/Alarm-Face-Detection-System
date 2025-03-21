import threading
import cv2
from deepface import DeepFace
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from subprocess import call
import pygame
import time

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

pygame.mixer.init()
alarm_sound = pygame.mixer.Sound("Mixkit.wav")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False
reference_img = cv2.imread("Priyanshu.jpg")
     

def check_face(frame):
    global face_match
    try:
        result = DeepFace.verify(frame, reference_img.copy())
        if result['verified']:
            face_match = True
        else:
            face_match = False
            execute_alarm_code()  # Execute alarm code when there is no face match
    except Exception as e:
        print("Error during face recognition:", str(e))
        face_match = False
        execute_alarm_code()


def execute_alarm_code():
    alarm_sound.play()
    print("Face not matched - Executing alarm code")


def execute_voice_code():
    command = take_voice_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'Who is' in command:
        person = command.replace('Who is', '')
        about = wikipedia.search(person)
        about = wikipedia.summary(person, sentences=1)
        print(about)
        talk(about)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single ' in command:
        talk('I am in a relationship with Priyanshu')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif 'are you single ' in command:
        talk('I am in a realationship with Priyanshu')
    elif 'track iss' in command:
        open_py_space()
    elif 'Snake game' in command:
        open_py_game()
    elif 'hack laptop' in command:
        open_py_rotater()
    elif 'massage' in command:
        open_py_massage()
    elif 'take attendance' in command:
        open_py_attendance()
    else:
        talk('Please say the command again. ')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def open_py_space():
    call(["python", "Space.py"])


def open_py_game():
    call(["python", "Snake game.py"])


def open_py_rotater():
    call(["python", "Rotater.py"])


def open_py_massage():
    call(["python", "Massage.py"])


def open_py_attendance():
    call(["python", "Attendance.py"])


def take_voice_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = r.listen(source)
            command = r.recognize_google(voice)
            command = command.lower()
            if 'priyanshu' in command:
                command = command.replace('priyanshu', '')
                print(command)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
    return command


def run_priyanshu():
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'are you single ' in command:
            talk('I am in a realationship with Priyanshu')
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            print(time)
        elif 'Who is' in command:
            person = command.replace('Who is', '')
            about = wikipedia.search(person)
            about = wikipedia.summary(person, sentences=1)
            print(about)
            talk(about)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single ' in command:
            talk('I am in a realationship with Priyanshu')
        elif 'track iss' in command:
            open_py_space()
        elif 'Snake game' in command:
            open_py_game()
        elif 'hack laptop' in command:
            open_py_rotater()
        elif 'massage' in command:
            open_py_massage()
        elif 'take attendance' in command:
            open_py_attendance()
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
            print(joke)
        else:
            talk('Please say the command again. ')

        time.sleep(10)


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = r.listen(source)
            command = r.recognize_google(voice)
            command = command.lower()
            if 'priyanshu' in command:
                command = command.replace('priyanshu', '')
                print(command)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
    return command


def main():
    global counter
    while True:
        ret, frame = cap.read()

        if ret:
            if counter % 30 == 0:
                try:
                    threading.Thread(target=check_face, args=(frame.copy(),)).start()
                except ValueError:
                    pass
            counter += 1

            if face_match:
                threading.Thread(target=execute_voice_code).start()
            else:
                execute_alarm_code()

        try:
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        except KeyboardInterrupt:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
