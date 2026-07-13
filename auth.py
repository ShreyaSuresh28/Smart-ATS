import bcrypt
from database import add_user,get_user


def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


def verify_password(password, hashed):
    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )


def signup(username, password, role):

    hashed = hash_password(password)

    return add_user(
        username,
        hashed,
        role
    )

def login(username, password):

    user = get_user(username)

    if user:

        stored_hash = user[2]

        if verify_password(
                password,
                stored_hash):

            return user

    return None