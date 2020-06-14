import requests

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'

def translate_file(files, loag):
    text = []
    with open(files, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip()
            text.append(line)

        params = {'key': API_KEY, 'text': text, 'lang': '{}-ru'.format(loag)}
        resp = requests.get(url, params=params)
        res = resp.json()

        with open('translate.txt', 'w') as fw:
            fw.write(''.join(res['text']))

translate_file('ES.txt', 'es')





