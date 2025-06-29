class ScreenSize:
    def __init__(self, width, height):
        if not isinstance(width, int):
            raise TypeError()
        if not isinstance(height, int):
            raise TypeError()
        self.__width = int(width)
        self.__height = int(height)
        
    def get_size(self):
        return (self.__width, self.__height)
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def __str__(self):
        return str(self.get_size())
    
    def __repr__(self):
        return self.__str__()
    
    def __tuple__(self):
        return self.get_size()

class Vector2:
    def __init__(self, x, y):
        if not isinstance(x, int):
            raise TypeError()
        if not isinstance(y, int):
            raise TypeError()
        self.__x = int(x)
        self.__y = int(y)
        
    def get_pos(self):
        return (self.__x, self.__y)
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def __str__(self):
        return str(self.get_pos())
    
    def __repr__(self):
        return self.__str__()
    
    def __tuple__(self):
        return self.get_pos()