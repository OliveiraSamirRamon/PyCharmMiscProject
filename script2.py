import asyncio
from math import factorial

valores = [3,4,5,6,7]

async def fatorial(n):
    await asyncio.sleep(n)
    print(f"Fatorial de {n} ", factorial(n))

async def main():
    tarefas = [asyncio.create_task(fatorial(n)) for n in valores]
    await asyncio.gather(*tarefas)

asyncio.run(main())