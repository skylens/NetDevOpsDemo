#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def root():

    return {"hosts": "1.14.108.65,144.34.225.231"}