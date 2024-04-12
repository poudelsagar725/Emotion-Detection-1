import sqlite3

# Load Database Pkg
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

# Fxn
def create_page_visited_table():
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT,timeOfvisit TIMESTAMP)')

def add_page_visited_details(pagename, timeOfvisit):
    with conn:
        c.execute('INSERT INTO pageTrackTable(pagename, timeOfvisit) VALUES(?, ?)', (pagename, timeOfvisit))

def view_all_page_visited_details():
    with conn:
        c.execute('SELECT * FROM pageTrackTable')
        data = c.fetchall()
        return data

# Fxn To Track Input & Prediction
def create_emotionclf_table():
    with conn:
        c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT, prediction TEXT, probability NUMBER, timeOfvisit TIMESTAMP)')

def add_prediction_details(rawtext, prediction, probability, timeOfvisit):
    with conn:
        c.execute('INSERT INTO emotionclfTable(rawtext, prediction, probability, timeOfvisit) VALUES(?, ?, ?, ?)', (rawtext, prediction, probability, timeOfvisit))

def view_all_prediction_details():
    with conn:
        c.execute('SELECT * FROM emotionclfTable')
        data = c.fetchall()
        return data
