import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!!")

    else:
        speak("Good Evening!!")

    speak("I Am Jarvis Sir. Please Tell Me How May I Help You")


if __name__ == "__main__":
    speak("Tyro Is A Beast")
