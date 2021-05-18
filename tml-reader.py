import turtle

class shape():
    def __init__(self):
        self.sub_shapes = list()
        
    def append_shape(self, shape):
        self.sub_shapes.append(shape)

    def prepare(self):
        print(self.__dict__)
        turtle.penup()
        turtle.setposition(self.x_pos, self.y_pos)
        turtle.pencolor(self.border_color)
        turtle.width(self.border_width)
        turtle.setheading(self.angle)
        turtle.pendown()

    def draw(self):
        for shape in self.sub_shapes:
            shape.draw()


class image(shape):
    def __init__(self, 
                 lower_left_x: int = 0, lower_left_y: int = 0, 
                 upper_right_x: int = 250, upper_right_y: int = 250,
                 background_color: str = None):
        super().__init__()
        self.lower_left_x = lower_left_x
        self.lower_left_y = lower_left_y
        self.upper_right_x = upper_right_x
        self.upper_right_y = upper_right_y
        self.background_color = background_color

    def draw(self):
        turtle.setworldcoordinates(self.lower_left_x,
                                   self.lower_left_y,
                                   self.upper_right_x,
                                   self.upper_right_y)
        
        # TODO: Screensize stimmend machen. Viel Glück dabei.
        turtle.screensize(self.upper_right_y - self.lower_left_y,
                          self.upper_right_x - self.lower_left_x)
        if self.background_color is not None:
            turtle.bgcolor(self.background_color)
        super().draw()
        turtle.done()
        turtle.bye()
    

class circle(shape):
    def __init__(self, x_pos: int = None, y_pos: int = None,
                 radius: int = None,
                 border_width: int = 1,
                 border_color: str = "black",
                 fill_color: str = None):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos - radius
        self.radius = radius
        self.border_width = border_width
        self.border_color = border_color
        self.fill_color = fill_color
        
        # TODO: angle löschen? wird derzeit für shape.prepare() benötigt
        self.angle = 0
        
    def draw(self):
        self.prepare()
        if self.fill_color is not None:
            turtle.fillcolor(self.fill_color)
            turtle.begin_fill()
            turtle.circle(self.radius)
            turtle.end_fill()
        else:
            turtle.circle(self.radius)
        super().draw()


class line(shape):
    def __init__(self, x_pos: int = None, y_pos: int = None,
                 angle: int = None, length: int = None,
                 border_width: int = 1,
                 border_color: str = "black"):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle
        self.length = length
        self.border_width = border_width
        self.border_color = border_color

    def draw(self):
        self.prepare()
        turtle.forward(self.length)
        super().draw()


class rectangle(shape):
    def __init__(self,
                 x_pos: int = None, y_pos: int = None,
                 angle: int = 0, 
                 height: int = None, width: int = None,
                 border_color: str = "black", border_width: int = 1,
                 fill_color: str = None):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle
        self.height = height
        self.width = width
        self.border_color = border_color
        self.border_width = border_width
        self.fill_color = fill_color
        
    
    def draw(self):
        self.prepare()
        if self.fill_color is not None:
            turtle.fillcolor(self.fill_color)
            turtle.begin_fill()
            
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
            
        if self.fill_color is not None:
            turtle.end_fill()
        super().draw()


class Tag():
    def find_tag(text, start: int, end: int):
        assert start <= end

        tag = Tag()
        # Wirft Fehler falls das Tag nicht gefunden werden kann
        try:
            tag.find_opening_tag(text, start, end)
        except ValueError:
            return None
        #print(tag.tag_name)
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
        text = file.read()
        tag = Tag.find_tag(text, start=0, end=len(text))

        shape = get_shape(tag.tag_name)
        find_elements(text, shape, tag.opening_tag_end, tag.closing_tag_start)
    shape.draw()


def get_shape(shape_name: str):
    if shape_name.lower() == "circle":
        return circle()
    if shape_name.lower() == "rectangle":
        return rectangle()
    if shape_name.lower() == "line":
        return line()
    if shape_name.lower() == "image":
        return image()
    #print(shape_name)
    return None


def find_elements(text: str, shape, start: int, end: int):
    #print(start, end)
    tag = Tag.find_tag(text, start, end)
    while tag:
        sub_shape = get_shape(tag.tag_name)
        if sub_shape is not None:
            shape.append_shape(sub_shape)
        else:
            print(tag.tag_name, text[tag.opening_tag_end+1:tag.closing_tag_start])
            setattr(shape, tag.tag_name, int(text[tag.opening_tag_end+1:tag.closing_tag_start]))
        
        find_elements(text, sub_shape, tag.opening_tag_end, tag.closing_tag_start)
        tag = Tag.find_tag(text, tag.closing_tag_end, end)
    # find each pair of brackets in the given text and call find_elements
    # recursively with the content
    # print("fertig")

print()
read_tml("sample.tml")
