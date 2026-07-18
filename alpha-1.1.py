from ursina import *
from ursina.color import white, light_gray, dark_gray
from ursina.prefabs.first_person_controller import *

sky = Sky()

def update():
    global block
    if held_keys['1']: block= 1
    if held_keys['2']: block = 2
    if held_keys['3']: block = 3
    if held_keys['4']: block = 4
    if held_keys['5']: block = 5
    if held_keys['6']: block= 6
    if held_keys['7']: block = 7
    if held_keys['8']: block = 8

    if held_keys['escape']: application.quit()

class Voxel(Button):
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
                    voxel = Voxel(position=self.position + mouse.normal, color=color.red)
                if block == 2:
                    voxel = Voxel(position=self.position + mouse.normal, color=color.orange)
                if block == 3:
                    voxel = voxel(position=self.position + mouse.normal, color=color.yellow)
                if block == 4:
                    voxel = Voxle(position=self.position + mouse.normal, color=color.green)
                if block == 5:
                    voxel = Voxle(position=self.position + mouse.normal, color=color.blue)
                if block == 6:
                    voxle = Voxle(position=self.position + mouse.normal, color=color.pink)
                if block == 7:
                    voxle = Voxle(position=self.position + mouse.normal, color=color.white)
                if block == 8:
                    voxle = Voxle(position=self.position + mouse.normal, color=color.black)
            if key == 'left mouse down':
                destroy(self)

app  = Ursina()

sky.texture='sky_default'

for z in range(10):
    for x in range(10):
        voxle = Voxle(position=(x,0,z))

player = FirstPersonController(y=100)

app.run()