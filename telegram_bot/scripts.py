import requests
import misc
# from langdetect import detect

URL = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key="

def get_dictionary(text):
    try:
        # r = detect(text)
        # print(r)
        # lang = "lang={}".format("en-ru" if r == "en" else "ru-en")
        lang = "lang={}".format("en-ru")
        url = URL + misc.api_key + "&" + lang + "&" + "text=" + text
        r = requests.get(url).json()

        s = "{} - {}, {}".format(text, r["def"][0]["tr"][0]["text"], r["def"][0]["tr"][0]["syn"][0]["text"])
        return s
    except:
        return "Упс, неправильное слово("

if __name__ == "__main__":
    print(get_dictionary("Dark"))
