from disnake import Activity, ActivityType, Status, Colour


class Tokens:
    bot = "токен"


class Branding: # do not change this
    name = "Wenda"
    description = "Приветствую, Я - Wenda. Меня интересует возможность более комфортного пребывания на Discord-серверах."

    class Colours:
        main = Colour.magenta()


environ = {
    "JISHAKU_NO_UNDERSCORE": "1",
    "JISHAKU_NO_DM_TRACEBACK": "1",
    "JISHAKU_HIDE": "1",
    "JISHAKU_FORCE_PAGINATOR": "1",
}
owner_ids = [0000000000000000000]  # your user id in discord
channels = {
    "guilds": 0000000000000000000,  # channel id where will be guild logs
    "bugs": 0000000000000000000,  # channel id where will be bugs
    "errors": 0000000000000000000  # channel id where will be errors of the bot
}
activity = Activity(type=ActivityType.listening, name="/help")
status = Status.dnd
