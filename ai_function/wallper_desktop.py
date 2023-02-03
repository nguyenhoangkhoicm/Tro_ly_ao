from datetime import datetime
import os
from ai_function.determine_most_similar import determine_most_similar_phrase
from ai_function.speaklisten import speaker
import urllib.request
import ctypes
import json
from pathlib import Path


class wallper():
    def main(self, text, intent):
        task = self.determine_search_or_open(text)
        if task == 'wallper':
            self.change_wallper()

    def determine_search_or_open(self, text):
        phrases = {
            'thay hình nền': 'wallper',
            'đổi hình nền': 'wallper',
            'đổi background': 'wallper',
            'thay ảnh nền': 'wallper'
        }

        most_similar = determine_most_similar_phrase(text, phrases)
        return phrases[most_similar]

    def change_wallper(self):

        api_key = "b_SSQ8aEiqQwVa_RU5zjHlOdYH0n6rA6jF47ehoOrKs"
        url = "https://api.unsplash.com/photos/random?client_id=" + \
            api_key
        f = urllib.request.urlopen(url)
        json_string = f.read()
        f.close()
        parsed_json = json.loads(json_string)
        photo = parsed_json["urls"]["full"]

        urllib.request.urlretrieve(
            photo, r".\wallper_change\image_change.png")
            
        path= r"C:\Users\Khoi Nguyen\Desktop\Virtual_assistant\wallper_change\image_change.png"
        image = os.path.join(path)
      
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 0)
        speaker.speak("Hình nền máy tính đã được thay đổi")



change_wallper = wallper()
