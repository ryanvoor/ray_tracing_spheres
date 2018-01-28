# author: Ryan Voor
# my ray class
#
# operates under the assumption that the eye is located at (0, 0, 0)

#####################
##### The Class #####
#####################

class MyRay:

    def __init__(self):
       self.x      = None
       self.y      = None
       self.z      = None
       self.dx     = None
       self.dy     = None
       self.dz     = None

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def set_dx(self, dx):
        self.dx = dx

    def set_dy(self, dy):
        self.dy = dy

    def set_dz(self, dz):
        self.dz = dz


#####################
##### Functions #####
#####################

# returns an eye ray for the specified pixel
def create_eye_ray(i, j, w, h, fov):
    k = tan(radians(fov) / 2)
    dx = (i * (2 * k / w)) - k
    dy = (j * (2 * k / h)) - k
    dz = -1

    # normalize the vector
    magnitude = sqrt(dx**2 + dy**2 + dz**2)
    dx = dx / magnitude
    dy = dy / magnitude
    dz = dz / magnitude

    my_ray = MyRay()
    my_ray.set_x(0)
    my_ray.set_y(0)
    my_ray.set_z(0)
    my_ray.set_dx(dx)
    my_ray.set_dy(dy)
    my_ray.set_dz(dz)

    return my_ray

# create a ray that starts at the origin and has a length of 1
def create_unit_vector(x_zero, y_zero, z_zero, dx, dy, dz):

    # move the ray to the origin
    dx = dx - x_zero
    dy = dy - y_zero
    dz = dz - z_zero
    x_zero = 0
    y_zero = 0
    z_zero = 0

    # make it a unit vector
    magnitude = sqrt(dx**2 + dy**2 + dz**2)
    dx = dx / magnitude
    dy = dy / magnitude
    dz = dz / magnitude

    my_ray = MyRay()
    my_ray.set_x(x_zero)
    my_ray.set_y(y_zero)
    my_ray.set_z(z_zero)
    my_ray.set_dx(dx)
    my_ray.set_dy(dy)
    my_ray.set_dz(dz)

    return my_ray
