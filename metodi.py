
#questo è il commit del post che non ho fatto prima

from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Funzione per connettersi al database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Videogiochi"
    )

# Rotta per ottenere il contenuto della tabella 'mammiferi' in formato JSON
@app.route('/api/dati', methods=['GET'])
def get_games():
    # Connessione al database
    mydb = connect_to_db()
    mycursor = mydb.cursor(dictionary=True)
    
    # Esecuzione della query per selezionare tutti i dati dalla tabella
    mycursor.execute("SELECT * FROM games")
    games = mycursor.fetchall()
    
    # Chiusura delle connessioni
    mycursor.close()
    mydb.close()
    
    # Restituisce i dati in formato JSON
    return jsonify(games)

@app.route('/api/dati', methods=['POST'])
def add_game():
    data = request.get_json()  # Recupera i dati JSON inviati dal client

    # Verifica che tutti i campi necessari siano presenti
    if not all(key in data for key in ('titolo', 'genere',  'piattaforma', 'data_uscita', 'sviluppatore')):
        return jsonify({"error": "Dati mancanti"}), 400

    titolo = data['titolo']
    genere = data['genere']
    piattaforma = data['piattaforma']
    data_uscita = data['data_uscita']
    sviluppatore = data['sviluppatore']

    # Connessione al database e inserimento dei dati
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    sql = "INSERT INTO games (titolo, genere, piattaforma, data_uscita, sviluppatore) VALUES (%s, %s, %s, %s, %s)"
    values = (titolo, genere, piattaforma, data_uscita, sviluppatore)
    
    mycursor.execute(sql, values)
    mydb.commit()

    mycursor.close()
    mydb.close()

    return jsonify({"message": "gioco inserito con successo!"}), 201



@app.route('/api/dati/<int:id>', methods=['DELETE'])
def delete_game(id):
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    # Verifica se il gioco con questo id esiste
    mycursor.execute("SELECT * FROM games WHERE Id = %s", (id,))
    if not mycursor.fetchone():
        mycursor.close()
        mydb.close()
        return jsonify({"message": "gioco non trovato"}), 404

    # Esegue l'operazione di DELETE
    sql = "DELETE FROM games WHERE Id = %s"
    mycursor.execute(sql, (id,))
    mydb.commit()

    mycursor.close()
    mydb.close()

    return jsonify({"message": "gioco eliminato con successo!"}), 200


if __name__ == '__main__':
    app.run(debug=True)