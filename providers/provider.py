class Provider:
    def __init__(self, data):
        raise NotImplementedError

    def send_message(self, message):
        raise NotImplementedError
