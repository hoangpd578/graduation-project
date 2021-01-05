from utils import configs


class User(object):

    def __init__(self, name, id, email, menuroles="user"):
        self.id = id
        self.name = name
        self.email = email
        self.email_verified_at = "2020-12-16 16:08:24"
        self.password = configs.PASSWORD
        self.menuroles = menuroles
        self.remember_token = None
        self.created_at = None
        self.updated_at = None
        self.deleted_at = None
