def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
import os
import re
from PIL import Image
path = os.getcwd()
g= open("train.txt","w")
for file in os.listdir("Annotations"):
    if ".txt" in file:
        filename = file[:-4]+".jpg"
        f = open("Annotations/"+file)
        h = open("labels/"+file,"w")
        filepath = path + "/imgs/"+filename
        g.write(filepath+"\n")
        for line in f.readlines():
            match = re.findall(r"\((\d+), (\d+)\) \((\d+), (\d+)\)", line)
            if match:
                xmin = float(match[0][0])
                ymin = float(match[0][1])
                xmax = float(match[0][2])
                ymax = float(match[0][3])
                b = (xmin,xmax,ymin,ymax)
                im = Image.open(filepath)
                size = im.size
                bb = convert(size,b)
                h.write("0"+" "+" ".join([str(a) for a in bb])+"\n")
        h.close()
        f.close()
g.close()



