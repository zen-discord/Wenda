from typing import Union

from datetime import timedelta
from humanize import naturaldelta
from disnake.ui import View
from disnake.ui import button as _button
from disnake.ui import Button as _Button
from disnake import (
    Member,
    Forbidden,
    HTTPException,
    User,
    Button,
    MessageInteraction,
    CommandInteraction,
)
from disnake.ext.commands import (
    Cog,
    has_permissions,
    bot_has_permissions,
    user_command,
    guild_only,
)

import src


class Moderation(Cog):
    def __init__(self, bot: src.instance):
        self.bot = bot

    def parse_date(self, date):
        values = {"s": 1, "m": 60, "h": 60 * 60, "d": 24 * 60 * 60}
        if date[-1] not in values or not date[: len(date) - 1].isnumeric():
            return None
        return int(date[: len(date) - 1]) * values[date[-1]]

    @user_command(name="Управлять")
    @has_permissions(manage_nicknames=True)
    @bot_has_permissions(manage_nicknames=True)
    @guild_only()
    async def control(self, inter: CommandInteraction, target: Member) -> None:
        class ControlMenu(View):
            def __init__(self):
                super().__init__()
                self.add_item(
                    _Button(
                        label=f"Доступные действия для {str(target)}:",
                        disabled=True,
                        row=0,
                    )
                )

            if inter.author.guild_permissions.moderate_members:

                @_button(label="Тайм-аут", row=1, emoji="🔇")
                async def timeout_user(
                    self, button: Button, interaction: MessageInteraction
                ) -> None:
                    pass

            if inter.author.guild_permissions.manage_messages:

                @_button(label="Очистить сообщения", row=1, emoji="🚯")
                async def delete_user_messages(
                    self, button: Button, interaction: MessageInteraction
                ) -> None:
                    pass

            if inter.author.guild_permissions.kick_members:

                @_button(label="Выгнать", row=1, emoji="❌")
                async def kick_member(
                    self, button: Button, interaction: MessageInteraction
                ) -> None:
                    pass

            if inter.author.guild_permissions.ban_members:

                @_button(label="Забанить", row=1, emoji="🔨")
                async def ban_member(
                    self, button: Button, interaction: MessageInteraction
                ) -> None:
                    pass

            @_button(label="Изменить никнейм", row=2, emoji="✏")
            async def edit_nickname(
                self, button: Button, interaction: MessageInteraction
            ) -> None:
                pass

            if inter.author.guild_permissions.manage_channels:

                @_button(label="Закрыть чат для этого пользователя", row=2, emoji="🚷")
                async def close_chat_for_this_user(
                    self, button: Button, interaction: MessageInteraction
                ) -> None:
                    pass

        await inter.response.send_message(view=ControlMenu())


def setup(bot: src.instance):
    bot.add_cog(Moderation(bot))
