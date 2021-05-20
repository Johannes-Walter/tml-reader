import turtle
import math

class shape:
    def __init__(self):
        self.sub_shapes=list ()
        self.x_pos=None
        self.y_pos=None
        self.border_color= "pink"
        self.border_width=1
        self.fill_color= None
        self.angle=0

    def append_shape(self, shape):
        self.sub_shapes.append ( shape )

    def set_attribute(self, attribute: str, value: str):
        attribute=attribute.strip ().lower ()

        if attribute in ("x_pos",):
            self.x_pos=int ( value )

        elif attribute in ("y_pos",):
            self.y_pos=int ( value )

        elif attribute in ("border_color",):
            self.border_color=value

        elif attribute in ("border_width",):
            self.border_width=int ( value )

        elif attribute == "fill_color":
            # TODO: überprüfen, ob value auch einer Farbe entspricht.
            # Kann (eigentlich) auch eine (oder mehrere) Zahlen sein.
            self.fill_color=value

        elif attribute == "angle":
            self.angle=int ( value )

        else:
            raise ValueError

    def prepare(self):
        print ( self.__dict__ )
        turtle.penup ()
        turtle.setposition ( self.x_pos, self.y_pos )
        turtle.pencolor ( self.border_color )
        turtle.width ( self.border_width )
        turtle.setheading ( self.angle )
        turtle.pendown ()

    def draw(self):
        for shape in self.sub_shapes:
            shape.draw ()


class image ( shape ):
    def __init__(self):
        super ().__init__ ()
        self.lower_left_x=0
        self.lower_left_y=0
        self.upper_right_x=1000
        self.upper_right_y=1000
        self.background_color=None

    def set_attribute(self, attribute: str, value: str):
        attribute=attribute.strip ().lower ()

        if attribute in ("llx", "lower_left_x"):
            self.lower_left_x=int ( value )

        if attribute in ("lly", "lower_left_y"):
            self.lower_left_y=int ( value )

        if attribute in ("urx", "upper_right_x"):
            self.upper_right_x=int ( value )

        if attribute in ("ury", "upper_right_y"):
            self.upper_right_y=int ( value )

        else:
            super ().set_attribute ( attribute, value )

    def draw(self):
        turtle.setworldcoordinates ( self.lower_left_x,
                                     self.lower_left_y,
                                     self.upper_right_x,
                                     self.upper_right_y )

        turtle.screensize ( self.upper_right_y - self.lower_left_y,
                            self.upper_right_x - self.lower_left_x )
        if self.background_color is not None:
            turtle.bgcolor ( self.background_color )
        super ().draw ()
        turtle.done ()
        turtle.bye ()

class circle ( shape ):
<<<<<<< Updated upstream
=======
    def __init__(self):
        super ().__init__ ()
        self.radius=None

    def set_attribute(self, attribute: str, value: str):
        attribute=attribute.strip ().lower ()
        if attribute in ("radius"):
            self.radius=int ( value )
        else:
            super ().set_attribute ( attribute, value )

    def draw(self):
        self.prepare ()
        turtle.penup()
        turtle.setposition(self.x_pos + self.radius, self.y_pos)
        turtle.pendown()
        
        if self.fill_color is not None:
            turtle.fillcolor(self.fill_color)
            turtle.begin_fill()
            turtle.circle(self.radius)
            turtle.end_fill()
        else:
            turtle.circle(self.radius)
        super().draw()


class line ( shape ):
    def __init__(self):
        super ().__init__ ()
        self.length=None

    def set_attribute(self, attribute: str, value: str):
        attribute=attribute.strip ().lower ()

        if attribute in ("length"):
            self.length=int ( value )

        else:
            super ().set_attribute ( attribute, value )

    def draw(self):
        self.prepare ()
        super ().draw ()


class rectangle ( shape ):
    def __init__(self):
        super ().__init__ ()
        self.height=None
        self.width=None

    def set_attribute(self, attribute: str, value: str):
        attribute=attribute.strip ().lower ()

        if attribute in ("height",):
            self.height=int ( value )

        elif attribute in ("width",):
            self.width=int ( value )

        else:
            super ().set_attribute ( attribute, value )

    def draw(self):
        if self.fill_color is not None:
            turtle.fillcolor(self.fill_color)
            turtle.begin_fill()
        if self.fill_color is not None:
            turtle.end_fill()
        super().draw()


class balloon ( shape ):
    def __init__(self):
        super ().__init__ ()
        self.radius=None
        self.thread =None
        self.thread_angle=None

    def set_attribute(self, attribute: str, value: str):
        attribute=attribute.strip ().lower ()
        if attribute in ("radius"):
            self.radius=int ( value )

        elif attribute in ("thread"):
            self.thread =int ( value)

        elif attribute in ("thread_angle"):
            self.thread_angle =int ( value)

        else:
            super ().set_attribute ( attribute, value )

    def draw(self):
        # face
        self.prepare ()

        for i in range(4):
            if self.fill_color is not None:
                turtle.fillcolor ( self.fill_color )
                turtle.begin_fill ()

            turtle.circle(self.radius-15*i)

            if self.fill_color is not None:
                turtle.end_fill()

        turtle.right (self.thread_angle )
        turtle.forward( self.thread )
        super ().draw ()


class rose_and_heart ( shape ):
    def __init__(self):
        super ().__init__ ()
        self.radius=None
        self.petal_color=None
        self.leaf_color=None
        self.heart_color=None

    def set_attribute(self, attribute: str, value: str):
        attribute=attribute.strip ().lower ()
        if attribute in ("radius"):
            self.radius=int ( value )

        elif attribute in ("petal_color"):
            self.petal_color= value

        elif attribute in ("leaf_color"):
            self.leaf_color= value

        elif attribute in ("heart_color"):
            self.heart_color= value
        else:
            super ().set_attribute ( attribute, value )

    def draw(self):
        self.prepare ()

        # Rosen und Herzballon

        # Blumen Basis

        turtle.fillcolor ( self.petal_color )
        turtle.begin_fill ()

        turtle.circle ( 9, 175 )
        turtle.circle ( 24, 111 )
        turtle.left ( 49 )
        turtle.circle ( 61, 44 )
        turtle.circle ( 21, 171 )
        turtle.right ( 25 )
        turtle.forward ( 31 )
        turtle.left ( 11 )
        turtle.circle ( 31, 111 )
        turtle.forward ( 21 )
        turtle.left ( 41 )
        turtle.circle ( 91, 71 )
        turtle.circle ( 31, 151 )
        turtle.right ( 31 )
        turtle.forward ( 16 )
        turtle.circle ( 81, 91 )
        turtle.left ( 16 )
        turtle.forward ( 46 )
        turtle.right ( 166 )
        turtle.forward ( 21 )
        turtle.left ( 156 )
        turtle.circle ( 151, 81 )
        turtle.left ( 51 )
        turtle.circle ( 151, 91 )
        turtle.end_fill ()

        # Blütenblatt 1
        turtle.left ( 149 )
        turtle.circle ( -89, 69 )
        turtle.left ( 21 )
        turtle.circle ( 76, 106 )
        turtle.setheading ( 61 )
        turtle.circle ( 80, 97 )
        turtle.circle ( -90, 41 )

        # Blütenblatt 2
        turtle.left ( 181 )
        turtle.circle ( 90, 41 )
        turtle.circle ( -80, 97 )
        turtle.setheading ( -82 )

        # Grünblatt 1
        turtle.forward ( 30.5 )
        turtle.left ( 90.5 )
        turtle.forward ( 25.6 )
        turtle.left ( 44 )
        turtle.fillcolor ( self.leaf_color)
        turtle.begin_fill ()
        turtle.circle ( -81, 91 )
        turtle.right ( 89 )
        turtle.circle ( -81, 91 )
        turtle.end_fill ()
        turtle.right ( 136 )
        turtle.forward ( 61 )
        turtle.left ( 181 )
        turtle.forward ( 86 )
        turtle.left ( 91 )
        turtle.forward ( 81 )

        # Grünblatt  2
        turtle.right ( 91 )
        turtle.right ( 44 )
        turtle.fillcolor ( self.leaf_color )
        turtle.begin_fill ()
        turtle.circle ( 81, 91 )
        turtle.left ( 89 )
        turtle.circle ( 81, 91 )
        turtle.end_fill ()
        turtle.left ( 136 )
        turtle.forward ( 61 )
        turtle.left ( 181 )
        turtle.forward ( 61 )
        turtle.right ( 91 )
        turtle.circle ( 201, 59 )

        # Ballon in Herzform
        turtle.fillcolor ( self.heart_color )
        turtle.begin_fill ()
        turtle.left ( 140 )
        turtle.forward ( 111.65 )
        for i in range ( 200 ):
            turtle.right ( 1 )
            turtle.forward ( 1 )
        turtle.left ( 120 )
        for i in range ( 200 ):
            turtle.right ( 1 )
            turtle.forward ( 1 )
        turtle.forward ( 111.65 )
        turtle.right ( 40 )

        # Ballongriff in Rundform
        turtle.circle ( self.radius )

        turtle.end_fill ()
        super ().draw ()


class triangle(shape):
>>>>>>> Stashed changes
    def __init__(self):
        super().__init__()
        self.length = None
        self.height = None

    def set_attribute(self, attribute: str, value: str):
<<<<<<< Updated upstream
        attribute=attribute.strip ().lower ()
        if attribute in ("radius"):
            self.radius=int ( value )
        else:
            super ().set_attribute ( attribute, value )

    def draw(self):
        self.prepare ()
        turtle.penup()
        turtle.setposition(self.x_pos + self.radius, self.y_pos)
        turtle.pendown()
        
        if self.fill_color is not None:
            turtle.fillcolor(self.fill_color)
            turtle.begin_fill()
            turtle.circle(self.radius)
            turtle.end_fill()
        else:
            turtle.circle(self.radius)
        super().draw()
=======
        attribute = attribute.strip().lower()

        if attribute in ("length",):
            self.length = int(value)
>>>>>>> Stashed changes

        elif attribute in ("height",):
            self.height = int(value)

        else:
            super().set_attribute(attribute, value)

    def draw(self):
        self.prepare()
        if self.fill_color is not None:
            turtle.fillcolor(self.fill_color)
            turtle.begin_fill()
        angle_right_corner = math.atan((self.length/2) / self.height)
        angle_right_corner = math.degrees(angle_right_corner)
        angle_top_corner = 2 * angle_right_corner
        angle_top_corner = 180 - angle_top_corner
        angle_right_corner = 180 - angle_right_corner
        angle_top_corner = 180 - angle_top_corner
        side_length = math.sqrt((self.length/2)**2 + (self.height**2))
        turtle.forward(self.length)
        turtle.left(angle_right_corner)
        turtle.forward(side_length)
        turtle.left(angle_top_corner)
        turtle.forward(side_length)

        if self.fill_color is not None:
            turtle.end_fill()
        print(angle_right_corner)
        print(angle_top_corner)

        super().draw()



class Tag ():
    def find_tag(text, start: int, end: int):
        assert start <= end

        tag=Tag ()
        # Wirft Fehler falls das Tag nicht gefunden werden kann
        try:
            tag.find_opening_tag ( text, start, end )
        except ValueError:
            return None
        # print(tag.tag_name)
        tag.find_closing_tag ( text, tag.opening_tag_end, end )
        if hasattr ( tag, "closing_tag_start" ) and hasattr ( tag, "closing_tag_end" ):
            return tag
        else:
            return None

    def find_opening_tag(self, text, start: int, end: int):
        self.opening_tag_start=text.index ( "<", start, end )
        self.opening_tag_end=text.index ( ">", self.opening_tag_start, end )

        # tag_name wird ohne die Klammern gespeichert
        self.tag_name=text[self.opening_tag_start + 1:
                           self.opening_tag_end]
        return self

    def find_closing_tag(self, text, start: int, end: int):
        opening_tag=f"<{self.tag_name}>"
        closing_tag=f"</{self.tag_name}>"

        # print(opening_tag, "#####", closing_tag)
        level=0
        # Die komplette Länge des Texts durchgehen und schauen, ob einer der
        # Tags gefunden wird.
        for index in range ( start, end ):
            # Falls der selbe Tag gefunden wird, sind wir ein level tiefer,
            # dieses Level muss auch wieder verlassen werden
            if text.startswith ( opening_tag, index ):
                level+=1
            if text.startswith ( closing_tag, index ):
                # Wenn wir auf dem richtigen Level sind, sind wir fertig mit
                # der suche nach dem schließenden Tag
                if level == 0:
                    self.closing_tag_start=index
                    self.closing_tag_end=index + len ( closing_tag )
                    break
                else:
                    level-=1
        return self


def read_tml(file_path: str):
    # open file with file reader
    with open ( file_path ) as file:
        # delegate everything in the file to the find_elements-function
        # to find all children in the code
        text=file.read ()
        tag=Tag.find_tag ( text, start=0, end=len ( text ) )

        shape=get_shape ( tag.tag_name )
        find_elements ( text, shape, tag.opening_tag_end, tag.closing_tag_start )
    shape.draw ()


def get_shape(shape_name: str):
    if shape_name.lower () == "circle":
        return circle ()
    if shape_name.lower () == "rectangle":
        return rectangle ()
    if shape_name.lower () == "line":
        return line ()
    if shape_name.lower () == "balloon":
        return balloon ()
    if shape_name.lower () == "rose_and_heart":
        return rose_and_heart ()
    if shape_name.lower() == "triangle":
        return triangle()
    if shape_name.lower () == "image":
        return image ()
    return None


def find_elements(text: str, shape, start: int, end: int):
    tag=Tag.find_tag ( text, start, end )
    while tag:
        sub_shape=get_shape ( tag.tag_name )
        if sub_shape is not None:
            shape.append_shape ( sub_shape )
        else:
            shape.set_attribute ( tag.tag_name,
                                  text[tag.opening_tag_end + 1:
                                       tag.closing_tag_start] )

        find_elements ( text, sub_shape, tag.opening_tag_end, tag.closing_tag_start )
        tag=Tag.find_tag ( text, tag.closing_tag_end, end )
    # suchen jedes Klammerpaar im angegebenen Text und rufen  find_elements auf, und rekursiv mit dem Inhalt


read_tml ( "sample.tml" )
