### XTREMLY IMPORTANT THINGS, OR NO GAME ###
from ursina import *
from ursina.color import white, light_gray, dark_gray
from ursina.prefabs.first_person_controller import *

sky = Sky() # ITS OBVIOUS TWIN

### LOADING MY NOT SO ORIGINAL ASSETS ###
load_texture('assets/grass_128.png')
load_texture('assets/stone_128.png')
load_texture('assets/wood_128.png')

### INPUT DETECTION AND OTHER SHIT ###
block = 1
def update():
    global block
    if held_keys['1']: block= 1
    if held_keys['2']: block = 2
    if held_keys['3']: block = 3
    if held_keys['escape']: application.quit()

### CREATING A MINE- VOXLECRAFT VOXLE! ###
class Voxle(Button):
    def __init__(self, position=(0,0,0), texture='grass_128'):
        super().__init__(
            parent=scene,
            position= position,
            model='cube',
            origi_yn=0.5,
            texture=texture,
            color=color.light_gray
        )

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block == 1:
                    voxle = Voxle(position=self.position + mouse.normal, texture='grass_128')
                if block == 2:
                    voxle = Voxle(position=self.position + mouse.normal, texture='stone_128')
                if block == 3:
                    voxle = Voxle(position=self.position + mouse.normal, texture='wood_128')
            if key == 'left mouse down':
                destroy(self)

### HOLY SHIT THE ACTUAL GAME ###
app  = Ursina()

sky.texture='sky_default'
for z in range(10): # PLEASE DO NOT REPLECATE FOR YOUR OWN SAFETY THIS IS AN AWFUL IDEA
    for x in range(10):
        voxle = Voxle(position=(x,0,z))

player = FirstPersonController()

app.run()