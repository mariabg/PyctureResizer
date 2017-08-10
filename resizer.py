from PIL import Image
import os, sys, datetime

# Starting value for naming the photos
i = 1
groupName = sys.argv[1]
reduction = sys.argv[2]
nPics = sys.argv[3]
directory = os.getcwd()

for filename in os.listdir(directory):
    if filename.lower().endswith(('.jpeg', '.jpg')):
        img = Image.open(filename)
        x = img.size[0]/int(reduction)
        y = img.size[1]/int(reduction)
        newImg = img.resize((x, y), Image.ANTIALIAS)
        name = groupName + '_' + str(i).zfill(int(nPics))
        newImg.save(name + ".JPEG")
        i += 1
