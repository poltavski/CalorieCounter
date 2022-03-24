from os import environ

env = environ.get("ENV")

DATABASE = {
    "db_name": environ["DB_NAME"],
    "user": environ["DB_USER"],
    "password": environ["DB_PASSWORD"],
    "host": environ["DB_HOST"],
    "port": environ["DB_PORT"],
    "autorollback": True,
}

# Tables
FOOD_TABLE = "food_nutrient"
FOLLOWERS_TABLE = "followers"
IMAGES_TABLE = "images"
POSTS_TABLE = "posts"
ROOM_USERS_TABLE = "room_users"
ROOMS_TABLE = "rooms"
USERS_TABLE = "users"

