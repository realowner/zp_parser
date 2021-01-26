from transliterate import translit, get_available_language_codes

class EmailGenerator:
    
    @staticmethod
    def email_generator(text):
        
        trans = text.maketrans(
            {
                ord('/'):'', 
                ord('\\'):'', 
                ord(':'):'', 
                ord(';'):'', 
                ord('.'):'', 
                ord(' '):'', 
                ord('!'):'', 
                ord('?'):'', 
                ord('"'):'', 
                ord('|'):'', 
                ord('<'):'', 
                ord('>'):'', 
                ord('*'):'',
                ord('\''):'',
                ord(','):'', 
            }
        )
        only_text = text.translate(trans)
        low_text = only_text.lower()
        tr_low_text = translit(low_text, 'ru', reversed=True)
        email_gen = tr_low_text + '@rabota.today'

        return email_gen