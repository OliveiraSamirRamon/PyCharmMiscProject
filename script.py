import asyncio
from asyncio import create_task


async def download():
    print("Iniciando download... ")
    await asyncio.sleep(3)
    print("Download concluído!")

async def analise():
    print("Iniciando análise de dados...  ")
    await asyncio.sleep(5)
    print("Análise de dados concluída! ")

async def main():
    gather1 = asyncio.gather(download(), analise())
    await gather1

asyncio.run(main())