import numpy as np
from utils import configs


class FaceService():

    def face_distance(self, face_encodings, face_to_compare):
        if len(face_encodings) == 0:
            return np.empty((0))
        face_dist_value = np.linalg.norm(face_encodings - face_to_compare, axis=1)

        return face_dist_value

    def compare_faces(self, know_face_encodings, face_encoding_to_check,
                      tolerance=configs.face_similarity_threshold):
        true_list = list(self.face_distance(know_face_encodings,
                         face_encoding_to_check) <= tolerance)
        similar_idx = list(np.where(true_list)[0])

        return similar_idx

