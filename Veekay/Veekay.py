import requests
from uuid import uuid4

class Veekay(object):
    
    def __init__(self):
        self.uuid = uuid4()
        self.client = requests.Session()
    
    def login(self, email : str, password : str):
        url : str = f'https://api.vk.com/oauth/token?2fa_supported=1&client_id=3140623&client_secret=VeWdmVclDCtn6ihuP1nt&device_id={self.uuid}&grant_type=password&password={password}&scope=all&username={email}&v=5.145'
        headers : dict = {
                            'Host': 'api.vk.com',
	                        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
	                        'Accept': '*/*',
	                        'User-Agent': 'com.vk.vkclient/1554 (iPhone, iOS 14.6, iPhone11,2, Scale/3.0)',
	                        'Accept-Language': 'en',
	                        'Connection': 'keep-alive'
                        }
        
        res = self.client.get(url, headers= headers)
        
        if 'access_token' in res.text:
            self.token = res.json()['access_token'] 
        
        return self.token

    def search_user(self, username : str):
        url : str = f'https://m.vk.com/{username}'
        return self.client.get(url)
    
    def change_username(self, new_username : str, access_token : str):
        url : str = f'https://api.vk.com/method/account.saveProfileInfo?lang=en&screen_name={new_username}&v=5.145'
        headers : dict  = {
                            'Host': 'api.vk.com',
	                        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
	                        'Accept-Language': 'ar',
	                        'Accept': 'image/webp',
	                        'User-Agent': 'com.vk.vkclient/2990 (iPhone, iOS 14.6, iPhone11,2, Scale/3.0)',
	                        'Authorization': f'Bearer {access_token}',
	                        'Connection': 'keep-alive'
                          }
        
        return self.client.get(url, headers= headers)
    
    def edit_bio(self, args : str, access_token : str):
        url : str = f'https://api.vk.com/method/status.set?lang=en&text={args}&v=5.179'
        headers : dict = {
                            'Host': 'api.vk.com',
	                        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
	                        'Accept-Language': 'ar',
	                        'Accept': 'image/webp',
	                        'User-Agent': 'com.vk.vkclient/2990 (iPhone, iOS 14.6, iPhone11,2, Scale/3.0)',
	                        'Authorization': f'Bearer {access_token}',
	                        'Connection': 'keep-alive'   
                        }
        
        return self.client.get(url, headers= headers)