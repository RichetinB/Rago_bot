import discord
from discord.ext import commands
from discord import app_commands
import json
import requests

with open('config.json', 'r') as f:
    config = json.load(f)
    bot_token = config['token']
    api_base_url = config['api_base_url']
    
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


@bot.tree.command(name="choose_role")
async def choose_role(interaction: discord.Interaction, role: str):
    roles = ['adc', 'support', 'mid', 'jungle', 'top']
    if role.lower() in roles:
        try:
            response = requests.get(f"{api_base_url}/champions/role={role.lower()}/random")
            champion = response.json()
            await interaction.response.send_message(f"Ton champion aléatoire pour le rôle {role} est {champion['name']}")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération du champion: {e}")            
            await interaction.response.send_message("Une erreur s'est produite. Veuillez réessayer plus tard.")
    else:
        await interaction.response.send_message("Rôle invalide. Choisis parmi adc, support, mid, jungle ou top.")



# @bot.tree.command(name="create_team")
# async def create_team(interaction: discord.Interaction):

    
#         response = requests.get(f"{api_base_url}/champions/get_team")
#         champion = response.json()

        
    
#         team_message = f"Composition de l'équipe :\n  {champion}"
        

#         await interaction.response.send_message(team_message)

@bot.tree.command(name="create_team")
async def create_team(interaction: discord.Interaction):
    try:
        response = requests.get(f"{api_base_url}/champions/get_team")
        teams = response.json()

        blue_side_champions = teams.get("blue_side", [])
        red_side_champions = teams.get("red_side", [])

        message = ""

        if blue_side_champions:
            message += "Composition de l'équipe (Blue Side):\n"
            for champion in blue_side_champions:
                # roles = ['top', 'jungle', 'mid', 'adc', 'support']
                message += f"{champion['name']}\n"
            message += "\n"

        if red_side_champions:
            message += "Composition de l'équipe (Red Side):\n"
            for champion in red_side_champions:
                # roles = ['top', 'jungle', 'mid', 'adc', 'support']
                message += f"{champion['name']}\n"
            message += "\n"

        if message:
            await interaction.response.send_message(message)
        else:
            await interaction.response.send_message("Aucun champion trouvé pour l'équipe Blue Side et Red Side.")

    except Exception as e:
        error_message = "Une erreur s'est produite lors de la création de l'équipe. Veuillez réessayer plus tard."
        print(f"Erreur lors de la récupération de l'équipe : {e}")
        await interaction.response.send_message(error_message)




bot.run(bot_token)
