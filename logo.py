#!/usr/bin/env python3
# AU82 logo at any W H (square/landscape/portrait): black, red circle of diameter min(W,H)/phi centered,
# white "AU82" in Arial at int(radius/phi), anchored at the center.   usage: python3 logo.py W H out.png
import sys,subprocess;from PIL import Image,ImageDraw,ImageFont
W,H,o=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3];p=(1+5**.5)/2;r=min(W,H)/p/2
im=Image.new('RGBA',(W,H),'#000000');d=ImageDraw.Draw(im)
d.ellipse([W/2-r,H/2-r,W/2+r,H/2+r],fill='#FF0000',outline='#FF0000')
d.text((W/2,H/2),'AU82',fill='#FFFFFF',font=ImageFont.truetype(subprocess.check_output(['fc-match','-f','%{file}','Arial']).decode(),int(r/p)),anchor='mm');im.save(o)
