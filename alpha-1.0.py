from ursina import *
from ursina.color import white, light_gray, dark_gray
from ursina.prefabs.first_person_controller import *

block = 1

def update():
    global block
    if held_keys['1']: block= 1
    if held_keys['2']: block = 2
    if held_keys['3']: block = 3

class Voxle(Button):
    def __init__(self, position=(0,0,0), texture='white_cube', color=color.green):
        super().__init__(
            parent=scene,
            position= position,
            model='cube',
            origi_yn=0.5,
            texture=texture,
            color=color,
        )

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block == 1:
                    voxel = Voxle(position=self.position + mouse.normal, color=color.green)
                if block == 2:
                    voxel = Voxle(position=self.position + mouse.normal, color=color.dark_gray)
                if block == 3:
                    voxel = Voxle(position=self.position + mouse.normal, color=color.brown)

            if key == 'left mouse down':
                destroy(self)

app  = Ursina()

for z in range(16):
    for x in range(16):
        voxel = Voxle(position=(x,0,z))

player = FirstPersonController(y=100)

app.run()