import asyncio, httpx

async def get_json(url: str):
    async with httpx.AsyncClient(timeout=10.0) as c:
        r = await c.get(url); r.raise_for_status(); return r.json()

async def main():
    data = await get_json("https://jsonplaceholder.typicode.com/todos/1")
    print(data)

asyncio.run(main())
