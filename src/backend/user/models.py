import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.validators import ASCIIUsernameValidator, UnicodeUsernameValidator
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    """カスタムユーザマネージャ"""
    use_in_migrations = True
    
    def _create_user(self, username, email, date_of_birth, password, **extra_fields):
        if not email:
            raise ValueError('Emailを入力してください')
        if not username:
            raise ValueError('ユーザー名を入力してください')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault()
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username=username, email=email, date_of_birth=date_of_birth, password=password, **extra_fields)
    
    def create_superuser(self, username, email, date_of_birth, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff=Trueである必要があります。')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser=Trueである必要があります。')
        return self._create_user(username=username, email=email, date_of_birth=date_of_birth, password=password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル"""
    # Validation
    username_validator = ASCIIUsernameValidator()
    nickname_validator = UnicodeUsernameValidator()

    # Properties
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_('username'), max_length=50, validators=[username_validator], unique=True)
    nickname = models.CharField(_('nickname'), max_length=30, validators=[nickname_validator], blank=True)
    email = models.EmailField(_('email_address'), unique=True, blank=True, null=True)
    date_of_birth = models.DateField(_('date_of_birth'), blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date_joined'), default=timezone.now)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'date_of_birth']
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        
    def email_user(self, subject, message, from_email=None, **kwargs):
        """メール送信"""
        send_mail(subject, message, from_email, [self.email], **kwargs)


def profileThumbnail_directory_path(instance, filename):
    """サムネイル画像名をUUIDに変更して保存"""
    return 'thumbnails/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])

def profileBackground_directory_path(instance, filename):
    """背景画像名をUUIDに変更して保存"""
    return 'backgrounds/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])

class Profile(models.Model):
    """プロフィール"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # ユーザー情報
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    # Images
    thumbnail = models.ImageField(_('thumbnail'), upload_to=profileThumbnail_directory_path, null=True, blank=True)
    background = models.ImageField(_('background'), upload_to=profileBackground_directory_path, null=True, blank=True)
    
    def __str__(self):
        return self.user.get_username()
    
