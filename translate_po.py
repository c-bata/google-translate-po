import functools
import json
import os

from google.cloud import translate

_cache_home = "."
_cache_filename = "po-translation-cache.json"
_translated_text_length = 0

service_account_json_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
translate_client = translate.Client.from_service_account_json(service_account_json_path)


def parse_po(filepath):
    pass


def calculate_fee(text_len, dollar_per_currency=None):
    """
    https://cloud.google.com/translate/pricing?hl=en

    * Google charges on per character basis, even if the character is multiple bytes,
      where a character corresponds to a (code-point).
    * Google does not charge extra for language detection when you do not specify
      the source language for the translate method.
    """
    if dollar_per_currency is None:
        dollar_per_currency = 1  # dollar
    dollar = text_len / (10 ** 6) * 20
    return dollar_per_currency * dollar


def cache_translation(callback):
    @functools.wraps(callback)
    def decorated(*args, **kwargs):
        file_path = os.path.join(_cache_home, _cache_filename)
        text = args[0]
        lang = kwargs.get("lang")
        key = f"{lang}:{text}"
        cache = {}
        try:
            with open(file_path) as f:
                cache = json.load(f)
        except FileNotFoundError:
            pass
        cached = cache.get(key)
        if cached:
            return cached
        result = callback(*args, **kwargs)
        cache[key] = result
        with open(file_path, "w") as f:
            json.dump(cache, f, indent=4)
        return result
    return decorated


@cache_translation
def translate(text, lang='ja'):
    if text == "":
        return ""
    global _translated_text_length
    _translated_text_length += len(text)
    translation = translate_client.translate(text, target_language=lang)
    return translation.get('translatedText')


def main():
    text = 'Hello World'
    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translate(text)))

    fee = calculate_fee(_translated_text_length, dollar_per_currency=111.90)
    print("Cost: {} yen".format(fee))


if __name__ == '__main__':
    main()
