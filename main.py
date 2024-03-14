import discord
from discord.ext import commands
from discord import app_commands
import json


with open('config.json', 'r') as f:
    config = json.load(f)
    bot_token = config['token']
    
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is Up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hey {interaction.user.mention}! This is a slash command', ephemeral=True)



bot.run(bot_token)
