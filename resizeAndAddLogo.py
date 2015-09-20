import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.jpg'

logoIm = Image.open(LOGO_FILENAME)
logoIm.resize((50, 50))
logoWidth, logoHeight = logoIm.size
if not os.path.exists('withLogo'):
    os.makedirs('withLogo')
    
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue
    
    im = Image.open(filename)
    width, height = im.size
    
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
            
        print('Resizing %s.....' % (filename))
        im = im.resize((width, height))
        
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight))
    
    im.save(os.path.join('withLogo', filename))