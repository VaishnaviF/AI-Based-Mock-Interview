import numpy as np
import cv2
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.optimizers import Adam
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array,load_img
#from tensorflow.keras.utils import img_to_array,
import os 

def build_cnnmodel():
        #Initialize the training and validation generators
        train_dir = 'dataset\\train'
        val_dir = 'dataset\\test'
        train_datagen = ImageDataGenerator(rescale=1./255)
        val_datagen = ImageDataGenerator(rescale=1./255)
        train_generator = train_datagen.flow_from_directory(
                train_dir,
                target_size=(64,64),
                batch_size=64,
                class_mode='categorical')
        validation_generator = val_datagen.flow_from_directory(
                val_dir,
                target_size=(64,64),
                batch_size=64,
                class_mode='categorical')

        #Build the convolution network architecture:
        emotion_model = Sequential()
        emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(64,64,3)))
        emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
        emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
        emotion_model.add(Dropout(0.25))
        emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
        emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
        emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
        emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
        emotion_model.add(Dropout(0.25))
        emotion_model.add(Flatten())
        emotion_model.add(Dense(1024, activation='relu'))
        emotion_model.add(Dropout(0.5))
        emotion_model.add(Dense(7, activation='softmax'))

        #ompile and train the model:
        emotion_model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=0.0001, decay=1e-6),metrics=['accuracy'])
        emotion_model.fit_generator(train_generator,
                steps_per_epoch=50,
                epochs=25,
                validation_data=validation_generator,
                validation_steps=7178 // 64)

        # save model
        if os.path.exists("models\\cnn_model.hdf5"):
                pass

        else:
                emotion_model.save("models\\cnn_model.hdf5")

#build_cnnmodel()

