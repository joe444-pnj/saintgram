import argparse
from saintgram.core import get_user_id, get_followers, get_following, get_follower_info, get_obfuscated_info
from saintgram.utils import print_banner, display_user_info, display_obfuscated_info, process_users

def main():
    print_banner()
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sessionid', help="Instagram session ID", required=True)
    parser.add_argument('-u', '--username', help="Username of the account", required=True)
    parser.add_argument('-o', '--option', help="Choose to get followers (f), following (w), or user info (i)", required=True)
    args = parser.parse_args()

    session_id = args.sessionid
    username = args.username
    option = args.option

    user_id_info = get_user_id(username, session_id)
    if user_id_info["error"]:
        print(colored(user_id_info["error"], 'red'))
        exit()

    user_id = user_id_info["id"]

    if option == 'f':
        followers = get_followers(user_id, session_id)
        if "error" in followers:
            print(colored(followers["error"], 'red'))
        else:
            process_users(followers["users"], session_id)

    elif option == 'w':
        following = get_following(user_id, session_id)
        if "error" in following:
            print(colored(following["error"], 'red'))
        else:
            process_users(following["users"], session_id)

    elif option == 'i':
        user_info = get_follower_info(user_id, session_id)
        if "error" in user_info:
            print(colored(user_info["error"], 'red'))
        else:
            display_user_info(user_info)
            obfuscated_info = get_obfuscated_info(username, session_id)
            if "error" in obfuscated_info:
                print(colored(obfuscated_info["error"], 'red'))
            else:
                display_obfuscated_info(obfuscated_info)

    else:
        print(colored("Invalid option. Please choose 'f' for followers, 'w' for following, or 'i' for user info.", 'red'))

if __name__ == "__main__":
    main()
