from email.policy import default
from user import db
import datetime 

class user(db.Document):
    fullname = db.StringField(required = True)
    email = db.EmailField()
    emailconfirmed = db.BooleanField(default = True)
    password = db.StringField(required=True)
    createdDate = db.DateTimeField(default=datetime.datetime.utcnow)
    isActive = db.BooleanField(default=True)
    gameHistory = db.ListField(db.StringField())
    phone = db.IntField()
    playedGame = db.ListField(db.DictField())

    def to_json(self):
        return{
            "id": str(self.pk),
            "fullname": self.fullname,
            "email": self.email,
            "password": self.password,
            "createdDate": self.createdDate,
            "isActive": self.isActive,
            "phone": self.phone,
            "playedGame": self.playedGame
        }
    def __repr__ (self):
        return '<User %r>' % self.fullname