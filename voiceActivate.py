import speech_recognition as sr
import pyttsx3
import string
class VoiceActivated:
    def __init__(self):
        self.answer = ""
        self.speech_engine = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
        self.activated = False
        self.activation_phrase = "hey calculator"
    def getAnswer(self):
        return self.answer
    def run(self):
        with sr.Microphone() as source:
            self.speech_engine.adjust_for_ambient_noise(source=source, duration=2)
            print("Ready")
            while True:
                try:
                    print("Recording.")
                    audio = self.speech_engine.listen(source, timeout=5)
                    print("Done Recording.")
                    if audio:
                        text = self.speech_engine.recognize_google(audio)
                        if self.activation_phrase.lower() in text.lower():
                            print("Activated")
                            self.tts_engine.say("Yes?")
                            self.tts_engine.runAndWait()
                            self.activated = True
                        elif self.activated:
                            self.process_command(text)
                            self.activated = False
                except sr.UnknownValueError:
                    self.tts_engine.say("I don't know what you said. Can you please repeat?")
                    self.tts_engine.runAndWait()
                except sr.RequestError as e:
                    print(f"Request Error {e}")
                except:
                    pass
    def process_command(self, command):
        try:
            for i in command:
                if i.lower() in string.ascii_lowercase:
                    self.tts_engine.say("Please speak math. For example 8 times 8 or 9+9.")
                    self.tts_engine.runAndWait()
                    return -1
            self.answer = str(eval(command))
            self.tts_engine.say(f"{command} is {str(eval(command))}")
            self.tts_engine.runAndWait()
            return 0
        except SyntaxError:
            self.tts_engine.say("Please speak math. For example 8 times 8 or 9+9.")
            self.tts_engine.runAndWait()
            return -1



if __name__ == "__main__":
    voice = VoiceActivated()
    voice.run()
