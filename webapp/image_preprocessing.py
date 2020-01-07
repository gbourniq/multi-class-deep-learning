def resize(image_URL):

    import requests
    from io import BytesIO
    from PIL import Image
    from PIL import ImageOps

    desired_size = 128
    response = requests.get(image_URL)
    im = Image.open(BytesIO(response.content))     
    old_size = im.size  # old_size[0] is in (width, height) format
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    im = im.resize(new_size, Image.ANTIALIAS)
    new_im = Image.new("RGB", (desired_size, desired_size))
    new_im.paste(im, ((desired_size-new_size[0])//2,
                        (desired_size-new_size[1])//2))

    delta_w = desired_size - new_size[0]
    delta_h = desired_size - new_size[1]
    padding = (delta_w//2, delta_h//2, delta_w-(delta_w//2), delta_h-(delta_h//2))
    new_im = ImageOps.expand(im, padding)
    new_im.save("base_image_resized.jpeg", "JPEG")
    
    return "base_image_resized.jpeg"

def equalize_image(image_path): #"imagename_resized.JPEG"

    from PIL import Image
    from PIL import ImageOps

    im = Image.open(image_path)
    im_out = ImageOps.equalize(im)
    im_out.save("base_image_resized_equalized.jpeg", "JPEG")

    return "base_image_resized_equalized.jpeg"
