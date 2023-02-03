import webbrowser
from ai_function.determine_most_similar import determine_most_similar_phrase
from ai_function.speaklisten import speaker
import re


class local_app():
    def main(self, text, intent):
        """
        Nhận vào một chuỗi văn bản và một từ điển các cụm từ, rồi trả về khóa của hầu hết
        cụm từ tương tự trong từ điển

        :param text: Văn bản mà người dùng đã nói
        :param intent: ý định được xác định bởi công cụ NLU
        """
        task = self.determine_search_or_open(text)
        if task == 'open':
            self.open(text)

    def determine_search_or_open(self, text):
        phrases = {
            'Mở Powerpoint': 'open',
            'word': 'open',
            'Mở Excel': 'open',
            'bạn có thể': 'open'
        }

        most_similar = determine_most_similar_phrase(text, phrases)
        return phrases[most_similar]

    def open(self, text):
        websites = {
            'microsoft edge': r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
            'powerpoint': r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE',
            'word': r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE',
            'excel': r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'
        }
        speaker.speak("Vâng!")
        text = text.lower()
        for website_name, web_address in websites.items():
            if website_name in text:
                webbrowser.open(web_address)


localapp = local_app()
