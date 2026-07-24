### XTREMLY IMPORTANT THINGS, OR NO GAME ###
import autoimport
from Infdev.autoimport import textures
from ursina import *
from ursina.color import white, light_gray, dark_gray
from ursina.prefabs.first_person_controller import *

SIZE = 20
SPAWN = 10.5  # SIZE / 2, IF THE SIZE IS A ROUND NUMBER ADD 0.5, OTHERWISE IGNORE IT

sky = Sky()  # ITS OBVIOUS TWIN

### LOADING MY NOT SO ORIGINAL ASSETS ###
textures()
LIST = [
    'vlec-grass',
    'vlec-dirt',
    'vlec-stone',
    'vlec-box',
    'vlec-wood',
    'vlec-cloth',
    'vlec-brick',
]

### INPUT DETECTION AND OTHER SHIT ###
BLOCK = 1
NUM_BLOCKS = len(LIST)

def update():
    global BLOCK
    for i in range(1, NUM_BLOCKS + 1):
        if held_keys[str(i)]:
            BLOCK = i
    if held_keys['escape']:
        application.quit()


### CREATING A MINE- VoxelCRAFT VOXEL! ###
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=LIST[0]):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.light_gray,
        )

    def input(self, key):
        if not self.hovered:
            return

        if key == 'right mouse down':
            HELD_BLOCK = LIST[BLOCK - 1]
            Voxel(position=self.position + mouse.normal, texture=HELD_BLOCK)

        if key == 'left mouse down':
            destroy(self)

### MUSIC GO BRRR ###
background = Audio('assets/Music/Placeholder.mp3', loop=True, autoplay=True)
background.volume = 1.0

### HOLY SHIT THE ACTUAL GAME ###
app = Ursina()
sky.texture = 'sky_default'

for z in range(SIZE):   # USE A MESH. NOT MULTIPLE VOXELS
    for x in range(SIZE):
        Voxel(position=(x, 0, z))

player = FirstPersonController(x=SPAWN, z=SPAWN)
app.run()