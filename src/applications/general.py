from disnake import CommandInteraction
from disnake.ext.commands import Cog, slash_command

import src


class General(Cog):
    def __init__(self, bot: src.instance) -> None:
        self.bot = bot

    @slash_command()
    async def ping(self, interaction: CommandInteraction) -> None:
        await interaction.response.send_message(
            f"🏓 `{round(self.bot.latency * 1000, 2)}ms`"
        )


def setup(bot: src.instance):
    bot.add_cog(General(bot))
