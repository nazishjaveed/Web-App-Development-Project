from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Create a Flask app
app = Flask(__name__)

# Function to generate an image based on the prompt
def generate_image(prompt):
    # Create a blank image with white background
    image = Image.new("RGB", (500, 500), "white")
    draw = ImageDraw.Draw(image)

    # Specify the path to the font file
    font_path = os.path.join(os.path.dirname(__file__), "arial.ttf")

    # Load a font with a larger size
    font = ImageFont.truetype(font_path, 24)

    # Wrap the prompt text
    wrapped_text = textwrap.fill(prompt, width=30)

    # Draw the wrapped text on the image
    draw.text((10, 10), wrapped_text, fill="black", font=font)

    # Save the image
    image_path = os.path.join(os.path.dirname(__file__), "generated_image.png")
    image.save(image_path)
    return image_path


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')

        if prompt:
            image_url = generate_image(prompt)
            return render_template('index.html', image_url=image_url)
        else:
            return render_template('index.html', error='Please enter a description.')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
