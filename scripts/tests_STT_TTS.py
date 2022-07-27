"""

"""

import random
import time
import os
import gtts
from playsound import playsound

import speech_recognition as sr

PLAY = True


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech recorded from `microphone`.
    Args:
        `microphone`: 

    Returns: dict
        "success": a boolean indicating whether or not the API request was
                successful
        "error":   `None` if no error occured, otherwise a string containing
                an error message if the API could not be reached or
                speech was unrecognizable
        "transcription": `None` if speech could not be transcribed,
                otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio, language="fr-FR")
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


def play():
    print("Start in 3sec...")
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    time.sleep(3)

    print('Speak!')

    response = {}

    while not response.get("success"):
        response = recognize_speech_from_mic(recognizer, microphone)
        if response["error"]:
            print(f"ERROR: {response['error']}")

    # show the user the transcription
    print(f"STT: {response['transcription']}")
    # make request to google to get synthesis
    tts = gtts.gTTS(response["transcription"], lang="fr")
    # save the audio file
    tts.save("response.mp3")
    # play the audio file
    playsound("response.mp3")
    os.remove("response.mp3")

    if input('Try again ? [Y/n]\t').lower() in ["n", "no"]:
        return False
    return True


if __name__ == "__main__":
    while PLAY:
        PLAY = play()
