from keras_vggface.vggface import VGGFace
from keras.preprocessing import image
from keras_vggface import utils
from imutils import paths
from loguru import logger
import numpy as np
import os
from utils import configs


class Img2Vec(object):

    def __init__(self):

        self.vgg_model = VGGFace(include_top=False, input_shape=(224, 224, 3),
                                 pooling="avg")
        self.vgg_model.summary()

    def get_vec(self, image_path):

        img = image.load_img(image_path, target_size=(224, 224, 3))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = utils.preprocess_input(x)
        intermediate_output = self.vgg_model.predict(x)
        return intermediate_output

    def get_vec_image(self, img):

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = utils.preprocess_input(x)
        intermediate_output = self.vgg_model.predict(x)

        return intermediate_output


def image2vec(path, optionals=0):
    embed_512 = []
    labels = []
    files = list(paths.list_images(path))

    img2vec = Img2Vec()
    logger.info("Loading images.")
    logger.info("Embedding images.png")
    count_images = 0

    if optionals == 0:
        files = list(paths.list_images(path))
    else:
        files = list(paths.list_images(configs.EMPLOYEE_IMAGES))

    for file in files:
        if count_images % 5 == 0:
            logger.info("Embedding images: {}/{} images".format(count_images,
                        len(files)))
        label = file.split("/")[-2]
        vec = img2vec.get_vec(file)
        embed_512.append(vec)
        labels.append(label)
        count_images += 1

    embed_512 = np.asarray(embed_512)
    labels = np.asarray(labels)

    if not os.path.exists(configs.X):
        np.save(configs.X, embed_512)
        np.save(configs.Y, labels)
    else:
        X = np.load(configs.X)
        Y = np.load(configs.Y)

        embed_512 = np.concatenate((X, embed_512))
        labels = np.concatenate((Y, labels))
        np.save(configs.X, embed_512)
        np.save(configs.Y, labels)
