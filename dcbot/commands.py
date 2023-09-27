import sqlite as database

from discord import Client
import time
from datetime import datetime
from typing import Optional

async def run(client: Client):
    @client.command(name="songs")
    async def songs(ctx, amount: Optional[str]):
        #Checks if "amount" parameter has something in it
        if amount:
            try:
                amount = int(amount)
            except ValueError:
                pass

        if isinstance(amount, int):
            conn = database.sqlite3.connect('songlist.db')
            response = database.get_latest_songs(conn, amount)
            #Formatting response so it looks clean as Discord message
            formatted_response = [f"{song} | <t:{int(time.mktime(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').timetuple()))}> | **Requested by: **{requester}" for _, song, requester, timestamp in response]
            formatted_response = "\n".join(formatted_response)
            await ctx.send(formatted_response)
        else:
            conn = database.sqlite3.connect('songlist.db')
            response = database.get_songs_last_day(conn)

            formatted_response = [f"{song} | <t:{int(time.mktime(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').timetuple()))}> | **Requested by: **{requester}" for _, song, requester, timestamp in response]
            formatted_response = "\n".join(formatted_response)
            await ctx.send(formatted_response)
