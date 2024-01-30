from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number,email, password = None, **extra_fields):
        if not phone_number:
            raise ValueError('we need your phone number ')
        if not email:
            raise ValueError('we need your email ')
        user = self.model(phone_number=phone_number,email = email, **extra_fields)
        
        user.set_password(password)
        user.save(using = self.db)
        return user 
    def create_superuser(self, phone_number, email, password = None,**extra_fields):
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_superuser' , True)
        extra_fields.setdefault('is_active' , True)

        return self.create_user(phone_number,email, password,**extra_fields)
