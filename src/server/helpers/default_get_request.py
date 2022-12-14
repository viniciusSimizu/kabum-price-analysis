from requests import get
from src.config.config import config


def default_get_request(url: str):
    return get("{}/{}".format(config.get('KABUM_BASE_API_URL'), url),
               headers={
                   'accept': 'application/json, text/plain, */*',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pt;q=0.7',
                   'origin': 'https://www.kabum.com.br',
                   'referer': 'https://www.kabum.com.br/',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/106.0.0.0 Safari/537.36 '
               })
