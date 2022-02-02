import logging
import os
import subprocess
from flask import Flask, request,jsonify
from random import randint
from smalltalk_data import SMALLTALK_LIST

################################### LOGGER #####################
name = __name__
log_file = os.path.dirname(os.path.realpath(__file__)) + "/app_log.txt"
level = logging.DEBUG

formatter = logging.Formatter(
    fmt='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

handler = logging.FileHandler(log_file)
handler.setFormatter(formatter)

logger = logging.getLogger(name)
logger.setLevel(level)
logger.addHandler(handler)

############################## SERVER #########################

app = Flask(__name__)


def get_process_output(cmd):
    res = subprocess.check_output(cmd)
    return res.decode("utf-8").replace("\n", "").split("=")[-1]


@app.route("/healthcheck")
def healthcheck():
    logger.info(request.remote_addr + ' calls healthcheck')

    VC = "vcgencmd"
    health = {
        "clock": {},
        "mem": {},
        "volts": {}
    }

    for src in "arm core h264 isp v3d uart pwm emmc pixel vec hdmi dpi".split():
        cmd = [VC, "measure_clock", src]
        health['clock'][src] = get_process_output(cmd)

    for a in "core sdram_c sdram_i sdram_p".split():
        cmd = [VC, "measure_volts", a]
        health['volts'][a] = get_process_output(cmd)

    for a in "arm gpu".split():
        cmd = [VC, 'get_mem', a]
        health['mem'][a] = get_process_output(cmd)

    health['temp'] = get_process_output([VC, "measure_temp"])

    response = jsonify(health)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/smalltalk")
def smalltalk():
    logger.info(request.remote_addr + ' calls smalltalk')
    number = randint(0, 49)
    ret = {"message": SMALLTALK_LIST[number], "number": number}

    response = jsonify(ret)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    logger.info('Flask server starting')
    app.run(host="0.0.0.0", port=7778)
