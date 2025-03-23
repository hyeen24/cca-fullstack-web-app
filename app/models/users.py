from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from extensions import db  # ✅ Fix circular import

class User(UserMixin, db.Document):
    meta = {'collection': 'appUsers'}
    
    email = db.StringField(required=True, unique=True, max_length=30)
    password = db.StringField(required=True)
    name = db.StringField(required=True, max_length=50)
    role = db.StringField(default="user")

    # Needed for Flask-Login
    @property
    def id(self):
        return str(self.pk)  # ✅ Ensures compatibility with Flask-Login

    @staticmethod
    def getUser(email):
        return User.objects(email=email).first()

    @staticmethod    
    def getAllUsers():
        return User.objects().order_by('name')

    @staticmethod 
    def createUser(email, name, password, role="user"):
        user = User.getUser(email)
        if not user:
            hashed_password = generate_password_hash(password)  # ✅ Hash password
            user = User(email=email, name=name, password=hashed_password, role=role).save()
            print(f"✅ User {name} created.")
        return user
