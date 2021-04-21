from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


class AsciiPasswordValidator:
    def validate(self, password, user=None):
        # print(f'MyValidPass my {password}')
        res_re = re.search(r'[а-яA-Z]', password)
        if (res_re != None):
            raise ValidationError(
                _('Пароль не соотвецтвует заданным параметрам'),
                code='password_not_Ascii'
            )

    def get_help_text(self):
        return _(
            "Пароль на латинском"
        )
