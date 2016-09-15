import requests
from lxml import html
import os
import argparse
from datetime import datetime

BASE_PATH = os.getcwd()	#Set the download path for your comics here.
COMIC_PATH = BASE_PATH + '/C&H'	
comic_exists = False
months = ['none', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def create_directory(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)

def download_image(url, title, dir = COMIC_PATH):
	data = html.fromstring(requests.get(url).text)
	image = 'http:' + str(data.xpath('//img[@id = "main-comic"]/@src')[0])
	image_name = dir + '/%s.png' % title

	if not os.path.exists(image_name):
		open(image_name, 'wb').write(requests.get(image).content) 
		comic_exists = True
		print 'Saved image %s.' % title

BASE_URL = 'http://explosm.net/comics/archive'

parser = argparse.ArgumentParser()
parser.add_argument('mode', nargs = '?', default = 1, help = "1 to download comic for a specific day(today by default), 2 to download comics for the entire month.")
parser.add_argument('year', nargs = '?', default = datetime.now().strftime('%Y'), help = 'Specify the year you wish to download comics for.')
parser.add_argument('month', nargs = '?', default = datetime.now().strftime('%m'), help = 'Specify the month you wish to download comics for.')
parser.add_argument('day', nargs = '?', default = datetime.now().strftime('%d'), help = 'Specify the day you wish to download comics for.')

args = parser.parse_args()

BASE_URL += '/' + args.year + '/' + args.month

#print 'test %s %s %s' % (args.day, args.month, args.year)

print 'Looking for comic(s) at %s' % BASE_URL
print 'Download path is set to %s' % COMIC_PATH
data = html.fromstring(requests.get(BASE_URL).text)
comics = data.xpath('//h3[@class = "zeta small-bottom-margin past-week-comic-title"]')

if args.mode == 1:
	for comic in comics:
		title = str(comic.xpath('./a/text()')[0]).split('.')[2]

		if title == args.day.zfill(2):
			extra = '-' + args.month + '-' + args.year + ' ' + str(comic.xpath('./following-sibling::small[1]/text()')[0])
			title += extra
			download_image(str(comic.xpath('./a/@href')[0]), title)

	if not comic_exists:
		print 'No comic found. :('

else:
	print 'Found %d comics.' % len(comics)
	current_directory = COMIC_PATH + '/' + args.year + '/' + months[int(args.month)]
	create_directory(current_directory)

	for comic in comics:
		title = str(comic.xpath('./a/text()')[0]).split('.')[2]
		extra = '-' + args.month + '-' + args.year + ' ' + str(comic.xpath('./following-sibling::small[1]/text()')[0])
		title += extra
		download_image(str(comic.xpath('./a/@href')[0]), title, dir = current_directory)













