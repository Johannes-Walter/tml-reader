"""
A Class containig all possible shapes and a function to access them easily.
"""

import turtle
import math


class Shape:
    """Baseclass for shapes, contains basic functionality."""

    def __init__(self):
        """
        Generate a new Baseshape.

        It is useful to call this Baseobject in the init of Subclasses,
        in order to create some Basevalues to draw the shapes.

        Returns
        -------
        None.

        """
        self.sub_shapes = list()
        self.x_pos = None
        self.y_pos = None
        self.border_color = "black"
        self.border_width = 1
        self.fill_color = None
        self.angle = 0

    def append_shape(self, shape):
        """
        Add subshapes to this shape.

        Parameters
        ----------
        shape : Shape
            Another shape to add..

        Returns
        -------
        None.

        """
        self.sub_shapes.append(shape)

    def set_attribute(self, attribute: str, value: str):
        """
        Try to set an given attribute to an given Value.

        Parameters
        ----------
        attribute : str
            Attribute to change. Should be the name of a Tag.
        value : str
            Value to set.

        Raises
        ------
        ValueError
            If there is no such Attribute, a ValueError is raised.

        Returns
        -------
        None.

        """
        attribute = attribute.strip().lower()

        if attribute in ("x_pos",):
            self.x_pos = int(value)

        elif attribute in ("y_pos",):
            self.y_pos = int(value)

        elif attribute in ("border_color",):
            self.border_color = value

        elif attribute in ("border_width",):
            self.border_width = int(value)

        elif attribute in ("fill_color",):
            self.fill_color = value

        elif attribute in ("angle",):
            self.angle = int(value)

        else:
            raise ValueError

    def prepare(self):
        """
        Call this function before drawing a shape.

        It will set the position and Angle of the turtle, as well as
        set the fill_color, border_color and border_width.
        Additionally, the pen is lifted and set.

        Returns
        -------
        None.

        """
        turtle.penup()
        turtle.setposition(self.x_pos, self.y_pos)
        turtle.setheading(self.angle)
        turtle.pencolor(self.border_color)
        turtle.width(self.border_width)
        turtle.pendown()

    def draw(self):
        """
        Standart draw call, calls all subshapes to draw.

        Returns
        -------
        None.

        """
        print(self.__dict__)
        for shape in self.sub_shapes:
            shape.draw()


class Image(Shape):
    """
    Image-"Shape". This class contains information about the drawingboard.

    I.e. how big the image should be or which backgroundcolor should be used.
    """

    def __init__(self):
        """
        Generate an Image and set the standart-configuration.

        Returns
        -------
        None.

        """
        super().__init__()
        self.lower_left_x = 0
        self.lower_left_y = 0
        self.upper_right_x = 1000
        self.upper_right_y = 1000
        self.background_color = None

    def set_attribute(self, attribute: str, value: str):
        """
        Try to set an given attribute to an given Value.

        In this variant of the Funktion only some Attributes are allowed to
        be set, like 'lower_left_x'.

        Parameters
        ----------
        attribute : str
            Attribute to change. Should be the name of a Tag.
        value : str
            Value to set.

        Raises
        ------
        ValueError
            If there is no such Attribute, a ValueError is raised.

        Returns
        -------
        None.

        """
        attribute = attribute.strip().lower()

        if attribute in ("llx", "lower_left_x"):
            self.lower_left_x = int(value)

        elif attribute in ("lly", "lower_left_y"):
            self.lower_left_y = int(value)

        elif attribute in ("urx", "upper_right_x"):
            self.upper_right_x = int(value)

        elif attribute in ("ury", "upper_right_y"):
            self.upper_right_y = int(value)

        else:
            raise ValueError

    def draw(self):
        """
        Draw the whole image with every Shape contained.

        Returns
        -------
        None.

        """
        turtle.setworldcoordinates(self.lower_left_x,
                                   self.lower_left_y,
                                   self.upper_right_x,
                                   self.upper_right_y)

        turtle.screensize(self.upper_right_y - self.lower_left_y,
                          self.upper_right_x - self.lower_left_x)
        if self.background_color is not None:
            turtle.bgcolor(self.background_color)
        super().draw()
        turtle.done()
        turtle.bye()


class Circle(Shape):
    """A shape for a circle."""

    def __init__(self):
        """
        Generate an Circle to draw inside the Image.

        Returns
        -------
        None.

        """
        super().__init__()
        self.radius = None

    def set_attribute(self, attribute: str, value: str):
        """
        Try to set an given attribute to an given Value.

        Parameters
        ----------
        attribute : str
            Attribute to change. Should be the name of a Tag.
        value : str
            Value to set.

        Raises
        ------
        ValueError
            If there is no such Attribute, a ValueError is raised.

        Returns
        -------
        None.

        """
        attribute = attribute.strip().lower()
        if attribute in ("radius",):
            self.radius = int(value)

        else:
            super().set_attribute(attribute, value)

    def draw(self):
        """
        Draw this Circle and all subshapes.

        Returns
        -------
        None.

        """
        self.prepare()

        # We have to move the turtle around, in order to position it correctly
        # The "normal" implementation would draw the circle to the right of
        # the turtle, but we want the "origitn" of the circle in the
        # lower-left-corner.
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


class Line(Shape):
    """A simple Line which can be drawn by the turtle."""

    def __init__(self):
        """
        Generate a Line to draw inside the Image.

        Returns
        -------
        None.

        """
        super().__init__()
        self.length = None

    def set_attribute(self, attribute: str, value: str):
        """
        Try to set an given attribute to an given Value.

        Parameters
        ----------
        attribute : str
            Attribute to change. Should be the name of a Tag.
        value : str
            Value to set.

        Raises
        ------
        ValueError
            If there is no such Attribute, a ValueError is raised.

        Returns
        -------
        None.

        """
        attribute = attribute.strip().lower()

        if attribute in ("length",):
            self.length = int(value)

        else:
            super().set_attribute(attribute, value)

    def draw(self):
        """
        Draw this Line and all subshapes.

        Returns
        -------
        None.

        """
        self.prepare()
        super().draw()


class Rectangle(Shape):
    """A simple Rectangle-Shape."""

    def __init__(self):
        """
        Generate a rectangle to draw inside the image.

        Returns
        -------
        None.

        """
        super().__init__()
        self.height = None
        self.width = None

    def set_attribute(self, attribute: str, value: str):
        """
        Try to set an given attribute to an given Value.

        Parameters
        ----------
        attribute : str
            Attribute to change. Should be the name of a Tag.
        value : str
            Value to set.

        Raises
        ------
        ValueError
            If there is no such Attribute, a ValueError is raised.

        Returns
        -------
        None.

        """
        attribute = attribute.strip().lower()
        
        if attribute in ("height",):
            self.height = int(value)

        elif attribute in ("width",):
            self.width = int(value)

        else:
            super().set_attribute(attribute, value)

    def draw(self):
        """
        Draw this Rectangle and all subshapes.

        Returns
        -------
        None.

        """
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


class Balloon ( Shape ):
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
        """
        

        Returns
        -------
        None.

        """
        # face
        self.prepare ()

        for i in range(4):
            if self.fill_color is not None:
                turtle.fillcolor ( self.fill_color )
                turtle.begin_fill ()

            turtle.circle(self.radius-15 * i)

            if self.fill_color is not None:
                turtle.end_fill()

        turtle.right(self.thread_angle)
        turtle.forward( self.thread )
        super ().draw ()


class Rose_and_heart ( Shape ):
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


class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.length = None
        self.height = None

    def set_attribute(self, attribute: str, value: str):
        attribute=attribute.strip ().lower ()
        print(value)
        if attribute in ("length",):
            self.length = int(value)
        elif attribute in ("height",):
            self.height = int(value)
        else:
            super().set_attribute(attribute, value)

    # def draw(self):
    #     self.prepare()
    #     if self.fill_color is not None:
    #         turtle.fillcolor(self.fill_color)
    #         turtle.begin_fill()
    #     angle_right_corner = math.atan((self.length/2) / self.height)
    #     angle_right_corner = math.degrees(angle_right_corner)
    #     angle_top_corner = 2 * angle_right_corner
    #     angle_top_corner = 180 - angle_top_corner
    #     angle_right_corner = 180 - angle_right_corner
    #     angle_top_corner = 180 - angle_top_corner
    #     side_length = math.sqrt((self.length/2)**2 + (self.height**2))
    #     turtle.forward(self.length)
    #     turtle.left(angle_right_corner)
    #     turtle.forward(side_length)
    #     turtle.left(angle_top_corner)
    #     turtle.forward(side_length)
    #     turtle.left(angle_right_corner)
    #     turtle.forward(self.length)

    #     if self.fill_color is not None:
    #         turtle.end_fill()
    #     print(angle_right_corner)
    #     print(angle_top_corner)

    #     super().draw()

    def draw(self):
        self.prepare()
        if self.fill_color is not None:
            turtle.fillcolor(self.fill_color)
            turtle.begin_fill()
        angle_right_corner = math.atan(self.height / (self.length/2))
        angle_right_corner = math.degrees(angle_right_corner)
        angle_top_corner = 2 * angle_right_corner
        angle_right_corner = 180 - angle_right_corner
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



def get_shape(shape_name: str):
    """
    Get the shape named as Variable.

    Parameters
    ----------
    shape_name : str
        DESCRIPTION.

    Returns
    -------
    TYPE
        A shape, None if .

    """
    if shape_name.lower() == "circle":
        return Circle()
    if shape_name.lower() == "rectangle":
        return Rectangle()
    if shape_name.lower() == "line":
        return Line()
    if shape_name.lower() == "balloon":
        return Balloon()
    if shape_name.lower() == "rose_and_heart":
        return Rose_and_heart()
    if shape_name.lower() == "triangle":
        return Triangle()
    if shape_name.lower() == "image":
        return Image()
    return None
