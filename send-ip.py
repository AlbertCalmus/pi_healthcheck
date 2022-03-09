import requests
from utils import get_logger

# Parameters
NAME = "TO"
SEND_TO_IP = "alcal.ovh"
PORT = 8432

url = f'https://{SEND_TO_IP}:{PORT}/ips/{NAME}'

logger = get_logger(__name__)

# Get current external ip and send it
external_ip = requests.get('https://api.ipify.org').content.decode('utf8')
my_json = {'ip': external_ip}
ret = requests.put(url, json=my_json, verify=False)

# log result
if(ret.status_code == 200):
    logger.info('IP updated successfully')
else:
    logger.info('IP updating failure')
