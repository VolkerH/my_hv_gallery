# see https://stackoverflow.com/questions/7877282/how-to-send-image-generated-by-pil-to-browser#10170635

def serve_pil_image(pil_img):
    img_io = StringIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


@app.route('some/route/')
def serve_img():
    img = Image.new('RGB', ...)
    return serve_pil_image(img)
