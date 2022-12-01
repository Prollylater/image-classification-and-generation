from keras.utils import load_img
from keras.utils import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

import pickle
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt

from PySide2 import QtCore

def PredictWithBaseModel(pixmap):
    # load the model
    model = VGG16()
    # load an image from file
    image = load_img(pixmap, target_size=(224, 224))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare the image for the VGG model
    image = preprocess_input(image)
    # predict the probability across all output classes
    yhat = model.predict(image)
    # convert the probabilities to class labels
    label = decode_predictions(yhat)
    # retrieve the most likely result, e.g. the highest probability
    label = label[0][0]
    # print the classification
    global result
    result = str(label[1])
    global confidence
    confidence = str(round(label[2]*100, 2))#Round to make the decimal to 2 max
    return 'The picture most likely belongs to ' + result + '\n with a ' + confidence + ' % of confidence'

def PredictWithCustomModel(pixmap,dictionnary,model):
    # Load model from wherever
    model = tf.keras.models.load_model("Classify/ClassifyProgram/Models and dictionnary/"+ model +".h5")

    # Show model architecture
    model.summary()

    # Load associated dictionary
    dic = open("Classify/ClassifyProgram/Models and dictionnary/"+ dictionnary +".pkl", "rb")
    dictionary = pickle.load(dic)

    # Loading image
    from keras.preprocessing import image
    from keras.utils import load_img

    # load an image from file at VGG16 input size
    image = load_img(pixmap,
                     target_size=(224, 224))

    from keras.utils import img_to_array

    # convert the image pixels to a numpy array
    imgarr = img_to_array(image)

    from keras.applications.vgg16 import preprocess_input

    # create batch
    imgbatch = np.expand_dims(imgarr, axis=0)

    # imgarr = imgarr.reshape(1, 224, 224, 3)
    # predict the probability across all output classes
    prediction = model.predict(imgbatch)

    # Join classifaction score
    score = tf.nn.softmax(prediction[0])

    global resultCustom
    resultCustom = str(dictionary[np.argmax(score)])
    global confidenceCustom
    confidenceCustom = str(round(100*100 * np.max(score),2))  # Round to make the decimal to 2 max
    return 'The picture most likely belongs to ' + resultCustom + '\n with a ' + confidenceCustom + ' % of confidence'

    #print(
        #"{} most likely belongs to {} with a {:.2f} percent confidence."
       # .format("Image inputted :", , )
   # )

    # print to verify shape
    #plt.figure(figsize=(2, 2))
    # plt.imshow((imgarr[0]).astype('uint8'))
    #plt.imshow((image))
    #plt.title("{}:{:.2f}".format(dictionary[np.argmax(score)],
                                 #100 * np.max(score)))  # remplacer par label, 100 * np.max(score)))
    #plt.axis('off')


def OtherPredictionWithVGG16(pixmap):
    # load the model VGG16
    vggmodel = VGG16(weights='imagenet')
    vggmodel.trainable = False  # Freeze VGG-16 for now

    # Loading image
    from keras.preprocessing import image
    from keras.utils import load_img

    # load an image from file at VGG16 input size
    image = load_img(pixmap,
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


def PredictWithSecondCustomModel(pixmap,dictionnary,model):
    # Load model from wherever
    model = tf.keras.models.load_model("Classify/ClassifyProgram/Models and dictionnary/"+ model +".h5")

    # Show model architecture
    model.summary()

    # Load associated dictionary
    dic = open("Classify/ClassifyProgram/Models and dictionnary/"+ dictionnary +".pkl", "rb")
    dictionary = pickle.load(dic)

    # Loading image
    from keras.preprocessing import image
    from keras.utils import load_img

    # load an image from file at VGG16 input size
    image = load_img(pixmap,
                     target_size=(224, 224))

    from keras.utils import img_to_array

    # convert the image pixels to a numpy array
    imgarr = img_to_array(image)

    from keras.applications.vgg16 import preprocess_input

    # create batch
    imgbatch = np.expand_dims(imgarr, axis=0)

    # imgarr = imgarr.reshape(1, 224, 224, 3)
    # predict the probability across all output classes
    prediction = model.predict(imgbatch)

    # Join classifaction score
    score = tf.nn.softmax(prediction[0])

    global resultCustom
    resultCustom = str(dictionary[np.argmax(score)])
    global confidenceCustom
    confidenceCustom = str(round(100 * np.max(score),2))  # Round to make the decimal to 2 max
    return 'The picture most likely belongs to ' + resultCustom + '\n with a ' + confidenceCustom + ' % of confidence'


def PredictWith10CustomModel(pixmap, dictionnary, model):
    # Load model from wherever
    model = tf.keras.models.load_model("Classify/ClassifyProgram/Models and dictionnary/" + model + ".h5")

    # Show model architecture
    model.summary()

    # Load associated dictionary
    dic = open("Classify/ClassifyProgram/Models and dictionnary/" + dictionnary + ".pkl", "rb")
    dictionary = pickle.load(dic)

    # Loading image
    from keras.preprocessing import image
    from keras.utils import load_img

    # load an image from file at VGG16 input size
    image = load_img(pixmap,
                     target_size=(224, 224))

    from keras.utils import img_to_array

    # convert the image pixels to a numpy array
    imgarr = img_to_array(image)

    from keras.applications.vgg16 import preprocess_input

    # create batch
    imgbatch = np.expand_dims(imgarr, axis=0)

    # imgarr = imgarr.reshape(1, 224, 224, 3)
    # predict the probability across all output classes
    prediction = model.predict(imgbatch)

    # Join classifaction score
    score = tf.nn.softmax(prediction[0])

    global resultCustom
    resultCustom = str(dictionary[np.argmax(score)])
    global confidenceCustom
    confidenceCustom = str(round(10* 100 * np.max(score), 2))  # Round to make the decimal to 2 max
    return 'The picture most likely belongs to ' + resultCustom + '\n with a ' + confidenceCustom + ' % of confidence'
