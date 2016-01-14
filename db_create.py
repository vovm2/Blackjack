from app import db
from models import AllDeck, UserCards, DealerCards

# create the database and the db table
db.create_all()

# insert data
db.session.add(AllDeck("Test"))
db.session.add(UserCards("Test"))
db.session.add(DealerCards("Test"))

# commit the changes
db.session.commit()
