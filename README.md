# google-translate-po

Auto-input po-style translation files using Google Translate API.

![screenshot](./img/auto-translate.png)

See [PR: Translate into English using Google Translate API - c-bata/webframework-in-python](https://github.com/c-bata/webframework-in-python/pull/13)
or [my Japanese blog article](https://nwpct1.hatenablog.com/entry/google-translate-sphinx-project).

## Setup

This requires Python3 and `google-cloud-translate` library.

```console
$ pip install --upgrade google-cloud-translate
$ export GOOGLE_SERVICE_ACCOUNT_JSON=/path/to/service-account-credential.json
```

## Usage


```console
$ python translate_po.py --help
usage: translate_po.py [-h] [--lang LANG] [--currency CURRENCY] filepath

positional arguments:
  filepath

optional arguments:
  -h, --help           show this help message and exit
  --lang LANG          target language (default: "ja")
  --currency CURRENCY  dollar per your currency. (default currency is yen: 111.90)
```


## LICENSE

MIT License.
