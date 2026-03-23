import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am Jarvis. Please tell me how may I help you.")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception:
        print("Say that again please...")
        return "none"


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your_app_password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if query == "none":
            continue

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            search_query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(search_query, sentences=2)
                print(results)
                speak("According to Wikipedia")
                speak(results)
            except Exception:
                speak("Sorry, I could not find anything.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'send whatsapp message' in query:
            try:
                speak("Tell me the message")
                message = takeCommand()

                phone_number = "+911234567890"   # replace with receiver number
                speak("Opening WhatsApp and sending the message")
                pywhatkit.sendwhatmsg_instantly(
                    phone_number,
                    message,
                    wait_time=15,
                    tab_close=True
                )
                speak("Message sent successfully")

            except Exception as e:
                print(e)
                speak("Sorry, I could not send the WhatsApp message")


        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = r'D:\Non Critical\songs\Favorite Songs2'
            try:
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found.")
            except Exception:
                speak("Music folder not found.")

        elif 'time is' in query or 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = r"C:\Users\Harshita\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            try:
                os.startfile(codePath)
            except Exception:
                speak("Unable to open VS Code.")

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "example@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent.")
            except Exception:
                speak("Sorry, I am not able to send this email.")

        elif 'exit' in query or 'quit' in query or 'stop':
            speak("Goodbye!")
            break