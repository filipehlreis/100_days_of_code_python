from local_settings.local_settings import API_GOOGLE_CLOUD_TEXT_TO_SPEECH
import requests
import os

JSON = "C:\\github\\100_days_of_code_python\\day90\\local_settings\\client_secret_235438205509-aodvtfrtkbpupt1v21bve3u2rovojf7h.apps.googleusercontent.com.json"
GCTS_Endpoint = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"

google_parameters = {
    "input": {
        "text": "Android is a mobile operating system developed by Google, based on the Linux kernel and designed primarily for touchscreen mobile devices such as smartphones and tablets."
    },
    "voice": {
        "languageCode": "en-gb",
        "name": "en-GB-Standard-A",
        "ssmlGender": "FEMALE"
    },
    "audioConfig": {
        "audioEncoding": "MP3"
    },
    "key": API_GOOGLE_CLOUD_TEXT_TO_SPEECH,
    # "key": {
    #     "type": "string",
    #     "location": "query",
    #     "description": API_GOOGLE_CLOUD_TEXT_TO_SPEECH,
    # }
    "oauth_token": {
        "type": "string",
        "location": "query",
        "description": "235438205509-aodvtfrtkbpupt1v21bve3u2rovojf7h.apps.googleusercontent.com",
    }
}

headers = {
    "key": API_GOOGLE_CLOUD_TEXT_TO_SPEECH,
    # "oauth_token": "235438205509-aodvtfrtkbpupt1v21bve3u2rovojf7h.apps.googleusercontent.com"
}

response = requests.post(
    url=GCTS_Endpoint,
    # params=google_parameters,
    # params=google_parameters,
    json=google_parameters,
    headers=headers,
)
response.raise_for_status()


def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice,
                 "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
