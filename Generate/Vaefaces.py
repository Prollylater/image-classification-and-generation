import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.layers import Layer, Input, Conv2D, Dense, Flatten, Reshape, Lambda, Dropout
from tensorflow.keras.layers import Conv2DTranspose, MaxPooling2D, UpSampling2D, LeakyReLU, BatchNormalization
from tensorflow.keras.activations import relu
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
tf.compat.v1.disable_eager_execution()

#Define sampling layer,
class Sampling(Layer):
    def call(self, inputs):
        #get output of variances and means layers, reparametrage
        means, logvar = inputs
        batch = tf.shape(means)[0]
        dim = tf.shape(means)[1]
        epsilon = tf.random.normal(shape=(batch, dim))
        samples = means + tf.exp(0.5*logvar)*epsilon
        return samples



def Vaecreate():
   laten_dim = 256
   Imgshape= (128,128,3)
##Building the encoder part
#Functional creation to accomadate the multi output need
 
   inpuenc = Input(shape=Imgshape)
   modelenc = Conv2D(filters=32,kernel_size=3,strides = 2 ,padding="same")(inpuenc)
   modelenc = BatchNormalization()(modelenc)
   modelenc = LeakyReLU(alpha =0.2)(modelenc)
   modelenc = Conv2D(filters=64,kernel_size=3,strides = 2 ,padding="same")(modelenc)
   modelenc = BatchNormalization()(modelenc)
   modelenc = LeakyReLU(alpha =0.2)(modelenc)
   modelenc = Conv2D(filters=128,kernel_size=3,strides = 2,padding="same")(modelenc)
   modelenc = BatchNormalization()(modelenc)
   modelenc = LeakyReLU(alpha =0.2)(modelenc)
   modelenc = Conv2D(filters=256,kernel_size=3,strides = 2,padding="same")(modelenc)
   modelenc = BatchNormalization()(modelenc)
   modelenc = LeakyReLU(alpha =0.2)(modelenc)

   modelenc = Flatten()(modelenc)
   modelenc = Dense(256)(modelenc)
   modelenc = LeakyReLU(alpha =0.3)(modelenc)

#dividing the layer and senging layrny variable
   means = Dense(laten_dim)(modelenc)
   logvar = Dense(laten_dim)(modelenc)
   latents = Sampling()([means, logvar])

   encoder = Model(inputs=inpuenc, outputs=[means, logvar,latents]) #encoder is returned

#encoder.summary()


#Building the decoder part keept out of the function

   inpudec = Input(shape=(laten_dim,), )
   modeldec = Dense(4 * 4 * 64, activation='relu')(inpudec)

   modeldec = Reshape((4, 4, 64))(modeldec)  # idk, idk at amm
   modeldec = Conv2DTranspose(filters=256, kernel_size=3, strides=2, padding="same")(modeldec)
   modeldec = BatchNormalization()(modeldec)
   modeldec = LeakyReLU(alpha=0.3)(modeldec)
   modeldec = Conv2DTranspose(filters=128, kernel_size=3, strides=2, padding="same")(modeldec)
   modeldec = BatchNormalization()(modeldec)
   modeldec = LeakyReLU(alpha=0.3)(modeldec)
   modeldec = Conv2DTranspose(filters=64, kernel_size=3, strides=2, padding="same")(modeldec)
   modeldec = BatchNormalization()(modeldec)
   modeldec = LeakyReLU(alpha=0.3)(modeldec)
   modeldec = Conv2DTranspose(filters=32, kernel_size=3, strides=2, padding="same")(modeldec)
   modeldec = BatchNormalization()(modeldec)
   modeldec = LeakyReLU(alpha=0.3)(modeldec)

   modeldec = Conv2DTranspose(filters=3, kernel_size=(3, 3), strides=2, padding='same', activation='sigmoid')(modeldec)
   decoder = Model(inputs=inpudec, outputs=modeldec)  # encoder is returned

 # COMBINE ENCODER AND DECODER THE COMPLETE THE VARIATIONAL AUTO ENCODER
   reconstructions = decoder(latents)

   vae = Model([inpuenc], outputs=[reconstructions])

   return vae

vae = Vaecreate()
vae.summary()

#Defining loss function relative to the task
def vae_kl_loss(y_true, y_pred):
    kl_loss =- 0.5 * tf.reduce_mean(1 + logvar - tf.square(means) - tf.exp(logvar))
    return kl_loss

#reconstruction loss
def vae_rc_loss(y_true, y_pred):
    #rc_loss = tf.keras.losses.binary_crossentropy(y_true, y_pred)
    rc_loss = tf.keras.losses.MSE(y_true, y_pred)
    return rc_loss

#total loss
def vae_loss(y_true, y_pred):
    kl_loss = vae_kl_loss(y_true, y_pred)
    rc_loss = vae_rc_loss(y_true, y_pred)
    kl_weight_const = 0.02
    return kl_weight_const*kl_loss + rc_loss


##############"LOADING THE WEIGHT Of the trained model
model_path = "/Generate/vae128.h5"
vae.load_weights(model_path)

"""""
#A new dolder should be created
def Reconstruct(tempfolderpath) :
#Image data only take a folder path and prove itself to be the best method to reconstruct i could prepare for now
   test2_datagen = ImageDataGenerator(rescale=1./255)
   test2_generator = test2_datagen.flow_from_directory(tempfolderpath, target_size=(128, 128), batch_size=10, class_mode=None)

   sample_img = next(test2_generator)

   z_points = encoder.predict(sample_img)
# reconstructed images
   reconst_images = decoder.predict(z_points)
   return reconst_images
"""""

def Gen() :
########################GENERATE FROM PREXISTING NOISE
   z_dim = 256
   z_samples = tf.random.normal(shape=(20, z_dim))
#Newly generated images is stored there
   images = decoder.predict(z_samples, steps = 2)
   return images
