# see https://stackoverflow.com/questions/7877282/how-to-send-image-generated-by-pil-to-browser#10170635
from flask import Flask, send_file
from PIL import Image                                                            
import numpy as np
from io import BytesIO
app = Flask(__name__)

def generate_random_image(size=(100,100,3), range=(0,255)):
    img = np.random.randint(low=range[0], high=range[1], size=(100,100))
    im = Image.fromarray(img.astype(np.uint8))
    return(im)

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


@app.route('/randomimage/')
def serve_img():
    #img = Image.new('RGB', ...)
    img = generate_random_image()
    return serve_pil_image(img)

if __name__ == "__main__":
    app.run()
