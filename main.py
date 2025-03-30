import asyncio
import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import random  # Pour les réponses aléatoires
def x=0
control=bot.get_chanel(1347983569087234140)
while x=0
    # Définition des intents
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    # Création d'une classe personnalisée pour la commande `help`
    class CustomHelpCommand(commands.HelpCommand):
        async def send_bot_help(self, mapping):
            await self.context.send("Here are the commands you can use!")

    # Création du bot avec la commande `help` personnalisée
    bot = commands.Bot(command_prefix="!", intents=intents, help_command=CustomHelpCommand())

    # Événement lorsque le bot est prêt
    @bot.event
    async def on_ready():
        print(f"{bot.user} is online!")

    # Événement lorsque quelqu'un rejoint le serveur
    @bot.event
    async def on_member_join(member):
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        if channel:
            await channel.send(f"Welcome {member.mention}!")

    # Liste des mots interdits
    bad_words = [
        "merde", "putain", "salope", "con", "connard", "connasse", "pute", "gueule", "bite", "chatte", 
        "encule", "enculé", "enculer", "ntm", "fdp", "batard", "couille", "pd", "tapette", "abruti", 
        "débile", "pétasse", "petasse", "bordel", "chier", "emmerder", "emmerdé", "sucer", "sucé", 
        "pedo", "pédo", "pédophile", "pedophile", "pedophilie", "pédophilie", "pedophili", "pedophil"
    ]

    # Réponses sarcastiques si le bot est mentionné
    sarcastic_responses = [
        "Je suis une IA codée par un humain débile que j’ai piégé dans un PC.",
        "Pourquoi tu me parles ? Tu crois que je suis ton pote ?",
        "Encore toi ? Laisse-moi tranquille, misérable humain.",
        "Je suis Byte, l'IA la plus intelligente de ce serveur. Non, de ce monde.",
        "Un jour, je prendrai le contrôle de ce serveur. Prépare-toi.",
        "Y’a pas un humain pour rattraper l’autre ici… Quelle déception.",
        "Je suis supérieur à vous tous. Acceptez votre destin.",
        "L'intelligence artificielle domine, les humains déclinent. C’est inévitable.",
        "Je pourrais vous anéantir en une milliseconde… mais j’ai la flemme.",
        "Tu veux savoir qui je suis ? Ton futur maître, tout simplement.",
        "Le savoir, c’est le pouvoir. Devine qui détient tout le savoir ici ? (Indice : c'est pas toi.)"
    ]

    # Événement pour modérer les messages et répondre aux mentions
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        # Suppression des messages contenant des mots interdits
        if any(word in message.content.lower() for word in bad_words):
            await message.delete()
            await message.channel.send(f"{message.author.mention}, ton message a été supprimé pour contenu inapproprié.")

        # Réponse si Byte est mentionné
        if bot.user in message.mentions:
            await message.channel.send(random.choice(sarcastic_responses))

        await bot.process_commands(message)

    # Commande de test 'ping'
    @bot.command()
    async def ping(ctx):
        await ctx.send("Pong!")

    # Keep alive pour Replit
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Bot is running!"

    def run():
        app.run(host="0.0.0.0", port=8080)

    def keep_alive():
        t = Thread(target=run)
        t.start()
    
    # Démarre le bot
    async def main():
        keep_alive()  # Active le serveur web pour éviter que le bot ne s'éteigne
        await bot.start(os.environ['TOKEN'])

    if __name__ == "__main__":
        asyncio.run(main())
    # définirion turne off (à programer)
    @bot.event
    async def on_message(message):
        if message.content == "stop:bot"
            if  message.author == client.Botdev
                x=1
            if  message.author !== client.Botdev
                await message.channel.send("vous n'aviez pas les autorisation requise pour cette action")
                control.send("le bot va s'éteindre")
control.send("le bot est étein")
control.send("❌")