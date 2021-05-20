# Project: TML-READER

**Topic**: 

The theme of this project aims to develop a markup language, such as TML, in order to be able to easily create graphics from turtle in a declarative way.

**Structure**:

This project is mainly divided into three parts, which comprises validator, TML file and renderer. 

1. The first part validator determines whether an entered string is a valid markup language according to the given rules, which refers to two python scripts, that is tml-reader.py and shapes.py. 

a) 

Initially, for the sake of parsing the file of TML, it is necessary to structure the parse script in python. Therefore, we have defined a class of *Tag*, a class of *find_elements* as well as a class of *read_tml*.

*Tag* class tries to read tag-pairs in TML, simultaneously to save the position of the tags in a given text as well as the name of the tag. Within tag class, three functions are defined. They are “find_tag”, “find_opening_tag” and “find_closing_tag”. In the function of “find_tag”, opening tag and closing tag have been positioned. In the function of “find_opening_tag”, the start of opening tag and the end of opening tag as well as opening tag name have been placed have been read. In the function of “find_closing_tag”, it is crucial to search the closing tag start and the closing tag end via the complete length of texts according to its existing position. 

*Find_elements* class is expected to search recursively the text element within defined shape by using the aforementioned method of finding tag. 

*Read_tml* class is designed to open and read TML file. The tags and shapes can be linked and parsed, as they are defined in the script and appeared in file with given variables. 

b) 

After the laying down of parsing foundation in tml-reader script, we can deliberately add up the shapes which we would like to draw by using turtle function. 
Hence, a separate script “shapes.py” is drafted with importing turtle and math functions. 

On top of the individual shapes design, a class *Shape* shall be defined as the basement and contains all basic shape drawing functionality. According to the turtle function, the basic shape function such as x position, y position, border color, border width, fill color and others can be set with given attribute to a given value. Hereby, the function of “__init__” and the function of “set_attribute” are assigned to default. Besides, the function of “prepare” and the function of “draw” are also designed in order. The function of prepare stands for setting up starting position and other functions and ready for draw. The function of draw is standard draw call and calls all sub-shapes to draw. Thereafter, a class of *Image* encompass all necessary information about the drawing board. It has similar function as turtle.screen. 

All functions defined in class *Shape* shall be also included in individual sub-shape class, except the function of “prepare”, which can be replaced as self.prepare() in sub-shape class. With such structural foundation, we have defined several individual shapes by following its shaping rules. The individual sub-shapes we have drawn here are circle, rectangle, balloon, rose and heart, triangle as well as parallelogram.  

Last but not the least, a function of “get_shape” is vital for getting individual names of sub-shapes defined as variables in order to call all defined functions. 

2. The second part TML file comprise the standard Markup Language structure with parent and children hierarchy.  The names of each sub-shapes will be given here as attributes, along with the given variables in each function. The variables can be changed at will, as the script maintains unchangeable as what we design for. 

3. The third part renderer generates a graphic from the script with the help of turtle function and by reading variables in TML file. In addition, the renderer function is a program for the visualization of Markup Language and Scalable Vector Graphics. It allows to play back content streamed with the player from the server and to operate the player with a Digital Media Controller device that is connected via the network. In our case, the renderer shows as “output_graphics” in the folder.  

