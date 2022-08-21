# -*- coding: utf-8 -*-

# = = = = = = = = = = = = = = = = = = [ IMPORTED ] = = = = = = = = = = = = = = = = >

from __future__ import unicode_literals
from pyrogram import Client, filters
from pyrogram.types import Message
import time
from requests import get
import requests
import asyncio, random
import json
from pyrogram.types import InputPhoneContact
import os.path
import pyuseragents
import re
import os
import base64

# < = = = = = = = = = = = = = = = = = = = = [ CODE ] = = = = = = = = = = = = = >
Fosh = ["کص ننت","کونی","ننتو گاییدم","کص مادرت","کیرم لا پا ننت زجه نزن","ریدم ت کص مادرت","کص نصلت","ننت زیرمه خارجنده","کیرمی بصیک","بدو نبینمت خارجنده😂😂","کیرم ت کص مردع و زندت\nخارتو میگام زنازاده کیرم لا ممه ننت خارجنده حرومی کیرمو میدم دس ننت ننه فیشری ننه کیر دزد ننه حروم لقمه کیرم ت اولو اخرت کیروم ت قبر مردهات کیرم ت کون بابات ننتو عمودی میگام ننتو رو هوا میگام خارکصه","مادر زنازاده😂","هعیی ننتو گاییدم زجه بزن","توپ تانک فشفشه مادر تو کونکشه","ننتو ع کون گاییدم😂😂","ننتو انال گاییدم ","خارجنده ننت پیشمه","خبری از  خواهرت داری ؟ میدونی دارم میگامش ؟","کیر برع ت مادر کیر پرستت","هعی کص  ناموصت","زجه بزن درت بیارم😂😂","خار کیر دزد","ابجی بچه سالتو گاییدم😂😂","زیرمی زجه بزن","مادرتو یام یام کردم😂😂"]
req = requests.session()
platform = pyuseragents.random()
headers = {"content-type":"application/json","user-agent":platform}

#                          [ SET ADMIN ]                           #

admin = ("1469547340")

#                          [ SET LIST  ]	                       #

listsEnemy = []
lock = []

#                          [ SET PROXY ]                           #
proxy = {
	"scheme": "socks5",
	"hostname": "127.0.0.1",
	"port": 9050,
	"username": "",
	"password": ""
 }
app = Client('ER-STR',config_file="config.ini") 
print('----------------------------------------')
print('\033[37m======>.. \033[32m[  ER-STR  ]\033[37m ..<=======')
print('----------------------------------------')
print('\n\033[32mSuccessfully!\n\n\033[0m')

#                          [ BOT CODE ]                           #

@app.on_message(filters.me) 
async def Bot(c:Client, m:Message):
	try:

		user = await c.get_me()

		text = m.text

		chat_id = m.chat.id

		user_id = m.from_user.id

		message_id = m.message_id

		reply_id = m.reply_to_message_id

		reply_message = m.reply_to_message
		if text.startswith('.sethelp '):
			command = text.replace(".sethelp", "")
			open("Tools/SETHELP","w").write(command)
			await m.edit(f"𝘏𝘦𝘭𝘱 𝘚𝘦𝘵\n𝐶𝑜𝑚𝑚𝑎𝑛𝑑 => {command}")
		if text == ".help" or text == ".Help" or text == "Help" or text == "help":
			helpset = open("Tools/SETHELP").read()
			url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
			url2 = get("https://api.codebazan.ir/ping/?url=www.google.com").text
			await c.send_photo(chat_id,"Tools/video/4.jpg",caption=f"""
	𝐸𝑅-𝑆𝑇𝑅 __V1.0.0__ {helpset}

	**├** • **M**O**D**E** S**e**t**t**i**n**g**s** ↬ (`.mode`)
	**├** • **T**oo**l**s** ↬ (`.tools`)
	**├** • **E**N**E**`M`**Y** ↬ (`.Enemy`)
	**├** • **T**EX**T** ↬ (`.text`)

	 ᴹᵞ ᴵᴰ [{user.username}](http://t.me/{user.username})

	𝑃𝐼𝑁𝐺 ↬\t`{url2}`𝘔𝘴 | [{url['result']['time']}](http://t.me/{user.username})
""")
		if text == ".text" or text =="textmode" or text == "تکست":
			url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
			await m.edit(f"""
𝑇𝑒𝑥𝑡 𝐿𝑖𝑠𝑡 | [{url['result']['time']}](tg://openmessage?user_id={user.id})

┏━━━━━✦❘ 𝑋-𝑇𝑒𝑥𝑡 ❘✦━━━━━┓ 
┃𓇬╭────────────╼❥ 
┃𖢊├─⪧ `text1` ⇎ ( TEXT )
┃𖢊├─⪧ `text2` ⇎ 😂 TEXT 😐
┃𖢊├─⪧ `text3` ⇎ ▁▂▃ TEXT ▃▂▁
┃𖢊├─⪧ `text4` ⇎ ~ TEXT ~
┃𖢊├─⪧ `text5` ⇎ ' TEXT '
┃𖢊├─⪧ `text6` ⇎ 00:00:00 | TEXT
┃𓇬╰────────────╼❥ 
┗━━━━━✦❘༻꙳༺❘✦━━━━━┛
""")

		if text == ".mode" or text == "mode" or text == "مود":
			user = await c.get_me()
			url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
			await m.reply(f"""
	𝑀𝑂𝐷𝐸 S**e**T**T**i**N**g**S** | __[{url['result']['time']}](tg://openmessage?user_id={user.id})__

	├ • `.ti  	  | [on] [off] `
	├ • `.echo   | [on] [off] `
	├ • `.for    | [on] [off] `
	├ • `.copy 	 | [on] [off] `
	├ • `.Hyper  | [on] [off] `
	├ • `.kmode  | [on] [off] `
	├ • `.bold 	 | [on] [off] `
	├ • `.emoje  | [on] [off] `
	├ • `.reply  | [on] [off] `
	├ • `.lock   | [on] [off] `
	├ • `.tags   | [on] [off] `
	├ • `.mes 	  | [on] [off] `
	├ • `.setuser|`   [user]
	├ • `.emojes |`   [😐]
	├ • `.list   |`   **None**
	├ • `.clear  |`   **None**

	""",quote=True)
		if text == ".Enemy" or text == "Enemy" or text == "انمی":
			user = await c.get_me()
			url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
			await m.reply(f"""
	𝐸𝑛𝑒𝑚𝑦 S**e**T**T**i**N**g**S** ☠️ | __[{url['result']['time']}](tg://openmessage?user_id={user.id})__

	├ • `.enemy    | [on] [off] `
	├ • `.senemy   | [id] `
	├ • `.ListEnemy|`   **None**
	├ • `.delenemy |`   **None**
	├ • `.list     |`   **None**
	├ • `.clear    |`   **None**
	""",quote=True)
		if text == ".tools" or text == "tools" or text == "ابزار":
			user = await c.get_me()
			url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
			await m.reply(f"""
	𝒯ℴℴ𝓁𝓈 S**e**T**T**i**N**g**S** | __[{url['result']['time']}](tg://openmessage?user_id={user.id})__

	├ • `.sethelp  | [text]`
	├ •	`.openuser | [id]`
	├ • `.phishing | [site] `
	├ • `.b 	      | [username][Reply] `
	├ • `.un       | [username][Reply] `
	├ • `.ping     | [site] `
	├ • `.font     | [text] `
	├ • `.Shot     | [text] `
	├ • `.i        | [user] `
	├ • `.text     | [text] `
	├ • `.num      | [Number] `
	├ • `.card     | [Number Card] `
	├ • `.join     | [link] `
	├ • `.pin      | [username][Reply] `
	├ • `.upin     | [username][Reply] `
	├ • `.ban      | [username][Reply] `
	├ •	`.id       | [pv] `
	├ • `.v        | [text] `
	├ •	`.ip       | [ip] `
	├ •	`.setbio   | [bio] `
	├ •	`.bomber   | [912XXXXXXX] `
	├ • `.list     |`   **None**
	├ • `.clear    |`   **None**
	├ • `.date `
	├ • `.bio`
	├ • `.jok` 
	├ • `.FullHelp`	
	""",quote=True)


	#                      	   [  ER-STR  ]                           #
	#                          [ @EBLETSM ]                           #


		if text.startswith(".phishing "):
			url = json.loads(get(f"https://api.codebazan.ir/fishinfo/index.php?link={text.replace('.phishing','').strip()}").text)
			time.sleep(0.88)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n{url['t']} ➤ [+]")

		if text.startswith(".bio"):
			url = get("https://api.codebazan.ir/bio/").text
			time.sleep(0.88)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n`{url}` ➤ [+]")

		if text.startswith(".card"):
			url = json.loads(get(f"https://api.codebazan.ir/codemelli/?code={text.replace('.card','').strip()}").text)
			time.sleep(0.88)
			if url["Result"] == "The code is valid":
				URLR = "کد معتبر است . "
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n{URLR}")
			else: 
				URLR = "کد نامعتبر است . "
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n{URLR}")
		if text.startswith(".poll"):
			command = text.replace(".poll", "").strip()
			await c.send_poll(chat_id,command, [".",".",".","."])

		if text.startswith(".b "):
			await c.block_user(text.replace('.b','').strip())
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nBlock {text.replace('.b','').strip()}")

		if text.startswith("create") or text == "سازنده":
			await m.edit("𝙀𝙍-𝙎𝙏𝙍 𝑆𝐸𝐿𝐹-𝐵𝑂𝑇\n\n𝑀𝑦 𝑖𝑑 @EBLETSM\n𝑁𝑢𝑚𝑏𝑒𝑟: +989915052209\n")
			
		if text == ".b":
			await c.block_user(chat_id)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nBlock @{m.chat.username}")

		if text.startswith(".un "):
			await c.unblock_user(text.replace('.un','').strip())
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nUnBlock {text.replace('.un','').strip()}")


		elif text == ".un":
			await c.unblock_user(chat_id)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nUnBlock @{m.chat.username}")


		if text.startswith(".ping "):
			url = get(f"https://api.codebazan.ir/ping/?url=www.{text.replace('.ping','').strip()}").text
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nPING ➤ {url}")

		if text.startswith(".date"):
			for i in range(10):
				url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
				await m.edit(f"𝕮𝕴text**T**`i`**m**`e` ➤ **{url['result']['time']}**")
		elif text == ".i":
			try:
				url = await c.get_users(reply_message.from_user.username)
				if url.is_bot == False:
					bots = "USER"
				else:
					bots = "BOT"
				if url.is_fake == True:
					fake = "#FAKE"
				else:
					fake = "NOT FAKE"
				if url.is_scam == True:
					scam = "#SCAM"
				else:
					scam = "NOT SCAM"
				if url.status == "online":
					status = "#ONLINE"
				else:
					status = "#OFFLINE"
				await m.edit(f"""
**INF**__O__ **AC**O**__UNT__`S`

[+] **ID**  >_  `{url.id}`
[+] **USERNAME**  >_  ||@{url.username}||
[+] **ACC**O**__UN__`S`  >_  ||#{bots}||
[+] **NA**`ME`  >_  ||{url.first_name}||
[+] **FA**__KE__  >_  ||{fake}||
[+] **SC**`AM`  >_  ||{scam}||
[+] **STA**`TUS`  >_  ||{status}||
""")
			except:
				pass
		elif text == ".id":
			try:
				url = await c.get_users(chat_id)
				if url.is_bot == False:
					bots = "USER"
				else:
					bots = "BOT"
				if url.is_fake == True:
					fake = "#FAKE"
				else:
					fake = "NOT FAKE"
				if url.is_scam == True:
					scam = "#SCAM"
				else:
					scam = "NOT SCAM"
				if url.status == "online":
					status = "#ONLINE"
				else:
					status = "#OFFLINE"
				await m.edit(f"""
**INF**__O__ **AC**O**__UNT__`S`

[+] **ID**  >_  `{url.id}`
[+] **USERNAME**  >_  ||@{url.username}||
[+] **ACC**O**__UN__`S`  >_  ||#{bots}||
[+] **NA**`ME`  >_  ||{url.first_name}||
[+] **FA**__KE__  >_  ||{fake}||
[+] **SC**`AM`  >_  ||{scam}||
[+] **STA**`TUS`  >_  ||{status}||
""")	
			except:
				pass
		if text.startswith(".font "):
			url = get(f"https://api.codebazan.ir/font/?text={text.replace('.font','')}").json()
			await m.edit(f"\n".join(list(url["result"].values())[:110]))

		if text.startswith(".text "):
			time.sleep(0.88)
			await c.send_photo(chat_id, f"https://api.codebazan.ir/image/?type=texttopic&text={text.replace('.text','').strip()}",reply_to_message_id=message_id)

		if text.startswith(".Shot "):
			time.sleep(0.88)
			await c.send_photo(chat_id,f"https://api.otherapi.tk/carbon?type=create&code={text.replace('.Shot','').strip()}",reply_to_message_id=message_id)


		if text.startswith(".num "):
			url = json.loads(get(f"https://api.codebazan.ir/num/?num={text.replace('.num','').strip()}").text)
			await app.send_message(chat_id, f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n{url['result']['num']} ➤ [+]")


		if text.startswith(".v "):
			url = json.loads(get(f"https://api.codebazan.ir/vajehyab/?text={text.replace('.v','').strip()}").text)
			time.sleep(0.88)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n[+] Fa ➤ `{url['result']['fa']}`\n[+] En ➤ `{url['result']['en']}`\n[+] Mani ➤ `{url['result']['mani']}`\n[+] Fmoein ➤ `{url['result']['Fmoein']}`")

		if text.startswith(".ip "):
			url = json.loads(get(f"https://api.codebazan.ir/ipinfo/?ip={text.replace('.ip','').strip()}").text)
			time.sleep(0.88)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n[+] IP ➤ {url['ip']}\n[+] CITY ➤ {url['city']}\n[+] ISP ➤ {url['isp']}")


		if text.startswith(".join "):
			await c.join_chat(text.replace('.join','').strip())
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nJoin Group :)")

		if text.startswith(".c "):
			name_group = text.replace(".c", "")
			await c.create_group(name_group, text.replace('.c','c').strip())
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nCreated Group `{name_group}`")

		if text.startswith(".bomber"):
			number_spam = text.replace(".bomber","").strip()
			open("Tools/NumberSpam","w").write(number_spam)
			await m.edit("**𝕮𝕴**𝕻𝕳`𝕰𝕽-𝖃` ↴ \n**SPAM** `SMS` **RU**__N__...")
			try:
				for i in range(3):
						req.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",headers=headers,data=dumps({"cellphone": f"+98{number_spam}"}).encode())
						time(4)
						req.post("https://api.divar.ir/v5/auth/authenticate",headers=headers,data=dumps({"phone": f'0{number_spam}'}))
						time(4)
						req.post("https://www.sheypoor.com/api/v10.0.0/auth/send",headers=headers,data=dumps({"username":"0"+number_spam}))
						time(4)
						req.post("https://app.snapp-box.com/api/v2/auth/otp/send",headers=headers,data=dumps({"phoneNumber": "0"+number_spam}))
						time(4)
						req.post("https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",headers=headers,data=dumps({"UserName":"+98"+number_spam}).encode())
						time(4)
						req.post("https://api.toopmarket.com/api/v1/auth/login/number",headers=headers,data=dumps({"mobile":"0"+number_spam}))
						time(4)
						req.post("https://www.filimo.com/api/fa/v1/user/Authenticate/country_code",headers=headers,data=dumps({"mobile":"0"+number_spam,"guid":"ADB3488E-E512-E311-42FF-7EE1DE87F4FA"}).encode())
				await m.edit("𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n**SPAM** __D__`ONE`")
			except:
				print("ERROR SMS BOMBER")



		if text.startswith(".ban "):
			await c.ban_chat_member(chat_id, text.replace('.ban ','').strip())
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nBan Member @{reply_message.from_user.username}")

		elif text.startswith(".ban"):
			await c.ban_chat_member(chat_id, reply_message.from_user.username)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nBan Member @{reply_message.from_user.username}")
		if text == ".pin":
			await app.pin_chat_message(chat_id, reply_id)
			await m.edit("𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**P**`I`**N** `MESSAGE`")
		if text == ".upin":
			await app.unpin_chat_message(chat_id, reply_id)
			await m.edit("𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**UN**`PIN` **MESSAGE**")

		if os.path.exists("Tools/boldmode"):
			mode = open("Tools/boldmode").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"**{text}**")
		if text.startswith(".bold "):
			command = text.replace(".bold", "").strip()
			if command == "on"or"off":
				open("Tools/boldmode","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**Bold** **M**O**D**E `{command}`")

		if os.path.exists("Tools/TIMODE"):
			mode = open("Tools/TIMODE").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"__{text}__")
		if text.startswith(".ti "):
			command = text.replace(".ti", "").strip()
			if command == "on"or"off":
				open("Tools/TIMODE","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n__TI__ **M**O**D**E `{command}`")

		if text.startswith(".setuser "):
			command = text.replace(".setuser", "").strip()
			open("Tools/username","w").write(command)
			char = "on"if command == "on" else "off"
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**SET** __USERNAME__ ||{command}||")


		if os.path.exists("Tools/Kmode"):
			mode = open("Tools/Kmode").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"||{text}||")
		if text.startswith(".kmode "):
			command = text.replace(".kmode", "").strip()
			if command == "on"or"off":
				open("Tools/Kmode","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n||K||**MO**`DE` `{command}`")
		if text.startswith(".jok"):
			url = get("https://api.codebazan.ir/jok/").text
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n\n{url}")

		if text.startswith(".for "):
			command = text.replace(".for", "").strip()
			if command == "on"or"off":
				open("Tools/For","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**F**`O`__R__ **M**O**D**E `{command}`")
		if text.startswith(".vote "): 
			command = text.replcae(".vote","")
			await c.vote_poll(chat_id, reply_message, command)
			await m.edit(f"**YOU** __VOTE__ `LIST` ||{command}||")

		if os.path.exists("Tools/copy"):
			mode = open("Tools/copy").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"`{text}`")
		if text.startswith(".copy "):
			command = text.replace(".copy", "").strip()
			if command == "on"or"off":
				open("Tools/copy","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**CO**`PY` **M**O**D**E `{command}`")
		if os.path.exists("Tools/Hyper"):
			mode = open("Tools/Hyper").read()
		else: 
			mode = "off"
		if mode == "on":
			user = await c.get_me()
			await m.edit(f"[{text}](tg://openmessage?user_id={user.id})")
		if text.startswith(".Hyper "):
			command = text.replace(".Hyper", "").strip()
			if command == "on"or"off":
				open("Tools/Hyper","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n[Hyper](.chat) **M**O**D**E `{command}`")
		if os.path.exists("Tools/text1"):
			mode = open("Tools/text1").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"( {text} )")
		if text.startswith(".text1 "):
			command = text.replace(".text1", "").strip()
			if command == "on"or"off":
				open("Tools/text1","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n𝑇𝑒𝑥𝑡 1 **M**O**D**E `{command}`")

		if os.path.exists("Tools/text2"):
			mode = open("Tools/text2").read()
		else: 
			mode = "off"
		if mode == "on":
			emoji = ["😂","🗿","🔰","😑","👾","😐","🚶‍♂️"]
			await m.edit(f"{random.choice(emoji)} {text} {random.choice(emoji)}")
		if text.startswith(".text2 "):
			command = text.replace(".text2", "").strip()
			if command == "on"or"off":
				open("Tools/text2","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n𝑇𝑒𝑥𝑡 2 **M**O**D**E `{command}`")

		if os.path.exists("Tools/text3"):
			mode = open("Tools/text3").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"▁▂▃▄▅▆▇▉ {text} ▉▇▆▅▄▃▂▁")
		if text.startswith(".text3 "):
			command = text.replace(".text3", "").strip()
			if command == "on"or"off":
				open("Tools/text3","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n𝑇𝑒𝑥𝑡 3 **M**O**D**E `{command}`")

		if os.path.exists("Tools/text4"):
			mode = open("Tools/text4").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"~ {text} ~")
		if text.startswith(".text4 "):
			command = text.replace(".text4", "").strip()
			if command == "on"or"off":
				open("Tools/text4","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n𝑇𝑒𝑥𝑡 4 **M**O**D**E `{command}`")

		if os.path.exists("Tools/text5"):
			mode = open("Tools/text5").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"' {text} '")
		if text.startswith(".text5 "):
			command = text.replace(".text5", "").strip()
			if command == "on"or"off":
				open("Tools/text5","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n𝑇𝑒𝑥𝑡 5 **M**O**D**E `{command}`")
		if os.path.exists("Tools/text6"):
			mode = open("Tools/text6").read()
		else: 
			mode = "off"
		if mode == "on":
			url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
			await m.edit(f"__{url['result']['time']}__ | {text}")
		if text.startswith(".text6 "):
			command = text.replace(".text6", "").strip()
			if command == "on"or"off":
				open("Tools/text6","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n𝑇𝑒𝑥𝑡 6 **M**O**D**E `{command}`")						
		if text.startswith('.emojes '):
			command = text.replace('.emojes', '').strip()
			open("Tools/Emojes","w").write(command)
			await m.edit(f"**EMO**__JES__ `SET` **{command}**")

		if os.path.exists("Tools/Emoje"):
			mode = open("Tools/Emoje").read()
			emo = open("Tools/Emojes").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"{text} {emo}")
		if text.startswith(".emoje "):
			command = text.replace(".emoje", "").strip()
			if command == "on"or"off":
				open("Tools/Emoje","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**EMOJE** **M**O**D**E `{command}`")

		if os.path.exists("Tools/Tag"):
			mode = open("Tools/Tag").read()
		else: 
			mode = "off"
		if mode == "on":
			message = (text)
			s = re.sub(' ', '_',message)
			await m.edit(f"#{s}")

		if text.startswith(".tags "):
			command = text.replace(".tags", "").strip()
			if command == "on"or"off":
				open("Tools/Tag","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**TAG** **M**O**D**E `{command}`")


		if text.startswith(".lock "):
			command = m.text.replace(".lock", "").strip()
			if command == "on"or"off":
				open("Tools/lock","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n`L`**O**`CK` **M**O**D**E `{command} 🔐`")

		if text.startswith(".reply "):
			command = text.replace(".reply","").strip()
			if command == "on"or"off":
				open("Tools/reply","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n`RE`**P**`LY` **M**O**D**E `{command}` 🔐")

		if text.startswith(".delenemy"):
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**E**`N`**E**`M`**Y** `LI`**ST** `DELE`**TED** 👾 ➤ **{len(listsEnemy)}**")
			time.sleep(0.55)
			listsEnemy.clear()
			open("Tools/Enemy","w").write("off")
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**E**`N`**E**`M`**Y** `LI`**ST** `DELE`**TED** 👾 ➤ **{len(listsEnemy)}**")

		if text.startswith(".senemy "):
			command = text.replace(".senemy", "").strip()
			listsEnemy.append(command)
			open("Tools/Enemy","w").write("on")
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n𝐸𝑛𝑒𝑚𝑦 𝑈𝑠𝑒𝑟 ➤ `{command}` 👾")

		if text.startswith(".openuser "):
			command = text.replace(".openuser", "").strip()
			user = await c.get_users(command)
			link = "tg://openmessage?user_id="
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\nSuccessfully! ✅\n**LI**`NK` ➤ ||[CLICK]({link}{command})||")

		if text.startswith(".enemy "):
			command = text.replace(".enemy","").strip()
			if command == "on"or"off":
				open("Tools/Enemy","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n`En`**E**`My` **M**O**D**E `{command}` 👾 ")	

		if text.startswith(".mes "):
			command = text.replace(".mes","").strip()
			if command == "on"or"off":
				open("Tools/Message","w").write(command)
				open("Tools/ID","w").write(str(chat_id))
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**ME**SS**A**GE** **M**O**D**E `{command}` 🔰 ")	
		if text == "lolo" or text == "لولو":
			await m.edit("""
😐<><><><><><><><><><><><><><><><><><><><><><><>👻
""")
			time.sleep(0.07)
			await m.edit("""
😐<><><><><><><><><><><><><><><><><><><><>👻
		""")
			time.sleep(0.07)
			await m.edit("""
😐<><><><><><><><><><><><><><><><><>👻
		""")
			time.sleep(0.7)
			await m.edit("""
😐<><><><><><><><><><><><><><>👻
		""")

			time.sleep(0.07)
			await m.edit("""
😐<><><><><><><><><><><><👻
		""")
			time.sleep(0.07)
			await m.edit("""
😐<><><><><><><><><>👻
		""")
			time.sleep(0.7)
			await m.edit("""
😐<><><><><><>👻
""")	

			await m.edit("""
😐<><><>👻

		""")
			time.sleep(0.07)
			await m.edit("""
😐<>👻
		""")
			time.sleep(0.07)
			await m.edit("""
😲👻
		""")

		if text == "اپدیت" or text == "update":
			await m.edit("""
🟩 **10** %

		""")
			time.sleep(0.07)
			await m.edit("""
🟩🟩 **20** %	
		""")
			time.sleep(0.07)
			await m.edit("""
🟩🟩🟩 **30** %
		""")
			time.sleep(0.7)
			await m.edit("""
🟩🟩🟩🟩 **40** %
		""")

			time.sleep(0.07)
			await m.edit("""
🟩🟩🟩🟩🟩 **50** %
		""")
			time.sleep(0.07)
			await m.edit("""
🟩🟩🟩🟩🟩🟩 **60** %
		""")
			time.sleep(0.7)
			await m.edit("""
🟩🟩🟩🟩🟩🟩🟩 **70** %
		""")

			time.sleep(0.07)
			await m.edit("""
🟩🟩🟩🟩🟩🟩🟩🟩 **80** %	
		""")
			time.sleep(0.07)
			await m.edit("""
🟩🟩🟩🟩🟩🟩🟩🟩🟩 **90** %
		""")
			time.sleep(0.7)
			await m.edit("""
❗️ERROR, Update Failed❗️
		""")


		if "text".startswith(".setbio "):
			command = text.replace(".setbio", "").strip()
			await c.update_profile(bio=command)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\nSuccessfully! ✔️")
		if text.startswith(".clear"):
			a = open("Tools/Enemy","w").write("off")
			b = open("Tools/ListEnemy","w")
			c = open("Tools/lock","w").write("off")
			d = open("Tools/copy","w").write("off")
			e = open("Tools/boldmode","w").write("off")
			f = open("Tools/reply","w").write("off")
			g = open("Tools/TIMODE","w").write("off")
			h = open("Tools/Kmode","w").write("off")
			i = open("Tools/Echo","w").write("off")
			j = open("Tools/For","w").write("off")
			k = open("Tools/Hyper","w").write("off")
			l = open("Tools/Emoje","w").write("off")
			tags = open("Tools/Tag","w").write("off")
			text1 = open("Tools/text1","w").write("off")
			text2 = open("Tools/text2","w").write("off")
			text3 = open("Tools/text3","w").write("off")
			text4 = open("Tools/text4","w").write("off")
			text5 = open("Tools/text5","w").write("off")
			text6 = open("Tools/text6","w").write("off")
			await m.edit(f"""
	**AC**__T__`IO`[N](tg://openmessage?user_id=1469547340) **CL**`EA`**R**

	├ • **ENEMY** ➤ `off`
	├ • **LIST ENEMY** ➤ `DELE`**T**__E__**D**
	├ • **LOCK** ➤ `off`
	├ • **COPY** ➤ `off`
	├ • **BOLD** ➤ `off`
	├ • **REPLY** ➤ `off`
	├ • **TI MODE** ➤ `off`
	├ • **K MODE** ➤   `off`
	├ • **EC**`HO` ➤ 	`off`
	├ • **HY**__P__`ER` ➤ `off`
	├ • **F**`O`__R__ ➤ `off`
	├ • **EMO**JE** ➤ `off`
	├ • **TAGS** ➤ `off`
	├ • **TEXT** 1 ➤   `off`	
	├ • **TEXT** 2 ➤   `off`
	├ • **TEXT** 3 ➤   `off`
	├ • **TEXT** 4 ➤   `off`
	├ • **TEXT** 5 ➤   `off`
	├ • **TEXT** 6 ➤   `off`
	""")
		if text.startswith(".ListEnemy"):
			await m.edit(f"""
				𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴
				**Successfully**!
				𝔼𝕟𝕖𝕞𝕪 𝔽𝕚𝕟𝕕 ➤ ||{len(listsEnemy)}||
				""")
		if text.startswith(".FullHelp"):
			await m.edit("𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\nSuccessfully! ✔️\nPlease....")
			await c.send_document(chat_id, "Tools/HELP.txt",caption="__Files__ `HE`**LP**||ES||\n**Language** ↬ `Persian`")

		if text.startswith(".echo "):
			command = text.replace(".echo", "").strip()
			if command == "on"or"off":
				open("Tools/Echo","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**EC**`HO` **MO**__D__`E` `{command}`")

		if text.startswith(".list"):
			Enemy = open("Tools/Enemy").read()
			ListEnemy = open("Tools/ListEnemy").read()
			lock = open("Tools/lock").read()
			tag = open("Tools/copy").read()
			bold = open("Tools/boldmode").read()
			reply = open("Tools/reply").read()
			ti = open("Tools/TIMODE").read()
			Kmode = open("Tools/Kmode").read()
			Hyper = open("Tools/Hyper").read()
			echo = open("Tools/Echo").read()
			fOr = open("Tools/For").read()
			mes = open("Tools/Message").read()
			userreply = open("Tools/username").read()
			emojemode = open("Tools/Emoje").read()
			setemoje = open("Tools/Emojes").read()
			tags = open("Tools/Tag").read()
			text1 = open("Tools/text1").read()
			text2 = open("Tools/text2").read()
			text3 = open("Tools/text3").read()
			text4 = open("Tools/text4").read()
			text5 = open("Tools/text5").read()
			text6 = open("Tools/text6").read()
			await m.edit(f"""
	S**e**t**t**i**n**g**s** **AC**`TI`**O**`N`

	├ • **EN**`E`**M**`Y` ➤ `{Enemy}`
	├ • **LO**`CK` ➤     `{lock}`
	├ • **CO**`PY` ➤    `{tag}`
	├ • **Bo**`L`**D** ➤    `{bold}`
	├ • **R**`E`**P**`LY` ➤  `{reply}`
	├ • **TI**`MODE` ➤ `{ti}`
	├ • **K** `MODE` ➤ `{Kmode}`
	├ • **EC**`HO` ➤ 	  `{echo}`
	├ • **HY**__P__`ER` ➤ `{Hyper}`
	├ • **F**`O`__R__ ➤      `{fOr}`
	├ • **MES** ➤     `{mes}`
	├ • **EMO**JE** ➤`{emojemode}`
	├ • **TA**__GS__➤    `{tags}`
	├ • **User**__Re__`ply` ➤     **{userreply}**
	├ • **EMOJE** __SET__ ➤     **{setemoje}**
	├ • **TEXT** 1 ➤   `{text1}`	
	├ • **TEXT** 2 ➤   `{text2}`
	├ • **TEXT** 3 ➤   `{text3}`
	├ • **TEXT** 4 ➤   `{text4}`
	├ • **TEXT** 5 ➤   `{text5}`
	├ • **TEXT** 6 ➤   `{text6}`
	""")

	except:
		pass

@app.on_message(filters.private)
async def Enemy1(c:Client, m:Message):
	try:
		if os.path.exists("Tools/Enemy"):
			mode = open("Tools/Enemy").read()
		else:
			mode = "off"
		if mode == "on":
			try:
				for i in listsEnemy:
					user = m.from_user.id
					if user == int(i):
						await m.reply(random.choice(Fosh),quote=True)

			except:
				pass 
	except ValueError:
		open("Tools/Enemy","w").write("off")
		await c.send_message("me", f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**EN**`EM`**Y** **o**`f`**f**")
@app.on_message(filters.private)
async def Lock(c:Client, m:Message):
	try:
		if os.path.exists("Tools/lock"):
			mode = open("Tools/lock").read()
		else: 
			mode = "off"
		if mode == "on":
			print(m)
		if os.path.exists("Tools/Echo"):
			mode = open("Tools/Echo").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.copy(m.chat.id)
		if os.path.exists("Tools/For"):
			mode = open("Tools/For").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.forward(m.chat.id)
	except ValueError:
		print("LOCK ERROR")

@app.on_message()
async def Enemy(c:Client, m:Message):
	texts = m.text
	try:
		if os.path.exists("Tools/username"):
			user = open("Tools/username").read()
		if m.text == user:
			await c.send_video(m.chat.id, "Tools/video/1.mp4",reply_to_message_id=m.message_id)

		if os.path.exists("Tools/Enemy"):
			mode = open("Tools/Enemy").read()
		else:
			mode = "off"
		if mode == "on":
			try:
				for i in listsEnemy:
					user = m.from_user.id
					if user == int(i):
						await m.reply(random.choice(Fosh),quote=True)
			except:
				pass
	except ValueError:
		open("Tools/Enemy","w").write("off")
		await c.send_message("me", f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**EN**`EM`**Y** **o**`f`**f**")

@app.on_message() 
async def Messages(c:Client,m:Message):
	try:

		if os.path.exists("Tools/Message"):
			mode = open("Tools/Message").read()
		else: 
			mode = "off"
		if mode == "on":
			file = open("Tools/ID").read()
			inter = int(file)
			if m.chat.id == inter:
				print(f"\033[32m=====>\033[37m {m.text}\n")
	except:
		pass
app.run()
