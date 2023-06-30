import speech_recognition as sr
from config import voice_recognitio_language
from explicit_check import explicit_check

def voice_recognition():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("start speaking...")
        try:
            audio = r.listen(source)

            text = r.recognize_google(audio, language=voice_recognitio_language)

            explicit_check(text)

        except sr.UnknownValueError:
            print("voice not recognize")
        except sr.RequestError as e:
            print("Error:", str(e))
