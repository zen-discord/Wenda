from traceback import format_exc
from typing import Union

from aiohttp import ClientSession
from disnake.ext.commands import AutoShardedBot
from disnake import utils

from context import Context
from log import Logger


class DiscordBot(AutoShardedBot):
    def __init__(
        self, http_session: ClientSession, bot_config, logger: Logger, **kwargs
    ) -> None:
        self.session = http_session
        self.config = bot_config
        self.log = logger
        self.ctx = Context
        self.ready_at_once: bool = False
        self.guilds_on_startup: Union[None, int] = None
        super().__init__(**kwargs)

    async def __aenter__(self):
        self.load_all_extensions(["applications", "internal"], ["jishaku"])
        return super()

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.session.close()
        self.log.info("Bye-bye!")

    async def on_ready(self) -> None:
        if not self.ready_at_once:
            self.guilds_on_startup = len(self.guilds)
            self.ready_at_once = True
            self.log.info("Bot is ready to work")

    async def on_connect(self) -> None:
        self.log.info("Connected to Discord API")

    async def get_context(self, message, cls=None) -> Context:
        return await super().get_context(message, cls=Context)

    def load_all_extensions(self, paths: list, custom: list) -> None:
        total = 0
        loaded = 0

        for path in paths:
            for module in utils.search_directory(path):
                total += 1
                try:
                    self.load_extension(module)
                    loaded += 1
                except (Exception,):
                    self.log.error(format_exc())
                    continue

        for module in custom:
            total += 1
            try:
                self.load_extension(module)
                loaded += 1
            except (Exception,):
                self.log.error(format_exc())
                continue

        self.log.info(f"Loaded {loaded} out of {total} modules")
