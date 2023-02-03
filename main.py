
from ai_function.wallper_desktop import change_wallper
from ai_function.func import function
from ai_function.notepad import note
from ai_function.weather import weather
from ai_function.datatime import assistant_time
from ai_function.open_app import localapp
from ai_function.open_web_search import assistant_browser
from ai_function.speaklisten import speaker
from intentclassification.intent_classification import IntentClassifier
from ai_function.reply import reply
import pyaudio
import struct
import pvporcupine


class Assistant:

    def __init__(self, name):
        self.name = name

    def reply(self, text):
        """
        Nếu ý định là 'rời đi', thì trợ lý nói "rất vui được phục vụ bạn." và thoát chương trình. 
        Nếu không, gọi chức năng trong mục /ai_function trả lời tương ứng với mục đích của người dùng.

        :param text: Văn bản mà người dùng đã nhập
        """

        intent = intentclassifier.predict(text)

        if intent == 'leaving':
            speaker.speak("Rất vui được phục vụ bạn.")
            quit()

        replies = {
            'greeting': reply,
            'insult': reply,
            'install': reply,
            'function': function.main,
            'open_app': localapp.main,
            'datatime': assistant_time.main,
            'open_in_browser': assistant_browser.main,
            'weather': weather.main,
            'wallper': change_wallper.main,
            'note': note.main

        }

        try:

            reply_func = replies[intent]
            # Kiểm tra xem chức năng có thể gọi được không.
            if callable(reply_func):
                reply_func(text, intent)

        except KeyError:
            speaker.speak("Xin lỗi mình chưa đủ thông minh để giúp bạn😣😣")

    def main(self):

        print("...")
        #  khởi tạo các biến.
        self.porcupine = None
        pa = None
        audio_stream = None

        # Phát hiện từ đánh thức.
        access_key = "08RPO8infyitaLPnJPEfKTK3+l3Cc73mZB2JDtEIVz71RYJ9TOYk/Q=="
        self.porcupine = pvporcupine.create(
            access_key=access_key, keywords=[self.name])

        # Tạo một đối tượng PyAudio.
        pa = pyaudio.PyAudio()

        # mở luồng tới micrô.
        audio_stream = pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length)

        while True:

            try:
                # Đọc luồng âm thanh và chuyển đổi nó sang định dạng mà porcupine có thể
                # hiểu.
                pcm = audio_stream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from(
                    "h" * self.porcupine.frame_length, pcm)
            except:
                # mở luồng tới micrô.
                audio_stream = pa.open(
                    rate=self.porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=self.porcupine.frame_length)

            # Xử lý luồng âm thanh và kiểm tra xem từ khóa có được phát hiện hay không.
            keyword_index = self.porcupine.process(pcm)

            # Trợ lý nghe được từ đánh thức và sau đó lắng nghe đầu vào của người dùng.
            if keyword_index >= 0:
                speaker.speak("Vâng, có mình đây!")

                if audio_stream is not None:
                    audio_stream.close()
                said = speaker.command()  # Lắng nghe đầu vào của người dùng
                self.reply(said)


# Gọi chức năng chính của lớp Trợ lý.
intentclassifier = IntentClassifier()
assistant = Assistant("hey siri")
assistant.main()
