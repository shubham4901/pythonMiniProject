import re

class validation:
    @staticmethod
    def validateemail(eemail):
        e_regex = re.compile(r'[\w\.-]+@[\w\.-]+')

        if e_regex.search(eemail):
            return True
        else:
            return False
    @staticmethod
    def validatetemobile(emob):
        m_regex = re.compile(r'\d{10}')

        if m_regex.search(emob):
            return True
        else:
            return False