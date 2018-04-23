
# TODO
def get_current_user():
    return 'root'

# TODO: Thread safety
class Tokens:
    __token_map__ = {}

    def __init__(self):
        pass

    @classmethod
    def reset(cls):
        cls.__token_map__ = {}

    @classmethod
    def set_token(cls, uid, token):
        cls.__token_map__[token] = uid

    @classmethod
    def get_uid(cls, token):
        return cls.__token_map__[token]

    @classmethod
    def remove_token(cls, token):
        del cls.__token_map__[token]
