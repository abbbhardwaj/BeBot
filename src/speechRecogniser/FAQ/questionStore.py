import os

from speechRecogniser import policies
from speechRecogniser.repository.pto import answers
import playsound


def store_questions(policyname, question):
    if "personal" in policyname or "time off" in policyname or "pto" in policyname or "time" in policyname:
        if answers(question) != "":
            playsound.playsound(policies.audio(answers(question), policies.get_current_time()), True)
        else:
            playsound.playsound(policies.audio("Your question is currently being processed by our representative."
                                           " We will get back to you shortly via your email",
                                           policies.get_current_time()), True)
    else:
        playsound.playsound(policies.audio("Your question is currently being processed by our representative."
                                           " We will get back to you shortly via your email",
                                           policies.get_current_time()), True)
    myfile = open("C:/Users\divya\PycharmProjects\Bbot/frequentlyAskedQuestions.txt", mode="w", encoding="utf-8")
    myfile.write(question + "? /n")
    myfile.close()
    exit(1)