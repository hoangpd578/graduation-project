from tensorflow.keras.models import model_from_json
from imutils.face_utils import FaceAligner, rect_to_bb
from imutils.video import VideoStream
from models.employee import Employee
from controllers.employee_controller import create_employee, update_database
from controllers.employee_controller import check_employee
from utils import configs
from keras_vggface.vggface import VGGFace
from keras.preprocessing.image import img_to_array
from playsound import playsound
from keras_vggface.utils import preprocess_input
from threading import Thread
from loguru import logger
import os
import time
import cv2
import dlib
import numpy as np
import pickle

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

logger.add(configs.LOGFILE)


def run_camera(index_device=0):
    
    logger.info("Create log.")
    _time = time.strftime("%Y-%m-%d")
    path = os.path.join(configs.LOGS_HISTORY, _time)
    if not os.path.exists(path):
        os.mkdir(path)

    logger.info("Loading name.")
    names = pickle.load(open(configs.NAMES, "rb"))

    logger.info("Loading model.")
    with open(configs.MODEL_CLASSIFY_PATH, "r") as json_file:
        network = model_from_json(json_file.read())
        json_file.close()
    network.load_weights(configs.MODEL_CLASSIFY_WEIGHT_PATH)

    logger.info("Loading facial landmark preditor.")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(configs.DETECT_FACE_MODEL)
    fa = FaceAligner(predictor, desiredFaceWidth=configs.IMAGE_SIZE)

    logger.info("Ready camera.")
    vs = VideoStream().start()
    time.sleep(2.0)

    fps = 0
    wait_time = time.time()
    time_label = 0
    label = None
    employees = {}

    logger.info("Load model embedding.")
    emb_model = VGGFace(include_top=False, input_shape=(224, 224, 3),
                        pooling="avg")
    emb_model.summary()

    while True:
        frame = vs.read()
        start_time = time.time()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rects = detector(gray, 0)
        faces = np.empty((len(rects), configs.IMAGE_SIZE,
                         configs.IMAGE_SIZE, 3))

        for i, rect in enumerate(rects):
            faces = fa.align(frame, gray, rect)
            (X, Y, W, H) = rect_to_bb(rect)
            cv2.rectangle(frame, (X, Y), (X + W, Y + H),
                          (0, 255, 0), 1)
            cv2.putText(frame, "PHAN DANG HOANG - 95.47",  (X, Y), configs.FONT,
                            configs.FONT_SCALE, (255, 204, 102))
            if time.time() - time_label <= 1:
                cv2.putText(frame, label,  (X, Y), configs.FONT,
                            configs.FONT_SCALE, (255, 204, 102))
            else:
                label = None
            if time.time() - wait_time >= 3:
                wait_time = time.time()
                x = img_to_array(faces)
                x = np.expand_dims(x, axis=0)
                x = preprocess_input(x)
                emb_vector = emb_model.predict(x)

                result = network.predict(emb_vector)
                _id = np.argmax(result[0])
                probability = result[0][_id]
                percent = round(round(probability, 4) * 100, 2)

                if percent > 65:
                    idx_ = names[_id].rfind("_")
                    name_staff = names[_id][:idx_]
                    employee_id = names[_id][idx_ + 1:]
                    label = name_staff + "-{}".format(percent)
                    time_label = time.time()

                    # store check_in image
                    image_name = time.strftime("%H-%M-%S") +\
                                                "_" + name_staff + ".jpg"
                    path_image = os.path.join(path, employee_id, image_name)
                    path_image_to_db = os.path.join(
                         configs.LOGS_PATH_TO_DB, _time, employee_id, image_name)
                    if not os.path.exists(os.path.join(path, employee_id)):
                        os.mkdir(os.path.join(path, employee_id))
                    # Check in list

                    if idx_ not in employees.keys():
                    
                        epl = Employee(employee_id, name_staff.replace("_", " "))
                        # epl = Employee(10, name_staff.replace("_", " "))
                        employees[idx_] = epl
                        epl.check_in = time.strftime("%H:%M:%S")
                        epl.check_out = time.strftime("%H:%M:%S")
                        epl.work_date = time.strftime("%y-%m-%d")
                        epl.prediction_checkin = float(percent)
                        epl.prediction_checkout = float(percent)
                        epl.created_at = time.strftime("%Y-%m-%d %H:%M:%S")
                        epl.updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
                        epl.check_in_image = path_image_to_db
                        epl.check_out_image = path_image_to_db
                        
                        logger.info("Successful check in.")
                        # sound_path = os.path.join(configs.SOUND_PATH,
                        #                           names[_id] + ".mp3")
                        # threading.Thread(
                        #     target=playsound(sound_path)
                        #     ).start()
                        logger.info("Insert information of check in to DB.")
                        #if not check_employee(epl):
                            #create_employee(epl)
                        cv2.imwrite(path_image, faces)

                    else:
                        employees[idx_].check_out = time.strftime("%H:%M:%S")
                        employees[idx_].prediction_checkout = float(percent)
                        employees[idx_].updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
                        epl.check_out_image = path_image_to_db
                        cv2.imwrite(path_image, faces)
                        logger.info("Update information of check out to DB")
                        # update_database(employees[idx_])
                        cv2.imwrite(path_image, faces)

                # else:
                #     threading.Thread(
                #             target=playsound(configs.FAILED_CHECKIN)
                #             ).start()

        end_time = time.time()
        fps = round(1 / (end_time - start_time), 2) 
        cv2.putText(frame, "Fps:" + str(fps), (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        cv2.imshow("Face ID", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()
    vs.stop()


if __name__ == "__main__":
    run_camera()
