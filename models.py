from app import db


class AllDeck(db.Model):

    __tablename__ = "AllDeck"

    id = db.Column(db.Integer, primary_key=True)
    cards = db.Column(db.String)

    def __init__(self, cards):
        self.cards = cards


class UserCards(db.Model):

    __tablename__ = "UserCards"

    id = db.Column(db.Integer, primary_key=True)
    cards = db.Column(db.String)

    def __init__(self, cards):
        self.cards = cards


class DealerCards(db.Model):

    __tablename__ = "DealerCards"

    id = db.Column(db.Integer, primary_key=True)
    cards = db.Column(db.String)

    def __init__(self, cards):
        self.cards = cards
