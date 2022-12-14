#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def commmysql():
    from pandas import pandas as pd
    import os

    path = os.path.abspath(os.path.dirname(__file__)) + "/Inventory.csv"

    data = pd.read_csv(path, header=None)
    myresult = data.values
    print(myresult)
    data = dict()
    #####查询出group分组并去重#############
    groups = list(set([i[1] for i in myresult]))
    data["all"] = {"children": groups}
    data["_meta"] = {"hostvars": {}}
    for group in groups:
        data[group] = dict()
        data[group]["hosts"] = list()
        for x in myresult:
            if x[1] == group:
                data[group]["hosts"].append(x[0])
    return json.dumps(data,indent=3)


def main():
    from optparse import OptionParser
    parse = OptionParser()
    parse.add_option("-l", "--list", action="store_true", dest="list", default=False)
    (option, arges) = parse.parse_args()
    if option.list:
        print(commmysql())
    else:
        print("abc")



if __name__ == '__main__':
    from optparse import OptionParser
    parse = OptionParser()
    parse.add_option("-l", "--list", action="store_true", dest="list", default=False)
    (option, arges) = parse.parse_args()
    if option.list:
        print(commmysql())
    else:
        print("test")
    # commmysql()