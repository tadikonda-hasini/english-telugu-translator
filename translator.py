import requests
from urllib.parse import quote


def translate_text(text, source, target):
    if source == "eng_Latn" and target == "tel_Telu":
        langpair = "en|te"
    elif source == "tel_Telu" and target == "eng_Latn":
        langpair = "te|en"
    else:
        raise ValueError("Unsupported language pair")

    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": langpair
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    if data.get("responseStatus") != 200:
        raise Exception("Translation API failed")

    return data["responseData"]["translatedText"]