from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_migrate import Migrate
from models import db, User, Content, Favorite
import os
from sqlalchemy import func, or_


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///streamvision.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)
migrate = Migrate(app, db)


# Home route
@app.route('/')
def index():
    search_query = request.args.get('search')
    if search_query:
        # Perform search query
        movies = Content.query.filter(
            Content.content_type == 'movie',
            or_(
                Content.title.ilike(f'%{search_query}%'),
                Content.description.ilike(f'%{search_query}%')
            )
        ).all()
        series = Content.query.filter(
            Content.content_type == 'series',
            or_(
                Content.title.ilike(f'%{search_query}%'),
                Content.description.ilike(f'%{search_query}%')
            )
        ).all()
        animations = Content.query.filter(
            Content.content_type == 'animation',
            or_(
                Content.title.ilike(f'%{search_query}%'),
                Content.description.ilike(f'%{search_query}%')
            )
        ).all()
    else:
        # Original query to display all content
        movies = Content.query.filter_by(content_type='movie').all()
        series = Content.query.filter_by(content_type='series').all()
        animations = Content.query.filter_by(content_type='animation').all()
     

         # Add the debugging code right here
    print(f"Number of movies loaded: {len(movies)}")
    for movie in movies:
        print(f"Movie: {movie.title}, Image: {movie.image_file}")
    
    print(f"Number of series loaded: {len(series)}")
    for sery in series:
        print(f"Series: {sery.title}, Image: {sery.image_file}")

    print(f"Number of animations loaded: {len(animations)}")
    for animation in animations:
        print(f"Animation: {animation.title}, Image: {animation.image_file}")


    return render_template('index.html',
                           movies=movies,
                           series=series,
                           animations=animations,
                           search_query=search_query)  # Pass search_query to template


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')


# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user exists...
        user_exists = User.query.filter((User.username == username) | (User.email == email)).first()
        if user_exists:
            flash('Username or email already exists!', 'danger')
            return redirect(url_for('register'))

        # Create new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))


# Content detail route
@app.route('/content/<int:content_id>')
def content_detail(content_id):
    content = Content.query.get_or_404(content_id)
    # Fetch similar content (e.g., same genre)
    similar_contents = Content.query.filter(
        Content.genre == content.genre,
        Content.id != content_id,
        Content.content_type == 'movie'  # Ensure it's a movie
    ).limit(5).all()  # Exclude the current content

    return render_template('movie.html', content=content, similar_contents=similar_contents)


# Add to favorites
@app.route('/favorite/<int:content_id>', methods=['POST'])
def add_favorite(content_id):
    if 'user_id' not in session:
        flash('Please login to add favorites.', 'danger')
        return redirect(url_for('login'))

    # Check if already in favorites
    favorite_exists = Favorite.query.filter_by(
        user_id=session['user_id'],
        content_id=content_id
    ).first()

    if favorite_exists:
        flash('This content is already in your favorites!', 'info')
    else:
        new_favorite = Favorite(user_id=session['user_id'], content_id=content_id)
        db.session.add(new_favorite)
        db.session.commit()
        flash('Added to favorites!', 'success')

    return redirect(url_for('content_detail', content_id=content_id))


# Profile route
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('Please login to view your profile.', 'danger')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    favorites = Favorite.query.filter_by(user_id=session['user_id']).all()

    return render_template('profile.html', user=user, favorites=favorites)


# Initialize the database with sample data
def initialize_db():
    with app.app_context():
        db.create_all()

        # Check if there's any content already
        if Content.query.count() == 0:
            # Create initial content based on the provided images
            contents = [
                Content(
                    title="Joker",
                    description="In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime. This path brings him face-to-face with his alter-ego: the Joker.",
                    image_file="joker.jpg",
                    content_type="movie",
                    genre="Thriller",
                    release_year=2019,
                    rating=8.4
                ),
                Content(
                    title="Naruto",
                    description="Naruto Uzumaki, a mischievous adolescent ninja, struggles as he searches for recognition and dreams of becoming the Hokage, the village's leader and strongest ninja.",
                    image_file="naruto.jpg",
                    content_type="animation",
                    genre="Anime",
                    release_year=2002,
                    rating=8.3
                ),
                Content(
                    title="Squid Game",
                    description="Hundreds of cash-strapped players accept a strange invitation to compete in children's games. Inside, a tempting prize awaits with deadly high stakes: a survival game that has a whopping 45.6 billion-won prize at stake.",
                    image_file="squidgame.jpg",  
                    content_type="series",
                    genre="Thriller",
                    release_year=2021,
                    rating=8.0
                ),
                Content(
                    title="Attack on Titan",
                    description="In a world where humanity lives within cities surrounded by enormous walls due to the Titans, gigantic humanoid creatures who devour humans seemingly without reason, a young boy named Eren Yeager vows to cleanse the earth of the Titans when they bring about the destruction of his city and the death of his mother.",
                    image_file="attack_on_titans.jpg",
                    content_type="animation",
                    genre="Anime",
                    release_year=2013,
                    rating=9.0
                ),
                Content(
                    title="The Maze Runner",
                    description="Thomas is deposited in a community of boys after his memory is erased, soon learning they're all trapped in a maze that will require him to join forces with fellow 'runners' for a shot at escape.",
                    image_file="maze_runner.jpg",
                    content_type="movie",
                    genre="Sci-Fi",
                    release_year=2014,
                    rating=6.8
                ),
                Content(
                    title="The 100",
                    description="Set ninety-seven years after a nuclear war has destroyed civilization, when a spaceship housing humanity's lone survivors sends one hundred juvenile delinquents back to Earth, in hopes of possibly re-populating the planet.",
                    image_file="The-100-opening.jpg",
                    content_type="series",
                    genre="Sci-Fi",
                    release_year=2014,
                    rating=7.6
                ),
                 Content(
                    title="Stranger Things",
                    description="A group of young friends in 1980s Indiana encounter secret experiments, supernatural forces, and a mysterious girl with powers.",
                    image_file="stranger_things.jpg",
                    content_type="series",
                    genre="Sci-Fi",
                    release_year=2016,
                    rating=8.7
                ),
                Content(
                    title="The Wheel of Time",
                    description="In a world where magic exists but only women can use it, Moiraine leads five young villagers on a journey that could change the fate of humanity.",
                    image_file="wheel_of_time.jpg",
                    content_type="series",
                    genre="Fantasy",
                    release_year=2021,
                    rating=7.1
                ),
                Content(
                    title="Interstellar",
                    description="When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.",
                    image_file="Interstellar.jpg",
                    content_type="movie",
                    genre="Sci-Fi",
                    release_year=2014,
                    rating=8.6
                ),
                Content(
                    title="The Nun",
                    description="A priest with a haunted past and a novice on the threshold of her final vows are sent by the Vatican to investigate the death of a young nun in Romania and confront a malevolent force in the form of a demonic nun.",
                    image_file="the-nun.jpg",
                    content_type="movie",
                    genre="Horror",
                    release_year=2018,
                    rating=5.3
                ),
                Content(
                    title="Mufasa: The Lion King",
                    description="Lost and alone, orphaned cub Mufasa meets a sympathetic lion named Taka, the heir to a royal bloodline. The chance meeting sets in motion an expansive journey of an extraordinary group of misfits searching for their destinies.",
                    image_file="mufasa.jpg",
                    content_type="movie",
                    genre="Animation",
                    release_year=2024,
                    rating=7.2
                ),
                Content(
                    title="Wicked",
                    description="Misunderstood because of her green skin, a young woman named Elphaba forges an unlikely but profound friendship with Glinda, a student with an unflinching desire for popularity. Following an encounter with the Wizard of Oz, their relationship soon reaches a crossroad as their lives begin to take very different paths.",
                    image_file="wicked.jpg",
                    content_type="movie",
                    genre="Musical",
                    release_year=2024,
                    rating=7.4
                ),
                Content(
                    title="Beetlejuice Beetlejuice",
                    description="Still haunted by Beetlejuice, Lydia's life gets turned upside down when her daughter discovers a portal to the afterlife. When someone says Beetlejuice's name three times, the mischievous demon soon returns to unleash his very own brand of mayhem.",
                    image_file="beetlejuice2.jpg",
                    content_type="movie",
                    genre="Comedy",
                    release_year=2024,
                    rating=7.0
                ),
                Content(
                    title="Demon Slayer",
                    description="A young boy becomes a demon slayer after his family is slaughtered and his sister is turned into a demon.",
                    image_file="demon_slayer.jpg",
                    content_type="animation",
                    genre="Anime",
                    release_year=2019,
                    rating=8.7
                ),
                Content(
                    title="One Piece",
                    description="Monkey D. Luffy and his pirate crew explore the Grand Line in search of the world's ultimate treasure known as the One Piece.",
                    image_file="one_piece.jpg",
                    content_type="animation",
                    genre="Anime",
                    release_year=1999,
                    rating=8.9
                ),
                Content(
                    title="Challengers",
                    description="A tennis coach gets caught in a love triangle between her husband and her ex-lover.",
                    image_file="challengers.jpg",
                    content_type="movie",
                    genre="Drama",
                    release_year=2024,
                    rating=7.5
                ),
                Content(
                    title="The Wild Robot",
                    description="A robot finds herself stranded on an island and must adapt to survive among wild animals.",
                    image_file="wild_robot.jpg",
                    content_type="movie",
                    genre="Animation",
                    release_year=2024,
                    rating=7.8
                ),
                Content(
                    title="Anora",
                    description="Anora, a young woman from Brooklyn, gets her chance at a Cinderella story when she meets and marries the son of an oligarch. Once the news reaches Russia, her fairytale is threatened as the parents set out for New York to get the marriage annulled.",
                    image_file="anora.jpg",
                    content_type="movie",
                    genre="Comedy",
                    release_year=2024,
                    rating=7.9
                ),
                Content(
                    title="The Substance",
                    description="An aging actress discovers a black market drug that lets her become young again, but at a cost.",
                    image_file="the_substance.jpg",
                    content_type="movie",
                    genre="Horror",
                    release_year=2024,
                    rating=7.3
                ),
                 Content(
                    title="Divergent",
                    description="In a dystopian future, a young woman discovers she's Divergent and must fight to survive in a society divided by factions.",
                    image_file="divergent.jpg",
                    content_type="movie",
                    genre="Sci-Fi",
                    release_year=2014,
                    rating=6.6
                ),
                Content(
                    title="Avatar",
                    description="A paraplegic Marine is sent to the moon Pandora, where he becomes torn between following orders and protecting an alien civilization.",
                    image_file="avatar.jpg",
                    content_type="movie",
                    genre="Sci-Fi",
                    release_year=2009,
                    rating=7.9
                ),
                Content(
                    title="Tokyo Revengers",
                    description="A young man travels back in time to his school days to save his girlfriend and change the fate of his friends.",
                    image_file="tokyo_revengers.jpg",
                    content_type="animation",
                    genre="Anime",
                    release_year=2021,
                    rating=7.9
                ),
                Content(
                    title="The Hunger Games",
                    description="In a dystopian future, Katniss Everdeen volunteers to take her sister's place in a televised fight to the death.",
                    image_file="hunger_games.jpg",
                    content_type="movie",
                    genre="Sci-Fi",
                    release_year=2012,
                    rating=7.2
                ),
                Content(
                    title="Game of Thrones",
                    description="Noble families vie for control of the Iron Throne as an ancient enemy returns after being dormant for millennia.",
                    image_file="game_of_thrones.jpg",
                    content_type="series",
                    genre="Fantasy",
                    release_year=2011,
                    rating=9.2
                ),
                Content(
                    title="Vikings",
                    description="The legendary Viking chieftain Ragnar Lothbrok rises to power, exploring and raiding new lands.",
                    image_file="vikings.jpg",
                    content_type="series",
                    genre="Action",
                    release_year=2013,
                    rating=8.5
                ),
                Content(
                    title="Spy x Family",
                    description="A spy, an assassin, and a telepath form a fake family for a secret mission, each hiding their true identity.",
                    image_file="spy.jpg",
                    content_type="animation",
                    genre="Anime",
                    release_year=2022,
                    rating=8.5
                ),
                Content(
                    title="Avatar: The Last Airbender",
                    description="A young Avatar must master all four elements and save the world from the Fire Nation.",
                    image_file="last_airbender.jpg",
                    content_type="animation",
                    genre="Anime",
                    release_year=2005,
                    rating=9.3
                ),
                Content(
                    title="Outer Banks",
                    description="A group of teens in the Outer Banks of North Carolina hunt for a legendary treasure tied to the disappearance of their leader's father.",
                    image_file="outer_banks.jpg",
                    content_type="series",
                    genre="Adventure",
                    release_year=2020,
                    rating=7.5
                ),
                Content(
                    title="My Happy Marriage",
                    description="In a world where supernatural powers are common, a mistreated young woman finds hope and love in an arranged marriage.",
                    image_file="my_happy_marriage.jpg",
                    content_type="animation",
                    genre="Anime",
                    release_year=2023,
                    rating=8.2
                ),
                Content(
                    title="Jujutsu Kaisen",
                    description="A high schooler gains supernatural powers after ingesting a cursed object and joins a secret organization to fight evil spirits.",
                    image_file="jujutsu_kaisen.jpg",
                    content_type="animation",
                    genre="Anime",
                    release_year=2020,
                    rating=8.6
                ),
                Content(
                    title="Castlevania",
                    description="A vampire hunter fights to save Eastern Europe from Dracula and his army of monsters.",
                    image_file="castlevania.jpg",
                    content_type="animation",
                    genre="Anime",
                    release_year=2017,
                    rating=8.3
                ),
                Content(
                    title="One Punch Man",
                    description="Saitama, a superhero who can defeat any opponent with a single punch, seeks a real challenge.",
                    image_file="one_punch_man.jpg",
                    content_type="animation",
                    genre="Anime",
                    release_year=2015,
                    rating=8.7
                ),
                Content(
                    title="Avengers: Endgame",
                    description="The Avengers assemble for a final stand against Thanos to restore balance to the universe.",
                    image_file="avengers_endgame.jpg",
                    content_type="movie",
                    genre="Action",
                    release_year=2019,
                    rating=8.4
                ),
                Content(
                    title="The Death's Game",
                    description="A man is forced to experience multiple lives and deaths after making a deal with Death.",
                    image_file="deaths_game.jpg",
                    content_type="series",
                    genre="Fantasy",
                    release_year=2023,
                    rating=8.1
                ),
                Content(
                    title="Dark",
                    description="Four interconnected families uncover a time travel conspiracy spanning several generations in a small German town.",
                    image_file="dark.jpg",
                    content_type="series",
                    genre="Sci-Fi",
                    release_year=2017,
                    rating=8.7
                ),
                Content(
                    title="All of Us Are Dead",
                    description="Students trapped in a high school must fight for survival as a zombie outbreak sweeps through their city.",
                    image_file="allofus.jpg",
                    content_type="series",
                    genre="Horror",
                    release_year=2022,
                    rating=7.5
                ),
            ]

            db.session.bulk_save_objects(contents)
            db.session.commit()

if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)

    