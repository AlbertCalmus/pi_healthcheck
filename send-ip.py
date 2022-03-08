import requests
from utils import get_logger

NAME = "TO"
SEND_TO_IP = "alcal.ovh"
PORT = 8432

url = f'https://{SEND_TO_IP}:{PORT}/ips/{NAME}'
#url = f'https://{SEND_TO_IP}:{PORT}/ips'

logger = get_logger(__name__)

external_ip = requests.get('https://api.ipify.org').content.decode('utf8')

my_json = {'ip': external_ip}

#ret = requests.get(url, verify=False)
ret = requests.put(url, json=my_json, verify=False)

if(ret.status_code == 200):
    logger.info('IP updated successfully')
else:
    logger.info('IP updating failure')
