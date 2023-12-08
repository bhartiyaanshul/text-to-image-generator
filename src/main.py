from fastapi import FastAPI, HTTPException
from starlette.responses import StreamingResponse
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a custom font size
custom_font_size = 20

custom_font_size_name = 50
custom_font_size_num = 40
custom_font_size_token = 30
verticle_space = 120

def generate_image(name, num, token_text):
    width = 400
    height = 400    

    img = Image.open("/Users/anshulbhartiya/Desktop/Eth Project/sample2.jpeg")
    draw = ImageDraw.Draw(img)
    
    font1 = ImageFont.truetype("/Users/anshulbhartiya/Desktop/Eth Project/arial/arial.ttf", size=custom_font_size_name)
    font2 = ImageFont.truetype("/Users/anshulbhartiya/Desktop/Eth Project/arial/arial.ttf", size=custom_font_size_num)
    font3 = ImageFont.truetype("/Users/anshulbhartiya/Desktop/Eth Project/arial/arial.ttf", size=custom_font_size_token)
    

    name_bbox = draw.textbbox((0, 0), name, font=font1)
    name_width = name_bbox[2] - name_bbox[0]
    xName = (width - name_width) / 2
    yName = (height - custom_font_size_name - verticle_space) / 2 
    
    combined_text = f"{num} {token_text}"
    
    combined_bbox = draw.textbbox((0, 0), combined_text, font=font2)
    combined_width = combined_bbox[2] - combined_bbox[0]
    xCombined = (width - combined_width) / 2
    yCombined = yName + custom_font_size_name + verticle_space / 2

    draw.text((xName, yName), name, align='center',font=font1, fill =(0, 0, 0))
    draw.text((xCombined, yCombined), combined_text, align='center', font=font2, fill=(0, 0, 0))
    
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    return img_buffer

@app.get("/generate_image/{name}/{num}")
async def generate_image_endpoint(name: str, num: str, token_text: str):
    try:
        img_buffer = generate_image(name, num, token_text)
        return StreamingResponse(img_buffer, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
