Simple log of IP changes
1. Install `nslookup`

2. Use crontab for monitoring
    e.g. `*/10 * * * * python3 <path_to_file>/main.py >/dev/null 2>&1`

    The result is logged to the collection_ip.json file

3. To show changes run $ `python3 show_ip.py`