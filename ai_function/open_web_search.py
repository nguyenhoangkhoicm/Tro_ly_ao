from ai_function.determine_most_similar import determine_most_similar_phrase
from ai_function.speaklisten import speaker
from youtube_search import YoutubeSearch
import wikipedia as wk
import webbrowser as wb


class AssistantBrowser():
    def main(self, text, intent):
        task = self.determine_search_or_open(text)
        if task == 'search':
            self.wk_search()
        elif task == 'google':
            self.google_search()
        elif task == 'youtube':
            self.youtube_search()

    def determine_search_or_open(self, text):
        phrases = {
            'tìm kiếm': 'search',
            'google': 'google',
            'nghe nhạc': 'youtube',
            'xem phim': 'youtube',
            'mở youtube': 'youtube',
            'mở wiki': 'search'
        }
        most_similar = determine_most_similar_phrase(text, phrases)
        return phrases[most_similar]

    def wk_search(self):
        speaker.speak("Bạn muốn tìm gì trên wiki vậy.")
        wk.set_lang("vi")
        keyword = speaker.command().lower()
        if keyword:
            pass
        wk_result = wk.summary(keyword, sentences=2)
        speaker.speak(wk_result)

    def google_search(self):
        speaker.speak("Bạn muốn tìm gì trên google vậy.")
        search = speaker.command().lower()
        url = "https://www.google.com/search?q=" + search
        wb.open(url)
        speaker.speak(f"Tìm thấy {search} trên google")

    def youtube_search(self):
        speaker.speak("Bạn muốn tìm gì trên youtube vậy.")
        search = speaker.command().lower()
        url = "https://www.youtube.com/search?q=" + search
        wb.open(url)
        speaker.speak(f"Tìm thấy {search} trên youtube")


assistant_browser = AssistantBrowser()
