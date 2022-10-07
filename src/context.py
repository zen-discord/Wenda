from disnake import Embed
from disnake.ext.commands import Context as _Context

import config


class Context(_Context):
    def embed(*arg, **kwargs) -> Embed:
        kwargs.setdefault('colour', config.Branding.Сolours.main)
        return Embed(*arg, **kwargs)

    @staticmethod
    def error(title: str, message: str) -> str:
        return f"**⚠ {title}**\n{message}"
