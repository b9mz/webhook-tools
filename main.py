import os
from time import sleep as wait
import colorama
from colorama import *
from dhooks import Webhook
import discord
colorama.init(autoreset=True)

def WebhookGuildInfo():
        
        os.system("cls")

        WebhookGuildInfoFrame = """
                


        
                                ░██████╗░██╗░░░██╗██╗██╗░░░░░██████╗░  ██╗███╗░░██╗███████╗░█████╗░
                                ██╔════╝░██║░░░██║██║██║░░░░░██╔══██╗  ██║████╗░██║██╔════╝██╔══██╗
                                ██║░░██╗░██║░░░██║██║██║░░░░░██║░░██║  ██║██╔██╗██║█████╗░░██║░░██║
                                ██║░░╚██╗██║░░░██║██║██║░░░░░██║░░██║  ██║██║╚████║██╔══╝░░██║░░██║
                                ╚██████╔╝╚██████╔╝██║███████╗██████╔╝  ██║██║░╚███║██║░░░░░╚█████╔╝
                                ░╚═════╝░░╚═════╝░╚═╝╚══════╝╚═════╝░  ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░


        """

        print(Fore.BLUE + WebhookGuildInfoFrame)

        hook = Webhook(input("[-] WEBHOOK LINK > "))
        hook.get_info()
        print("\n\n")
        print(f"[+] ID OF THE SERVEUR : {hook.guild_id}")
        print(f"[+] ID OF THE CHANNEL : {hook.channel_id}")
        print(f"[+] NAME OF THE WEBHOOK : {hook.guild_id}")
        print(f"[+] AVATAR LINK : {hook.default_avatar_url}")

def Spam():

        os.system("cls")

        SpamFrame = f"""
        


        
                                ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
                                ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
                                ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
                                ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
                                ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
                                ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝


        """

        print(Fore.LIGHTBLUE_EX + SpamFrame)

        hook = Webhook(input("[-] WEBHOOK LINK > "))
        print("\n\n")
        message = (input("[-] Enter your message > "))

        while True:
                        hook.send(f"{message}")
                
        
        
        

def Informations():

        os.system("cls")

        InformationsFrame = f"""
        
        
        
                ██╗███╗░░██╗███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
                ██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
                ██║██╔██╗██║█████╗░░██║░░██║██████╔╝██╔████╔██║███████║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
                ██║██║╚████║██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
                ██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
                ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░
        
        """

        

        print(Fore.YELLOW + InformationsFrame)

        Webhook = str(input("                Enter your webhook > "))

        print(f"\n\n")
        os.system(f"curl {Webhook}")


def Delete():

        os.system("cls")

        DeleteWebhookFrame = f"""
        
        

        
                                        ██████╗░███████╗██╗░░░░░███████╗████████╗███████╗
                                        ██╔══██╗██╔════╝██║░░░░░██╔════╝╚══██╔══╝██╔════╝
                                        ██║░░██║█████╗░░██║░░░░░█████╗░░░░░██║░░░█████╗░░
                                        ██║░░██║██╔══╝░░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░
                                        ██████╔╝███████╗███████╗███████╗░░░██║░░░███████╗
                                        ╚═════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░╚══════╝

        
        """

        print(Fore.GREEN + DeleteWebhookFrame)

        Webhook = str(input("                                        Enter your webhook > "))
        os.system(f"curl -X DELETE {Webhook}")

def Menu():
        MenuFrame = f"""


                        ░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗░██████╗
                        ░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝
                        ░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░╚█████╗░
                        ░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░░╚═══██╗
                        ░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗██████╔╝
                        ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░


        """

        Choices = f"""


        
                        1 : Webhook Informations               2 : Delete Webhook

                        3 : Spam Webhook                       4 : Get Webhook Server Info
        
        


        """

        

        print(Fore.LIGHTRED_EX + MenuFrame, Fore.CYAN + Choices)

        SetChoice = str(input("                        Choose a number > "))

        if SetChoice == "1":
                Informations()
        
        if SetChoice == "2":
                Delete()

        if SetChoice == "3":
                Spam()

        if SetChoice == "4":
                WebhookGuildInfo()

Menu()