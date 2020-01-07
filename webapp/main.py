from image_preprocessing import resize, equalize_image
from model_functions import image_to_array, run_model, label_decoder
import time
from flask import Flask, request

#Run using exe below
######################################
##  .\tensorflow\python.exe main.py ##
######################################

#IMAGE PREPROCESSING
#img_URL = "https://i1.adis.ws/i/jpl/bl_285379_a?w=861&h=861" #insulated jacket
#img_URL = "https://www.urbanrider.co.uk/media/catalog/product/cache/1/thumbnail/9df78eab33525d08d6e5fb8d27136e95/s/t/stylmartin-legend-r-boots---brown.jpg" #Boots
#img_URL = "https://www.donnawilson.com/wp-content/uploads/Gloves-Bunny-Gloves-Grey.jpg" #Gloves
#img_URL = "https://saferight-startdigital.netdna-ssl.com/wp-content/uploads/2017/01/rope.jpg" #Rope
#img_URL = "https://www.decathlon.co.uk/media/832/8322006/big_9568ef11b29f4158b1153604562c400f.jpg" #Tent
#img_URL = "https://www.camp-usa.com/outdoor/wp-content/uploads/2016/08/carabiners-2467-PHOTON-STRAIGHT-GATE-17.jpg" #Carabiner
#img_URL = "https://www.cyclechic.co.uk/sites/default/files/imagecache/mouseover_zoom/images/products/2998-9109.jpg" #helmet
#img_URL = "https://www.bfgcdn.com/1500_1500_90/303-0171-0311/mammut-ophir-4-slide-harness.jpg" #Harness
img_URL = "https://s7d2.scene7.com/is/image/academy/10608443?wid=1200"

app = Flask(__name__)

@app.route('/predict', methods=["GET","POST"])
def main_route():
    if request.method == "GET":
        return "That's a GET request!"
    
    if request.method == "POST":

        start_time = time.time()

        #img_URL = request.data['img_URL']

        #Get parameters from POST request
        img_URL = request.form["img_URL"]

        #IMAGE PREPROCESSING
        resized_image_name = resize(img_URL)
        print(resized_image_name)
        equalized_image_path = equalize_image(resized_image_name)
        print(equalized_image_path)

        #IMAGE TO NUMPY ARRAY
        numpy_data = image_to_array(equalized_image_path)
        numpy_data = numpy_data.reshape(1, 3, 128, 128)

        #PREDICT
        result_array = run_model(numpy_data)
        result_label = label_decoder(result_array)
        print(result_label)

        execution_time = round(time.time() - start_time, 2)
        
        return("Result: {} (elapsed time: {})".format(result_label, execution_time))


if __name__ == '__main__':
  app.run(debug=True)