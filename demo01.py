#!/usr/bin/python3
# coding  :  utf-8
import json
import sys


def group():
    host1 = ['192.168.0.112']
    host2 = ['192.168.0.112', '192.168.0.109']
    group1 = 'test1'
    group2 = 'test2'
    hostdata = {
        group1: {"hosts": host1},
        group2: {"hosts": host2}
    }
    print(json.dumps(hostdata, indent=4))


def host(ip):
    info_dict = {
        "192.168.0.112": {
            "ansible_ssh_host": "192.168.0.112",
            "ansible_ssh_port": 22,
            "ansible_ssh_user": "root",
            "ansible_ssh_pass": "123457"
        },
        "192.168.0.109": {
            "ansible_ssh_host": "192.168.0.109",
            "ansible_ssh_port": 22,
            "ansible_ssh_user": "root",
            "ansible_ssh_pass": "xxxx"
        }
    }
    #  判断key是否在字典中，在的话打印出来，不在的话打印空字典。  
    if ip in info_dict:
        print(json.dumps(info_dict[ip], indent=4))
    else:
        print(json.dumps({}, indent=4))


if len(sys.argv) == 2 and (sys.argv[1] == '--list'):
    group()
elif len(sys.argv) == 3 and (sys.argv[1] == '--host'):
    host(sys.argv[2])
else:
    print("Usage:  %s  --list  or  --host  <hostname>" % sys.argv[0])
sys.exit(1)
