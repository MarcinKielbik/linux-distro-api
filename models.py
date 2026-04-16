from extensions import db

class Distro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    based_on = db.Column(db.String(100))
    release_date = db.Column(db.String(20))
    version = db.Column(db.Integer)
    developers = db.Column(db.Integer)
    image = db.Column(db.String(200))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "based_on": self.based_on,
            "release_date": self.release_date,
            "version": self.version,
            "developers": self.developers,
            "image": self.image
        }