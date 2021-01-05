import os
from PIL import Image
from pathlib import Path

for foldername, subfolders, filenames in os.walk(Path('/home')):
    #print(foldername)
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.endswith('.jpg') or filename.endswith('png')) :
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        try:
            im = Image.open(Path(foldername, filename))
        except:
            continue

        # Check if width & height are larger than 500.
        width, height = im.size
        if width>500 and height>500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,

    if numPhotoFiles > numNonPhotoFiles:
    # print the absolute path of the folder.
        print(Path(foldername))
