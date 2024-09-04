import requests
from urllib.parse import quote_plus
from json import dumps, decoder
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code
import pycountry
from termcolor import colored

def get_user_id(username, session_id):
    try:
        headers = {"User-Agent": "iphone_ua", "x-ig-app-id": "936619743392459"}
        response = requests.get(
            f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}',
            headers=headers,
            cookies={'sessionid': session_id}
        )
        
        if response.status_code == 404:
            return {"id": None, "error": "User not found"}
        
        user_id = response.json()["data"]['user']['id']
        return {"id": user_id, "error": None}

    except decoder.JSONDecodeError:
        return {"id": None, "error": "Rate limit exceeded or invalid session ID"}
    except Exception as e:
        return {"id": None, "error": f"Unexpected error: {str(e)}"}

def get_obfuscated_info(username, session_id):
    try:
        data = "signed_body=SIGNATURE."+quote_plus(dumps(
            {"q": username, "skip_recovery":"1"},
            separators=(",",":")
        ))
        response = requests.post(
            'https://i.instagram.com/api/v1/users/lookup/',
            headers={
                "Accept-Language": "en-US",
                "User-Agent": "Instagram 101.0.0.15.120",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-IG-App-ID": "124024574287414",
                "Accept-Encoding": "gzip, deflate",
                "Host": "i.instagram.com",
                "Connection": "keep-alive",
                "Content-Length": str(len(data))
            },
            data=data,
            cookies={'sessionid': session_id}
        )
        return response.json()
    except decoder.JSONDecodeError:
        return {"error": "Rate limit exceeded or invalid session ID"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

def get_follower_info(follower_id, session_id):
    try:
        url = f'https://i.instagram.com/api/v1/users/{follower_id}/info/'
        headers = {'User-Agent': 'Instagram 64.0.0.14.96'}
        response = requests.get(url, headers=headers, cookies={'sessionid': session_id})
        return response.json()["user"]
    except decoder.JSONDecodeError:
        return {"error": "Rate limit exceeded or invalid session ID"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

def get_followers(user_id, session_id):
    try:
        url = f'https://i.instagram.com/api/v1/friendships/{user_id}/followers/?count=50'
        headers = {
            'User-Agent': 'Instagram 64.0.0.14.96',
            'X-IG-App-ID': '936619743392459'
        }
        response = requests.get(url, headers=headers, cookies={'sessionid': session_id})
        return response.json()
    except decoder.JSONDecodeError:
        return {"users": [], "error": "Rate limit exceeded"}
    except Exception as e:
        return {"users": [], "error": f"Unexpected error: {str(e)}"}

def get_following(user_id, session_id):
    try:
        url = f'https://i.instagram.com/api/v1/friendships/{user_id}/following/?count=50'
        headers = {
            'User-Agent': 'Instagram 64.0.0.14.96',
            'X-IG-App-ID': '936619743392459'
        }
        response = requests.get(url, headers=headers, cookies={'sessionid': session_id})
        return response.json()
    except decoder.JSONDecodeError:
        return {"users": [], "error": "Rate limit exceeded"}
    except Exception as e:
        return {"users": [], "error": f"Unexpected error: {str(e)}"}
