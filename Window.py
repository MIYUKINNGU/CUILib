import CUILib.CUI as CUI
import CUILib.Structs as Structs
import CUILib.Error as Error

class Window:
    def __init__(self, name, x, y, width, height, useframe=True, isreadonly=False):
        self.__name = name
        self.__useframe = useframe
        self.__isreadonly = isreadonly
        self.__x = x
        self.__y = y
        
        if width < 2 or height < 2:
            raise ValueError()
        self.__size = Structs.ScreenSize(width, height)
        self.__data = [[" " for j in range(width)] for i in range(height)]
        if not CUI.can_draw(x, y, self.__data):
            raise ValueError()

        if useframe:
            self.resize(width, height)
        self.rename(name)
    
    def draw(self, x, y, data):
        if x < 2-int(not self.__useframe) or y < 2-int(not self.__useframe) or x+len(max(data, key=lambda a:len(a)))-1 > self.__size.get_width()-int(self.__useframe) or y+len(data)-1 > self.__size.get_height()-int(self.__useframe):
            raise ValueError()
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.__data[y+i-1][x+j-1] = data[i][j]
    
    def clear(self):
        self.__data = [[" " for j in range(self.__size.get_width())] for i in range(self.__size.get_height())]
        if self.__useframe:
            self.resize(self.__size.get_width(), self.__size.get_height())
    
    def show(self):
        CUI.draw(self.__x, self.__y, self.__data)
    
    def get_size(self):
        return self.__size
    
    def get_name(self):
        return self.__name
    
    def get_pos(self):
        return Structs.Vector2(self.__x, self.__y)
    
    def is_readonly(self):
        return self.__isreadonly
    
    def use_frame(self):
        return self.__useframe
    
    def rename(self, name):
        if self.__isreadonly:
            raise Error.PropertyError()
        
        self.__name = name
        width = self.__size.get_width()
        if width >= 5 and self.__useframe:
            newname = ""
            if width-2 < len(name):
                newname = name[0:width-5]+"..."
            else:
                newname = name
            n = len(newname)
            for i in range(n):
                self.__data[0][(width-n)//2+i] = newname[i]
    
    def resize(self, width, height):
        if self.__isreadonly:
            raise Error.PropertyError()
        
        self.__data = [["+" if (i == 0 or i == height-1) and (j == 0 or j == width-1) \
                            else "|" if j == 0 or j == width-1 \
                            else "-" if i == 0 or i == height-1 \
                            else self.__data[i][j] if i < self.__size.get_height() and j < self.__size.get_width() \
                            else " " for j in range(width)] for i in range(height)]
        if not CUI.can_draw(self.__x, self.__y, self.__data):
            raise ValueError()
        self.__size = Structs.ScreenSize(width, height)
        self.rename(self.__name)
    
    def set_pos(self, x, y):
        if self.__isreadonly:
            raise Error.PropertyError()
        
        if not CUI.can_draw(x, y, self.__data):
            raise ValueError()
        self.__x = x
        self.__y = y
