from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import decode_predictions
from matplotlib import pyplot as plt
import keras
import numpy as np
# load the model VGG16
vggmodel = VGG16(weights='imagenet')
vggmodel.trainable = False  # Freeze VGG-16 for now

# Loading image
from keras.preprocessing import image
from keras.utils import load_img

# load an image from file at VGG16 input size
image = load_img('../input/animal-image-dataset-90-different-animals/animals/animals/butterfly/016caf0681.jpg',
                 target_size=(224, 224))

from keras.utils import img_to_array

# convert the image pixels to a numpy array
imgarr = img_to_array(image)

from keras.applications.vgg16 import preprocess_input

# create batch
imgbatch = np.expand_dims(imgarr, axis=0)
##imgbatch = preprocess_input(imgbatch)

imgarr = imgarr.reshape(1, 224, 224, 3)
# Predict the inputs on the model
predict_img = vggmodel.predict(imgbatch)
predict_img
# Decode the three most likly predictions mad by the model
predict = decode_predictions(predict_img)

 


# print to Image with title
plt.figure(figsize=(2, 2))
plt.imshow((imgarr[0]).astype('uint8'))
plt.title("{}dd".format(predict))
plt.axis('off')

