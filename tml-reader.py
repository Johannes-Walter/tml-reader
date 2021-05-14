import time
class Tag():
    def find_tag(text, start: int, end: int):
        assert start <= end

        tag = Tag()
        # Wirft Fehler falls das Tag nicht gefunden werden kann
        try:
            tag.find_opening_tag(text, start, end)
        except ValueError:
            return None
        print(tag.tag_name)
        tag.find_closing_tag(text, tag.opening_tag_end, end)
        if hasattr(tag, "closing_tag_start") and hasattr(tag, "closing_tag_end"):
            return tag
        else:
            return None

    def find_opening_tag(self, text, start: int, end: int):
        self.opening_tag_start = text.index("<", start, end)
        self.opening_tag_end = text.index(">", self.opening_tag_start, end)

        # tag_name wird ohne die Klammern gespeichert
        self.tag_name = text[self.opening_tag_start + 1:
                             self.opening_tag_end]
        return self

    def find_closing_tag(self, text, start: int, end: int):
        opening_tag = f"<{self.tag_name}>"
        closing_tag = f"</{self.tag_name}>"

        #print(opening_tag, "#####", closing_tag)
        level = 0
        # Die komplette Länge des Texts durchgehen und schauen, ob einer der
        # Tags gefunden wird.
        for index in range(start, end):
            # Falls der selbe Tag gefunden wird, sind wir ein level tiefer,
            # dieses Level muss auch wieder verlassen werden
            if text.startswith(opening_tag, index):
                level += 1
            if text.startswith(closing_tag, index):
                # Wenn wir auf dem richtigen Level sind, sind wir fertig mit
                # der suche nach dem schließenden Tag
                if level == 0:
                    self.closing_tag_start = index
                    self.closing_tag_end = index + len(closing_tag)
                    break
                else:
                    level -= 1
        return self


def read_tml(file_path: str):
    # open file with file reader
    with open(file_path) as file:
        # delegate evereything in the file to the find_elements-function
        # to find all children in the code
        find_elements(file.read())


def find_elements(text: str, start = 0, end = None):
    if end is None:
        end = len(text)
    #print(text)
    #print(text)
    tag = Tag.find_tag(text, start, end)
    while tag:
        find_elements(text, tag.opening_tag_end, tag.closing_tag_start)
        
        tag = Tag.find_tag(text, tag.closing_tag_end, end)
        #time.sleep(0.2)
    # find each pair of brackets in the given text and call find_elements
    # recursively with the content
    # print("fertig")


read_tml("sample.tml")