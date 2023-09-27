def save_user(**user):
    print(user['name'])
    print(user.get('idf', 1))


save_user(name = "Mohamed",age = 20)