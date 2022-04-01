# Import the gTTS module for text
# to speech conversion
import os
from playsound import playsound
from gtts import gTTS
import pyttsx3
from PyPDF2 import PdfFileReader
# This module is imported so that we can
# play the converted audio

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


book_dir = "day90\\assets\\test.pdf"
book = PdfFileReader(book_dir)
num_pages = book.getNumPages()
full_text = ""


for i in range(0, num_pages):
    page = book.getPage(i)
    print(f"{i} pages converted.")
    full_text += page.extractText()  # + "\n"
    print(page.extractText())

# engine.save_to_file(full_text, 'teste.mp3')
# engine.runAndWait()

# It is a text value that we want to convert to audio
text_val = 'Welcome to geeksforgeeks!'

# Here are converting in English Language
language = 'en'

# Passing the text and language to the engine,
# here we have assign slow=False. Which denotes
# the module that the transformed audio should
# have a high speed
obj = gTTS(text=text_val, lang=language, slow=False)

# Here we are saving the transformed audio in a mp3 file named
# exam.mp3
obj.save("exam.mp3")

# Play the exam.mp3 file
playsound("exam.mp3")

# os.system("mpg321 exam.mp3")
