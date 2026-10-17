import asyncio, json, os, websockets
from dotenv import load_dotenv
print ("hello")
load_dotenv()
API_KEY = os.getenv("AISSTREAM_API_KEY")

async def connect():
    async with websockets.connect("wss://stream.aisstream.io/v0/stream") as ws:
        subscribe_msg = { 
            "APIKey" : API_KEY,
            "BoundingBoxes": [[[41.30, 2.10], [41.45,2.30]]]
        }
        await ws.send(json.dumps(subscribe_msg))
        async for message in ws:
            if isinstance(message, bytes):
                message = message.decode("utf-8")
            print(message)

if __name__ == "__main__":
    asyncio.run(connect())
