from urllib.request import urlopen

with urlopen('https://sts2.wiki/cards/') as request:
    for line in request:
        print(line)
