'''SQLAlchemy models for Twitoff'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    follower_count = db.Column(db.Integer, nullable=False)
    # Tweet IDs are ordinal ints, so we can fetch most recent tweets
    newest_tweet_id = db.Column(db.BigInteger)
    #tweets = db.relationship('Tweet', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Tweet(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    text = db.Column(db.String(300))
    embedding = db.Column(db.PickleType, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweet', lazy=True))

    def __repr__(self):
        return '<Tweet %r>' % self.text

# if __name__ == "__main__":
#     # db.drop_all()
#     db.create_all()

#     u1 = User(username = 'elonmusk', follower_count = 37000000)
#     u2 = User(username = 'ladygaga', follower_count = 80000000)
#     u3 = User(username = 'ellen', follower_count = 79900000)
#     u4 = User(username = 'youtube', follower_count = 72200000)
#     u5 = User(username = 'britney', follower_count = 56000000)
#     u6 = User(username = 'demi', follower_count = 55000000)

#     db.session.add_all([user1, user2, user3, user4, user5, user6])

#     db.session.commit()

