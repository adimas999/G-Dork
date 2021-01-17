# @name:    Katana-DorkScanner
# @repo:    https://github.com/adimas999/G-Dork
# @author:  MrDevils
import asyncio
from proxybroker import Broker
from termcolor import colored, cprint
import sys
import os

B = """
 ____
|  _ \ _ __ _____  ___   _
| |_) | '__/ _ \ \/ / | | |    G-Dork
|  __/| | | (_) >  <| |_| |    Proxy Mode
|_|   |_|  \___/_/\_\\__,  |   Coded by MrDevils
                     |___/
"""
print(B)
print ("")
print(colored('[+] This will find 25 Different working Proxy server Each time :', 'green')) 
print(colored('[+] Starting...', 'green' ))

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None:
            break
        print('Found proxy: %s' % proxy)


proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTP', 'HTTPS'], limit=100 ), show(proxies)
)

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)
print(colored('[+] Done', 'green'))

