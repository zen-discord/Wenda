from disnake import Activity, ActivityType, Status, Colour


class Tokens:
    bot = "токен"


class Branding:  # do not change this
    name = "Wenda"
    description = "Я - Wenda. Меня интересует возможность более комфортного пребывания на Discord-серверах. Discord-бот, который может ответить на все потребности пользователей при поломке или ошибке - исправить все недочеты в случае возникновения проблем."
    compact_description = (
        "Discord-бот, который может ответить на все потребности пользователей"
    )
    english_description = "I am Wenda. I am interested in being more comfortable on Discord servers. Discord-bot that can answer all the needs of users in case of breakdown or error - to fix all the shortcomings in case of problems."
    english_compact_description = "Discord-bot that can answer all user needs"

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
    "errors": 0000000000000000000,  # channel id where will be errors of the bot
}
activity = Activity(type=ActivityType.listening, name="/help")
status = Status.dnd
