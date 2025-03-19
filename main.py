import discord
import os # default module
from dotenv import load_dotenv

from graphgen import grab_graph

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
    try:
        await grab_graph(ctx)
    except Exception as e:
        await ctx.respond("ERROR ENCOUNTERED\n{}".format(e))

bot.run(os.getenv('TOKEN')) # run the bot with the token