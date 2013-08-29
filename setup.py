import os
from distutils.core import setup
import py2exe

#hack which fixes the pygame mixer and pygame font
origIsSystemDLL = py2exe.build_exe.isSystemDLL # save the orginal before we edit it
def isSystemDLL(pathname):
    # checks if the freetype and ogg dll files are being included
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll","sdl_ttf.dll"): # "sdl_ttf.dll" added by arit.
            return 0
    return origIsSystemDLL(pathname) # return the orginal function
py2exe.build_exe.isSystemDLL = isSystemDLL # override the default function with this one
 
img_files = []
for file in os.listdir('C:/Users/Paul/Desktop/HurryUpChef/image/'):
    filePath = 'C:/Users/Paul/Desktop/HurryUpChef/image/' + file
    if os.path.isfile(filePath): # skip directories
        img_files.append('image/'+file)

font_files = []
for file in os.listdir('C:/Users/Paul/Desktop/HurryUpChef/font/'):
    filePath = 'C:/Users/Paul/Desktop/HurryUpChef/font/' + file
    if os.path.isfile(filePath): # skip directories
        font_files.append('font/'+file)

sound_files = []
for file in os.listdir('C:/Users/Paul/Desktop/HurryUpChef/sound/'):
    filePath = 'C:/Users/Paul/Desktop/HurryUpChef/sound/' + file
    if os.path.isfile(filePath): # skip directories
        sound_files.append('sound/'+file)

Mydata_files = []
Mydata_files.append(('image', img_files))
Mydata_files.append(('font', font_files))
Mydata_files.append(('sound', sound_files))

setup(
    #version = "0.1",
    #description = "Hurry Up Chef",
    #name = "HurryUpChef",
    windows = [{"script":"game.py"}],
    data_files = Mydata_files
)