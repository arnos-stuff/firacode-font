import shutil
from pathlib import Path


def template(name, path):
    return (
        "@font-face {" +
    f"\n    font-family: '{name}';" +
    f"\n    src: url(https://github.com/arnos-stuff/fonts/raw/main/{path});" +
    "\n}\n\n"
    )

content = []
open('fonts.css', 'w+').write('')

with open('fonts.css', 'a') as fp:
    with open('fonts')
    for font in Path(".").glob("**/*.ttf"):
        old_name = font.name
        new_name = font.name.replace(" ", "-")
        newpath = Path(str(font).replace(old_name, new_name))
        shutil.move(font, newpath)
        font_css = template(newpath.stem, newpath).replace('\\', '/')
        fp.write(font_css)
