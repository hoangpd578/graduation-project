import cv2
import dlib
import base64
import os
import time
import requests
import numpy as np
from imutils.face_utils import rect_to_bb, FaceAligner
from utils import configs
from loguru import logger
from imutils.video import VideoStream


def cap_image(name, id_=None, index_device=0):
    if not id_:
        logger.error("You haven't had Employee's id.")
        raise ValueError("You haven't had Employee's id.")
    path_save = os.path.join(configs.EMPLOYEE_IMAGES, name + "_"
                             + str(id_))
    if not os.path.exists(path_save):
        os.makedirs(path_save)

    logger.info("Loading facial landmark predictior.")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(configs.DETECT_FACE_MODEL)
    fa = FaceAligner(predictor,
                     desiredFaceWidth=configs.IMAGE_SIZE)
    logger.info("Camare ready.")
    vs = VideoStream().start()
    time.sleep(2.0)

    # set some information
    num_images = 0
    fps = 0
    counter = time.time()
    start_time = time.time()
    logger.info("Collecting image.")

    while True:

        fps_time = time.time()
        frame = vs.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rects = detector(gray, 0)
        faces = np.empty((len(rects), configs.IMAGE_SIZE,
                         configs.IMAGE_SIZE, 3))

        for i, rect in enumerate(rects):
            faces = fa.align(frame, gray, rect)
            (X, Y, W, H) = rect_to_bb(rect)
            cv2.rectangle(frame, (X, Y), (X + W, Y + H),
                          (0, 255, 0), 1)
            if time.time() - counter >= 1.5 and num_images <= 25 :
                num_images += 1
                image_name = time.strftime("%H_%M_%S") + "_" + \
                                             str(num_images) + ".jpg"
                path_name = os.path.join(path_save, image_name)
                counter = time.time()
                if num_images % 5 == 0:
                    logger.info("Collecting: {}/20".format(num_images))
                cv2.imwrite(path_name, faces)

        fps = 1 / (time.time() - fps_time)
        fps_info = "Fps: {:0.4f}".format(fps)
        num_images_info = "Numbers of Image: {}".format(num_images)

        if num_images <= 25:
            cv2.putText(frame, fps_info, (10, 50), configs.FONT, 0.5,
                        (255, 0, 0), 2)
            cv2.putText(frame, num_images_info, (10, 100), configs.FONT,
                        0.5, (255, 0, 0), 2)
        else:
            cv2.putText(frame, "Fbs: {:0.4f}".format(fps), (10, 50),
                        configs.FONT, 0.5, (255, 0, 0), 2)

        cv2.imshow("Output of predict", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q") or time.time() - start_time > 40:
            break
    # Clean up
    cv2.destroyAllWindows()
    vs.stop()

    return path_save


def text2sound(name, id_):
    name = name.replace("_", " ")
    data = {
        "input": {
            "text": "Xin chào " + name
        },
        "audioConfig": {
            "audioEncoding": "MP3"
        },
        "voice": {
            # "languageCode" : "en-US"
            "languageCode": "vi-VN"
        }

    }
    logger.info("Coverting name to Audio.")
    res = requests.post(configs.API_URL, json=data)
    audio_b64 = res.json()["audioContent"]
    audio_byte = base64.b64decode(audio_b64)
    if not os.path.exists(configs.SOUND_PATH):
        os.makedirs(configs.SOUND_PATH)

    audio_name = name + "_" + id_ + ".mp3"
    path = os.path.join(configs.SOUND_PATH, audio_name)
    with open(path, mode="wb") as f:
        f.write(audio_byte)

    return
