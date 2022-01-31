# Healthcheck Flask API for Raspberry Pi

## Download

```Bash
git clone git@github.com:AlbertCalmus/pi_healthcheck.git
cd pi_healthcheck
```
## Installation

### Venv

```Bash
python3 -m venv pi_healthcheck_venv
source pi_healthcheck_venv/bin/activate 
pip install -r requirements.txt
```
Add the pi_healthcheck_venv to `.gitignore`.

### App

Make sure that `app.py` & `app.sh` is executable
```Bash
sudo chmod +777 app.py
sudo chmod +777 app.sh
ls -l app.py #to check  persmission
```

Update `app.sh` with your path.

### Deamon

Create a new systemd service
```Bash
sudo nano /lib/systemd/system/pi-healthcheck.service
```

Paste the following code inside and save it using `ctrl+X`

```Bash
[Unit]
Description=pi-healthcheck
After=multi-user.target
[Service]
Type=idle
ExecStart=bash /home/pi/Projects/pi_healthcheck/app.sh
Restart=on-failure
[Install]
WantedBy=multi-user.target
```

Reload the systemd daemon
```Bash
sudo systemctl daemon-reload
```

Enable the new service
```Bash
sudo systemctl enable pi-healthcheck.service
```

Reboot your system
```Bash
sudo reboot
```

After rebooting, browse to `192.168.1.XY:777/healthcheck`. If everything worked fine, it should look like that
```json
{
  "clock": {
    "arm": "700074000",
    "core": "268750000",
    "h264": "0",
    "isp": "0",
    "v3d": "262500000",
    "uart": "48000000",
    "pwm": "100000000",
    "emmc": "200000000",
    "pixel": "337000",
    "vec": "108000000",
    "hdmi": "0",
    "dpi": "0"
  },
  "mem": {
    "arm": "948M",
    "gpu": "76M"
  },
  "volts": {
    "core": "1.2375V",
    "sdram_c": "1.2500V",
    "sdram_i": "1.2500V",
    "sdram_p": "1.2250V"
  },
  "temp": "58.5'C"
}
```

## Usage 

### App

Use the below to run the app (as a one off):
```Bash
bash app.sh
```

### Deamon 
#### Check status

```Bash
sudo systemctl status pi-healthcheck.service
```
#### Start service

```Bash
sudo systemctl start pi-healthcheck.service
```

#### Stop service

```Bash
sudo systemctl stop pi-healthcheck.service
```

#### Check service's log

```Bash
sudo journalctl -f -u pi-healthcheck.service
```


## Credits
- https://github.com/duckietown/rpi-health
- https://medium.com/@vishal.bala/flask-web-server-and-systemd-4b73cc22a9f8