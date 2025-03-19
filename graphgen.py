import os

import discord
from matplotlib import pyplot as plt
import numpy as np

from constants import GRAPH_IMAGE_LOCATION, START_TIME

async def grab_graph(ctx: discord.ApplicationContext) -> None:
    # get time
    time_delta = START_TIME - ctx.message.created_at
    minutes = time_delta.total_seconds() // 60

    # Sanity Checks
    if minutes <= 0:
        await ctx.respond("Stocks not yet available for SBFA", ephemeral=True)
        return
    if not os.path.exists(GRAPH_IMAGE_LOCATION):
        os.mkdir(GRAPH_IMAGE_LOCATION)

    # Open and Send File
    try:
        with open(os.path.join(GRAPH_IMAGE_LOCATION, f"{minutes}.png"), "rb") as pic:
            await ctx.respond(file=discord.File(pic, f"{minutes}.png"))
    except FileNotFoundError:
        await create_graph_image(minutes)


async def create_graph_image(minutes_elapsed: int) -> None:
    pass