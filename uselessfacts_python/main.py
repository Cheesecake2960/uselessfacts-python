from typing import Literal
import urllib.request
import json

class Fact:
    def __init__(self, id: str, text: str, source: str, source_url: str, language: Literal['en', 'de'], permalink: str):
        self.id = id
        self.text = text
        self.source = source
        self.source_url = source_url
        self.language = language
        self.permalink = permalink
        

def get_fact(
    endpoint: Literal['random', 'today'] = 'random',
    language: Literal['en', 'de'] = 'en'
) -> Fact:
    "Getting a fact from the api."
    if endpoint not in ['random', 'today']: raise Exception("Unsupported endpoint: '{}'".format(endpoint))
    if language not in ['en', 'de']: raise Exception("Unsupported language: '{}'".format(language))

    url = 'https://uselessfacts.jsph.pl/api/v2/facts/{}?language={}'.format(endpoint, language)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read()

    return Fact(**json.loads(body))