# author: Ryan Voor
# my light class

#####################
##### The Class #####
#####################

class MyLight:

    def __init__(self):
       self.x       = None
       self.y       = None
       self.z       = None
       self.color_r = None
       self.color_g = None
       self.color_b = None

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def set_color_r(self, color_r):
        self.color_r = color_r

    def set_color_g(self, color_g):
        self.color_g = color_g

    def set_color_b(self, color_b):
        self.color_b = color_b


#####################
##### Functions #####
#####################

# returns a sphere with the specified parameters
def create_light(x, y, z, color_r, color_g, color_b):
    my_light = MyLight()
    my_light.set_x(x)
    my_light.set_y(y)
    my_light.set_z(z)
    my_light.set_color_r(color_r)
    my_light.set_color_g(color_g)
    my_light.set_color_b(color_b)

    return my_light

