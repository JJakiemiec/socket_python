import asyncio

HOST = "127.0.0.1"
PORT = 45451


async def client():
    print("connecting to host...")
    reader, writer = await asyncio.open_connection(HOST, PORT)

    message = input("Enter message:")
    print(f"send: {message}")
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"Recieved: {data.decode()}")

    print("close the connection")
    writer.close()
    await writer.wait_closed()


asyncio.run(client())