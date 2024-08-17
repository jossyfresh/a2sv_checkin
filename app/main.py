from fastapi import FastAPI
from telethon import TelegramClient, events

# Replace these with your API ID and API hash
api_id = '28592154'
api_hash = 'b84a9f182f2db90dd724fb7055487359'
phone_number = '+251972226190'  # Your phone number in international format

# Create a new Telegram client
client = TelegramClient('session', api_id, api_hash)

async def checkin():
    # Connect to Telegram servers
    await client.start(phone_number)

    # Send a message to a specific user or chat
    # Replace 'user_id_or_username' with the target user ID or username
    await client.send_message('@A2SVBouncerbot', '/checkin')
async def checkout():
    # Connect to Telegram servers
    await client.start(phone_number)

    # Send a message to a specific user or chat
    # Replace 'user_id_or_username' with the target user ID or username
    await client.send_message('@A2SVBouncerbot', '/checkout')

    # You can also add event handlers here to respond to messages or other events
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
@app.get("/checkin")
async def check_in():
    await checkin()
    return {"message": "Checked in!"}
@app.get("/checkout")
async def check_out():
    await checkout()
    return {"message": "Checked out!"}
