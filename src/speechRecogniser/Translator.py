import speech_recognition as sr
from speechRecogniser import policies
import playsound
from speechRecogniser.FAQ.questionStore import store_questions


def config_recogniser():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        return audio


def main():
    r = sr.Recognizer()
    while True:
        print("Which Bebo policy you want me to tell you about?")
        playsound.playsound(policies.audio("Which policy you want me to tell you about?", policies.get_current_time()), True)
        try:
            text = r.recognize_google(config_recogniser())
            print("You mean: " + text)
            policies.play(text)
            questions(text)
        except sr.UnknownValueError:
            print("Joanna could not understand what you mean")
                # playsound.playsound('downloads/intro-sounds/not-understandable.mp3', True)
        except sr.RequestError as e:
            print("Joanna could not request results from Google Speech Recognition service; {0}".format(e))
        except ConnectionError:
            print("Not able to create connection")


def questions(policyname):
    r = sr.Recognizer()
    ques = ""
    playsound.playsound(policies.audio("In case of more queries. Kindly speak your question "
                                "in 3, 2 , 1", policies.get_current_time()), True)
    try:
        ques = r.recognize_google(config_recogniser())
        print("You mean: " + ques)
        store_questions(policyname, ques)
        '''playsound.playsound(policies.audio("Your question is currently being processed by our representative."
                                           " We will get back to you shortly via your email", policies.get_current_time()), True)'''
    except sr.UnknownValueError:
        print("Joanna could not understand what you mean")
        # playsound.playsound('downloads/intro-sounds/not-understandable.mp3', True)
    except sr.RequestError as e:
        print("Joanna could not request results from Google Speech Recognition service; {0}".format(e))
    except ConnectionError:
        print("Not able to create connection")


if __name__ == "__main__":
    main()