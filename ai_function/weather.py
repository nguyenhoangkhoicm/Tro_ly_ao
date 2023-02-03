import datetime
import webbrowser
from ai_function.determine_most_similar import determine_most_similar_phrase
from ai_function.speaklisten import speaker
import re
import time
import requests


class weather():
    def main(self, text, intent):
        task = self.determine_search_or_open(text)
        if task == 'weather':
            self.current_weather()

    def determine_search_or_open(self, text):
        phrases = {
            'thời tiết hôm nay thế nào': 'weather',
            'trời hôm nay thế nào': 'weather',
            'hôm này trời ra sao': 'weather',
            'thời tiết hôm nay ra sao': 'weather'
        }

        most_similar = determine_most_similar_phrase(text, phrases)
        return phrases[most_similar]

    def weather(self, text):
        temp = "Trời quang mây tạnh"
        if "moderate rain" in text:
            temp = "Trời hôm nay có mưa vừa, bạn ra ngoài nhớ mang theo áo mưa"
        elif "heavy intensity rain" in text or "thunderstorm with light rain" in text or "very heavy rain" in text:
            temp = "Trời hôm nay có mưa rất lớn kèm theo giông sét, bạn nhớ đem ô dù khi ra ngoài"
        elif "light rain" in text:
            temp = "Trời hôm nay mưa nhẹ, rải rác một số nơi"
        elif "heavy intensity shower rain" in text:
            temp = "Trời hôm nay có mưa rào với cường độ lớn"
        elif "broken clouds" in text or "few clouds" in text:
            temp = "Trời hôm nay có mây rải rác, không mưa"
        elif "overcast clouds" in text:
            temp = "Trời hôm nay nhiều mây, u ám, dễ có mưa"
        elif "scattered clouds" in text:
            temp = "Trời hôm nay có nắng, có mây rải rác"

        return temp

    def temperature(self, text):
        temp = "mát mẻ"
        if text < 15:
            temp = "lạnh buốt giá"
        elif text < 20:
            temp = "khá lạnh"
        elif text < 30:
            temp = "mát mẻ"
        elif text < 33:
            temp = "khá nóng"
        else:
            temp = "nóng bức"

        return temp

    def current_weather(self):
        speaker.speak("Bạn muốn xem thời tiết ở đâu vậy.")
        time.sleep(2)
        ow_url = "http://api.openweathermap.org/data/2.5/weather?"
        city = speaker.command()
        if city == "":
            self.current_weather()
        else:
            api_key = "b0d4f9bfd2bbc40d10976e6fd3ea7514"
            call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
            response = requests.get(call_url)
            data = response.json()
            if data["cod"] != "404":
                city_res = data["main"]
                current_humidity = city_res["humidity"]
                current_temperature = city_res["temp"]
                temperature1 = self.temperature(current_temperature)
                suntime = data["sys"]
                sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
                sunset = datetime.datetime.fromtimestamp(suntime["sunset"])

                weather_description = data["weather"][0]["description"]
                weather1 = self.weather(weather_description)
                content = """
        Thời tiết hôm nay {temperature} có nhiệt độ trung bình là {temp} độ C 
        Độ ẩm là {humidity}%
        {weather}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút.""".format(hourrise=sunrise.hour, minrise=sunrise.minute,
                                                                weather=weather1, temperature=temperature1,
                                                                hourset=sunset.hour, minset=sunset.minute,
                                                                temp=current_temperature, humidity=current_humidity)
                speaker.speak(content)
                time.sleep(5)
            else:
                speaker.speak("Không tìm thấy địa chỉ của bạn")
                time.sleep(2)
                self.current_weather()


weather = weather()
