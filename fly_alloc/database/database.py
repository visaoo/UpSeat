from tinydb import TinyDB, Query

# Conecta-se ao banco de dados 'db.json'
# Se o arquivo não existir, ele será criado.
db = TinyDB('db.json')
print("Conectado ao banco de dados 'db.json' com sucesso!")