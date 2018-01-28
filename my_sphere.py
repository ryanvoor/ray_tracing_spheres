# author: Ryan Voor
# my sphere class

#####################
##### The Class #####
#####################

class MySphere:

    def __init__(self):
       self.radius              = None
       self.x                   = None
       self.y                   = None
       self.z                   = None
       self.surface_color_r     = None
       self.surface_color_g     = None
       self.surface_color_b     = None

    def set_radius(self, radius):
        self.radius = radius

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def set_surface_color_r(self, surface_color_r):
        self.surface_color_r = surface_color_r

    def set_surface_color_g(self, surface_color_g):
        self.surface_color_g = surface_color_g

    def set_surface_color_b(self, surface_color_b):
        self.surface_color_b = surface_color_b


#####################
##### Functions #####
#####################

# returns a sphere with the specified parameters
def create_sphere(radius, x, y, z, surface_color_r, surface_color_g, surface_color_b):
    my_sphere = MySphere()
    my_sphere.set_radius(radius)
    my_sphere.set_x(x)
    my_sphere.set_y(y)
    my_sphere.set_z(z)
    my_sphere.set_surface_color_r(surface_color_r)
    my_sphere.set_surface_color_g(surface_color_g)
    my_sphere.set_surface_color_b(surface_color_b)

    return my_sphere

