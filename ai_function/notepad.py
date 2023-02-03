from datetime import datetime
import os
from ai_function.determine_most_similar import determine_most_similar_phrase
from ai_function.speaklisten import speaker


class notepad():
    def main(self, text, intent):
        task = self.determine_search_or_open(text)
        if task == 'note':
            self.notes()

    def determine_search_or_open(self, text):
        phrases = {
            'ghi chú': 'note',
            'chú thích': 'note'
        }

        most_similar = determine_most_similar_phrase(text, phrases)
        return phrases[most_similar]

    def notes(self):
        speaker.speak('Bạn cần ghi chú gì')
        writes = speaker.command()
        time = datetime.now().strftime("%H:%M")
        filename = str(time).replace(":", "-")+"-note.txt"
        with open(filename, 'w+', encoding='utf-8') as file:
            file.write(writes)
        path_1 = r".\{}".format(str(filename))
        path_2 = r".\note\{}".format(str(filename))
        os.rename(path_1,path_2)
        os.startfile(path_2)
        


note = notepad()
