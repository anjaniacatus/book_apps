import os
from config.env import env, BASE_DIR

env.read_env(os.path.join(BASE_DIR, ".env"))
STORAGE_CLOUD_NAME = env("CLOUDINARY_CLOUD_NAME")
STORAGE_API_KEY = env("CLOUDINARY_API_KEY")
STORAGE_API_SECRET = env("CLOUDINARY_API_SECRET")
