#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import argparse

def get_empty_vars():
    return json.dumps({})

def get_host_vars(host: str) -> dict:
    if host == 'test1':
        return {'ansible_host': '10.0.24.12', 'ansible_port': 2222}
    elif host == 'test2':
        return {'ansible_host': '10.0.24.13'}

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
    group_name = 'test'
    test_group_hosts = ['test1', 'test2']
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
            print(get_empty_vars())
        elif args.list:
            print(get_list())
        else:
            raise ValueError("Expecting either --host $HOSTNAME or --list")
    except ValueError:
        raise
