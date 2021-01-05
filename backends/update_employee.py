from utils.cap_image_tool import cap_image, text2sound
from utils.image2vec import image2vec
from utils.train_classifier import run_classifier
from controllers.user_controller import create_user
from models.user import User
from loguru import logger
from utils import configs
import argparse
import os
import threading

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


logger.add(configs.LOGFILE)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-n", "--name", help="Enter Staff's name")
    # parser.add_argument("-i", "--id", help="Enter Staff's ID")
    # parser.add_argument("-e", "--email", default="abc@gmail.com",
    #                     help="Enter Staff's email")
    # parser.add_argument("-o", "--optionals", default=0, type=int,
    #                     help="0-Embedding with new images. 1-Embedding \
    #                          total images")
    # parser.add_argument("-m", "--menuroles", default="user",
    #                     help='''user or "user, admin"''')

    # args = vars(parser.parse_args())
    # logger.info("PROCESS - UPDATE EMPLOYEE")
    # logger.info("Collect Employee's image.")
    # path_save = cap_image(args["name"], args["id"])
    # user = User(args["name"], args["id"], args["email"], args["menuroles"])
    # # create_user(user)
    # threading.Thread(target=text2sound(args["name"], args["id"])).start()
    # threading.Thread(target=image2vec(path_save,
    #                  optionals=args["optionals"])).start()

    run_classifier()