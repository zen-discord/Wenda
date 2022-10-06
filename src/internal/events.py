from disnake import Guild
from disnake.ext.commands import Cog

import src


class Events(Cog):
    def __init__(self, bot: src.instance) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_guild_join(self, guild: Guild):
        embed = self.bot.context.embed() # пока что в пизду...


def setup(bot: src.instance):
    bot.add_cog(Events(bot))
