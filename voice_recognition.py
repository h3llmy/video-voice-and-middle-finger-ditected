import speech_recognition as sr
from config import voice_recognitio_language

def voice_recognition():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Berbicara...")
        try:
            audio = r.listen(source)

            text = r.recognize_google(audio, language=voice_recognitio_language)
            print("Anda mengatakan:", text)

        except sr.UnknownValueError:
            print("Tidak dapat mengenali suara")
        except sr.RequestError as e:
            print("Error:", str(e))
