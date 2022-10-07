from disnake import Guild
from disnake.ext.commands import Cog

import src


# It's a cog that handles events
class Events(Cog):
    def __init__(self, bot: src.instance) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_guild_join(self, guild: Guild) -> None:
        embed = (
            self.bot.ctx.embed()
            .set_author(name="Бот был добавлен на сервер")
            .add_field(name="Название", value=guild.name)
            .add_field(name="Владелец", value=f"{guild.owner} ({guild.owner.id})")
            .add_field(
                name="Пользователей",
                value=f"Участников: {len(list(filter(lambda x: not x.bot, guild.members)))}"
                f"\nБотов: {len(list(filter(lambda x: x.bot, guild.members)))}",
            )
            .set_footer(text=f"Теперь у меня {len(self.bot.guilds)} • {guild.id}")
        )
        channel = self.bot.get_channel(self.bot.config.channels["guilds"])
        await channel.send(embed=embed)

    @Cog.listener()
    async def on_guild_remove(self, guild: Guild) -> None:
        embed = (
            self.bot.ctx.embed()
            .set_author(name="Бота убрали с сервера")
            .add_field(name="Название", value=guild.name)
            .set_footer(text=f"Теперь у меня {len(self.bot.guilds)} • {guild.id}")
        )
        channel = self.bot.get_channel(self.bot.config.channels["guilds"])
        await channel.send(embed=embed)


def setup(bot: src.instance):
    bot.add_cog(Events(bot))
