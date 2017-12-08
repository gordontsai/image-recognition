import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time


##First Part
#i= Image.open('images/dot.png')


# #iar outputs an array within an array within an array
# #Each array within first array represents a row.
# #Each row within an array represents a row
# #There are four columns within a row with ['r','g','b',alpha] values
# #Alpha is basically like fade
# #Larger values are more transparent so 255 for red is ligther than 230 for red
# iar=np.asarray(i)


# plt.imshow(iar)
# plt.show()


def thresholde(imageArray):
  blanceAr=[]
  newAr=imageArray

  for eachRow in imageArray:
    for eachPix in eachRow:
      print(eachPix)

      time.sleep(5)


i1=Image.open('images/numbers/0.1.png')
iar1=np.asarray(i1)

i2=Image.open('images/numbers/y0.4.png')
iar2=np.asarray(i2)

i3=Image.open('images/numbers/y0.5.png')
iar3=np.asarray(i3)

i4=Image.open('images/sentdex.png')
iar4=np.asarray(i4)

fig=plt.figure()
ax1=plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax2=plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax3=plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
ax4=plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)

ax1.imshow(iar1)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()
