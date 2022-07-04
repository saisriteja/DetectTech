

from unicodedata import category

categories =       {'ignored-regions': 0, 'pedestrian': 1, 'people': 2, 'bicycle': 3, 'car': 4, 'van': 5, 'truck': 6,
                    'tricycle': 7, 'awning-tricycle': 8, 'bus': 9, 'motor': 10, 'others': 11}


categories = {value:key for key, value in categories.items()}

print(categories)


def writetxt(lines, filename):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')


    


def readtxt(filname):
    with open(filname) as f:
        lines = f.readlines()
    data = []
    for i in lines:
        print(i)
        print( i.split('\n')[0].split(',') )
        x,y,w,h,cla,cat,_,_ = map(int, i.split('\n')[0].split(','))
        # print(i.split('\n')[0])
        # print(x,y,w,h,cla,cat)
        # print('-----------------')
        if cla == 1:
            'car 0.00 0 0.00 587.01 173.33 614.12 200.12 0.00 0.00 0.00 0.00 0.00 0.00 0.00'
            data.append(f'{categories[cat]} 0.00 0 0.00 {x} {y} {w} {h} 0.00 0.00 0.00 0.00 0.00 0.00 0.00')
    return data


print()

import os
from glob import glob

path = '/home/saiteja/DetectTech/dataset/VisDrone2019-DET-train/annotations'

all_files = os.listdir(path)

for f in all_files:
    d = readtxt(os.path.join(path,f))
    print(d)
    writetxt(d, os.path.join('/home/saiteja/DetectTech/dataset/VisDrone2019-DET-train/', 'labels',f))