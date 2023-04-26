#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Author: Yeiser Jimenez

import argparse
import requests
import json
import sys
from colorama import init, Fore, Style


banner = r'''
   _____      _   _    _           _   
  / ____|    | | | |  | |         | |  
 | |  __  ___| |_| |__| | ___  ___| |_ 
 | | |_ |/ _ \ __|  __  |/ _ \/ __| __|
 | |__| |  __/ |_| |  | | (_) \__ \ |_ 
  \_____|\___|\__|_|  |_|\___/|___/\__|
  
'''

print(Fore.GREEN + banner + Style.RESET_ALL)

init()  # Inicializa colorama

parser = argparse.ArgumentParser(description='Get JSON data from a URL')
parser.add_argument('-u', '--url', type=str, required=True, help='URL to get JSON data from')
parser.add_argument('-o', '--save', type=str, help='file to save JSON data to')
parser.add_argument('-s', '--show', action='store_true', help='display JSON data in console')

args = parser.parse_args()

response = requests.get(args.url)
status_code = response.status_code

if status_code == 200:
    json_data = response.json()

    if args.show:
        # Imprimir JSON con colores
        print(Fore.WHITE + '{' + Fore.RESET)
        for key, value in json_data.items():
            print(Fore.BLUE + f'    "{key}": ' + Fore.CYAN + f'{json.dumps(value)}' + Fore.RESET + ',')
        print(Fore.WHITE + '}' + Fore.RESET)

    if args.save:
        # Agregar extensión de archivo si no se proporciona
        if not args.save.endswith('.json'):
            args.save += '.json'
        with open(args.save, 'w') as file:
            json.dump(json_data, file, indent=4)
else:
    print(f'{Fore.RED}Error {status_code}:{Fore.RESET} Failed to retrieve JSON data from {args.url}')

if not args.show and not args.save:
    if status_code == 200:
        print(f'{Fore.GREEN}Status code: {status_code}{Fore.RESET}')
    else:
        print(f'{Fore.RED}Status code: {status_code}{Fore.RESET}')
