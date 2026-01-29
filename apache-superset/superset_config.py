from dotenv import load_dotenv
import os

load_dotenv()

SUPERSET_HOME = os.getenv("SUPERSET_HOME")
SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = f"sqlite:///{SUPERSET_HOME}/superset.db"
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True
}
