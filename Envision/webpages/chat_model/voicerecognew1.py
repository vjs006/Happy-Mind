# Import necessary modules
import speech_recognition as sr,nltk
from deep_translator import GoogleTranslator
import pyttsx3
class Speech:
    # Initialize the recognizer
    def _init_(self) -> None:
        self.translation = None
        self.nouns, self.gerunds,self.keywords = None, None, None
    def speak(self):
        recognizer = sr.Recognizer()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        # Capture voice input from the microphone
        with sr.Microphone() as source:
            engine = pyttsx3.init()
            print("At your service!Please tell me...")
            engine.say("At your service!Please tell me...")
            engine.runAndWait()
            try:
                audio = recognizer.listen(source)
                print("Recording finished.")
            except:
                print("No voice heard. Kindly speak.")
                audio = recognizer.listen(source)
                print("Recording finished.")

        # Recognize the speech (convert audio to text)
        try:
            spoken_text = recognizer.recognize_google(
                audio, language="en"
            )  # Specify the language for recognition
            #print(f"Recognized text: {spoken_text}")
            
            # Translate the recognized text to English
            if spoken_text not in ('dhanyvad','dhanyavad','sukria','sukriya','shukriya','namaste','namaskar'):
                self.translation = GoogleTranslator(source="hi", target="en").translate(
                    spoken_text
                )
                return self.translation
            elif spoken_text in ('namaste','namaskar','hello','greetings','hi','hey'):
                return 'hello'
            else:
                return 'thank you'
        except sr.UnknownValueError:
                print('HappyMind could not understand')
                return None
            
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}"
            )
            return None

