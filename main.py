import discord 
from discord.ext import commands
import asyncio
import os
from webserver import keep_alive


client = commands.Bot(command_prefix= "!")
client.remove_command("help")

@client.event
async def on_ready():
  print("Bot is online")

@client.command(pass_context = True)
async def help(ctx):
        author = ctx.message.author
        embed = discord.Embed(
          colour = discord.Colour.orange()
        )
        embed.set_author(name = "Help: ")
        embed.add_field(name = "!help", value = "Help command", inline = False)
        await client.send_message(author, embed=embed)
        await client.say("WOW")

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
