class Employee(object):

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.work_date = None
        self.check_in = None
        self.check_out = None
        self.prediction_checkin = None
        self.prediction_checkout = None
        self.created_at = None
        self.updated_at = None
        self.check_in_image = None
        self.check_out_image = None
