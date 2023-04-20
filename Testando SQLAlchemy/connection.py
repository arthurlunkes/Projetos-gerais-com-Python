from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/BASEPESSOAL', echo=True)
con = engine.connect()
cur = con.cursor

con.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")

con.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

# Read
result_set = con.execute("SELECT * FROM films")  
for r in result_set:  
    print(r)