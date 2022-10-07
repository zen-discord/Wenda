from disnake import Embed
from disnake.ext.commands import Context as _Context

import config


class Context(_Context):
    @staticmethod
    def embed(**kwargs) -> Embed:
        kwargs.setdefault("colour", config.Branding.colours.main)
        return Embed(**kwargs)

    @staticmethod
    def error(title: str, message: str) -> str:
        return f"**⚠ {title}**\n{message}"
