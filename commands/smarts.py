from discord.ext import commands
import wolframalpha
from decouple import config

wf_id = config("WF_TOKEN")


class Smarts(commands.Cog):
    """ A lot of Smart Commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wf", help="Pesquisa no Wolfram Alpha. Requer uma expressão como argumento.")
    async def wolfram_alpha(self, ctx, *arguments):
        try:
            client = wolframalpha.Client(wf_id)
            question = ''.join(arguments)

            res = client.query(question)
            answer = next(res.results).text

            await ctx.send(answer)

        except Exception:
            await ctx.send(f"Não foi possível achar um resultado para essa expressão.")


def setup(bot):
    bot.add_cog(Smarts(bot))
