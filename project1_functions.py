import math as m



def circle_area(radius: int):
    """
    Function to get the area of a circle
    :param radius: Radius of a circle
    :return: The area of a circle
    
    """
    if type(radius) != int and type(radius) != float:
        raise TypeError('Not a numeric input')
    if radius <= 0:
        raise ValueError('Not positive')
    area = m.pi * radius * radius
    return area
    
    

def rectangle_area(length: int, width: int):
    """
    Function to get the area of a rectangle
    :param lenght: Lenght of the rectangle
    :param width: Width of the rectangle
    :return: The area of a rectangle
    
    """
    if type(length) != int and type(length) != float:
        raise TypeError('Not a numeric input')
    if type(width) != int and type(width) != float:
        raise TypeError('Not a numeric input')
    if length <= 0:
        raise ValueError('Not positive')
    if width <= 0:
        raise ValueError('Not positive')
    area = length * width
    return area
    


def square_area(side_length: int):
    """
    Function to get the area of a square
    :param side lenght: Side lenght of a square
    :return: The area of a square
    
    """
    if type(side_length) != int and type(side_length) != float:
        raise TypeError('Not a numeric input')
    if side_length <= 0:
        raise ValueError('Not positive')
    area = side_length * side_length
    return area
    

def triangle_area(base: int, height: int):
    """
    Function to get the area of a triangle
    :param base: Base of the triangle
    :param height: Height of the triangle
    :return: The area of a triangle
    
    """
    if type(base) != int and type(base) != float:
        raise TypeError('Not a numeric input')
    if type(height) != int and type(height) != float:
        raise TypeError('Not a numeric input')
    if base <= 0:
        raise ValueError('Not positive')
    if height <= 0:
        raise ValueError('Not positive')
    area = (base * height) / 2
    return area
