

from difflib import SequenceMatcher
import random


def how_similar(a, b):
    """
    So sánh hai chuỗi và trả về tỷ lệ phần trăm giống nhau giữa chúng
    param a: Chuỗi đầu tiên để so sánh
    param b: chuỗi để so sánh 
    return: Tỷ lệ của dãy con khớp liền kề dài nhất trên tổng số phần tử trong
    chuỗi đầu vào dài nhất.
    """
    return int(SequenceMatcher(None, a, b).ratio()*100)


def determine_most_similar_phrase(text, intent_dict):
    """
    Nếu chỉ có một ý định, trả lại ý định đó. Nếu có nhiều hơn một ý định, trả lại ý định 
    có cụm từ giống nhất với đầu vào của người dùng

    text: văn bản mà người dùng đang nói
    dict: từ điển các ý định và các cụm từ tương ứng của chúng
    return: Cụm từ giống nhất với đầu vào của người dùng.
    """
    my_list = []
    my_dict = {}
    if len(intent_dict) == 1:
        for key, value in intent_dict.items():
            return key

    elif len(intent_dict) > 1:
        for key,  value in intent_dict.items():
            my_list.append(value)
            my_dict.update({key: how_similar(text.lower(), key)})
        sorted_dict = sorted(
            my_dict.items(),  key=lambda x: x[1], reverse=True)
        what_user_is_saying = list(sorted_dict[0])[0]
        return what_user_is_saying
