from disnake import Embed
from disnake.ext.commands import Context as _Context

import config


class Context(_Context):

    def embed(*arg, **kwargs):
        kwargs.setdefault('colour', config.Branding.Сolours.main)
        return Embed(*arg, **kwargs)