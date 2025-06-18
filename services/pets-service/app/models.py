from app import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    breed = db.Column(db.String(50))
    documents = db.Column(db.String(255))

    def to_dict(self):
        return {"id": self.id, "name": self.name, "type": self.type}
