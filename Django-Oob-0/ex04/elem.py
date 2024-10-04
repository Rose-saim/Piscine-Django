class Elem:
    class ValidationError(Exception):
        pass

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr if attr is not None else {}
        self.content = []
        if content:
            self.add_content(content)
        self.tag_type = tag_type

    def __str__(self):
        attr_str = ' '.join([f'{key}="{value}"' for key, value in self.attr.items()])
        if self.tag_type == 'double':
            return f"<{self.tag} {attr_str}>{self.content_to_str()}</{self.tag}>"
        elif self.tag_type == 'simple':
            return f"<{self.tag} {attr_str}/>"

    def content_to_str(self):
        if isinstance(self.content, list):
            return ''.join([str(elem) for elem in self.content])
        return str(self.content)

    def add_content(self, content):
        if isinstance(content, list):
            self.content.extend(content)
        else:
            self.content.append(content)

# Testing Elem
if __name__ == "__main__":
    html = Elem(tag="html", content=[
        Elem(tag="head", content=Elem(tag="title", content="Hello ground!")),
        Elem(tag="body", content=[
            Elem(tag="h1", content="Oh no, not again!"),
            Elem(tag="img", attr={"src": "http://i.imgur.com/pfp3T.jpg"}, tag_type="simple")
        ])
    ])
    print(html)
