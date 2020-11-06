import requests, re

class Stock:
    def __init__(self, stock):
        self.author = ["Amani"]
        self.contact = ["akutosecurity@protonmail.ch", "https://github.com/AkutoSecurity"]
        self.version = [0.1]
        
        self.stock = stock
        self.url = "https://old.nasdaq.com/symbol/" + self.stock # Getting values from Nasdaq website

    def get_price(self):
        price = re.findall(r'<div id="qwidget_lastsale" class="qwidget-dollar">(.*?)</div>', requests.get(self.url).text)[0]
        price = "%.2f" % float(price.strip('$')) # Formatting value to the nearest cent.
        return float(price)

    def get_perChange(self):
        percent = re.findall(r'<div id="qwidget_percent" class="qwidget-percent qwidget-Red" style="white-space:nowrap">(.*?)</div>', requests.get(self.url).text)[0]
        return percent
    
    def get_priceChange(self):
        price = re.findall(r'<div id="qwidget_netchange" class="qwidget-cents qwidget-Red">(.*?)</div>', requests.get(self.url).text)[0]
        return "%.2f" % float(price)

    def get_prevClose(self):
        pattern = r"""                <div class="table-row">
                    <div class="table-cell">
                        <b>Previous Close</b>
                    </div>
                    <div class="table-cell">
                        $&nbsp;(.*?)
                    </div>
                </div>"""
        prevClose = re.findall(pattern, request.get(self.url).text)[0]
        return prevClose

    def get_todayHigh(self):
        pattern = r"""                <div class="table-row">
                    <div class="table-cell">
                        <b>Today's High / Low</b>
                    </div>
                    <div class="table-cell">
                        $&nbsp;(.*?)&nbsp;/&nbsp;$&nbsp;(.*?)
                    </div>
                </div>"""
        high, low = re.findall(pattern, request.get(self.url).text)
        return high


    def get_todayLow(self):
        pattern = r"""                <div class="table-row">
                    <div class="table-cell">
                        <b>Today's High / Low</b>
                    </div>
                    <div class="table-cell">
                        $&nbsp;(.*?)&nbsp;/&nbsp;$&nbsp;(.*?)
                    </div>
                </div>"""
        high, low = re.findall(pattern, request.get(self.url).text)
        return low

    def get_marketCap(self):
        pattern = r"""                <div class="table-row">
                    <div class="table-cell">
                        <b>Market Cap</b>
                    </div>
                    <div class="table-cell">
                        (.*?)
                    </div>
                </div>"""
        marketCap = re.findall(pattern, request.get(self.url).text)
        return marketCap
