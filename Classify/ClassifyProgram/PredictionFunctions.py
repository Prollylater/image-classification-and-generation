def PredictWithBaseModel(pixmap):
    from keras.utils import load_img
    from keras.utils import img_to_array
    from keras.applications.vgg16 import preprocess_input
    from keras.applications.vgg16 import decode_predictions
    from keras.applications.vgg16 import VGG16
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
    return print('%s (%.2f%%)' % (label[1], label[2] * 100))

def PredictWithCustomModel(pixmap,dictionnary,model):
    from keras.applications.vgg16 import VGG16
    from keras.applications.vgg16 import decode_predictions
    import pickle
    import tensorflow as tf
    import numpy as np
    from matplotlib import pyplot as plt
    import math
    import keras
    from keras import models

    # Load model from wherever
    model = tf.keras.models.load_model('Models and dictionnary/'+ model +'.h5')

    # Show model architecture
    model.summary()

    # Load associated dictionary
    dic = open("Models and dictionnary/"+ dictionnary +".pkl", "rb")
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

    print(
        "{} most likely belongs to {} with a {:.2f} percent confidence."
        .format("Image inputted :", dictionary[np.argmax(score)], 100 * np.max(score))
    )

    # print to verify shape
    plt.figure(figsize=(2, 2))
    # plt.imshow((imgarr[0]).astype('uint8'))
    plt.imshow((image))
    plt.title("{}:{:.2f}".format(dictionary[np.argmax(score)],
                                 100 * np.max(score)))  # remplacer par label, 100 * np.max(score)))
    plt.axis('off')


