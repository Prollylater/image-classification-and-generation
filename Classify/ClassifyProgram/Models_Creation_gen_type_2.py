import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import pickle
# Single quote: comment
# Double Quote: code left out but usable

import tensorflow as tf
from matplotlib import pyplot as plt
import keras
from keras import models
from keras.models import Sequential  # Not used but in case

from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, EarlyStopping
import os

# Load dataset directory, must modify directories

traindir = ''
testdir = ''
# Count how many classes lies in directory
totalDir = 0
for base, dirs, files in os.walk(traindir):
    for directories in dirs:
        totalDir += 1

print('Total Dir is = ', totalDir)

# Data augmentation and Training/Validation Data generation
traingen = ImageDataGenerator(rescale=1. / 255, horizontal_flip=True, zoom_range=0.2,
                              rotation_range=0.5)
valgen = ImageDataGenerator(rescale=1. / 255)

# if allocation of xxxxx exceeds 10% of free system memory error add in flow_from_xxxx batch_size = (number less than 32)
traindata = traingen.flow_from_directory(traindir, class_mode='categorical', target_size=(224, 224))

testdata = valgen.flow_from_directory(testdir, class_mode='categorical', target_size=(224, 224))

# get dictionary
label = traindata.class_indices

# reverse dictionary mappings
labelinv = {v: k for k, v in traindata.class_indices.items()}

# save dictionary for further use
filename = '.pkl'  # change name, must be indicative of the current model name
file = open(filename, 'wb')
pickle.dump(labelinv, file)
file.close()


# VGG16 loading and fine tuning

from keras.applications.vgg16 import VGG16

base_model = tf.keras.applications.VGG16(
    include_top=False,
    weights='imagenet'
)
##base_model.trainable = True  # Unfreeze  all layers of VGG-16 for now

##for layers in (base_model.layers)[:18]:  # Freezing of the 18 first layers of VGG-16 w
##   layers.trainable = False
base_model.trainable = False

# If too slow, can just set  base_model.trainable = False and freeze all layers
# If not precise enough and too slow, freeze all and cut all layers but the preprocess_input, base model, flatten and last dense
# layers as it is gave the best result in the shortest amount of time
# Modify the model

from keras.layers import Dense, Dropout, Flatten

inputs = tf.keras.Input(shape=(224, 224, 3))
x = tf.keras.applications.vgg16.preprocess_input(inputs)
x = base_model(x)
##x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = Flatten()(x)
##x = Dense(256, activation='relu')(x)
##x = Dropout(0.2)(x)
outputs = tf.keras.layers.Dense(totalDir, activation='softmax')(x)
model = tf.keras.Model(inputs, outputs)

model.summary()

opti = tf.keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=opti,
              loss=keras.losses.categorical_crossentropy,
              metrics=['accuracy'])

# Part may be cut if not needed, but modify or cut callback accordingly
early = tf.keras.callbacks.EarlyStopping(
    # Stop training when `val_loss` is no longer improving
    monitor="val_loss",
    # "no longer improving" being defined as "no better than 1e-2 less"
    min_delta=1e-2,
    # "no longer improving" being further defined as "for at least 2 epochs"
    patience=5,
    verbose=1,
    restore_best_weights=True)

# Part may be cut if not needed,but modify or cut callback accordingly
# Change name of model, currently vgg16_animals.h5
checkpoint = ModelCheckpoint("vgg16_animals.h5", monitor='val_loss', verbose=1, save_best_only=True,
                             save_weights_only=True, mode='auto', patience=4, period=1)
# Define callback with the two previous variable, not always necessary
callback = [checkpoint, early]
hist = model.fit(traindata, validation_data=testdata, epochs=15,
                 callbacks=callback
                 )

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title("model accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.legend(["Accuracy", "Validation Accuracy", "loss", "Validation Loss"])
plt.show()

# evaluate our model accuracy may cut it
loss, acc = model.evaluate(testdata, batch_size=32)

# Save the entire model as a SavedModel in h5 format
# Modify name to correspond to current data sets
model.save('temp.h5')
