# TODO
def get_current_user():
    return 'root'


# TODO: Thread safety
class Tokens(object):
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


class Error(object):
    __error_dict__ = {
        0: 'No error',
        1: 'Token invalid',
        2: 'Username or password incorrect',
        3: 'Invalid path',
    }

    UNKNOWN_ERROR = -1
    NO_ERROR = 0
    TOKEN_INVALID = 1
    USERNAME_OR_PASSWORD_INCORRECT = 2
    INVALID_PATH = 3

    def get_error_message(self, code):
        ret = 'Unknown error'
        if code in self.__error_dict__:
            ret = self.__error_dict__[code]
        return ret
