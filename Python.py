from ursina import *
import random

def update():
    #cube.x += 0.01
    #cube.y += 0.01
    #cube.z += 0.1

    #cube.rotation_z += 1
    #cube.rotation_y += 1

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    cube.color = color.rgb(r,g,b)
    cube.rotation_y += 1

app = Ursina()

cube = Entity(model="cube", color=color.rgb(200,200,0), scale=6)

app.run()