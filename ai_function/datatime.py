from ai_function.determine_most_similar import determine_most_similar_phrase
from ai_function.speaklisten import speaker
import datetime


class assistantdatatime():
    def main(self, text, intent):
        task = self.determine_search_or_open(text)
        if task == 'time':
            self.get_time()
        elif task == 'day':
            self.get_day()
        

    def determine_search_or_open(self, text):
        phrases = {
            'mấy giờ': 'time',
            'ngày mấy': 'day'
        }
        most_similar = determine_most_similar_phrase(text, phrases)
        return phrases[most_similar]

    def get_time(self):
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speaker.speak("Bây giờ là: " + time)

    def get_day(self):
        now = datetime.datetime.now()
        speaker.speak("Ngày tháng hiện tại là: " + now.strftime("%d/%m/%Y"))


assistant_time = assistantdatatime()
