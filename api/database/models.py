# type: ignore
"""These are the data models used for queries via the peewee ORM."""
from peewee import (
    BooleanField,
    ForeignKeyField,
    Model,
    CharField,
    TimestampField,
    UUIDField,
    CompositeKey,
    TextField,
    IntegerField,
    FloatField
)

from playhouse.postgres_ext import ArrayField

from .settings import (
    FOOD_TABLE, POSTS_TABLE, FOLLOWERS_TABLE, USERS_TABLE, IMAGES_TABLE
)
from .database import db


class FoodModel(Model):
    """Model for users."""

    class Meta:
        """TODO document this."""

        database = db
        table_name = FOOD_TABLE

    id = IntegerField(unique=True, null=False, primary_key=True)
    food_group = CharField()
    calories = IntegerField()
    id_book = CharField()
    name = CharField()
    energy_with_dietary_fibre_kj = IntegerField()
    energy_without_dietary_fibre_kj = IntegerField()
    moisture_g = FloatField()
    protein_g = FloatField()
    fat_g = FloatField()
    carbs_g = FloatField()
    sugars_g = FloatField()



class UserModel(Model):
    """Model for users."""

    class Meta:
        """TODO document this."""

        database = db
        table_name = USERS_TABLE

    id = UUIDField(unique=True, null=False, primary_key=True)
    username = CharField(unique=True, null=False)
    email = CharField(unique=True, null=False)
    first_name = CharField(null=False)
    last_name = CharField(null=False)
    description = CharField(null=True)
    password_hash = CharField(null=False)
    create_time = TimestampField(null=True, default=None, resolution=0, utc=False)
    disabled = BooleanField(null=False, default=True)


class FollowerModel(Model):
    """Model for followers."""

    class Meta:
        """TODO document this."""

        database = db
        table_name = FOLLOWERS_TABLE
        primary_key = CompositeKey("user_id", "follower_id")

    user_id = ForeignKeyField(
        UserModel,
        on_delete="CASCADE",
        on_update="CASCADE",
        column_name="user_id",
    )
    follower_id = ForeignKeyField(
        UserModel,
        on_delete="CASCADE",
        on_update="CASCADE",
        column_name="follower_id",
    )
    create_time = TimestampField(default=None, resolution=0, utc=False)


class ImageModel(Model):
    """Model for images."""

    class Meta:
        """TODO document this."""

        database = db
        table_name = IMAGES_TABLE

    id = UUIDField(unique=True, null=False, primary_key=True)
    user_id = ForeignKeyField(
        UserModel,
        on_delete="CASCADE",
        on_update="CASCADE",
        column_name="user_id",
    )
    format = CharField(null=True)
    is_profile = BooleanField(default=False)
    create_time = TimestampField(default=None, resolution=0, utc=False)


class PostModel(Model):
    """Model for posts."""

    class Meta:
        """TODO document this."""

        database = db
        table_name = POSTS_TABLE

    id = UUIDField(unique=True, null=False, column_name="id", primary_key=True)
    user_id = ForeignKeyField(
        UserModel,
        on_delete="CASCADE",
        on_update="CASCADE",
        column_name="user_id",
    )
    image_id = ForeignKeyField(
        ImageModel,
        on_delete="CASCADE",
        on_update="CASCADE",
        column_name="image_id",
        null=True,
    )
    content = CharField(null=True)
    create_time = TimestampField(default=None, resolution=0, utc=False)
    edited = BooleanField(null=False, default=False)
    edit_time = TimestampField(default=None, resolution=0, utc=False)
    visibility = CharField(null=False, default="public")
    likes = ArrayField(null=True, field_class=TextField)
