from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

host = os.environ["host"]
database = os.environ["database"]
user = os.environ["user"]
password = os.environ["password"]

# Função para criar conexão no banco
def conecta():
  con = psycopg2.connect(host=host, 
                         database=database,
                         user=user, 
                         password=password)
  return con

# Função para criar tabela no banco
def criar(sql):
  con = conecta()
  cur = con.cursor()
  cur.execute(sql)
  con.commit()
  con.close()

# Função para inserir dados no banco
def inserir(sql):
    con = conecta()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

# Função para consultas no banco
def consultar(sql):
  con = conecta()
  cur = con.cursor()
  cur.execute(sql)
  recset = cur.fetchall()
  con.close()
  return recset