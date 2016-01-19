#! python3
# feelingLucky.py - Opens several google search result tabs

import webbrowser, sys, requests, pyperclip, bs4

if len(sys.argv)  > 1:
	search_term = ' '.join(sys.argv[1:]) 
else:
	search_term = pyperclip.paste()

address = 'https://www.google.com/search?q=' + search_term

res = requests.get(address)

try:
	res.raise_for_status()
except Exception as exc:
	print('Error: opening website')

#Use this to parse
soup = bs4.BeautifulSoup(res.text)

linkElems = soup.select('.r a')

numOpen = min(5,len(linkElems))

for i in range(numOpen){
	webbrowser.open('http://google.com' + linkElems[i].get('href'));
	}
