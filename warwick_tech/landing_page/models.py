from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, 
            course, year_of_study, gender, password=None):
        """
        Creates and saves user with given fields.
        """
        if not email:
            raise ValueError("Users must have an email")

        user = self.model(
                email = self.normalize_email(email),
                first_name=first_name,
                last_name=last_name,
                course=course,
                year_of_study=year_of_study,
                gender=gender
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    
    def create_superuser(self, email, first_name, last_name,
            course, year_of_study, gender, password=None):
        """
        Creates and saves user with given fields.
        """
        if not email:
            raise ValueError("Users must have an email")

        user = self.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                course=course,
                year_of_study=year_of_study,
                gender=gender,
                password=password
        )

        user.is_admin = True
        user.save(using=self._db)

        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=30, default="")
    last_name  = models.CharField(max_length=30, default="")
    course     = models.CharField(max_length=50, default="")
    is_active  = models.BooleanField(default=True)
    is_admin   = models.BooleanField(default=False)
    year_of_study = models.IntegerField(default=1)
    
    male = 'M'
    female = 'F'
    other = 'O'
    prefer_not_to_say = 'X'
    gender_choices = (
            (male, "Male"),
            (female, "Female"),
            (other, "Other"),
            (prefer_not_to_say, "Prefer not to say")
    )
    gender = models.CharField(
            max_length=1,
            choices=gender_choices,
            default=male
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
            'first_name',
            'last_name',
            'course',
            'year_of_study',
            'gender'
    ]

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_short_name(self):
        "Return an abreviated name of the user"
        return self.first_name

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
