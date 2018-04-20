
# TODO
def get_current_user():
    return 'root'

# TODO: Thread safety
class Tokens:
    __token_map__ = {}

    def __init__(self):
        pass

    @classmethod
    def reset(self):
        self.__token_map__ = {}

    @classmethod
    def set_token(self, uid, token):
        self.__token_map__[token] = uid

    @classmethod
    def get_uid(self, token):
        return self.__token_map__[token]

    @classmethod
    def remove_token(self, token):
        del self.__token_map__[token]
