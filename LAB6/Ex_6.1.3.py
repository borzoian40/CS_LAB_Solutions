"""
Write functions:
def sphere_volume(r)
def sphere_surface(r)
def cylinder_volume(r,h)
def cylinder_surface(r,h)
def cone_volume(r,h)
def cone_surface(r,h)

"""

import math

def sphere_volume(r):
    volume_Sphere = float((4 / 3) * (math.pi) * (r ** 3))
    print(f"Sphere Volume: {volume_Sphere:0.2f}")
    # 4/3(pi)(r**3)


def sphere_surface(r):
    surface_Sphere = float((4) * (math.pi) * (r ** 2))
    print(f"Sphere surface: {surface_Sphere:0.2f}")
    # 4(pi)(r**2)


def cylinder_volume(r, h):
    volume_Cylinder = float((math.pi) * (r ** 2) * (h))
    print(f"Cylinder Volume:{volume_Cylinder: 0.2f}")


# (pi)(r**2)(h)

def cylinder_surface(r, h):
    surface_Cylinder = float(
        (2 * (math.pi) * r * h) + (2 * (math.pi) * (r ** 2))
    )
    print(f"Cylinder surface:{surface_Cylinder: 0.2f}")


# 2πrh+2πr**2

def cone_volume(r, h):
    volume_Cone = float((math.pi) * (r ** 2) * (h / 3))
    print(f"Cone volume: {volume_Cone: 0.2f}")


# (pi)(r**2)(h/3)

def cone_surface(r, h):
    l = float((r ** 2) + (h ** 2))
    surface_Cone = float((math.pi) * (r ** 2) + (math.pi) * (r) * l)
    print(f"Cone surface: {surface_Cone: 0.2f}")


##SA = πr2 + πrl

if __name__ == "__main__":
    radius = int(input("Please enter the length of your radius: "))
    height = int(input("Please enter the length of your height: "))
    sphere_volume(radius)
    sphere_surface(radius)
    cylinder_volume(radius, height)
    cylinder_surface(radius, height)
    cone_volume(radius, height)
    cone_surface(radius, height)
