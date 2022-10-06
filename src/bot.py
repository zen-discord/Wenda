from typing import Union

from aiohttp import ClientSession
from disnake.ext.commands import AutoShardedBot

import src


class DiscordBot(AutoShardedBot):
    def __init__(self, bot_session: ClientSession, bot_config, **kwargs) -> None:
        self.session = bot_session
        self.config = bot_config
        self.log = ...
        self.ready_at_once: bool = False
        self.guilds_on_startup: Union[None, int] = None
        super().__init__(**kwargs)

    async def __aenter__(self) -> src.instance:
        self.load_all_extensions()
        return super()

    async def __aexit__(self) -> None:
        await self.session.close()
        self.log.info("Bye bye")

    async def on_ready(self) -> None:
        if not self.ready_at_once:
            self.guilds_on_startup = len(self.guilds)
            self.ready_at_once = True
            self.log.info("Bot is ready to work")

    async def on_connect(self) -> None:
        self.log.info("Connected to Discord API")

    def load_all_extensions(self) -> None:
        pass
