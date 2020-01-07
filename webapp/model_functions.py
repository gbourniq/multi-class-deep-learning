def image_to_array(image_path):

    import numpy as np
    from PIL import Image

    im = Image.open(image_path)
    im_array = np.array(im, dtype=float)
    return im_array


def run_model(data):

    from keras.models import model_from_yaml

    # load YAML and create model
    yaml_file = open('model.yaml', 'r')
    loaded_model_yaml = yaml_file.read()
    yaml_file.close()
    loaded_model = model_from_yaml(loaded_model_yaml)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    results = loaded_model.predict(data).tolist()[0][1:]
    
    return results

def label_decoder(result_array):
    index = result_array.index(max(result_array)) + 1
    if index == 1:
        return "axes"
    elif index == 2:
        return "boots" 
    elif index == 3:
        return "carabiners"
    elif index == 4:
        return "crampons"
    elif index == 5:
        return "gloves"
    elif index == 6:
        return "hardshell_jackets"
    elif index == 7:
        return "harnesses"
    elif index == 8:
        return "helmets"
    elif index == 9:
        return "insulated_jackets"
    elif index == 10:
        return "pulleys"
    elif index == 11:
        return "rope"
    elif index == 12:
        return "tents"
    else:
        return "Error"