import time
import requests

class NocaptchaAi:
    def __init__(self, apikey):
        self.apikey = apikey

    def log(self, data):
        open('logs.log', 'a+').write(f'{data}\n')

    def req(self, url=None, headers=None, data=None):
        while True:
            try:
                if data is None:
                    res = requests.get(url, headers=headers)
                    return res

                res = requests.post(url, headers=headers, json=data)
                return res

            except (
            requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
                print("[x] connection error / timeout ", flush=True, end='\r')
                time.sleep(3)
                print("                                  ", flush=True, end="\r")
                continue

    def hcaptcha_token(self, site_key, site_url,
                       user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"):
        url_in = "https://token.nocaptchaai.com/token"
        headers = {"Content-Type": "application/json", "apikey": self.apikey}
        data = {
            "url": site_url,
            "sitekey": site_key,
            "useragent": user_agent
        }
        res = self.req(url_in, headers, data)
        self.log(res.text)
        url_res = res.json()['url']
        while True:
            res = self.req(url_res, headers)
            self.log(res.text)
            if res.json()['status'] == "processed":
                return True, res.json()['token']

            if res.json()['status'] == 'processing':
                time.sleep(3)
                continue

            if res.json()['status'] == 'failed':
                return False, res.text


api_key = "UR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT ITUR API KEY HERE REMMBER TO PUT IT "
solver = NocaptchaAi(api_key)

# Solve the captcha to obtain the token
site_key = "4c672d35-0701-42b2-88c3-78380b0db560"
site_url = "https://discord.com"
success, token = solver.hcaptcha_token(site_key, site_url)

if success:
    # Define the headers and payload for the POST request
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://discord.com",
        "Referer": "https://discord.com/",
        "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "X-Fingerprint": "1238098118487052349.RKxgKx60SYsRmFRKnwed0tVvp5Q",
        "X-Track": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjM3NTAyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
    }

    payload = {
        "captcha_key": token,
        "consent": True,
        "fingerprint": "1238098118487052349.RKxgKx60SYsRmFRKnwed0tVvp5Q",
        "global_name": "skibidi rizz",
        "unique_username_registration": True
    }

    url = "https://discord.com/api/v9/auth/register"

    # Make the POST request
    response = requests.post(url, headers=headers, json=payload)

    # Print the response status code and content
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)
else:
    print("Failed to solve captcha.")
