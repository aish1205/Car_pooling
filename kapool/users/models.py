from django.db import models

# users/models.py
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

GENDER_OPTIONS = (
    ('female', 'Female'),
    ('male', 'Male'),
    ('wont-say', "Won't say"),
)

class User(AbstractUser):
    """
    Custom user model to replace the one provided by django
    """
    gender = models.CharField(
        null=True,
        blank=True,
        max_length=30,
        choices=GENDER_OPTIONS,
        default='wont-say',
        verbose_name=_('Gender'),
        help_text=_("User's gender")
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Date of birth'),
        help_text=_('Date of birth')
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def save(self, *args, **kwargs):
        if self.birth_date:
            # check if date is in future
            if self.birth_date > date.today():
                raise ValidationError(
                    'Birth date cannot be in the future'
                )
            # check if user is 18 or older
            age = relativedelta(date.today(), self.birth_date).years
            if age < 18:
                raise ValidationError(
                    'User should be 18 years or older'
                )
        super(User, self).save(*args, **kwargs)







