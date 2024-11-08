import mysql.connector



# Creare una connessione al database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Videogiochi"
)

mycursor = mydb.cursor()

# Query di inserimento in una variabile
insert_query = '''
INSERT INTO games (titolo, genere, piattaforma, data_uscita, sviluppatore) VALUES ( %s, %s, %s, %s, %s)
'''

# Dati degli animali
giochi = [
('The Legend of Zelda: Breath of the Wild', 'Azione-avventura', 'Nintendo Switch', 2017, 'Nintendo'),
('The Witcher 3: Wild Hunt', 'RPG', 'PC, PS4, Xbox One', 2015, 'CD Projekt Red'),
('Red Dead Redemption 2', 'Azione-avventura', 'PC, PS4, Xbox One', 2018, 'Rockstar Games'),
('Grand Theft Auto V', 'Azione-avventura', 'PC, PS4, Xbox One', 2013, 'Rockstar Games'),
('Minecraft', 'Sandbox', 'PC, PS4, Xbox One', 2011, 'Mojang Studios'),
('Elden Ring', 'Azione RPG', 'PC, PS5, Xbox Series X/S', 2022, 'FromSoftware'),
('Cyberpunk 2077', 'RPG', 'PC, PS4, Xbox One', 2020, 'CD Projekt Red'),
('The Last of Us', 'Azione-avventura', 'PS3', 2013, 'Naughty Dog'),
('Fortnite', 'Battle Royale', 'PC, PS4, Xbox One', 2017, 'Epic Games'),
('Dota 2', 'MOBA', 'PC', 2013, 'Valve')
]

# Eseguire l'inserimento

mycursor.executemany(insert_query, giochi)



# Salvare (commit) le modifiche
mydb.commit()


# Chiudere la connessione
mycursor.close()
mydb.close()
