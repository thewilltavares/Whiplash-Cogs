from redbot.core.bot import Red
from .userinfo import UserInfo

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)

async def setup(bot: Red):
    cog = UserInfo()
    bot.add_cog(cog)
    await cog.initialize()