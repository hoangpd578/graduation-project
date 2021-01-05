import cv2


# config frame
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.5
IMAGE_SIZE = 224
FRAME_WIDTH, FRAME_HEIGHT = 2500, 2500


# config function text2sound
API_KEY = "AIzaSyAN8LcZhriwuNa94u4L4ZE4NJbVglUm5uM"
API_URL = "https://texttospeech.googleapis.com/v1/text:synthesize?key={}".format(API_KEY)

# image2vec
EMPLOYEE_IMAGES = "data/employee_images"
X = "data/data_vec/X.npy"
Y = "data/data_vec/Y.npy"

#
MODEL_PATH = "models"
MODEL_CLASSIFY_WEIGHT_PATH = "data/models/classifiers/best_weights.h5"
MODEL_CLASSIFY_PATH = "data/models/classifiers/model.json"
VECTOR_SHAPE = 512
DETECT_FACE_MODEL = "data/models/detections/shape_predictor_68_face_landmarks.dat"
# DETECT_FACE_MODEL = "data/models/detections/shape_predictor_5_face_landmarks.dat"

#
NAMES = "models/name.pkl"

#
face_similarity_threshold = 0.1

# sound
SOUND_PATH = "data/sounds/"
FAILED_CHECKIN = "data/sounds/no_name.mp3"

# logs
LOGFILE = "logs/logs.txt"
LOGS_HISTORY = "public/assets/img/history_checkin/"
LOGS_PATH_TO_DB = "./public/assets/img/history_checkin/"

# LOGS_HISTORY = "/home/dang-hoang/history_checkin"
INFOFILE = "logs/info.txt"

#
PASSWORD = "$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi"
