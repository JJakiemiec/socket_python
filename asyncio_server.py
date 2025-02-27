import asyncio

HOST = "127.0.0.1"
PORT = 45451

connection_list = list()

async def connection(reader, writer):
    addr = writer.get_extra_info("peername")

    print(f"new connection {addr}...")
    data = await reader.read(100)
    message = data.decode()
    print(f"Recieved: {message}")


    print(f"sending thanks to {addr}...")
    thanks = f"thank you for sending '{message}'"
    writer.write(thanks.encode())
    await writer.drain()

    print(f"closing connection {addr}...")
    writer.close()
    await writer.wait_closed()


async def server():
    print("waiting for connection...")
    server = await asyncio.start_server(connection, host=HOST, port=PORT)
    

    async with server:
        await server.serve_forever()


asyncio.run(server())