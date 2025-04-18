import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    print(f"Loading image data from {data_dir}...")

    images = []
    labels = []

    categories = [
        category for category in os.listdir(data_dir)
    ]

    for category in categories:
        for filename in os.listdir(os.path.join(data_dir, category)):
            image = cv2.resize(
                cv2.imread(
                    os.path.join(
                        data_dir,
                        category,
                        filename
                    )
                ),
                dsize=(IMG_WIDTH, IMG_HEIGHT)
            )

            images.append(image)
            labels.append(category)

    print("Image data loaded.")

    return (images, labels) 


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    print("Compiling the convolutional neural network model...")

    model = tf.keras.models.Sequential()
    
    print("Adding first convolutional and pooling layer to model...")

    model.add(
        tf.keras.layers.Conv2D(
            filters=32,
            kernel_size=(3, 3),
            activation="relu",
            input_shape=(IMG_WIDTH, IMG_HEIGHT, 3),

        )
    )

    model.add(
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2))
    )

    print("Adding second convolutional and pooling layer to model...")

    model.add(
        tf.keras.layers.Conv2D(
            filters=64, 
            kernel_size=(3, 3), 
            activation="relu"
        )
    )

    model.add(
        tf.keras.layers.MaxPooling2D(
            pool_size=(2, 2)
        )
    )

    print("Adding third convolutional and pooling layer to model...")

    model.add(
        tf.keras.layers.Conv2D(
            filters=64, 
            kernel_size=(3, 3), 
            activation="relu")
    )

    model.add(
        tf.keras.layers.MaxPooling2D(
            pool_size=(2, 2)
        )
    )

    print("Flattening the input...")

    model.add(
        tf.keras.layers.Flatten()
    )

    print("Adding densely connected NN layer...")

    model.add(
        tf.keras.layers.Dense(
            NUM_CATEGORIES,
            activation="softmax"
        )
    )

    print("Compiling the model...")

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    print("Model compiled.")

    return model


if __name__ == "__main__":
    main()
