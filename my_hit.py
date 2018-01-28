# author: Ryan Voor
# my hit class

#####################
##### The Class #####
#####################

class MyHit:

    def __init__(self):
       self.x      = None
       self.y      = None
       self.z      = None
       self.t      = None
       self.object = None
       self.normal = None
       self.eyeray = None

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    # the distance along the ray that the collision took place at
    def set_t(self, t):
        self.t = t

    # the object that the ray collided with
    def set_object(self, object):
        self.object = object

    def set_normal(self, normal):
        self.normal = normal

    def set_eyeray(self, eyeray):
        self.eyeray = eyeray


#####################
##### Functions #####
#####################

# returns an eye ray for the specified pixel
def create_hit(x, y, z, t, object, normal, eyeray):
    my_hit = MyHit()
    my_hit.set_x(x)
    my_hit.set_y(y)
    my_hit.set_z(z)
    my_hit.set_t(t)
    my_hit.set_object(object)
    my_hit.set_normal(normal)
    my_hit.set_eyeray(eyeray)

    return my_hit

