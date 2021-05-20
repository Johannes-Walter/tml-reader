"""
TML-Reader-Module (Turtle-Markup-File).

https://github.com/Johannes-Walter/tml-reader
"""

import shapes


class Tag():
    """
    A Class which reads Tag-Pairs.

    It saves the position of the Tags in a given Text with their
    starting-position and the name of the tag.
    """

    def find_tag(text: str, start: int, end: int):
        """
        Find the first Tag-Pair in the given Text.

        Parameters
        ----------
        text : str
            Text which will be searched in.
        start : int
            Start index of the search.
        end : int
            Ending index of the search.

        Returns
        -------
        tag : Tag
            A Tag-Object containing all Information or
            None, if not Tag is found.
        """
        assert start <= end

        tag = Tag()
        # Wirft Fehler falls das Tag nicht gefunden werden kann
        try:
            tag.__find_opening_tag(text, start, end)
        except ValueError:
            return None

        tag.__find_closing_tag(text, tag.opening_tag_end, end)
        if (hasattr(tag, "closing_tag_start")
                and hasattr(tag, "closing_tag_end")):
            return tag
        else:
            return None

    def __find_opening_tag(self, text: str, start: int, end: int):
        """
        Find the first Tag in the Text.

        Parameters
        ----------
        text : str
            Texxt which will be searched in.
        start : int
            Start index of the search.
        end : int
            Ending index of the search.

        Returns
        -------
        Tag
            Returns the Tag which was worked on.

        """
        self.opening_tag_start = text.index("<", start, end)
        self.opening_tag_end = text.index(">", self.opening_tag_start, end)

        # tag_name wird ohne die Klammern gespeichert
        self.tag_name = text[self.opening_tag_start + 1:
                             self.opening_tag_end]
        return self

    def __find_closing_tag(self, text, start: int, end: int):
        """
        Find the closing tag in the given Text.

        Parameters
        ----------
        text : str
            Texxt which will be searched in.
        start : int
            Start index of the search.
        end : int
            Ending index of the search.

        Returns
        -------
        Tag
            Returns the Tag which was worked on.

        """
        assert self.tag_name != ""
        opening_tag = f"<{self.tag_name}>"
        closing_tag = f"</{self.tag_name}>"

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


def __read_tml(file_path: str):
    """
    Read the given TML.

    Parameters
    ----------
    file_path : str
        Path to the File.

    Returns
    -------
    None.

    """
    # open file with file reader
    with open(file_path) as file:
        # delegate everything in the file to the find_elements-function
        # to find all children in the code
        text = file.read()
        tag = Tag.find_tag(text, start=0, end=len(text))

        shape = shapes.get_shape(tag.tag_name)
        __find_elements(text,
                        shape,
                        tag.opening_tag_end,
                        tag.closing_tag_start)
    shape.draw()


def __find_elements(text: str, shape, start: int, end: int):
    tag = Tag.find_tag(text, start, end)
    while tag:
        sub_shape = shapes.get_shape(tag.tag_name)
        if sub_shape is not None:
            shape.append_shape(sub_shape)
        else:
            shape.set_attribute(tag.tag_name,
                                text[tag.opening_tag_end + 1:
                                     tag.closing_tag_start])

        __find_elements(text,
                        sub_shape,
                        tag.opening_tag_end,
                        tag.closing_tag_start)
        tag = Tag.find_tag(text, tag.closing_tag_end, end)
    # suchen jedes Klammerpaar im angegebenen Text und rufen find_elements auf
    # und rekursiv mit dem Inhalt


__read_tml("sample.tml")
