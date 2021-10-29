import discord
from discord.ext import commands


class Talks(commands.Cog):
    """ Works with talks """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="oi", help="Envia um oi. Não requer argumento.")
    async def send_hello(self, ctx):
        name = ctx.author.name
        response = "Olá, " + name

        await ctx.send(response)

    @commands.command(name="segredo", help="Envia um segredo no privado. Não requer argumento.")
    async def secret(self, ctx):

        try:
            await ctx.author.send("Olá, eu sou um robo feito pelo Penido :)")
            await ctx.author.send("Se você tiver qualquer sugestão de manutenção ou uma nova funcionalidade, será super bem vindo!")
            await ctx.author.send("Mande sua mensagem para o meu criador, o LePenidon#8405")
        except discord.errors.Forbidden:
            await ctx.send(f"Não posso te contar o segredo, {ctx.author.name} :(")
            await ctx.send("Habilite em: (Opções > Privacidade)")

        await ctx.message.delete()

    @commands.command(name="calcII", help="Envia as informações de Cálculo II. Não requer argumento.")
    async def calc_II(self, ctx):

        await ctx.send("Link Aula: https://meet.google.com/skg-brgb-pct?hs=122&authuser=0")
        await ctx.send("Link Monitoria: https://meet.google.com/mcy-hrct-hgb?authuser=1")


def setup(bot):
    bot.add_cog(Talks(bot))
