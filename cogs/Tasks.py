import discord
from discord.ext import tasks, commands
from discord.commands import slash_command
from discord.commands import Option
import random

class ScheduleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.printer.start()

    @tasks.loop(seconds=30)
    async def printer(self):
        print(self.index)
        self.index +=1

    
                     
async def sendmsg(self, ctx, msg, rol, chan, jobid):
    msg=rol.mention+' '+msg
    await chan.send(msg)
    print('JobID: {} has sent the message'.format(jobid))

def setup(bot):
    bot.add_cog(ScheduleCog(bot))
