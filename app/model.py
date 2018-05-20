from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unique_word_count = db.Column(db.Integer)
    short_description = db.Column(db.String(60))
    text = db.Column(db.Text())

    def __repr__(self):
        return '<Note %r>' % self.id
