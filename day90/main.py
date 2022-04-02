from base64 import b64decode
from local_settings.local_settings import API_GOOGLE_CLOUD_TEXT_TO_SPEECH
import requests
import fitz

GCTS_ENDPOINT = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"
pdf_dir = "day90\\assets\\the_black_cat.pdf"


headers = {
    "X-Goog-Api-Key": API_GOOGLE_CLOUD_TEXT_TO_SPEECH,
}


with fitz.open(pdf_dir) as doc:
    for part in str(doc.name).split('\\'):
        if ".pdf" in part:
            nome_arquivo = part.split('.')[0]

    text = ""
    num_pagina = -1
    for page in doc:
        num_pagina += 1
        text = page.get_text()
    # print(text)

        google_parameters = {
            "audioConfig": {
                "audioEncoding": "LINEAR16",
                "pitch": 0,
                "speakingRate": 1
            },
            "input": {
                "text": text,
            },
            "voice": {
                "languageCode": "en-US",
                "name": "en-US-Wavenet-D",
            },
        }

        response = requests.post(
            url=GCTS_ENDPOINT,
            json=google_parameters,
            headers=headers,
        )

        response.raise_for_status()
        texto = response.json()
        texto_string = texto['audioContent']

        assets_dir = "day90\\assets"
        file_name = f"{nome_arquivo}\\{nome_arquivo}_{num_pagina}.mp3"
        mp3_dir = f"{assets_dir}\\{file_name}"

        with open(mp3_dir, mode='wb') as file:
            audio = b64decode(texto_string)
            file.write(audio)

        print(texto)
