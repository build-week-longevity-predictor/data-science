import psycopg2
import os
from dotenv import load_dotenv



class DbHelper():
    def __init__(self):
        load_dotenv()
        self.dbname=os.getenv("dbname")
        self.user=os.getenv("user")
        self.password=os.getenv("password")
        self.host=os.getenv("host")


    # create db connection
    def get_cursor(self):
        conn = psycopg2.connect(database=self.dbname, user=self.user, 
                                password=self.password, host=self.host)
        return conn.cursor()


    def query_player(self, name:str):
        cur = self.get_cursor()
        cur.execute(f'''SELECT * FROM players_nba as p WHERE p.player = '{name}' ''')
        results = cur.fetchone()
        cur.close()

        return results
    
    def query_all_players(self):
        cur = self.get_cursor()
        cur.execute('''SELECT * FROM players_nba''')
        results = cur.fetchall()
        cur.close()
        return results
