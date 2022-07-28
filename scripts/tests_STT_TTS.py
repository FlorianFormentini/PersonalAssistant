"""
Local voice interface to talk with a rasa chatbot
"""
import requests
import time
import os
import gtts
from playsound import playsound

import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech recorded from `microphone`.
    Args:
        `recognizer`: speech_recognition.Recognizer
        `microphone`: speech_recognition.Microphone

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
    response = {"success": True, "error": None, "transcription": None}

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


def stt():
    """Speech-To-Text
    Returns:
        str: transcription of recorded speech
    """
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    time.sleep(0.5)
    print("Listening...")
    # recording until obtaining a response
    response = {}
    while not response.get("success"):
        response = recognize_speech_from_mic(recognizer, microphone)
        if response["error"]:
            print(f"ERROR: {response['error']}")
    return response["transcription"]


def tts(text):
    """Text-To-Speech
    Args:
        text (str): text to say
    """
    # make request to google to get synthesis
    tts = gtts.gTTS(text, lang="fr")
    # save the audio file
    tts.save("temp.mp3")
    # play the audio file
    playsound("temp.mp3")
    os.remove("temp.mp3")


def send_msg(msg, host="http://localhost:5005", sender="script"):
    """Send message to rasa chatbot through REST channel
    Args:
        msg (str): message to send
        host (str, optional): chatbot host. Defaults to 'http://localhost:5005'.
        sender (str, optional): sender name. Defaults to 'script'.
    Returns:
        dict: Chatbot response
    """
    url = host + "/webhooks/rest/webhook"
    headers = {"Content-type": "application/json"}
    r = requests.post(url, headers=headers, json=dict(sender=sender, message=msg))
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    talk = True
    while talk:
        # record message
        msg = stt()
        # display the transcription
        print(f"You: {msg}")
        # send message to bot
        response = send_msg(msg)
        if not response:
            # if an http error occurs its raised in send_msg()
            raise Exception(
                "Its broken somewhere 🤷‍♂️",
                "\n- check rasa/rasa-sdk version compatibility",
                "\n- make sure there is a trained model in `models/`",
            )
        bot_res = response[0].get("text")
        print(f"Bot: {bot_res}")
        # say bot response
        tts(bot_res)
        # retry
        talk = input("Continue ? (y/[n])").lower() not in ["", "n", "no"]

# its maybe possible to improve this by setting a custom action at the end
# of a story to return something that trigger the end of the while loop
