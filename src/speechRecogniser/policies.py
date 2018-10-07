from gtts import gTTS
from speechRecogniser.repository import appraisal
import playsound
import os, shutil
from speechRecogniser.repository import education
from speechRecogniser.repository import pto
from datetime import datetime
from speechRecogniser.gmail import send_email


def audio(line, location):
        language = 'en-uk'
        myobj = gTTS(text=line, lang=language, slow=False,)
        loc = "sounds/" + str(location) + ".mp3"
        myobj.save(loc)
        return loc


def play(command):
    text = ''
    if "appraisal" in command or "appraise" in command:
        text = appraisal.appr()
    elif "education" in command or "Education" in command:
        text = education.reuimbursement()
    elif "personal" in command or "time off" in command or "pto" in command or "time" in command:
        text = pto.pto()
    for each_line in text:
        playsound.playsound(audio(each_line, get_current_time()), True)
    playsound.playsound(audio("To receive policy details in email, Please enter Yes or No on the screen",
                              get_current_time()), True)
    choice = input("Type Y or N: ")
    if "Y" in choice or "y" in choice:
        mail(command)
    elif "n" in choice or "N" in choice:
        pass
    else:
        playsound.playsound(audio("You have not provided the input. Please enter Yes or No (Y/N): ", get_current_time()), True)
        choice = input("Type Y or N: ")
        if "Y" in choice or "y" in choice:
            mail(command)
        elif "n" in choice or "N" in choice:
            pass
    folder = "C:/Users\divya\PycharmProjects\Bbot\src\speechRecogniser\sounds"
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def get_current_time():
    df = "{:%Y%m%d%H%M%S}"
    today = datetime.now()
    date_string = df.format(today)
    return date_string


def mail(command):
        playsound.playsound(audio("Please enter your valid email eye D below", get_current_time()), True)
        email_id = input("Enter your valid email ID: ")
        send_email(str(email_id), command)
        playsound.playsound(audio("Email successfully sent to " + email_id, get_current_time()), True)


# play("pto")

# get_current_time()