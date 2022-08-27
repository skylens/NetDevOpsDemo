#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pandas import pandas as pd
import os

path = os.path.abspath(os.path.dirname(__file__)) + "/Inventory.csv"

data = pd.read_csv(path,header=None)
print(data.values)