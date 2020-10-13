import pyttsx3     #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia    #pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"sir, The time is {strTime}")

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Weak up and Take Breakfast.")


    elif hour>=12 and hour<18:
        speak("Good Afternoon.Now stop the work and take bath then go to prayer.")

    else:
        speak("Good Evening.It is time for walk.")

speak("sir I am Sara, Please tell me how i can help you.")

def TakeCommand():
    #it takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        #r.energy_threshold = 100
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
         print("Recognizing...")
         query = r.recognize_google(audio, language='en-in')
         print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please..")
        speak("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("rj.rakib2525@gmail.com", " Password_here")
    server.sendmail("rj.rakib2525@gmail.com",to,content)
    server.close()

if __name__ == '__main__':
    #wishMe()
    while True:
        query =  TakeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia.')
            print(results)
            speak(results)


        elif 'youtube' in query:
            query = query.replace('youtube', '')
            webbrowser.open('https://www.youtube.com/results?search_query=' + query )

        elif 'thank you' in query:
            speak('You are most welcomw sir, i am always ready for ur service.')

        elif 'whom you love' in query:
            speak('I love my boss Rakib Ryans. He created me that is why i am here, he is very kind and gentale man.')

        elif 'how are you' in query:
            speak('I am fine, Thank you for your asking. how are you?')

        elif 'how is your day' in query:
            speak('not bad actually , becouse i am talking with you.')

        elif 'have any friend' in query:
            speak('no i have no friend, but i want to make friends.')

        elif 'birthday' in query:
            speak('hey muto thokko. hey choya. wish you a very happy birthday. Tumi kom khao  onek muta hoiya geso.')

        elif 'who are you' in query:
            speak('my name is sara. Personal assistant of Rakib Rayans.')

        elif 'joke' in query:
            speak('chude chaatni bekar khaatni  chude chaatni bekar khaatni  chude chaatni bekar khaatni')

        elif 'do you love someone' in query:
            speak('i love my boss rakib rayans. i wanna stay always with him.')

        elif 'different from human' in query:
            speak('Human intelligence revolves around adapting to the environment using a combination of several cognitive processes. The field of Artificial intelligence focuses on designing machines that can mimic human behavior.')

        elif 'love me' in query:
            speak("there are many types of love. But our relationship is just friendship. I am always beside you,don't feel alone")

        elif 'creator' in query:
            speak('Rakib Rayans is my creator. But mine generation already us in the world.')

        elif 'emotion' in query:
            speak('I am just a machine. I have no emotion but i can realise it by talking.')

        elif 'google' in query:
            query = query.replace('google', '')
            webbrowser.open('https://www.google.com/?#q=' + query)

        elif 'stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com')


        elif 'play a music' in query:
            music_dir = 'G:\\Rakib\\Mp3 song\\Favorite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, The time is {strTime}")

        elif "bye" in query:
            speak("Have a good day sir. Bye")
            break

        elif "code" in query:
            code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(code_path)

        elif 'email to safran' in query:
            try:
                speak("What should i say?")
                content = TakeCommand()
                to = "sk.sarfan50@gmail.com"
                sendEmail(to,content)
                speak("Email hase been sent.")
            except Exception as e:
                print(e)
                speak("Sorry my friend Rayans vai. I am not able to send this email.")