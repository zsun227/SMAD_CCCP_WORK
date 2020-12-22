import requests
import json
import os
from bs4 import BeautifulSoup
import re
import sys
from pattern.web import URL
import textract
import xlrd

sys.setrecursionlimit(10000)

class AppleJobsScraper(object):
    def __init__(self):
        self.search_request = {
        }
    def scrape(self,term,date,publication_id,date_range):
        id = self.scrape_1(term,date,publication_id,date_range)
        if id != None:
            pdf_store = self.scrape_2(id)
            return pdf_store
        else:
            return

    def scrape_1(self,term,date,publication_id,date_range):
        payload = {
            'terms':term,
            'testing_clipping_search_date_range_clone':date_range,
            'pubblication_ids[]':publication_id,
            'date_from':date,
        }
        r = requests.post(
            url = 'http://badgerlink.newsmemory.com/eebrowser/bbe/develop.20893.ant.clip.badgerdemo/public//freesearchtest/search/search/type/badger/format/html',


            data = payload,
            headers={
                'Accept':'text/html, */*; q=0.01',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Encoding':'deflate',
                'Host': 'badgerlink.newsmemory.com',
                'Connection': 'keep-alive',
                'Referer': 'http://badgerlink.newsmemory.com/eebrowser/bbe/develop.20893.ant.clip.badgerdemo/public/freesearchtest/search/index/type/badger/badger/427d49844052b17b3108bc9a7d0adce2',
                'Cookie': '_ga=GA1.2.508404352.1511898676; PHPSESSID=5bc159lsnur2m3him7bpsivvn1; _gid=GA1.2.1964665085.1518449964',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest'
            }
        )
        s = BeautifulSoup(r.text,'lxml')
        id = re.findall(r"session_id/(.*?)/type", str(s))
        if len(id) > 0:
            return id[0]

    def scrape_2(self, id):

        r = requests.post(
            url='http://badgerlink.newsmemory.com/eebrowser/bbe/develop.20893.ant.clip.badgerdemo/public/freesearchtest/search/get-search-results/format/json/session_id/'+id+'/type/badger/xtext_version//clipping_id/',
            headers={
                'Host':'badgerlink.newsmemory.com',
                'Connection':'keep-alive',
                'Referer':'http://badgerlink.newsmemory.com/eebrowser/bbe/develop.20893.ant.clip.badgerdemo/public/freesearchtest/search/index/type/badger/badger/427d49844052b17b3108bc9a7d0adce2',
                'Cookie':'_ga=GA1.2.508404352.1511898676; PHPSESSID=5bc159lsnur2m3him7bpsivvn1; _gid=GA1.2.1964665085.1518449964',

                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest'
            })
        # logged_in_page = requests.get('http://badgerlink.newsmemory.com/eebrowser/bbe/develop.20893.ant.clip.badgerdemo/public//freesearchtest/search/search/type/badger/format/html')
        soup = BeautifulSoup(r.text,'lxml')

        sssoup = re.findall(r"href.*?target",str(soup))
        pdf_store = []
        for x in sssoup:
            t1 = re.findall(r"psetup=(.*?)&",x)
            t2 = re.findall(r"issue=(.*?)&",x)
            t3 = re.findall(r"page=(.*?)&", x)
            if t2[0].startswith('2012'):
                pdf_url = 'http://usbbe01.newsmemory.com/nm_archive/'+t1[0]+'/'+t2[0][0:4]+'/'+t2[0][4:6]+'/'+t2[0]+'/'+t3[0]
            else:
                pdf_url = 'http://usbbe01.newsmemory.com/newsmemg/'+t1[0]+'/'+t2[0]+'/'+t3[0]
            pdf_store.append(pdf_url)
        return pdf_store

def get_pdf(pdf_link,path):
    url = URL(pdf_link)
    f = open(path, 'w')
    f.write(url.download(cached=False))
    f.close()

def get_txt(outlet_name, date_range, pdf,path):
    try:
        text = textract.process(pdf)
        f2 = open(path, 'w')
        f2.write(text)
        f2.close()
    except textract.exceptions.ShellError:
        print pdf, 'this one can not be decoded'
        get_pdf(pdf,
                '/Users/sunzhongkai/Desktop/text2012/' + outlet_name + '/' + date_range + '/' + 'failed' + '/' + str(
                    pdf.split('/')[8].split('.')[0]) + '.pdf')


def main():
    # I have to import a .csv file which contains the keywords
    csv_path = '/Users/sunzhongkai/Desktop/Newspaper-term-test.xlsx'
    csv = xlrd.open_workbook(csv_path)
    table= csv.sheets()[0]
    #

    outlets = ['Ashland Daily Post','Eau Claire Leader Telegram','Waukesha Freeman','Wisconsin State Journal','Beloift Daily News']
    time = ['01-31-2012','02-29-2012','03-31-2012','04-30-2012','05-31-2012','06-30-2012','07-31-2012','08-31-2012','09-30-2012','10-31-2012','11-30-2012','12-31-2012']
    terms = []
    for x in table.col_values(0):
        terms.append(x)
    for x in outlets:
        for y in time:
            # 'combine' is the combination of the whole search keywords, like  "Trump OR Clinton". You may want to use your own keyword by replacing 'combine'
            combine=''
            for z in terms[1:]:
                combine = z + ' ' + 'OR' + ' ' + combine
            combine = combine[:-3]
            ##

            outlet_name = x
            date_range = y
            os.makedirs('/Users/sunzhongkai/Desktop/text2012/' + outlet_name + '/' + date_range )
            os.makedirs('/Users/sunzhongkai/Desktop/text2012/' + outlet_name + '/' + date_range + '/' + 'failed')
            scraper = AppleJobsScraper()
            all_pdfs = scraper.scrape(term=combine, publication_id='115', date=y, date_range='30')
            i = 1
            if all_pdfs == None:
                print (' this term has no result')
            else:
                for pdf in all_pdfs:

                    url = URL(pdf)
                    f = open('store.pdf', 'wb')
                    f.write(url.download(cached=False, timeout=100))
                    f.close()

                    try:
                        get_txt(outlet_name,date_range,'store.pdf',
                            '/Users/sunzhongkai/Desktop/text2012/' + outlet_name + '/' + date_range + '/' + str(pdf.split('/')[8].split('.')[0]) + '.txt')

                    except UnicodeDecodeError:
                        print pdf, 'this one can not be decoded'
                        get_pdf(pdf,
                                '/Users/sunzhongkai/Desktop/text2012/' + outlet_name + '/' + date_range + '/' + 'failed' + '/' + str(
                                    pdf.split('/')[8].split('.')[0]) + '.pdf')
                    i += 1
                    print i
                    os.remove('store.pdf')

if __name__ == '__main__':
    main()



