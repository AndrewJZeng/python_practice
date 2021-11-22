import requests, os, bs4, threading

url = 'http://xkcd.com/#'
if not os.path.exists('xkcd'):
    os.makedirs('xkcd')
def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text)
        
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
def main():
    downloadThreads = []
    
    for i in range(1070, 1570, 100):
        downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
        downloadThreads.append(downloadThread)
        downloadThread.start()
        
    for downloadThread in downloadThreads:
        downloadThread.join()
    print('Done.')

if __name__ == '__main__':
    main()