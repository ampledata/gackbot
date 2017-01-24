#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""GACKbot Plugin."""

import os
import re
import sys
import tempfile

import slackbot

import requests

import gackbot

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


@slackbot.bot.respond_to('demand')
def show_demand(message):
    demand_url = (
        'http://172.17.2.20:3031/render'
        '?target=cactiStyle(tomato.eagle.gauge-demand_f)'
        '&from=-2hours&until=now&width=400&height=200'
    )

    tmp_fd, tmp_file = tempfile.mkstemp()
    os.close(tmp_fd)

    demand_request = requests.get(demand_url)

    with open(tmp_file, 'w') as ofd:
        ofd.write(demand_request.content)

    message.channel.upload_file('Power Demand', tmp_file)
