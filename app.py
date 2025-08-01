# app.py

from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import io
import base64
import random

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    title = data.get('title', 'No Title')
    description = data.get('description', 'No Description')
    background_color = data.get('backgroundColor', '#FDEBD0')

    width, height = 1000, 1500
    img = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(img)

    # Draw playful dots
    for _ in range(30):
        x, y = random.randint(0, width), random.randint(0, height)
        size = random.randint(20, 80)
        color = random.choice(["#F7CAC9", "#92A8D1", "#F6E2B3", "#F9AFAE", "#B5EAD7"])
        draw.ellipse([x, y, x+size, y+size], fill=color)

    try:
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 80)
        desc_font = ImageFont.truetype("DejaVuSans.ttf", 50)
    except IOError:
        title_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()

    draw.text((80, 500), title, font=title_font, fill="black")
    draw.text((80, 600), description, font=desc_font, fill="black")

    # Save image to bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Convert to base64 string
    img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')

    # Respond with base64 image string or you can upload to an image host here and send URL
    return jsonify({
        "image": f"data:image/png;base64,{img_base64}"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
