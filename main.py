#!/usr/bin/env python
# -*- coding: utf-8 -*-
import vk_api


def main():
    """ Пример получения последнего сообщения со стены """

    login, password = input('login:'), input('password:')
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    for get in [vk.groups.get, vk.groups.getInvites]:
        while True:
            response = get(count=500)

            try:
                groups = vk.groups.getById(group_ids=','.join((str(a) for a in response.get('items', []))))
            except:
                groups = response.get('items', [])
            if not groups:
                break
            continue_ = False
            for group in groups:
                if not group['is_admin']:
                    continue_ = True
                    vk.groups.leave(group_id=group['id'])
            if not continue_:
                break


if __name__ == '__main__':
    main()
