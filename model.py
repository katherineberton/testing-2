from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.

    #add it to testdb
    #commit testdb

    #create a Game object with variable names and description of our choosing
    g_1 = Game(name='Red Flags!', description='The dating games of RED FLAGS' )
    g_2 = Game(name='Eldritch Horror', description='Really difficult, basically impossible with less than 4 players' )
    g_3 = Game(name='Gloomhaven', description='A very very long but awesome game')

    db.session.add_all([g_1, g_2, g_3])
    db.session.commit()
    


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
