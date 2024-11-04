class Page:
    allowed_tags = {
        "html", "head", "body", "title", "meta", "img", "table", "th", "tr", "td",
        "ul", "ol", "li", "h1", "h2", "p", "div", "span", "hr", "br", "Text"
    }

    def __init__(self, root_elem):
        if not isinstance(root_elem, Elem):
            raise TypeError("root_elem must be an instance of Elem")
        self.root_elem = root_elem

    def is_valid(self):
        return self._validate(self.root_elem)

    def _validate(self, elem):
        if elem.tag not in self.allowed_tags:
            return False

        if isinstance(elem, Html):
            return self._validate_html(elem)
        elif isinstance(elem, Head):
            return self._validate_head(elem)
        elif isinstance(elem, Body):
            return self._validate_body(elem)
        elif isinstance(elem, Title):
            return self._validate_title(elem)
        return True

    def _validate_html(self, elem):
        head_count = sum(1 for child in elem.content if isinstance(child, Head))
        body_count = sum(1 for child in elem.content if isinstance(child, Body))
        return head_count == 1 and body_count == 1

    def _validate_head(self, elem):
        return len(elem.content) == 1 and isinstance(elem.content[0], Title)

    def _validate_body(self, elem):
        valid_body_types = {H1, Img, Text}  
        return all(isinstance(child, tuple(valid_body_types)) for child in elem.content)

    def _validate_title(self, elem):
        return len(elem.content) == 1 and isinstance(elem.content[0], Text)

    def __str__(self):
        doctype = "<!DOCTYPE html>\n" if isinstance(self.root_elem, Html) else ""
        return doctype + str(self.root_elem)

class Elem:
    def __init__(self, tag, content=None, **attributes):
        self.tag = tag
        self.content = content if content else []
        self.attributes = attributes

    def __str__(self):
        opening = f"<{self.tag}>"
        closing = f"</{self.tag}>"
        content_str = ''.join(str(c) for c in self.content)
        return f"{opening}{content_str}{closing}"

class Text:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

class Html(Elem):
    def __init__(self, content=None):
        super().__init__("html", content)

class Head(Elem):
    def __init__(self, content=None):
        super().__init__("head", content)

class Title(Elem):
    def __init__(self, content):
        if isinstance(content, str):
            content = [Text(content)]  # Convertir une chaîne en liste de Text
        super().__init__("title", content)

class Body(Elem):
    def __init__(self, content=None):
        super().__init__("body", content)

class H1(Elem):
    def __init__(self, content=None):
        super().__init__("h1", content)

class Img(Elem):
    def __init__(self, **attributes):
        super().__init__("img", None, **attributes)

# Testing
if __name__ == "__main__":
    html = Html([
        Head(Title("Hello ground!")),
        Body([
            H1("Oh no, not again!"),
            Img(src="http://i.imgur.com/pfp3T.jpg")
        ])
    ])
    page = Page(html)
    print(page.is_valid())  # True
    print(page)  # Output HTML
