import pymongo as pyM
from pprint import pprint

# Conectando ao MongoDB / Conecta ao cluster
client = pyM.MongoClient("mongodb connection string") # string retirada do mongodb atlas

# Buscando coleções
db = client.clientes # cria o db chaamado 'clientes'
collection = db.bank # cria a coleção chamada bank


# Inserindo dados na coleção bank
posts = [{
    "nome" : "Bruno Daniel",
    "cpf": "072056924",
    "endereço": "Rua Joaquim Barreiros, 132",
    "conta": "001",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}, {
    "nome" : "Samuel Nunes",
    "cpf": "092657852",
    "endereço": "Rua Lucas Silva, 101",
    "conta": "002",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}, {
    "nome" : "Danilo Marques",
    "cpf": "073659852",
    "endereço": "Rua Jorge Luiz, 58",
    "conta": "003",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}, {
    "nome" : "Thais Fernandes",
    "cpf": "0455358",
    "endereço": "Rua Dom aguirre, 231",
    "conta": "004",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}]

# postando = collection.insert_many(posts)

post = {
    "nome" : "Marcos Augusto",
    "cpf": "3873860",
    "endereço": "Rua Marinho, 37",
    "conta": "005",
    "agencia": "0002",
    "tipo" : "corrente",
    "saldo": 0
}
# postando = collection.insert_one(post)


# Recuperando dados da collection bank

pprint(collection.find())
find = collection.find()
for post in find:
    pprint(post)

print(collection.count_documents({}))

print(collection.count_documents({"agencia": "0001"}))

for post in collection.find({}).sort("nome"): # sort("campo a ser ordenado")
    pprint(post)