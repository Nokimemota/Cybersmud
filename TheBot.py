import discord
import os
from discord.commands import slash_command
from discord.ext import commands

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.slash_command(guild_ids = [913475950786793493])
async def close(ctx):
    """Command that turns the bot off"""
    await ctx.send("Goodbye! Turning off now...")
    await ctx.bot.close()

@bot.message_command(guild_ids = [913475950786793493], name="Show ID")  # creates a global message command
async def show_id(ctx, message: discord.Message):  # message commands return the message
    await ctx.respond(f"{ctx.author.name}, here's the message id: {message.id}!")



initial_extensions = []

for filename in os.listdir('./cogs'): 
    if filename.endswith('.py'):
        initial_extensions.append("cogs."+filename[:-3])

print(initial_extensions)
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


bot.run('OTEzNDc3NDMyMjk4ODUyNDIy.YZ_EJw.nQa6vFdQSXEtw5FjwLVhdoUP7HQ')