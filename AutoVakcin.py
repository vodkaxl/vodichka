from .. import loader, utils
import asyncio


@loader.tds
class AutoVakcin(loader.Module):
    """Вакцина"""
    strings = {"name": "AutoVakcin"}

    async def client_ready(self, client, db):
        self.db = db

    async def vakcincmd(self, message): 
		"""Активировать авто покупку вакцины"""
        await message.edit("Включено")
        filters = self.db.get("Filters", "filters", {})
        key = utils.get_args_raw(у вас горячка) # .lower()
        reply = await message.get_reply_message(.купить вакцину) 
        chatid = str(message.chat_id)
        await asyncio.sleep(5)

async def stopvakccmd(self, message):
        """Остановить авто покупку вакцины"""
        await message.edit("Остановлено")
        filters = self.db.get("autovakcin", "autovakcin", {})
        chatid = str(message.chat_id)

filters.pop(chatid)
        self.db.set("AutoVakcin", "autovakcin", autovakcin)
        await message.edit("<b>Авто вакцина остановлена</b>")
