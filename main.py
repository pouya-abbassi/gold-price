from urllib.request import urlopen
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '256')

netprice = ''

class MainWidget(GridLayout):
    label_widget = ObjectProperty()
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
    def refresh(self):
        self.talanews.text = talanews()
        self.iranshemsh.text = iranshemsh()
        self.parsisgold.text = parsis()

class GoldPriceApp(App):
    def build(self):
        return MainWidget()

def talanews():
    global netprice
    page = urlopen('http://www.talanews.com/fa/%D9%82%D9%8A%D9%85%D8%AA-%D8%A2%D9%86%D9%84%D8%A7%D9%8A%D9%86-%D8%A7%D9%85%D8%B1%D9%88%D8%B2-%D8%B7%D9%84%D8%A7%D8%8C-%D8%B3%DA%A9%D9%87-%D9%88-%D8%A7%D8%B1%D8%B2-%D8%AF%D8%B1-%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1.html')
    for each in page:
        if '<span style="width:65%;float:right;text-align:left;">یک گرم طلای 24 عیار:' in each.decode():
            ret = '1m 17K GoldBar:        ' + each.decode().split('یک مثقال طلای 17 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n1g 18K GoldBar:        ' + each.decode().split('یک گرم طلای 18 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n1g 19K GoldBar:        ' + each.decode().split('یک گرم طلای 19 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n1g 20K GoldBar:        ' + each.decode().split('یک گرم طلای 20 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n1g 21K GoldBar:        ' + each.decode().split('یک گرم طلای 21 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n1g 22K GoldBar:        ' + each.decode().split('یک گرم طلای 22 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n1g 24K GoldBar:        ' + each.decode().split('یک گرم طلای 24 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            netprice = int(each.decode().split('یک گرم طلای 24 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',',''))
            return ret

def iranshemsh():
    global netprice
    price = []
    page = urlopen('http://webtools.khaneweb.ir/application/core.webtools.gold/components/service_proxy.svc/GetCurrentGoldValue18')
    for each in page:
        price += [each.decode()[7:-4]]
    price += [int(((0.1 * 995) / 750) * int(price[0]) + 15001)]    # ((vazn * 995) / 750) * gheymate 18ayar + sud
    price += [int(((0.15 * 995) / 750) * int(price[0]) + 17501)]
    price += [int(((0.25 * 995) / 750) * int(price[0]) + 21000)]
    price += [int(((0.5 * 995) / 750) * int(price[0]) + 23501)]
    price += [int(((0.75 * 995) / 750) * int(price[0]) + 26000)]
    price += [int(((1 * 995) / 750) * int(price[0]) + 28000)]
    ret =  '1g    18K GoldBar:        ' + str(price[0])
    ret += '\n0.1g  24K GoldBar:        ' + str(price[1])
    ret += '\n0.15g 24K GoldBar:        ' + str(price[2])
    ret += '\n0.25g 24K GoldBar:        ' + str(price[3])
    ret += '\n0.5g  24K GoldBar:        ' + str(price[4])
    ret += '\n0.75g 24K GoldBar:        ' + str(price[5])
    ret += '\n1g    24K GoldBar:        ' + str(price[6])
    ret += '\n\n10g   24K fee    :        ' + str(netprice-price[6])
    return ret

def parsis():
    global netprice
    price = []
    pages = ['http://parsisgold.com/productdetails.aspx?itemid=4',
            'http://parsisgold.com/productdetails.aspx?itemid=5',
            'http://parsisgold.com/productdetails.aspx?itemid=6',
            'http://parsisgold.com/productdetails.aspx?itemid=7',
            'http://parsisgold.com/productdetails.aspx?itemid=8']
    for page in pages:
        page = urlopen(page)
        for each in page:
            if '<span id="ctl00_lblPrice" class="ProductPrice">' in each.decode():
                price += [each.decode().split('<span id="ctl00_lblPrice" class="ProductPrice">')[1].split('</span>')[0].replace(',','')]
    ret = '1g   24K GoldBar:        ' + str(price[0])
    ret += '\n2.5g 24K GoldBar:        ' + str(price[1])
    ret += '\n5g   24K GoldBar:        ' + str(price[2])
    ret += '\n10g  24K GoldBar:        ' + str(price[3])
    ret += '\n1oz  24K GoldBar:        ' + str(price[4])
    ret += '\n\n1g   24K fee    :        ' + str(netprice-int(price[0]))
    ret += '\n1oz   24K fee   :        ' + str(int((netprice*31.1)-int(price[4])))
    return ret

if __name__ == '__main__':
    GoldPriceApp().run()
