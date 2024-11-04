from elem import Elem

class Html(Elem):
    def __init__(self, content=None):
        super().__init__(tag="html", content=content)

class Head(Elem):
    def __init__(self, content=None):
        super().__init__(tag="head", content=content)

class Body(Elem):
    def __init__(self, content=None):
        super().__init__(tag="body", content=content)

class Title(Elem):
    def __init__(self, content=None):
        super().__init__(tag="title", content=content)

class Img(Elem):
    def __init__(self, src=""):
        super().__init__(tag="img", attr={"src": src}, tag_type="simple")

class H1(Elem):
    def __init__(self, content=None):
        super().__init__(tag="h1", content=content)

# Example test
if __name__ == "__main__":
    html = Html([
        Head(Title("Hello ground!")),
        Body([
            H1("Oh no, not again!"),
            Img(src="http://i.imgur.com/pfp3T.jpg")
        ])
    ])
    print(html)
