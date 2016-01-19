#! python3
# feelingLucky.py - Opens several google search result tabs

import webbrowser, sys, requests, pyperclip, bs4, os, urllib

address = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok = True)

while not address.endswith('#'):
	print('Opening website %s...' %address)
	res = requests.get(address)

	res.raise_for_status()

	#Use this to parse html
	soup = bs4.BeautifulSoup(res.text)

	comic = soup.select('#comic img')

	if comic == []:
		print('Couldn\'t find image')
	else:
		try:
			comic_url = 'http:' + comic[0].get('src')

			#download img
			print('Downloading image: %s...' %comic_url)
			res = requests.get(comic_url)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			#skip comic
			prev_link = soup.select('a[rel="prev"]')[0]
			address = 'http://xkcd.com' + prevLink.get('href')
			continue

		image_file = open(os.path.join('xkcd',os.path.basename(comic_url)),'wb')
		for chunk in res.iter_content(100000):
			image_file.write(chunk)
		print(image_file)
		image_file.close()

	prev_link = soup.select('a[rel="prev"]')[0]
	address = 'http://xkcd.com' + prev_link.get('href')

print('done')