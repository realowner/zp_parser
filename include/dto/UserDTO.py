from include.helpers.PasswordGen import PasswordGen as pw
import time


class UserDTO:
    def __init__(self, user):
        dt: int = int(round(time.time()))
        self.comp_id = user['id']
        self.email = user['email']
        self.title = user['title']
        self.website = user['external_url']
        self.username = user['email']
        self.description = user['description']
        self.password_hash = pw.password_hash(pw.generate_str())
        self.auth_key = pw.generate_str(32)
        self.confirmed_at = dt
        self.created_at = dt
        self.updated_at = dt

        self.firstname = ''
        self.lastname = ''
        if any([item for item in user.get('contacts', [])]):
            self.firstname = user['contacts'][0].get('firstname', '')
            self.lastname = user['contacts'][0].get('lastname', '')
            phones = user['contacts'][0].get('phones', [])
            if any([item for item in phones]):
                self.phone = phones[0].get('phone', None)

        self.logo = ''
        try:
            if any([item for item in user.get('logo', [])]):
                self.logo = user['logo'].get('url')
        except:
            self.logo = None

        self.activity_field = ''
        if any([item for item in user.get('rubrics', [])]):
            for rubric in user.get('rubrics'):
                self.activity_field = self.activity_field + rubric.get('title', '') + ' '

        self.user_id = user['id']
        self.vk = None
        self.facebook = None
        self.instagram = None
        self.skype = None
        self.status = None
        self.is_trusted = None
        self.valance = None
        self.valance_renew_count = None
        self.create_vacancy = None
