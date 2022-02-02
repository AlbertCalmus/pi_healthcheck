import requests
import json
from utils import get_logger

SEND_TO_IP = "192.168.1.10"
PORT = '7778'

logger = get_logger(__name__)

url = f'http://{SEND_TO_IP}:{PORT}/receive-ip'

external_ip = requests.get('https://api.ipify.org').content.decode('utf8')

my_json = {'name': 'TO', 'ip': external_ip}

ret = requests.post(url, json=my_json)

if(json.loads(ret.text) == my_json):
    logger.info('IP updated successfully')
else:
    logger.info('IP updating failure')
