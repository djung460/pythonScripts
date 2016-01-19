#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip, requests, pyperclip, bs4
from selenium import webdriver

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard.
	address = pyperclip.paste()

address = 'https://www.google.com/maps/place/' + address

# Get request
res = requests.get(address)
res.raise_for_status()

# Catch any exceptions in failing to open website
try:
	res.raise_for_status()
except Exception as exc:
	print('Error: opening website')

webbrowser.open(address)


print('PAUSE')