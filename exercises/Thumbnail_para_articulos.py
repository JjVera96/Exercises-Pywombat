from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


if __name__ == '__main__':
    color = input('Ingresa un color hexadecimal: ')
    text = input('Ingresa el titulo de la imagen: ')
    size = (1000, 300)
    image = Image.new('RGBA', size, color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/roboto/hinted/Roboto-Bold.ttf', 65)
    name = './resources/{}.png'.format(text.replace(' ', '_'))
    text_width, text_height = draw.textsize(text, font)
    print(text_width, text_height)

    image.show()
    image.save(name)
