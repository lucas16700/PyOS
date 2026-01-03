import asyncio
from lib.wprotoc import server,print


async def main():
    programa = server("pyos", "serverbrabo")

    # inicia a escuta em paralelo
    asyncio.create_task(programa.search())
    print("task criada")
    # código convencional continua
    while programa.down:
        await asyncio.sleep(0)
    print(programa.__dict__)
    addr = programa.last_id
    programa.activate(addr)

    data = True
    while data:
        data = programa.get(addr)
        print(data)

asyncio.run(main())