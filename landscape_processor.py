import numpy as np
from PIL import Image
import os
from tqdm import tqdm
import numpy as np
import math

size = (1596*2,1078*2)
if __name__ == '__main__':
    print(os.listdir('number_pngs'))
    for file_name in tqdm(os.listdir('landscapes')):
        if '.jpg' in file_name:
            im = Image.open('landscapes/' + file_name)
            if (im.size[0]/im.size[1]) < 1600/1080*1.3 and  (im.size[0]/im.size[1]) < 1600/1080/1.3:
                resized = im.resize(size,Image.BICUBIC)
                resized.save(f'landscapes_{size[0]}_{size[1]}/{file_name}')

