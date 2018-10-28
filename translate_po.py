import os

from google.cloud import translate

service_account_json_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
translate_client = translate.Client.from_service_account_json(service_account_json_path)


def parser_po(filepath):
    pass


def translate(text, lang='ja'):
    translation = translate_client.translate(text, target_language=lang)
    import pdb; pdb.set_trace()
    return translation['translatedText']


def main():
    text = 'Hello World'
    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translate(text)))


if __name__ == '__main__':
    main()
