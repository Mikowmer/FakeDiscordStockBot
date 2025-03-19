import discord
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!\ntest")

@bot.slash_command(name="plotgraph", description="Plot a graph")
async def plotgraph(ctx: discord.ApplicationContext):
    await ctx.send_response("Plotting graph...")
    await ctx.send_followup("https://en.wikipedia.org/wiki/File:Trollface.png")

bot.run(os.getenv('TOKEN')) # run the bot with the token