from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/FACULDADE')
con = engine.connect()
response = con.execute('SELECT * FROM academico;')
for row in response:
    print(row)