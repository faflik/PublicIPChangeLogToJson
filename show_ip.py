#!/usr/bin/python3
import json

def run():
    with open('collections_ip.json') as f:
        json_data = json.load(f)
        collected_ip = json_data['collections_ip']
        for coll in collected_ip:
            date = coll['datetime']
            ip = coll['ip']
            print(f'IP changed {date}, new IP {ip}')

if __name__ == "__main__":
    run()