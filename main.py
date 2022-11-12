import speech_recognition
import pyttsx3
from chatbot import chatbot


def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def speech():
    recognizer = speech_recognition.Recognizer()

    listen = True

    while listen:
        print('Ask a question.')
        try:
            with speech_recognition.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)

                audio = recognizer.listen(source)

                recognizer_function = getattr(recognizer, 'recognize_google')
                result = recognizer_function(audio)
                print(result)

                response = chatbot.get_response(text=result)

                print(response)
                speak_text(response)

                listen = False

        except speech_recognition.RequestError as e:
            print('Could not request results; {0}'.format(e))

        except speech_recognition.UnknownValueError:
            print('No input detected.')


def written():
    written_text = input('Input a question: ')
    response = chatbot.get_response(text=written_text)

    print(response)


if __name__ == '__main__':
    answer = input('Do you want to use speech? (y/n): ').lower()
    if answer == 'y':
        speech()
    elif answer == 'n':
        written()
    else:
        print('Invalid input.')
