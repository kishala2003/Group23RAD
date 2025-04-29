-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create contents table
CREATE TABLE IF NOT EXISTS contents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    description Text NOT NULL,
    image_file VARCHAR(100) NOT NULL,
    content_type VARCHAR(20) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    release_year INTEGER NOT NULL,
    rating FLOAT DEFAULT 0.0
);

-- Create favorites table
CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    content_id INTEGER NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (content_id) REFERENCES contents (id)
);

-- Insert initial content
INSERT INTO contents (title, description, image_file, content_type, genre, release_year, rating) VALUES
('Joker', 'In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime. This path brings him face-to-face with his alter-ego: the Joker.', 'joker.jpg', 'movie', 'Thriller', 2019, 8.4),
('Naruto', 'Naruto Uzumaki, a mischievous adolescent ninja, struggles as he searches for recognition and dreams of becoming the Hokage, the village''s leader and strongest ninja.', 'naruto.jpg', 'animation', 'Anime', 2002, 8.3),
('The Maze Runner', 'Thomas is deposited in a community of boys after his memory is erased, soon learning they''re all trapped in a maze that will require him to join forces with fellow ''runners'' for a shot at escape.', 'maze_runner.jpg', 'movie', 'Sci-Fi', 2014, 6.8),
('The 100', 'Set ninety-seven years after a nuclear war has destroyed civilization, when a spaceship housing humanity''s lone survivors sends one hundred juvenile delinquents back to Earth, in hopes of possibly re-populating the planet.', 'The-100-opening.jpg', 'series', 'Sci-Fi', 2014, 7.6),
('Interstellar', 'When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.', 'Interstellar.jpg', 'movie', 'Sci-Fi', 2014, 8.6),
('The Nun', 'A priest with a haunted past and a novice on the threshold of her final vows are sent by the Vatican to investigate the death of a young nun in Romania and confront a malevolent force in the form of a demonic nun.', 'the-nun.jpg', 'movie', 'Horror', 2018, 5.3),
('Squid Game', 'Hundreds of cash-strapped players accept a strange invitation to compete in children''s games. Inside, a tempting prize awaits with deadly high stakes: a survival game that has a whopping 45.6 billion-won prize at stake.', 'squidgame.jpg', 'series', 'Thriller', 2021, 8.0),
('Attack on Titan', 'In a world where humanity lives within cities surrounded by enormous walls due to the Titans, gigantic humanoid creatures who devour humans seemingly without reason, a young boy named Eren Yeager vows to cleanse the earth of the Titans when they bring about the destruction of his city and the death of his mother.', 'attack_on_titans.jpg', 'animation', 'Anime', 2013, 9.0),
('Mufasa: The Lion King', 'Lost and alone, orphaned cub Mufasa meets a sympathetic lion named Taka, the heir to a royal bloodline. The chance meeting sets in motion an expansive journey of an extraordinary group of misfits searching for their destinies.', 'mufasa.jpg', 'movie', 'Animation', 2024, 7.2),
('Wicked', 'Misunderstood because of her green skin, a young woman named Elphaba forges an unlikely but profound friendship with Glinda, a student with an unflinching desire for popularity. Following an encounter with the Wizard of Oz, their relationship soon reaches a crossroad as their lives begin to take very different paths.', 'wicked.jpg', 'movie', 'Musical', 2024, 7.4),
('Beetlejuice Beetlejuice', 'Still haunted by Beetlejuice, Lydia''s life gets turned upside down when her daughter discovers a portal to the afterlife. When someone says Beetlejuice''s name three times, the mischievous demon soon returns to unleash his very own brand of mayhem.', 'beetlejuice2.jpg', 'movie', 'Comedy', 2024, 7.0),
('Demon Slayer', 'A young boy becomes a demon slayer after his family is slaughtered and his sister is turned into a demon.', 'demon_slayer.jpg', 'animation', 'Anime', 2019, 8.7),
('One Piece', 'Monkey D. Luffy and his pirate crew explore the Grand Line in search of the world''s ultimate treasure known as the "One Piece".', 'one_piece.jpg', 'animation', 'Anime', 1999, 8.9),
('Challengers', 'A tennis coach gets caught in a love triangle between her husband and her ex-lover.', 'challengers.jpg', 'movie', 'Drama', 2024, 7.5),
('The Wild Robot', 'A robot finds herself stranded on an island and must adapt to survive among wild animals.', 'wild_robot.jpg', 'movie', 'Animation', 2024, 7.8),
('Anora', 'Anora, a young woman from Brooklyn, gets her chance at a Cinderella story when she meets and marries the son of an oligarch. Once the news reaches Russia, her fairytale is threatened as the parents set out for New York to get the marriage annulled.', 'anora.jpg', 'movie', 'Comedy', 2024, 7.9),
('The Substance', 'An aging actress discovers a black market drug that lets her become young again, but at a cost.', 'the_substance.jpg', 'movie', 'Horror', 2024, 7.3),
('Stranger Things', 'A group of young friends in 1980s Indiana encounter secret experiments, supernatural forces, and a mysterious girl with powers.', 'stranger_things.jpg', 'series', 'Sci-Fi', 2016, 8.7),
('The Wheel of Time', 'The lives of five villagers change forever when a powerful woman arrives, claiming one is the prophesied Dragon Reborn who could save or doom the world as the Last Battle approaches.', 'wheel_of_time.jpg', 'series', 'Fantasy', 2021, 7.1),
('Divergent', 'In a dystopian future, a young woman discovers she is Divergent and must fight to survive in a society divided by factions.', 'divergent.jpg', 'movie', 'Sci-Fi', 2014, 6.6),
('Avatar', 'A paraplegic Marine is sent to the moon Pandora, where he becomes torn between following orders and protecting an alien civilization.', 'avatar.jpg', 'movie', 'Sci-Fi', 2009, 7.9),
('Tokyo Revengers', 'A young man travels back in time to his school days to save his girlfriend and change the fate of his friends.', 'tokyo_revengers.jpg', 'animation', 'Anime', 2021, 7.9),
('The Hunger Games', 'In a dystopian future, Katniss Everdeen volunteers to take her sister''s place in a televised fight to the death.', 'hunger_games.jpg', 'movie', 'Sci-Fi'.2021,7.2),
('Game of Thrones, Noble families vie for control of the Iron Throne as an ancient enemy returns after being dormant for millennia.','game_of_thrones.jpg', 'series','Fantasy', 2011, 9.2),
('Vikings, The legendary Viking chieftain Ragnar Lothbrok rises to power, exploring and raiding new lands.','vikings.jpg','series','Action', 2013, 8.5),
('Spy x Family, A spy, an assassin, and a telepath form a fake family for a secret mission, each hiding their true identity.','spy.jpg','animation','Anime',2022,8.5), 
('Avatar: The Last Airbender','A young Avatar must master all four elements and save the world from the Fire Nation.','last_airbender.jpg','animation','Anime',2005,9.3),
('Outer Banks','A group of teens in the Outer Banks of North Carolina hunt for a legendary treasure tied to the disappearance of their leaders father.','outer_banks.jpg','series','Adventure',2020,7.5),
('My Happy Marriage','In a world where supernatural powers are common, a mistreated young woman finds hope and love in an arranged marriage.','my_happy_marriage.jpg','animation','Anime',2023,8.2),
('Jujutsu Kaisen','A high schooler gains supernatural powers after ingesting a cursed object and joins a secret organization to fight evil spirits.','jujutsu_kaisen.jpg','animation','Anime',2020,8.6),
('Castlevania','A vampire hunter fights to save Eastern Europe from Dracula and his army of monsters.','castlevania.jpg','animation','Anime',2017,8.3),
('One Punch Man','Saitama, a superhero who can defeat any opponent with a single punch, seeks a real challenge.','one_punch_man.jpg','animation','Anime',2015,8.7),
('Avengers: Endgame','The Avengers assemble for a final stand against Thanos to restore balance to the universe.','avengers_endgame.jpg','movie','Action',2019,8.4),
('The Deaths Game','A man is forced to experience multiple lives and deaths after making a deal with Death.','deaths_game.jpg','series','Fantasy',2023,8.1),          
('Dark','Four interconnected families uncover a time travel conspiracy spanning several generations in a small German town.','dark.jpg','series','Sci-Fi',2017,8.7),
('All of Us Are Dead','Students trapped in a high school must fight for survival as a zombie outbreak sweeps through their city.','allofus.jpg','series','Horror',2022,7.5),
                