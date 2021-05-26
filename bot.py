from instadm import instaDM
if __name__ == '__main__':
        insta = InstaDM(username='your_username', password='your_password', headless=False)
        insta.send.Message(user='username_target', message='hi')
        insta.sendGroupMessage(users=['user1', 'user2'] message='hi')
