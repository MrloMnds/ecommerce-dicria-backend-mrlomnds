from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(
              Account.objects.all(), massage="email already registered."
            )
        ]
    )
    phone_number = serializers.CharField(
        validators=[UniqueValidator(
              Account.objects.all(), massage="phone number already in use."
            )
        ]
    )

    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "password",
            "phone_number",
            "first_name",
            "last_name",
            "is_superuser"
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "phone_number": {"write_only": True},
            "is_superuser": {"read_only": True}
        }

    def create(self, validated_data: dict) -> Account:
        if validated_data["is_staff"]:
            return Account.objects.create_superuser(**validated_data)

        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
