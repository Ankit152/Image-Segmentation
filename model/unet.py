import tensorflow as tf
from tensorflow import keras


def unet(shape):
    img = Input(shape=shape)
    return model


if __name__=="__main__":
    model = unet()
    print(model.summary())