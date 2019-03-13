## Multi-Class Classification with Machine Learning and Deep Learning
This is a project to sharpen my knowledge in the following technologies :
- Python and Jupyter Notebooks
- Data Science librairies (Pandas and Numpy)
- Machine Learning and Deep Learning frameworks (Scikit-Learn and Keras using Tensorflow as backend)

As expected, the experiment demonstrates that Deep Learning is significantly more effective for image analysis compared to traditional Machine Learning algorithms.

This project is decomposed in 4 steps :

##### 1. Pre-process raw training images
The current product images are raw, unformatted pixel data. Before the images can be used to train a custom model, the image data needs preprocessing to create new pixel data in a normalised, clean format, so that images are comparable within the dataset.
In our case, we transform all images to a particular format: 128x128x3 pixels and ensure that the pixel range is [0,255] by applying an equalising function.
    
##### 2. Training and comparison of two mutli-class classifiers with Scikit-Learn
In this notebook, two multi-class classification algorithms are explored, in order to predict the category of outdoor gear equipment. The model training step is performed on the equalised 128x128x3 gear data from the previous step. The SVM model achieve a 80% accuracy and appears to be more effective than the Decision Tree algorithm.

##### 3. Training of a Deep Learning multi-class classifier with Keras
In this step, the goal is to try Deep Learning to conclude if the accuracy of the image classification improves, as Deep Learning and CNNs tend to perform well for complex data such as image. This model achieves an accuracy of 90% and is retained as the best model so far.

##### 4. Using the Deep Learning model to predict the category of new unseen image data
Finally, we can use the model created in the previous step and predict the class of new images. The new images will go through the same pre-processing steps before being used by our multi-class classification model.
