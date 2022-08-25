#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# time: 2022/8/25 14:46
# author: skylens

from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_table_inventory.plugins.inventory.table import CSVInventory
from nornir.core.plugins.inventory import InventoryPluginRegister

InventoryPluginRegister.register("table_inventory", CSVInventory)

nr = InitNornir(config_file=r'config.yml')

# runner = {
#     "plugin": "threaded",
#     "options": {
#         "num_workers": 100,
#     },
# }
#
# inventory = {
#     "plugin": "CSVInventory",
#     "options": {
#         "csv_file": "inventory.csv",
#     },
# }

# nr = InitNornir(runner=runner, inventory=inventory)

result = nr.run(task=netmiko_send_command, command_string='echo PONG')

print_result(result)