from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
@bot.command()
async def うんち(ctx):
    await ctx.send(':poop:')

    
    
 @role.command(
        name="set",
        pass_context=True
    )
    async def set_role(self, ctx: commands.Context, *roles: discord.Role):
        """
      
        /role set 
        """
        if not roles:
            raise commands.BadArgument()

        user = ctx.message.author
        await self.bot.add_roles(user, *roles)
        await self.bot.say("役職を追加しました。")



bot.run(token)
