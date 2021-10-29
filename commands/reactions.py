from discord.ext import commands


class Reactions(commands.Cog):
    """ Works with Reaction """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "😀":
            role = user.guild.get_role(881266251270328402)
            await user.add_roles(role)
        elif reaction.emoji == "👺":
            role = user.guild.get_role(881266289291690035)
            await user.add_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot))
