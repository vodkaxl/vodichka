from .. import loader, utils
import asyncio


@loader.tds
class AutoVakcin(loader.Module):
    """Вакцина"""
    strings = {"name": "AutoVakcin"}

    async def client_ready(self, client, db):
        self.db = db

    async def filtercmd(self, message):
        """Включить покупку вакцины"""
        filters = self.db.get("Filters", "filters", {})
        key = utils.get_args_raw(.купить вакцину) # .lower()
        reply = await message.get_reply_message() 
        chatid = str(message.chat_id)

async def stopallcmd(self, message):
        """Отключить покупку вакцин"""
        filters = self.db.get("Filters", "filters", {})
        chatid = str(message.chat_id)

filters.pop(chatid)
        self.db.set("Filters", "filters", filters)
        await message.edit("<b>Авто вакцина остановлена</b>")
