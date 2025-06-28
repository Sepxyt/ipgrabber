This Python script grabs both your **public IP** and your **local IP address**.

 **Public IP**: The IP seen by websites and online services.  
**Local IP**: The IP used inside your home or private network.

Useful for:
- Network diagnostics
- Checking VPN exposure
- Pentesting recon (see if the device is exposed to the internet)

# Features
- Fetches public IP using [`api.ipify.org`](https://api.ipify.org)
- Retrieves local IP using your system's hostname
- Handles errors gracefully (e.g. no internet)
  
# How to Use

# Requirements:
- Python 3.x
- `requests` library

# Install:
```bash
pip install requests
