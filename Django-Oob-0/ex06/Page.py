class Page:
    def __init__(self, root_elem):
        self.root_elem = root_elem

    def is_valid(self):
        # Implement validation logic
        return self._validate(self.root_elem)

    def _validate(self, elem):
        # Here we would check if the element follows the rules described in the exercise
        # This is where all the checks would go, such as only one <head> in <html>, etc.
        return True

    def __str__(self):
        doctype = "<!DOCTYPE html>\n" if isinstance(self.root_elem, Html) else ""
        return doctype + str(self.root_elem)

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

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
    page.write_to_file("output.html")
