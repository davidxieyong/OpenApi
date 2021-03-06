# -*- coding: utf-8 -*-

from examples.python3.dragonex import DragonExV1

ACCESS_KEY = 'ThisIsAccessKey'
SECRET_KEY = 'ThisIsSecretKey'

HOST = 'https://openapi.dragonex.im'

if __name__ == '__main__':
    dragonex = DragonExV1(access_key=ACCESS_KEY, secret_key=SECRET_KEY, host=HOST)
    dragonex.ensure_token_enable(False)
    r = dragonex.get_user_own_coins()
    print(r.data)
