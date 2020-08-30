from app import db


class HelloWorld(db.Model):
    __tablename__ = "follows"
    id = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.Integer)
    ## Foregin keys
    # access information by backref `user`
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # access information by backref `college`
    college_id = db.Column(db.Integer, db.ForeignKey('colleges.id'))
