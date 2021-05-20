"""
TML-Reader-Module (Turtle-Markup-File).

https://github.com/Johannes-Walter/tml-reader
"""

import shapes


class Tag():
    """
    A Class which reads tag-pairs.

    This class saves the position of the tags in a given text with their
    starting/endig position and the name of the tag.
    """

    def __init__(self):
        """
        Create a new tag.

        Returns
        -------
        None.

        """
        self.opening_tag_start = None
        self.opening_tag_end = None

        self.tag_name = None

        self.closing_tag_start = None
        self.closing_tag_end = None

    def find_tag(text: str, start: int, end: int):
        """
        Find the first tag-pair in the given text.

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
            A tag-object containing all information or
            None, if no tag is found.
        """
        # check if the end is after the beginnig
        assert start <= end

        tag = Tag()

        # if there is no opening tag, there will be an error
        # we will pass an "none" for no tag
        try:
            tag.__find_opening_tag(text, start, end)
        except ValueError:
            return None

        tag.__find_closing_tag(text, tag.opening_tag_end, end)
        if (tag.closing_tag_start is not None
                and tag.closing_tag_end is not None):
            return tag
        else:
            return None

    def __find_opening_tag(self, text: str, start: int, end: int):
        """
        Find the first Tag in the Text.

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
        Tag
            The tag which was worked on.

        """
        # find the index of the starting and closing tag and save them
        self.opening_tag_start = text.index("<", start, end)
        self.opening_tag_end = text.index(">", self.opening_tag_start, end)

        # tag_name is saved without the tags ('<', '>')
        self.tag_name = text[self.opening_tag_start + 1:
                             self.opening_tag_end]
        return self

    def __find_closing_tag(self, text: str, start: int, end: int):
        """
        Find the closing tag in the given text.

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
        Tag
            Returns the tag which was worked on.

        """
        assert self.tag_name != ""
        opening_tag = f"<{self.tag_name}>"
        closing_tag = f"</{self.tag_name}>"

        level = 0
        # scrutinize the text, looking for opening and closing tags
        # if an opening tag is found, the level will increase to 1
        # if it is a closing tag, the level will decrease
        for index in range(start, end):
            if text.startswith(opening_tag, index):
                level += 1
            if text.startswith(closing_tag, index):
                # we found our tag if the level is 0, thus leaving the loop
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
        text = file.read()
        tag = Tag.find_tag(text, start=0, end=len(text))

        shape = shapes.get_shape(tag.tag_name)

        # delegate everything else in the file to the find_elements-function
        # to find all children in the code
        __find_elements(text,
                        shape,
                        tag.opening_tag_end,
                        tag.closing_tag_start)
    return shape


def __find_elements(text: str, shape, start: int, end: int):
    """
    Find all tags in the given text and append everything to the tag.

    Parameters
    ----------
    text : str
        Text to search through.
    shape : TYPE
        Shape which will have all subshapes appended to.
    start : int
        Start index of the search.
    end : int
        Ending index of the search.

    Returns
    -------
    None.

    """
    tag = Tag.find_tag(text, start, end)
    while tag:
        # get the shape from the possible shapes
        sub_shape = shapes.get_shape(tag.tag_name)
        if sub_shape is not None:
            shape.append_shape(sub_shape)
        # if there is no shape, try to check the tag as attribute which belongs to shape
        # this may appear an error, if the found tag is not valid
        else:
            shape.set_attribute(tag.tag_name,
                                text[tag.opening_tag_end + 1:
                                     tag.closing_tag_start])

        # find the next tag, start to search at the end of the current tag
        __find_elements(text,
                        sub_shape,
                        tag.opening_tag_end,
                        tag.closing_tag_start)
        tag = Tag.find_tag(text, tag.closing_tag_end, end)

def draw_tml(file_path: str):
    """
    Draw the image contained in the given file.

    Parameters
    ----------
    file_path : str
        Path of the .tml file.

    Returns
    -------
    None.

    """
    image = __read_tml(file_path)
    image.draw()


def is_file_valid(file_path: str) -> bool:
    """
    Check if the given file should be readable by this parser and valid.

    Parameters
    ----------
    file_path : str
        Path of the .tml file.

    Returns
    -------
    bool
        True if the file is valid, false if not.
    """
    if not file_path.endswith(".tml"):
        return False

    try:
        __read_tml(file_path)
    except:
        return False
    return True


if __name__ == "__main__":
    draw_tml("samples//sample.tml")
