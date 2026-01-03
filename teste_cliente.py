from lib.wprotoc import client
lista=[
    f"name{x}" for x in range(200)
]
programa=client("pyos","tablet")
for n in lista:
    programa.send_str(n)
programa.send_obj(lista)