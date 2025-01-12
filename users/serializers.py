from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

# ----------------------------------
# UserSerializer -> Full Control for permissions.IsAdminUser
# ----------------------------------
class UserSerializers(serializers.ModelSerializer):

    password = serializers.CharField(
        required = False,
        write_only = True,
    )
    
    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
        )

    class Meta:
        model = User
        # exclude = []
        fields = (
            "id",
            "password",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            # "is_superuser",
            # "is_active",
            # "last_login",
            # "date_joined",
            # "groups",
            # "user_permissions",
        )
    
    #! password'ü şifreleme:
    def validate(self, attrs):
        if attrs.get('password', False):
            from django.contrib.auth.password_validation import validate_password # doğrulama fonksiyonu
            from django.contrib.auth.hashers import make_password # şifreleme fonksiyonu
            password = attrs["password"] # Password al.
            validate_password(password) # Validation'dan geçir.
            attrs.update(
                {
                    "password": make_password(password) # Password şifrele ve güncelle.
                }
            )
        return super().validate(attrs) # Orjinal methodu çalıştır.



# ----------------------------------
# UserCreateSerializer -> Only CreateUser for permissions.AllowAny
# ----------------------------------
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {"input_type" : "password"}
    )
    
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {"input_type" : "password"}
    )
    
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        'password2'
        ]
        # extra_kwargs ={
        #     "password" : {"write_only" : True},
        #     "password2" : {"write_only" : True},
        # }

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"message" : "Password fields didn't match!"}
            )
        return data
        
    def create(self, validated_data):
        password = validated_data.get("password")
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


# ------- TokenSerializer -------
# ---- Kullanıcı login olurken token key ile birlikte user datası da dönsün! ----
from dj_rest_auth.serializers import TokenSerializer

class UserTokenSerializer(TokenSerializer):
    
    user = UserSerializers()
    
    class Meta(TokenSerializer.Meta):
        fields = ("key", "user")
