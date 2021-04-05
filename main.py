#!/usr/bin/python3
import json
import subprocess
from datetime import datetime

json_data = dict()
currenent_ip = ""


def write_json():
    with open("collections_ip.json", "w") as f:
        json.dump(json_data, f, indent=4)


def read_json(filename="collections_ip.json"):
    with open(filename) as j_f:
        global json_data
        json_data = json.load(j_f)


def check_ip():
    proc = subprocess.Popen(["nslookup myip.opendns.com. resolver1.opendns.com"],
                            stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if out:
        global currenent_ip
        currenent_ip = out.decode("utf-8").split('Address')
        currenent_ip = currenent_ip[2][2:].strip('\n')
    else:
        exit(0)


def compare_ip():
    ip_last = json_data['ip_last']

    if ip_last != currenent_ip:
        json_data['ip_last'] = currenent_ip
        now = datetime.now()
        now = now.strftime(
            "%Y-%m-%d %H:%M:%S")
        dat = json_data['collections_ip']
        dat.append({'datetime': now, 'ip': currenent_ip})
        write_json()

    else:
        pass


def run():
    check_ip()
    read_json()
    compare_ip()
    


if __name__ == "__main__":
    run()
