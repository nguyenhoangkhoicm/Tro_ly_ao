from gtts import gTTS
import playsound
import os
import speech_recognition as sr


class speaker(object):
    def speak(text):
        """
        lấy một chuỗi làm đầu vào, chuyển đổi nó thành giọng nói, lưu nó dưới dạng tệp mp3, phát tệp mp3,
        và sau đó xóa tệp mp3

        :param text: Văn bản muốn chuyển thành giọng nói

        """
        print("🤖: " + text)
        tts = gTTS(text=text, lang='vi', slow=False)
        filename = 'voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    def command():
        """
        Nó phát âm thanh, sau đó đợi trong 4 giây im lặng, sau đó ghi âm trong 4 giây, sau đó cố gắng
        nhận dạng giọng nói, sau đó trả về văn bản được nhận dạng
        :return: Văn bản đang được trả về là văn bản đang được người dùng nói.

        """
        playsound.playsound("./sound/Ping.mp3", False)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("...")
            audio = r.record(source, duration=4)
        try:
            text = r.recognize_google(audio, language='vi')
            print("🧑: " + text)

        except sr.UnknownValueError:
            speaker.speak(
                "Xin lỗi tôi không nghe thấy bạn nói gì,bạn có thể nhập từ bàn phím")
            text = str(input("Mời bạn nhập: "))
        return text.lower()
