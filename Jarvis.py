import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


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


def takeCommand ():
	""" It Takes Microphone Input From The User And Returns String Output"""
	 
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		print("Listening....!!")
		r.pause_threshold = 1
		audio = r.listen(source)
		
	try:
		print("Recognizing..!!")
		query = r.recognize_google(audio, language='en-us')
		print(f"User Said: {query}\n")
	
	except Exception as e:
		# print(e)
		
		print("Say That Again Please...!!")
		return "None"
	return query
		

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 958)
	server.ehlo()
	server.starttls()
	server.login('youremail@gmail.com', 'your-password-here')
	server.sendmail('youremail@gmail.com', to, content)
	server.close()
	
		
if __name__ == "__main__":
    # speak("Tyro Is A Beast")
	wishMe()
	while True:
		query = takeCommand().lower()
		
		# Logic For Executing Tasks Based On Query
		if 'wikipedia' in query:
			speak('Searching Wikipedis....')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According To Wikipedia")
			print(results)
			speak(results)
			 
		elif 'open youtube' in query:
			webbrowser.open("youtube.com")
			
		elif 'open google' in query:
			webbrowser.open("google.com")
			
		elif 'play music' in query:
			music_dir = 'C:\\Users\\AYeddula\\yo_man'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir, songs[0]))
			
		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, The Time Is {strTime}")
			
		elif 'open geany' in query:
			geanyPath = "C:\\Program Files (x86)\\Geany\\bin\\geany.exe"
			os.startfile(geanyPath)
			
		elif 'email to tyro' in query:
			try:
				speak("What Should I Say?")
				content = takeCommand()
				to = "tyroyourEmail@gmail.com"
				sendEmail(to, content)
				speak("Email Has Been Sent!!")
				
			except Exception as e:
				print(e)
				speak("Sorry My Friend Tyro. I Am Not Able To Send This Email")
				
			
