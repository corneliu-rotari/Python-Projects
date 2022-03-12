class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def set_width(self, new):
        self.width = new

    def set_height(self, new):
        self.height = new
    
    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return (self.height + self.width) * 2 
    
    def get_diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** 0.5

    def get_picture(self):
        if self.height < 50 and self.width < 50:
            for i in range(self.height):
                pr = "*" * self.width + "" 
                print(pr)
        else:
            print("Too big for picture")
    
    def get_amount_inside(self, heigth_new, width_new):
        i = 0
        count = 0
        if heigth_new <= self.height and width_new <= self.width:
            while i < self.height:
                i = i+ heigth_new
                count = count + 1
            i = self.width // width_new
        return count * i

    def __str__(self):
        return f"Rectangle(height = {self.height}, width = {self.width})"

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self,side,side)
    
    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)
    
    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def __str__(self):
        return f"Square(side = {self.height})"



ret = Rectangle(4,8)
patrat = Square(3)
patrat.set_width(6)
ret.set_width(2)
ret.get_picture()
patrat.get_picture()