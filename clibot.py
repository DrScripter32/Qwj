from pyrogram import Client , filters



ah="b911e7836be5cbdc8688fa3d1269d377"
ai=9808879
print("startimg")
app = Client("acc",api_hash=ah,api_id=ai)
print("okeb")
#ch_id =1268460826
ch_id=-1001848523322
ch_us= "prrofile_purple"

txt= """
♨️ کانفیگ - v2ray -

"""

@app.on_message(filters.channel)
async def main(client,message):

	if message.chat.username == ch_us:
		print("okeb")
		print(message.text)
		pm = message.text
		if "vmess://" in pm:
			print("is vmess proxy")
			proxy = pm.split("\n")
			for i in proxy:
				if "vmess//" in i:
					i=r" ` "+i+r" `"
					i=txt+i+"\n#con\n•┣ ID : @ZeroDayProxy"
					i=i.replace("prrofile_purple","new")
					await app.send_message(chat_id="KernalError",text=str(i))
		elif "vless://" in pm:
			print("is vless proxy")
			proxy = pm.split("\n")
			for i in proxy:
				if "vless://" in i:
					i=r" ` "+i+r" `"
					i=txt+i+"\n#con\n•┣ ID : @ZeroDayProxy"
					i=i.replace("prrofile_purple","new")
					await app.send_message(chat_id="KernalError",text=str(i))
					
			
			
		elif "trojan://" in pm:
			print("is trojan proxy")
			proxy = pm.split("\n")
			for i in proxy:
				if "trojan//" in i:
					i=r" ` "+i+r" `"
					i=txt+i+"\n#con\n•┣ ID : @ZeroDayProxy"
					i=i.replace("prrofile_purple","new")
					await app.send_message(chat_id="KernalError",text=str(i))
		elif "ss://" in pm:
			print("is ss proxy")
			proxy = pm.split("\n")
			for i in proxy:
				if "ss://" in i:
					i=r" ` "+i+r" `"
					i=txt+i+"\n#con\n•┣ ID : @ZeroDayProxy"
					i=i.replace("prrofile_purple","new")
					await app.send_message(chat_id="KernalError",text=str(i))
	
app.run()

