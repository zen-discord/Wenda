import sys

import asyncio
from aiohttp import ClientSession
from os import environ
from disnake import Intents
from disnake.ext.commands import when_mentioned_or

import src
import config
from bot import DiscordBot
from log import get_logger

sys.dont_write_bytecode = True
sys.path.insert(0, ".")


async def main():
    async with ClientSession() as session:
        for key, value in config.environ.items():
            environ[key] = value

        src.instance = DiscordBot(
            bot_config=config,
            http_session=session,
            logger=get_logger('bot'),
            intents=Intents.all(),
            max_messages=100,
            activity=config.activity,
            status=config.status,
            command_prefix=when_mentioned_or(),
            owner_ids=config.owner_ids,
        )

        async with src.instance as _bot:
            await _bot.start(config.Tokens.bot)


if __name__ == "__main__":
    asyncio.run(main())
