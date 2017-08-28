from PIL import Image,ImageFont,ImageDraw

font_addr = "/home/king/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-M.ttf"
def font():
    return ImageFont.truetype(font_addr, size=font_size())

def font_size():
    return 80

text = "Never Complain"
pic_addr = "/home/king/Downloads/144025vmmuz2z0xyd29k6s.jpg"
pic = Image.open(pic_addr)
width, height = pic.size
draw = ImageDraw.Draw(pic)
ttf_width, ttf_height = font().getsize(text)
#获得字体的宽度和高度
draw.text(((width-ttf_width)/2, (height-ttf_height)/2), text, fill='white',  font=font())
#居中显示
# pic.save('/home/king/Downloads/Never Complain_2.jpg')
pic.show()
