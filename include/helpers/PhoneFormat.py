import re


class PhoneFormat:

    def __init__(self, phone=None, tpl=None):
        self.clear_phone = ''
        self.phone = phone
        self.tpl = tpl
        self.parse(phone)
        self.format_phone()

    def parse(self, phone):
        if phone:
            self.clear_phone = re.sub('[^0-9]+', '', phone)

    def format_phone(self):
        if self.tpl:
            tpl = self.tpl
            for num in self.clear_phone:
                self.phone = tpl.replace('$', num, 1)
                tpl = self.phone

    def set_tpl(self, tpl):
        self.tpl = tpl

    def set_phone(self, phone):
        self.phone = phone
        self.parse(phone)
