import PIL,os,glob
from PIL import Image,ImageColor
# filePath = input("拖入文件夹到这里: \t")


filePath="c:\\Users\\pc\\Desktop\\number"

files=glob.glob(filePath+"/*.png")

#######################可自定义区域
#字符间隔
space_x=1

######################

# print(len (images))

#计算最大宽度
max_width=0
#计算最大高度
max_height=0

#图片总宽度
total_width = 0

images=[]

for file in files:
    img = Image.open(file)

    width=img.size[0]

    max_width = max(img.size[0],max_width)
    max_height = max(img.size[1],max_height)
    

    print("img",img)

    images.append(img)

filesCount=len(files)
total_width=max_width*filesCount+(filesCount+1)*space_x

print("max_width",max_width)
print("max_heigth",max_height)
print("total_width",total_width)

newImg = Image.new("RGBA",[total_width,max_height])

cur_x=space_x
for img in images:
    width=img.size[0]
    print(img)
    newImg.paste(img,[cur_x,0])
    cur_x+=max_width+space_x
# newImg.show()

newImg.save(filePath+"\\out.png")
