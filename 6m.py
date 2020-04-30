#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function

import yaml
import os
import io
import sys
import re
import subprocess

from pathlib import Path
from pprint import pprint

import click
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image

import logging
logging.basicConfig()

logger = logging.getLogger(__name__)

try:
    basestring
except NameError:  # python3
    basestring = str

configdir = os.path.join(Path.home(), ".config", "6m")
configfile = os.path.join(configdir, "config.yaml")

if not os.path.isdir(configdir):
    os.makedirs(configdir)

config = -1
if not os.path.isfile(configfile):
    logger.error("No config file, fool")
    sys.exit(1)
else:
    with open(configfile, "r") as c:
        config = yaml.load(c, Loader=yaml.SafeLoader)
        config = config['6m']
        selected = config['selected']


@click.group(invoke_without_command=True)
@click.option('--loglevel', '-l', default="info", show_default=True,
              type=click.Choice(['debug', 'warn', 'info', 'error'],
                                case_sensitive=False), help="Logging level")
def cli(loglevel):
    if re.match(r'debug', loglevel, re.IGNORECASE):
        logger.setLevel(logging.DEBUG)
        logger.debug("logger level set to DEBUG")
    elif re.match(r'warn', loglevel, re.IGNORECASE):
        logger.setLevel(logging.WARN)
        logger.debug("logger level set to DEBUG")
    elif re.match(r'info', loglevel, re.IGNORECASE):
        logger.setLevel(logging.INFO)
        logger.debug("logger level set to INFO")
    elif re.match(r'error', loglevel, re.IGNORECASE):
        logger.setLevel(logging.ERROR)
        logger.debug("logger level set to ERROR")
    elif config['logging']:
        logger.setLevel(config['logging'])
        logger.debug(
            "logger level set to {} from configfile".format(
                config['logging']))


def get_state(v):
    def inner(item):
        return config['selected'] == v
    return(inner)

def save_state(player):
    global config
    logger.info("Saving state")
    try:
        c = {'6m': config}
        c['6m']['selected'] = player
        c['6m']['logging'] = logger.level
        with io.open(configfile, 'w', encoding='utf8') as outfile:
            yaml.dump(c, outfile, default_flow_style=False, allow_unicode=True)
        config = c['6m']
    except Exception as e:
        logger.warning(e)

def set_state(v):
    def inner(icon, item):
        global config
        logger.info("Setting player to: {}".format(v))
        save_state(v)
    return(inner)


@cli.command('tray')
def tray(**kwargs):
    """Runs the system tray selector"""
    traydir = os.path.dirname(os.path.realpath(__file__))
    logger.debug("traydir = {}".format(traydir))
    iconf = os.path.join(traydir, "6m.png")
    if os.path.isfile(iconf):
        icon("6m",
             Image.open(iconf),
             menu=menu(lambda: (
                item(
                    str(i),
                    set_state(i),
                    checked=get_state(i),
                    radio=True)
             for i in config['players']))).run()



@cli.command('set')
@click.argument('player')
def set_player(player):
    """Sets player, Stateful"""
    logger.info("Setting player to: {}".format(player))
    save_state(player)


@cli.command('list')
def list_players():
    """List available players"""
    pprint(config)


@cli.command('play')
def play(**kwargs):
    """Execute play command"""
    try:
        logger.info(config['players'][selected]['play'])
        cmd = []
        for c in config['players'][selected]['play'].split():
            cmd.append(c)
        logger.debug(cmd)
        logger.info(subprocess.run(cmd, capture_output=True))
    except Exception as e:
        logger.warning(e)


@cli.command('pause')
def pause(**kwargs):
    """Execute pause command"""
    try:
        logger.info(config['players'][selected]['pause'])
        cmd = []
        for c in config['players'][selected]['pause'].split():
            cmd.append(c)
        logger.debug(cmd)
        logger.info(subprocess.run(cmd, capture_output=True))
    except Exception as e:
        logger.warning(e)


@cli.command('stop')
def stop(**kwargs):
    """Execute stop command"""
    try:
        logger.info(config['players'][selected]['stop'])
        cmd = []
        for c in config['players'][selected]['stop'].split():
            cmd.append(c)
        logger.debug(cmd)
        logger.info(subprocess.run(cmd, capture_output=True))
    except Exception as e:
        logger.warning(e)


@cli.command('toggle')
def toggle(**kwargs):
    """Execute toggle command"""
    try:
        logger.info(config['players'][selected]['toggle'])
        cmd = []
        for c in config['players'][selected]['toggle'].split():
            cmd.append(c)
        logger.debug(cmd)
        logger.info(subprocess.run(cmd, capture_output=True))
    except Exception as e:
        logger.warning(e)


@cli.command('status')
def status(**kwargs):
    """Execute status command"""
    try:
        logger.info(config['players'][selected]['status'])
        cmd = []
        for c in config['players'][selected]['status'].split():
            cmd.append(c)
        logger.debug(cmd)
        logger.info(subprocess.run(cmd, capture_output=True))
    except Exception as e:
        logger.warning(e)


@cli.command('volup')
def volup(**kwargs):
    """Execute volup command"""
    try:
        logger.info(config['players'][selected]['volup'])
        cmd = []
        for c in config['players'][selected]['volup'].split():
            cmd.append(c)
        logger.debug(cmd)
        logger.info(subprocess.run(cmd, capture_output=True))
    except Exception as e:
        logger.warning(e)


@cli.command('voldown')
def voldown(**kwargs):
    """Execute voldown command"""
    try:
        logger.info(config['players'][selected]['voldown'])
        cmd = []
        for c in config['players'][selected]['voldown'].split():
            cmd.append(c)
        logger.debug(cmd)
        logger.info(subprocess.run(cmd, capture_output=True))
    except Exception as e:
        logger.warning(e)


@cli.command('next')
def next(**kwargs):
    """Execute next command"""
    try:
        logger.info(config['players'][selected]['next'])
        cmd = []
        for c in config['players'][selected]['next'].split():
            cmd.append(c)
        logger.debug(cmd)
        logger.info(subprocess.run(cmd, capture_output=True))
    except Exception as e:
        logger.warning(e)


@cli.command('prev')
def prev(**kwargs):
    """Execute prev command"""
    try:
        logger.info(config['players'][selected]['prev'])
        cmd = []
        for c in config['players'][selected]['prev'].split():
            cmd.append(c)
        logger.debug(cmd)
        logger.info(subprocess.run(cmd, capture_output=True))
    except Exception as e:
        logger.warning(e)


@cli.command('add')
def add(**kwargs):
    """Execute add command"""
    try:
        logger.info(config['players'][selected]['add'])
        cmd = []
        for c in config['players'][selected]['add'].split():
            cmd.append(c)
        logger.debug(cmd)
        logger.info(subprocess.run(cmd, capture_output=True))
    except Exception as e:
        logger.warning(e)


def main(**kwargs):
    logger.debug("Main")
    pass


if __name__ == "__main__":
    cli()
