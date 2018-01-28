# This is the starter code for the CS 3451 Ray Tracing project.
#
# The most important part of this code is the interpreter, which will
# help you parse the scene description (.cli) files.
#
# author: Ryan Voor
# I'm altering this code in order to create my project 3A

####################
##### Includes #####
####################

from my_sphere import *
from my_ray import *
from my_hit import *
from my_light import *


###################
##### Globals #####
###################

scene_objects = []
lights = []
fov = -1 # in degrees
background_r = 0
background_g = 0
background_b = 0
ambient_light_color = 0 # TODO this is going to change in project 3B

#####################
##### Functions #####
#####################

def setup():
    size(500, 500)
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)

# read and interpret the appropriate scene description .cli file based on key press
def keyPressed():
    if key == '1':
        print("i1.cli")
        interpreter("i1.cli")
    elif key == '2':
        print("i2.cli")
        interpreter("i2.cli")
    elif key == '3':
        print("i3.cli")
        interpreter("i3.cli")
    elif key == '4':
        print("i4.cli")
        interpreter("i4.cli")
    elif key == '5':
        print("i5.cli")
        interpreter("i5.cli")
    elif key == '6':
        print("i6.cli")
        interpreter("i6.cli")
    elif key == '7':
        print("i7.cli")
        interpreter("i7.cli")
    elif key == '8':
        print("i8.cli")
        interpreter("i8.cli")
    elif key == '9':
        print("i9.cli")
        interpreter("i9.cli")

def interpreter(fname):
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # my code
    current_surface_color_r = 0
    current_surface_color_g = 0
    current_surface_color_b = 0
    # end my code

    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            radius = float(words[1])
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])

            # my code
            global scene_objects
            scene_objects.append(create_sphere(radius, x, y, z, current_surface_color_r, current_surface_color_g, current_surface_color_b))
            # end my code

        elif words[0] == 'fov':

            # my code
            global fov
            fov = float(words[1])
            # end my code

        elif words[0] == 'background':

            # my code
            global background_r
            global background_g
            global background_b
            background_r = float(words[1])
            background_g = float(words[2])
            background_b = float(words[3])
            # end my code

        elif words[0] == 'light':

            # my code
            light_x = float(words[1])
            light_y = float(words[2])
            light_z = float(words[3])
            light_r = float(words[4])
            light_g = float(words[5])
            light_b = float(words[6])

            global lights
            lights.append(create_light(light_x, light_y, light_z, light_r, light_g, light_b))
            # end my code

        elif words[0] == 'surface':

            # my code
            current_surface_color_r = float(words[1])
            current_surface_color_g = float(words[2])
            current_surface_color_b = float(words[3])
            # end my code

        elif words[0] == 'begin':
            pass
        elif words[0] == 'vertex':
            pass
        elif words[0] == 'end':
            pass
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])  # write the image to a file

            # my code
            # reset the background to (0, 0, 0)
            global background_r
            global background_g
            global background_b
            background_r = 0
            background_g = 0
            background_b = 0
            # end my code

            pass

# render the ray tracing scene
def render_scene():
    # set background color
    background_color = color(background_r, background_g, background_b)
    for j in range(height):
        for i in range(width):
            set(i, j, background_color)

    # ray trace for each pixel on the screen
    for j in range(height):
        for i in range(width):
            ray = create_eye_ray(i, j, width, height, fov)

            hits = []
            for object_index in range(len(scene_objects)):
                hit = find_ray_sphere_intersection(ray, scene_objects[object_index])

                if hit is not None:
                    hits.append(hit)

            closest_hit = None
            current_t = None
            for x in range(len(hits)):
                if current_t is None or current_t > hits[x].t:
                    closest_hit = hits[x]
                    current_t = hits[x].t

            if closest_hit is not None:
                pix_color = calculate_pixel_color(closest_hit)
                # pixels are flipped in the Y-axis (not sure why but this fixes it)
                set(i, height - j, pix_color) # fill the pixel with the calculated color

    resetScene()

# should remain empty for this assignment
def draw():
    pass


############################
##### Helper Functions #####
############################

# finds and creates a hit object if there is an
# intersection between the parameter ray and the
# parameter sphere. Returns None if there is no
# such intersection
def find_ray_sphere_intersection(ray, sphere):
    # find t values (roots)
    # None means it's an imaginary root
    x_zero = ray.x
    y_zero = ray.y
    z_zero = ray.z
    x_center = sphere.x
    y_center = sphere.y
    z_center = sphere.z
    dx = ray.dx
    dy = ray.dy
    dz = ray.dz
    r = sphere.radius

    a = dx**2 + dy**2 + dz**2
    b = 2 * (x_zero - x_center) * dx + 2 * (y_zero - y_center) * dy + 2 * (z_zero - z_center) * dz
    c = (x_zero - x_center)**2 + (y_zero - y_center)**2 + (z_zero - z_center)**2 - r**2

    t_one = None
    t_two = None

    if sqrt(b**2 - 4 * a * c) >= 0:
        t_one = (-b + sqrt(b**2 - 4 * a * c)) / 2 * a # plus
        t_two = (-b - sqrt(b**2 - 4 * a * c)) / 2 * a # or minus

    # check to see which scenario we are in
    # 1: we have one root
    #   ray touches edge of the sphere
    #   don't count this as a hit
    # 2: we have 2 roots
    #   ray intersects the sphere directly
    #   check which of the two roots is closer to the ray and use it to make a hit
    # 3: we have imaginary roots
    #   ray misses the sphere entirely
    #   don't make a hit
    hit = None

    # this statement's condition should resolve to true if and only if we have to make a hit
    if t_one != t_two and t_one is not None and t_two is not None:
        hit_t = -1
        if t_one < t_two:
            hit_t = t_one
        else:
            hit_t = t_two

        # make the hit object
        hit_x = x_zero + hit_t * dx
        hit_y = y_zero + hit_t * dy
        hit_z = z_zero + hit_t * dz
        hit_object = sphere

        hit_normal_x_zero = x_center
        hit_normal_y_zero = y_center
        hit_normal_z_zero = z_center
        hit_normal_dx = hit_x
        hit_normal_dy = hit_y
        hit_normal_dz = hit_z

        hit_normal = create_unit_vector(hit_normal_x_zero, hit_normal_y_zero, hit_normal_z_zero, hit_normal_dx, hit_normal_dy, hit_normal_dz) # automatically normalizes

        hit = create_hit(hit_x, hit_y, hit_z, hit_t, hit_object, hit_normal, ray)

    return hit

# calculates and returns the color of the
# pixel for a hit of an eye ray onto an object based
# on the normal of the object at the location of the
# hit, the color of the object, the color of the
# light, the angle of the light sources, etc.
#
# only implements the diffuse shading equation, not the specular or other fancy stuff
def calculate_pixel_color(hit):

    color_r = ambient_light_color
    color_g = ambient_light_color
    color_b = ambient_light_color

    # add the color of the light times max(0, N dot L) to take angles into account
    for i in range(len(lights)):
        # figure out the angle stuff for this light
        light_vector = create_unit_vector(hit.x, hit.y, hit.z, lights[i].x, lights[i].y, lights[i].z) # automatically normalizes
        light_angle_dot_product = light_vector.dx * hit.normal.dx + light_vector.dy * hit.normal.dy + light_vector.dz * hit.normal.dz

        # add the red color of the lights
        current_light_color = lights[i].color_r * max(0, light_angle_dot_product)
        color_r = color_r + current_light_color

        # add the green color of the lights
        current_light_color = lights[i].color_g * max(0, light_angle_dot_product)
        color_g = color_g + current_light_color

        # add the blue color of the lights
        current_light_color = lights[i].color_b * max(0, light_angle_dot_product)
        color_b = color_b + current_light_color

    # multiply by the surface's color
    color_r = color_r * hit.object.surface_color_r
    color_g = color_g * hit.object.surface_color_g
    color_b = color_b * hit.object.surface_color_b

    pixel_color = color(color_r, color_g, color_b)
    return pixel_color

def resetScene():
    global scene_objects
    global lights
    global fov
    global background_r
    global background_g
    global background_b

    scene_objects = []
    lights = []
    fov = -1 # in degrees
    background_r = 0
    background_g = 0
    background_b = 0

