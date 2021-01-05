import os
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from keras.utils.np_utils import to_categorical
from tensorflow.keras import optimizers, models, layers
import pickle
from loguru import logger
import numpy as np
from utils import configs


def classification_model(classes_num, input_dim):
    model = models.Sequential()
    model.add(layers.Dense(512, activation="relu",
                           input_dim=input_dim))
    model.add(layers.Dense(256, activation="relu"))
    model.add(layers.Dense(classes_num, activation="softmax"))

    return model


def run_classifier():
    X = np.load(configs.X)
    y = np.load(configs.Y)
    X = np.reshape(X, (len(X), configs.VECTOR_SHAPE))
    encoder = preprocessing.LabelEncoder()
    y = encoder.fit_transform(y)

    pickle.dump(encoder.classes_, open(configs.NAMES, "wb"))
    weights_path = configs.MODEL_CLASSIFY_WEIGHT_PATH
    y = to_categorical(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                        random_state=42)
    early_stopping = EarlyStopping(monitor="val_accuracy", patience=10,
                                   verbose=1, mode="max")
    save_checkpoint = ModelCheckpoint(weights_path, monitor="val_accuracy",
                                      verbose=1, save_weights_only=True,
                                      save_best_only=True, mode="max")
    reduce_lr = ReduceLROnPlateau(monitor="val_loss", factor=0.2, patience=5,
                                  min_lr=0.001)
    callbacks = [save_checkpoint, early_stopping, reduce_lr]
    logger.info("Classifying.")
    net = classification_model(len(encoder.classes_), configs.VECTOR_SHAPE)
    net.compile(loss="categorical_crossentropy",
                optimizer=optimizers.Adam(lr=1e-4),
                metrics=["accuracy"])
    net.fit(X_train, y_train, epochs=1000, validation_data=(X_test, y_test),
            callbacks=callbacks)

    json_model = net.to_json()
    path_save_json_model = os.path.join(configs.MODEL_CLASSIFY_PATH)
    with open(path_save_json_model, "w") as f:
        f.write(json_model)
