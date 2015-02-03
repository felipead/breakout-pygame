from breakout.model.AbstractGameObject import AbstractGameObject
from breakout.geometry.Rectangle import Rectangle
from breakout.util.Drawing import Drawing


_BLOCK_POINTS_BLUE = 10
_BLOCK_POINTS_GREEN = 20
_BLOCK_POINTS_RED = 30

_DEFAULT_HEIGHT = 10
_DEFAULT_WIDTH = 20

_VERTICAL_BORDER = 0.5
_HORIZONTAL_BORDER = 0.5



class Block(AbstractGameObject):

    def __init__(self, engine, position, type, width=_DEFAULT_WIDTH, height=_DEFAULT_HEIGHT):
        AbstractGameObject.__init__(self, engine, position)
        self._width = width
        self._height = height
        self._type = type

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def color(self):
        return self._type.value.color

    @property
    def points(self):
        return self._type.value.points

    @property
    def boundaries(self):
        left = self.position.x - self.width/2.0
        right = self.position.x + self.width/2.0
        top = self.position.y + self.height/2.0
        bottom = self.position.y - self.height/2.0
        return Rectangle(left, bottom, right, top)

    def update(self, milliseconds, tick):
        pass

    def display(self, milliseconds, tick):
        colorTone = (tick % 10)/float(10)
        if colorTone > 1:
            colorTone = 1

        x = self.position.x
        y = self.position.y
        dy = self.height/2.0
        dx = self.width/2.0

        self.__drawOuterRectangle(x, y, dx, dy, colorTone)
        self.__drawInnerRectangle(x, y, dx, dy, colorTone)

    def __drawOuterRectangle(self, x, y, dx, dy, colorTone):
        rgb = self.color.value
        outerColor = (rgb[0] * (1 - colorTone), rgb[1] * (1 - colorTone), rgb[2] * (1 - colorTone))
        Drawing.drawRectangle2d(x, y, dx, dy, outerColor)

    def __drawInnerRectangle(self, x, y, dx, dy, colorTone):
        rgb = self.color.value
        innerColor = (rgb[0] * colorTone, rgb[1] * colorTone, rgb[2] * colorTone)
        Drawing.drawRectangle2d(x, y, dx - _HORIZONTAL_BORDER, dy - _VERTICAL_BORDER, innerColor)

    def __str__(self):
        return "Block {Type: " + str(self._type) + ", Position: " + str(self.position) + "}"
