"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game/<player>')
def show_madlib_form(player):

    name = player
    print(name)

    play_game = request.args.get('play')

    if play_game == 'True':
        return render_template('game.html')
    else:
        return render_template('goodbye.html',name=player)

@app.route('/madlib')
def show_madlib():

    player = request.args.get('person')
    fav_color = request.args.get('favColor')
    player_noun = request.args.get('noun')
    player_adj = request.args.get('adjective')

    return render_template('madlib.html', person=player, color=fav_color, noun=player_noun, adjective=player_adj)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
