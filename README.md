# Healthcheck Flask API for Raspberry Pi

## Installation

Install Flask
```
pip3 install flask
```

Clone this repo in your `Projects` folder
```
cd Projects/
git clone git@github.com:AlbertCalmus/pi_healthcheck.git
```

Make sure that `app.py` is executable
```
cd pi_healthcheck/
sudo chmod +777 app.py
```

Create a new systemd service
```
sudo touch /lib/systemd/system/pi-healthcheck.service
sudo nano /lib/systemd/system/pi-healthcheck.service
```

Paste the following code inside and save it using `ctrl+X`

```
[Unit]
Description=pi-healthcheck
After=multi-user.target
[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/pi/Projects/pi_healthcheck/app.py
Restart=on-failure
[Install]
WantedBy=multi-user.target
```

Reload the systemd daemon
```
sudo systemctl daemon-reload
```

Enable the new service
```
sudo systemctl enable pi-healthcheck
```

Reboot your system
```
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




