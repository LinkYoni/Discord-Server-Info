import requests
import os
import colorama
from colorama import Fore, Style
from datetime import datetime
from getpass import getpass
import shutil
import json

colorama.init()

def clear():
	os.system('cls')
clear()

with open('config.json', encoding="utf-8") as i:
    config = json.load(i)

token = config.get('token')

headers={"authorization": token,"content-type": "application/json"}

res = requests.get(f'https://discord.com/api/v9/users/@me', headers=headers)

default = ''' 
{0}{2}  ____{1}                             ___        __       
{0}{2} / ___|  ___ _ ____   _____ _ __{1}  |_ _|_ __  / _| ___  
{0}{2} \___ \ / _ \ '__\ \ / / _ \ '__|{1}  | || '_ \| |_ / _ \ 
{0}{2}  ___) |  __/ |   \ V /  __/ |{1}     | || | | |  _| (_) |
{0}{2} |____/ \___|_|    \_/ \___|_|{1}    |___|_| |_|_|  \___/ 

{4} Coded by {0}$ Yøni ⁶⁹ 🚬#0003{3}
'''.format(Fore.CYAN, Fore.RESET, Style.BRIGHT, Style.RESET_ALL, Fore.YELLOW) #default

correct = '''
{0}{2}  ____{1}                             ___        __       
{0}{2} / ___|  ___ _ ____   _____ _ __{1}  |_ _|_ __  / _| ___  
{0}{2} \___ \ / _ \ '__\ \ / / _ \ '__|{1}  | || '_ \| |_ / _ \ 
{0}{2}  ___) |  __/ |   \ V /  __/ |{1}     | || | | |  _| (_) |
{0}{2} |____/ \___|_|    \_/ \___|_|{1}    |___|_| |_|_|  \___/ 

{4} Coded by {0}$ Yøni ⁶⁹ 🚬#0003{3}
'''.format(Fore.GREEN, Fore.RESET, Style.BRIGHT, Style.RESET_ALL, Fore.YELLOW) #correct

fail = '''
{0}{2}  ____{1}                             ___        __       
{0}{2} / ___|  ___ _ ____   _____ _ __{1}  |_ _|_ __  / _| ___  
{0}{2} \___ \ / _ \ '__\ \ / / _ \ '__|{1}  | || '_ \| |_ / _ \ 
{0}{2}  ___) |  __/ |   \ V /  __/ |{1}     | || | | |  _| (_) |
{0}{2} |____/ \___|_|    \_/ \___|_|{1}    |___|_| |_|_|  \___/ 

{4} Coded by {0}$ Yøni ⁶⁹ 🚬#0003{3}
'''.format(Fore.RED, Fore.RESET, Style.BRIGHT, Style.RESET_ALL, Fore.YELLOW) #fail

default_txt = ''' 
  ____                             ___        __       
 / ___|  ___ _ ____   _____ _ __  |_ _|_ __  / _| ___  
 \___ \ / _ \ '__\ \ / / _ \ '__|  | || '_ \| |_ / _ \ 
  ___) |  __/ |   \ V /  __/ |     | || | | |  _| (_) |
 |____/ \___|_|    \_/ \___|_|    |___|_| |_|_|  \___/ 

 Coded by $ Yøni ⁶⁹ 🚬#0003

''' #default for txt

print(default)

if res.status_code == 200:

	input_id = input(f'{Fore.CYAN} [-] {Fore.RESET}ID: ')

	res = requests.get(f'https://discordapp.com/api/v9/guilds/{input_id}', headers=headers)
	res_json = res.json()

	if res.status_code == 200:
		clear()
		print(correct)

		res = requests.get(f'https://discord.com/api/v9/guilds/{input_id}', headers=headers)
		res_json = res.json()

		try:
			try:
				os.mkdir("Results")
			except:
				pass
			os.chdir("Results")

			#### INFO

			name = res_json['name']
			id = res_json['id']
			description = res_json['description']

			date = datetime.now()
			os.mkdir(f"{id}_{str(date.day)}-{str(date.month)}-{str(date.year)}_{str(date.hour)}.{str(date.minute)}.{str(date.second)}")
			directorio = (f"{id}_{str(date.day)}-{str(date.month)}-{str(date.year)}_{str(date.hour)}.{str(date.minute)}.{str(date.second)}")
			os.chdir(directorio)

			file = open('Info.txt', "w", encoding="utf-8")
			file.write(default_txt)

			owner_id = res_json['owner_id']
			res = requests.get(f'https://discordapp.com/api/v6/users/{owner_id}', headers=headers)
			res_json = res.json()
			owner = f"{res_json['username']}#{res_json['discriminator']}"
			res = requests.get(f'https://discord.com/api/v9/guilds/{input_id}', headers=headers)
			res_json = res.json()

			icon = res_json['icon']
			icon_url = f'https://cdn.discordapp.com/icons/{id}/{icon}'
			icon_all = f"{icon_url}.gif?size=1024" if requests.get(f'{icon_url}.gif', headers=headers).status_code == 200 else f"{icon_url}.png?size=1024"

			banner = res_json['banner']
			banner_url = f'https://cdn.discordapp.com/banners/{id}/{banner}'
			banner_all = f"{banner_url}.gif?size=1024" if requests.get(f'{banner_url}.gif', headers=headers).status_code == 200 else f"{banner_url}.png?size=1024"

			splash = res_json['splash']
			splash_url = f'https://cdn.discordapp.com/splashes/{id}/{splash}'
			splash_all = f"{splash_url}.gif?size=1024" if requests.get(f'{splash_url}.gif', headers=headers).status_code == 200 else f"{splash_url}.png?size=1024"

			print(f'\n {Fore.YELLOW}Name:{Fore.RESET} {name}\n {Fore.YELLOW}ID:{Fore.RESET} {id}')
			file.write(f'\n Name: {name}\n ID: {id}\n')
			if description != None:
				print(f' {Fore.YELLOW}Description:{Fore.RESET} {description}')
				file.write(f'Description: {description}\n')
			print(f' {Fore.YELLOW}Owner:{Fore.RESET} {owner} ({owner_id})')
			file.write(f' Owner: {owner} ({owner_id})\n')
			if icon != None:
				print(f' {Fore.YELLOW}Icon:{Fore.RESET} {icon_all}')
				file.write(f' Icon: {icon_all}\n')
			if banner != None:
				print(f' {Fore.YELLOW}Banner:{Fore.RESET} {banner_all}')
				file.write(f' Banner: {banner_all}\n')
			if splash != None:
				print(f' {Fore.YELLOW}Invite Photo:{Fore.RESET} {splash_all}')
				file.write(f' Invite Photo: {splash_all}\n')

			#### CHANNELS

			res = requests.get(f'https://discord.com/api/v9/guilds/{input_id}/channels', headers=headers)

			categ = []
			canal = []
			vc = []
			announces = []
			podcast = []

			print(f'\n\n {Fore.GREEN}Category {Fore.CYAN}(ID){Fore.RESET} --> {Fore.RED}Channel {Fore.CYAN}(ID){Fore.RESET}\n')
			file.write(f'\n\n Category (ID) --> Channel (ID)\n\n')

			for export in res.json():
				if not export["parent_id"] != None and (export["type"] == 0 or export["type"] == 2):
					print(f" {Fore.RED}{export['name']} {Fore.CYAN}({export['id']}) {Fore.GREEN}is not in a category{Fore.RESET}")
					file.write(f" {export['name']} ({export['id']}) is not in a category\n")
			for x in res.json():
				if not x["parent_id"] == None:
					for y in res.json():
						if y["id"] == x["parent_id"]:
							print(f" {Fore.GREEN}{y['name']} {Fore.CYAN}({y['id']}){Fore.RESET} ---> {Fore.RED}{x['name']} {Fore.CYAN}({x['id']}){Fore.RESET}")
							file.write(f" {y['name']} ({y['id']}) ---> {x['name']} ({x['id']})\n")
				if x['type'] == 4:
					categ.append(x['name'])
				elif x['type'] == 2:
					vc.append(x['name'])
				elif x['type'] == 5:
					announces.append(x['name'])
				elif x['type'] == 0:
					canal.append(x['name'])
				elif x['type'] == 13:
					podcast.append(x['name'])

			print('\n')
			file.write('\n\n')
			print(f' {Fore.YELLOW}Categories:{Fore.GREEN} {f"{Fore.RESET}, {Fore.GREEN}".join(categ)}\n')
			print(f' {Fore.YELLOW}Text Channels:{Fore.GREEN} {f"{Fore.RESET}, {Fore.GREEN}".join(canal)}\n')
			print(f' {Fore.YELLOW}Voice Channels:{Fore.GREEN} {f"{Fore.RESET}, {Fore.GREEN}".join(vc)}\n')
			print(f' {Fore.YELLOW}Announce Channels:{Fore.GREEN} {f"{Fore.RESET}, {Fore.GREEN}".join(announces)}\n')
			print(f' {Fore.YELLOW}Podcast Channels:{Fore.GREEN} {f"{Fore.RESET}, {Fore.GREEN}".join(podcast)}\n')
			file.write(f' Categories: {f", ".join(categ)}\n\n')
			file.write(f' Text Channels: {f", ".join(canal)}\n\n')
			file.write(f' Voice Channels: {f", ".join(vc)}\n\n')
			file.write(f' Announce Channels: {f", ".join(announces)}\n\n')
			file.write(f' Podcast Channels: {f", ".join(podcast)}\n\n')

			#### ROLES

			res = requests.get(f'https://discord.com/api/v9/guilds/{input_id}/roles', headers=headers)

			normal_roles = []
			bot_roles = []
			boost_roles = []
			admin_roles = []

			for x in res.json():
				if not x["managed"] == True:
					if (1 << 3) & int(x['permissions']) != (1 << 3):
						normal_roles.append(x['name'])
					elif (1 << 3) & int(x['permissions']) == (1 << 3):
						admin_roles.append(x['name'])
				elif not x["managed"] == False and x["hoist"] == False:
					bot_roles.append(x['name'])
				elif not x["hoist"] == False:
					boost_roles.append(x['name'])

			if normal_roles == ['@everyone']:
				print(f' {Fore.YELLOW}Normal Roles:{Fore.CYAN} @everyone\n')
			else:
				print(f' {Fore.YELLOW}Normal Roles:{Fore.GREEN} {f"{Fore.RESET}, {Fore.GREEN}".join(normal_roles).replace("@everyone", f"{Fore.CYAN}@everyone{Fore.RESET}")}{Fore.RESET},{Fore.RED} {f"{Fore.RESET}, {Fore.RED}".join(admin_roles)}\n')
			print(f' {Fore.YELLOW}Bot Roles:{Fore.GREEN} {f"{Fore.RESET}, {Fore.GREEN}".join(bot_roles)}\n')
			print(f' {Fore.YELLOW}Boost Role:{Fore.GREEN} {f"{Fore.RESET}, {Fore.GREEN}".join(boost_roles)}\n')
			if normal_roles == ['@everyone']:
				file.write(f' Normal Roles: @everyone\n\n')
			else:
				file.write(f' Normal Roles: {f", ".join(normal_roles)}, {f", ".join(admin_roles)}\n\n')
			file.write(f' Bot Roles: {f", ".join(bot_roles)}\n\n')
			file.write(f' Boost Role: {f", ".join(boost_roles)}\n\n')

			#### EMOJIS

			res = requests.get(f'https://discord.com/api/v9/guilds/{input_id}/emojis', headers=headers)

			emoji = []

			for x in res.json():
				emoji.append(x['name'])
			print(f' {Fore.YELLOW}Emojis:{Fore.GREEN} {f"{Fore.RESET}, {Fore.GREEN}".join(emoji)}\n')
			file.write(f' Emojis: {f", ".join(emoji)}\n')
			file.close()

			if icon != None:
				image_url = f'{icon_url}.gif' if requests.get(f'{icon_url}.gif', headers=headers).status_code == 200 else f'{icon_url}.png'
				filename = image_url.split("/")[-1]

				r = requests.get(image_url, stream = True)

				with open(filename,'wb') as f:
					shutil.copyfileobj(r.raw, f)
			if banner != None:
				image_url = f'{banner_url}.gif' if requests.get(f'{banner_url}.gif', headers=headers).status_code == 200 else f'{banner_url}.png'
				filename = image_url.split("/")[-1]

				r = requests.get(image_url, stream = True)

				with open(filename,'wb') as f:
					shutil.copyfileobj(r.raw, f)
			if splash != None:
				image_url = f'{splash_url}.gif' if requests.get(f'{splash_url}.gif', headers=headers).status_code == 200 else f'{splash_url}.png'
				filename = image_url.split("/")[-1]

				r = requests.get(image_url, stream = True)

				with open(filename,'wb') as f:
					shutil.copyfileobj(r.raw, f)
		except:
			clear()
			print(fail)
			print(f'{Fore.RED} [-] {Fore.RESET}Error\n')
	elif res.status_code == 400:
		clear()
		print(fail)
		print(f'{Fore.RED} [-] {Fore.RESET}Invalid ID (ID {Fore.RED}{input_id}{Fore.RESET} is not valid)\n')
	elif res.status_code == 403:
		clear()
		print(fail)
		print(f'{Fore.RED} [-] {Fore.RESET}Invalid ID (ID {Fore.RED}{input_id}{Fore.RESET} does not correspond to a server)\n')
else:
	clear()
	print(fail)
	print(f'{Fore.RED} [-] {Fore.RESET}Invalid Token\n')
getpass("")