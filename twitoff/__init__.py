'''Entry point to the Twitoff Flask Application'''

from .app import create_app


if __name__ == "__main__":
    db.create_all()
    APP = create_app()
    APP.run()

    # db.create_all()

    # user1 = User(username = 'elonmusk', follower_count = 37000000)
    # user2 = User(username = 'ladygaga', follower_count = 80000000)
    # user3 = User(username = 'ellen', follower_count = 79900000)
    # user4 = User(username = 'youtube', follower_count = 72200000)
    # user5 = User(username = 'britney', follower_count = 56000000)
    # user6 = User(username = 'demi', follower_count = 55000000)

    # db.session.add_all([user1, user2, user3, user4, user5, user6])

    # db.session.commit()
    # APP.run()