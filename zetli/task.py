class Task:
    def __init__(self, new_id, message):
        self.id = new_id
        self.message = message

    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message
        }