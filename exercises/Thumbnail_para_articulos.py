from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


if __name__ == '__main__':
    color = input('Ingresa un color hexadecimal: ')
    text = input('Ingresa el titulo de la imagen: ')
    size = (1000, 300)
    image = Image.new('RGBA', size, color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSerif.ttf', 65)
    name = './resources/{}.png'.format(text.replace(' ', '_'))
    size_font = draw.textsize(text, font)
    draw.text( ( (size[0] // 2) - (size_font[0] // 2), size[1] // 2 - size_font[1] // 2 ), text , (255, 255, 255), font=font)
    image.save(name)
