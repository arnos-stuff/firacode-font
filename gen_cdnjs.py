import requests
import re

url = "https://cdnjs.com/libraries/Iosevka/6.0.0"
css_pattern = 'https://cdnjs.cloudflare.com/ajax/libs/Iosevka/6.0.0/(iosevka-?[\w-]+/iosevka-?[\w-]+.min.css)'
ttf_pattern = 'https://cdnjs.cloudflare.com/ajax/libs/Iosevka/6.0.0/(iosevka-?[\w-]+/ttf/iosevka-?[\w-]+.ttf)'
base = "https://cdnjs.cloudflare.com/ajax/libs/Iosevka/6.0.0/"

response = requests.get(url)

raw = response.content.decode()

css_urls = re.findall(css_pattern, raw)
ttf_urls = re.findall(ttf_pattern, raw)

fcss = open('cdnjs-fonts-min.css', 'w+')
fttf = open('cdnjs-fonts-tff.css', 'w+')


def template(font_url):
    name = font_url.split('/')[-1].replace(".min.css", "").replace(".ttf", "")
    font_url = base + font_url
    return (
        "@font-face {" +
    f"\n    font-family: '{name}';" +
    f"\n    src: url({font_url});" +
    "\n}\n\n"
    )


for cssurl in css_urls:
    fcss.write(template(cssurl))
fcss.close()

for ttfurl in ttf_urls:
    fttf.write(template(ttfurl))
fttf.close()
