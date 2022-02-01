import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

def get_process_output(cmd):
  res = subprocess.check_output(cmd)
  return res.decode("utf-8").replace("\n", "").split("=")[-1]

@app.route("/healthcheck")
def healthcheck():
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

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=777)
