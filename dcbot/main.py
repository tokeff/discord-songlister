import os
import asyncio
import sqlite as database

import discord
from dotenv import load_dotenv
from discord import Message
from discord.ext.commands import Bot
import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

async def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = Bot(intents=intents, command_prefix="!")


    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        await commands.run(client)


    @client.event
    async def on_message(message: Message):
        await client.process_commands(message)

        if message.author.id != 736888501026422855:
            return
        
        if not message.embeds:
            return
        #Getting song names from Discord music bot messages
        embed = message.embeds[0]
        title = embed.title

        if title.startswith("Playing: "): 
            songname = title.replace("Playing: ","")

            requester = embed.fields[0]
            requester_id = requester.value
        #adding songs to SQLite
            database.conn.execute("INSERT INTO songlist (name, requester) VALUES (?, ?)", (songname, requester_id))
            database.conn.commit()
            
    await client.login(TOKEN)
    await client.connect()

if __name__=="__main__":
    asyncio.run(main())