from modules.spider import Spider
from modules.excel import Excel
from lxml import etree


if __name__ == '__main__':
    root = etree.parse('D:\\python\\HackMd_track_machine\\modules\\url.xml')
    url_list = [obj.text for obj in root.xpath('//url')]
    spiders = [Spider(url) for url in url_list]
    excel = Excel()

    excel.write_record(spiders)
    
