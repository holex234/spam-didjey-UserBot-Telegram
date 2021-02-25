from asyncio import sleep
from .. import loader, utils

def register(cb):
	cb(ЗаёбушкаMod())
	
class ЗаёбушкаMod(loader.Module):
	"""диджей ебан"""
	strings = {'name': 'диджей'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
		
	async def диджcmd(self, message):
		"""дидж <колличество> <реплай на того, кого диджедить>"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("<b>А кого диджедить-то?</b>")
			return
		id = reply.from_id
		args = utils.get_args(message)
		count = 50
		if args:
			if args[0].isdigit():
				if int(args[0]) < 0:
					count = 50
				else:
					count = int(args[0])
		txt = '<a href="tg://user?id={}">{}</a>'
		await message.edit(txt.format(id, "ЕБАН БАН БАН БАН БАН ЕБББААННННН БАН БАН БАН БАН БАН"))
		for _ in range(count):
			await sleep(0.3)
			msg = await message.client.send_message(message.to_id, txt.format(id, "Диджей ЕБАН БАН БАН БАН!!!!"), reply_to=message)
			if not msg.is_reply:
				await msg.edit("<b>Остановлено хуйня!</b>")
				break
			await sleep(0.3)
			await msg.delete()
				
			