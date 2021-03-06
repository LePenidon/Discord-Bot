from discord.ext import commands
import requests


class Cryptos(commands.Cog):
    """ Works with cryptocurrency """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="crypto", help="Verifica o preço de um par na binance. Argumentos: moeda, base.")
    async def cripto(self, ctx, coin, base):
        try:
            response = requests.get(
                f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")

            data = response.json()
            price = data.get("price")

            if price:
                await ctx.send(f"O valor do par {coin}/{base} é {price}")
            else:
                await ctx.send(f"O par {coin}/{base} é inválido!")
        except Exception as e:
            await ctx.send(f"Ops... Deu algum erro:\n{e}")


def setup(bot):
    bot.add_cog(Cryptos(bot))
