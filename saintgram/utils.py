from termcolor import colored
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code
import pycountry
from saintgram.core import get_follower_info  # Import get_follower_info

def print_banner():
    banner = """
                          /$$             /$$                                               
                    |__/            | $$                                               
  /$$$$$$$  /$$$$$$  /$$ /$$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$/$$$$ 
 /$$_____/ |____  $$| $$| $$__  $$|_  $$_/   /$$__  $$ /$$__  $$|____  $$| $$_  $$_  $$
|  $$$$$$   /$$$$$$$| $$| $$  \ $$  | $$    | $$  \ $$| $$  \__/ /$$$$$$$| $$ \ $$ \ $$
 \____  $$ /$$__  $$| $$| $$  | $$  | $$ /$$| $$  | $$| $$      /$$__  $$| $$ | $$ | $$
 /$$$$$$$/|  $$$$$$$| $$| $$  | $$  |  $$$$/|  $$$$$$$| $$     |  $$$$$$$| $$ | $$ | $$
|_______/  \_______/|__/|__/  |__/   \___/   \____  $$|__/      \_______/|__/ |__/ |__/
                                             /$$  \ $$                                 
                                            |  $$$$$$/                                 
                                             \______/                                  



    """
    print(colored(banner, 'green'))

def display_user_info(infos):
    try:
        print(colored("Informations about     : " + infos["username"], 'green'))
        print(colored("UserID                 : " + str(infos["pk"]), 'green'))  # Convert to string
        print(colored("Full Name              : " + infos["full_name"], 'green'))
        print(colored("Verified               : " + str(infos['is_verified']), 'green'))
        print(colored("Is Business Account    : " + str(infos["is_business"]), 'green'))
        print(colored("Is Private Account     : " + str(infos["is_private"]), 'green'))
        print(colored("Follower Count         : " + str(infos["follower_count"]), 'green'))
        print(colored("Following Count        : " + str(infos["following_count"]), 'green'))
        print(colored("Number of Posts        : " + str(infos["media_count"]), 'green'))

        if infos["external_url"]:
            print(colored("External URL           : " + infos["external_url"], 'green'))
        if "public_email" in infos.keys() and infos["public_email"]:
            print(colored("Public Email           : " + infos["public_email"], 'green'))
        if "public_phone_number" in infos.keys() and infos["public_phone_number"]:
            phone_number = f"+{infos['public_phone_country_code']} {infos['public_phone_number']}"
            try:
                parsed_number = phonenumbers.parse(phone_number)
                country_code = region_code_for_country_code(parsed_number.country_code)
                country = pycountry.countries.get(alpha_2=country_code)
                phone_number += f" ({country.name})"
            except:
                pass
            print(colored("Public Phone Number    : " + phone_number, 'green'))
    except KeyError as e:
        print(colored(f"Key error: Missing key {str(e)} in response", 'red'))
    except Exception as e:
        print(colored(f"Unexpected error: {str(e)}", 'red'))

def display_obfuscated_info(obfuscated_info):
    try:
        if "obfuscated_email" in obfuscated_info.keys():
            if obfuscated_info["obfuscated_email"]:
                print(colored("Obfuscated email       : " + obfuscated_info["obfuscated_email"], 'green'))
            else:
                print(colored("No obfuscated email found", 'green'))

        if "obfuscated_phone" in obfuscated_info.keys():
            if obfuscated_info["obfuscated_phone"]:
                print(colored("Obfuscated phone       : " + obfuscated_info["obfuscated_phone"], 'green'))
            else:
                print(colored("No obfuscated phone found", 'green'))
    except Exception as e:
        print(colored(f"Unexpected error: {str(e)}", 'red'))

    print(colored("-" * 24, 'green'))

def process_users(users, session_id):
    for user in users:
        follower_info = get_follower_info(user['pk'], session_id)
        
        if "error" in follower_info:
            print(colored(f"Error fetching info for user {user['username']}: {follower_info['error']}", 'red'))
            continue
        
        display_user_info(follower_info)
        print("\n")  # Add spacing between followers
