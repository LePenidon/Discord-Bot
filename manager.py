from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument


class Manage(commands.Cog):
    """ Manage the bot """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Estou pronto! Estou conectado como {self.bot.user}")
        # current_time.start()

    @commands.Cog.listener()
    async def on_message(self, message):
        palavrao = ['socorro', 'judas']

        if message.author == self.bot.user:
            return

        for i in palavrao:
            if i in message.content:
                await message.channel.send(
                    f"Por favor, {message.author.name}, não ofenda os demais usuários!"
                )

                await message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Favor enviar todos os argumentos. Digite !!help para entender melhor.")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Digite !!help para entender melhor.")
        else:
            raise error


def setup(bot):
    bot.add_cog(Manage(bot))
