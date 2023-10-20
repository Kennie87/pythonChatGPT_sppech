import speech_recognition as sr
import pyttsx4

OPENAI_KEY = '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'

import openai
openai.api_key = OPENAI_KEY

def SpeakText(command):
    engine = pyttsx4.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[4].id)
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()

def record_text():
    while(1):
        try: 
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)

                if MyText == 'shut down':
                    MyText = 'thank you pa pa'

                if MyText == 'I love you':
                    MyText = 'omg due'
                    
                return MyText
            

        except sr.RequestError as e:
            print("Could not request results: {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")

def send_to_chatGPT(messages, model="gpt-3.5-turbo"):

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)

    return message

messages = [{"role": "user", "content": "Your name is Jeevika two point zero"}]

while(1):
    text = record_text()
    if text == "thank you pa pa":
        response = "bye pa pa"
        SpeakText(response)
        break
    
    if text == "I love you":
        response = "omg due"
        SpeakText(response)


    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    SpeakText(response)
    print(response)
    