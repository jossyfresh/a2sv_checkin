from fastapi import FastAPI
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError, BotResponseTimeoutError
import asyncio

# Replace these with your API ID and API hash
api_id = '28592154'
api_hash = 'b84a9f182f2db90dd724fb7055487359'
phone_number = '+251972226190'  # Your phone number in international format

# Create a new Telegram client
client = TelegramClient('session', api_id, api_hash)

async def checkin():
    # Connect to Telegram servers
    await client.start(phone_number)

    # Send a message to the bot to initiate the check-in process
    await client.send_message('@A2SVBouncerbot', '/checkin')


    @client.on(events.NewMessage(from_users='@A2SVBouncerbot'))
    async def handler(event):
        message = event.message
        if message.buttons:
            # Find the button with "AASTU In Person" text and click it
            for row in message.buttons:
                for button in row:
                    if button.text == 'AASTU In Person':
                        await client(GetBotCallbackAnswerRequest(
                            peer=message.peer_id,
                            msg_id=message.id,
                            data=button.data
                        ))
                        print("Clicked 'AASTU In Person'")
                        return
        # Run the event handler

async def checkout():

    # Connect to Telegram servers
    await client.start(phone_number)

    # Send a message to the bot to initiate the checkout process
    await client.send_message('@A2SVBouncerbot', '/checkout')
    
    @client.on(events.NewMessage(from_users='@A2SVBouncerbot'))
    async def handler(event):
        message = event.message
        if message.buttons:
            # Find the button with "AASTU In Person" text and click it
            for row in message.buttons:
                for button in row:
                    if button.text == 'Check out':
                        await client(GetBotCallbackAnswerRequest(
                            peer=message.peer_id,
                            msg_id=message.id,
                            data=button.data
                        ))
                        print("Clicked 'AASTU In Person'")
                        return


# Initialize FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/checkin")
async def check_in():
    await checkin()
    return {"message": "Checked in!"}

@app.get("/checkout")
async def check_out():
    await checkout()
    return {"message": "Checked out!"}
