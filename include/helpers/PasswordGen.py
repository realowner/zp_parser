import secrets
import string
from passlib.hash import bcrypt


class PasswordGen:

    @staticmethod
    def generate_str(length=20):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(length))

        return password

    @staticmethod
    def password_hash(password):
        hashed = bcrypt.using(rounds=13, ident="2y").hash(password)

        return hashed
