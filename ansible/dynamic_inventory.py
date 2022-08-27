#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.modb.pro/db/395921

import json
import argparse
import sys

def get_empty_vars():
    return json.dumps({})

def get_host_vars(host: str) -> dict:
    if host == 'lighthouse':
        data = {"ansible_host": "1.14.108.65", "ansible_user": "root", "ansible_port": 22}
        return json.dumps(data)
    elif host == 'freebsd':
        data = {"ansible_host": "144.34.225.231", "ansible_user": "skylens116", "ansible_port": 22}
        return json.dumps(data)

def get_list() -> str:
    data = {
        '_meta': {
            'hostvars': {}
        },
        'all': {
            'children': [
                'ungrouped'
            ]
        },
    }
    group_name = 'linux'
    test_group_hosts = ['lighthouse', 'freebsd']
    # 加入all组
    data.get('all').get('children').append(group_name)
    data[group_name] = {}
    data[group_name]['hosts'] = test_group_hosts
    for host in test_group_hosts:
        data['_meta']['hostvars'][host] = get_host_vars(host)
    return json.dumps(data)

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='dynamic ansible inventories')
    # 创建互斥组
    mandatory_options = arg_parser.add_mutually_exclusive_group()
    mandatory_options.add_argument(
        '--list',
        action='store_true',
        help="Show JSON of all managed hosts"
    )
    mandatory_options.add_argument(
        '--host',
        help="Display vars related to the host"
    )
    try:
        args = arg_parser.parse_args()
        if args.host:
            print(get_host_vars(sys.argv[2]))
        elif args.list:
            print(get_list())
        else:
            raise ValueError("Expecting either --host $HOSTNAME or --list")
    except ValueError:
        raise
