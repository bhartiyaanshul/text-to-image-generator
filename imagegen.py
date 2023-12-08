from PIL import Image, ImageDraw, ImageFont

def generate_image(name, num):
    width = 100
    height = 100

    # Create an image with specified width and height
    img = Image.new('RGB', (width, height), color='white')

    # Create a drawing object
    imgDraw = ImageDraw.Draw(img)

    # Use the default font (system font)
    font = ImageFont.load_default()

    name_bbox = imgDraw.textbbox((0, 0), name, font=font)
    name_width = name_bbox[2] - name_bbox[0]
    name_height = name_bbox[3] - name_bbox[1]

    xName = (width - name_width) / 2
    yName = 10 

    num_bbox = imgDraw.textbbox((0, 0), num, font=font)
    num_width = num_bbox[2] - num_bbox[0]
    num_height = num_bbox[3] - num_bbox[1]

    xNum = (width - num_width) / 2
    yNum = height - num_height - 10 

    imgDraw.text((xName, yName), name, font=font, fill=(255, 0, 0))

    imgDraw.text((xNum, yNum), num, font=font, fill=(255, 0, 0))

    img.save('result.png')

name = input("Enter the Name: ")
num = input("Enter a number: ")

generate_image(name, num)
