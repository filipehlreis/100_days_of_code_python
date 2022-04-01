from base64 import b64decode
from local_settings.local_settings import API_GOOGLE_CLOUD_TEXT_TO_SPEECH
import requests

GCTS_ENDPOINT = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"


google_parameters = {
    "audioConfig": {
        "audioEncoding": "LINEAR16",
        "pitch": 0,
        "speakingRate": 1
    },
    "input": {
        "text": "Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with 100+ voices, available in multiple languages and variants. It applies DeepMind’s groundbreaking research in WaveNet and Google’s powerful neural networks to deliver the highest fidelity possible. As an easy-to-use API, you can create lifelike interactions with your users, across many applications and devices."
    },
    "voice": {
        "languageCode": "en-US",
        "name": "en-US-Wavenet-D",
    },
    # "X-Goog-Api-Key": API_GOOGLE_CLOUD_TEXT_TO_SPEECH,

}
headers = {
    "X-Goog-Api-Key": API_GOOGLE_CLOUD_TEXT_TO_SPEECH,
}

response = requests.post(
    url=GCTS_ENDPOINT,
    json=google_parameters,
    headers=headers,
)
response.raise_for_status()
texto = response.json()
texto_string = texto['audioContent']


with open('text.mp3', mode='wb') as file:
    audio = b64decode(texto_string)
    file.write(audio)

print(texto)
