import provider

import requests


class MobileFreeFr(provider.Provider):
    def __init__(self, cfg):
        self.user = cfg['user']
        self.token = cfg['token']

    def send_message(self, message):
        params = {'user': self.user,
                  'pass': self.token,
                  'msg': message}
        response = requests.get("https://smsapi.free-mobile.fr/sendmsg", params=params, verify=False)
        return response
