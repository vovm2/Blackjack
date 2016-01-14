from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my.db'

db = SQLAlchemy(app)

from models import *
from functions import new_deck, add, to_db, from_db2arr


@app.route('/')
def index():
    return render_template('main.html')


@app.route("/game", methods=["POST"])
def new_game():
    all_deck = new_deck()

    game = []
    for i in range(4):
        game.append(all_deck.pop())

    to_db(UserCards, [game[0], game[1]])
    to_db(DealerCards, [game[2], game[3]])
    to_db(AllDeck, all_deck)

    user_deck = [game[0], game[1]]
    dealer_deck = ['X', game[3]]

    return render_template('main.html', player=user_deck, dealer=dealer_deck)


@app.route("/hit", methods=["POST"])
def hit():
    all_deck = from_db2arr(AllDeck)
    user_deck = from_db2arr(UserCards)
    user_deck.append(all_deck.pop())

    to_db(UserCards, user_deck)
    to_db(AllDeck, all_deck)

    dealer_deck = from_db2arr(DealerCards)

    if add(user_deck) > 21:
        val1 = add(user_deck)
        val2 = add(dealer_deck)
        return render_template('main.html', val1=val1, val2=val2, msg="You lose", player=user_deck, dealer=dealer_deck)

    dealer_deck[0] = 'X'
    return render_template('main.html', player=user_deck, dealer=dealer_deck)


@app.route("/stand", methods=["POST"])
def stand():
    user_deck = from_db2arr(UserCards)
    val1 = add(user_deck)

    dealer_deck = from_db2arr(DealerCards)
    val2 = add(dealer_deck)

    if val2 < 17:
        all_deck = from_db2arr(AllDeck)
        while val2 < 17:
            dealer_deck.append(all_deck.pop())
            val2 = add(dealer_deck)

    if val2 > val1 and val2 <= 21:
        msg = "You lose"
    elif val2 == val1:
        msg = "A tied score"
    else:
        msg = "You win!"

    return render_template('main.html', val1=val1, val2=val2, msg=msg, player=user_deck, dealer=dealer_deck)
    

@app.route('/hello')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
