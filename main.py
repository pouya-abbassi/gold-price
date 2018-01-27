from arabic_reshaper import reshape
from bidi.algorithm import get_display
from urllib.request import urlopen
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MainWidget(GridLayout):
    label_widget = ObjectProperty()
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.talanews.text = get_display(reshape('روی دکمه‌ی ریفرش کلیک کنید.'))
        self.iranshemsh.text = get_display(reshape('روی دکمه‌ی ریفرش کلیک کنید.'))
        self.parsisgold.text = get_display(reshape('روی دکمه‌ی ریفرش کلیک کنید.'))
    def refresh(self):
        self.talanews.text = get_display(reshape(talanews()))
        self.iranshemsh.text = get_display(reshape(iranshemsh()))
        self.parsisgold.text = get_display(reshape(parsis()))

class GoldPriceApp(App):
    def build(self):
        return MainWidget()

def talanews():
    page = urlopen('http://www.talanews.com/fa/%D9%82%D9%8A%D9%85%D8%AA-%D8%A2%D9%86%D9%84%D8%A7%D9%8A%D9%86-%D8%A7%D9%85%D8%B1%D9%88%D8%B2-%D8%B7%D9%84%D8%A7%D8%8C-%D8%B3%DA%A9%D9%87-%D9%88-%D8%A7%D8%B1%D8%B2-%D8%AF%D8%B1-%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1.html')
    for each in page:
        if '<span style="width:65%;float:right;text-align:left;">یک گرم طلای 24 عیار:' in each.decode():
            ret = '\n۱ مثقال طلای ۱۷عیار:        ' + each.decode().split('یک مثقال طلای 17 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n۱ گرم ۱۸عیار:        ' + each.decode().split('یک گرم طلای 18 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n۱ گرم ۱۹عیار:        ' + each.decode().split('یک گرم طلای 19 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n۱ گرم ۲۰عیار:        ' + each.decode().split('یک گرم طلای 20 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n۱ گرم ۲۱عیار:        ' + each.decode().split('یک گرم طلای 21 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n۱ گرم ۲۲عیار:        ' + each.decode().split('یک گرم طلای 22 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            ret += '\n۱ گرم ۲۴عیار:        ' + each.decode().split('یک گرم طلای 24 عیار:&nbsp;&nbsp;</span><span class="highlight-2">')[1].split('</span>')[0].replace(',','')
            return ret

def iranshemsh():
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
    ret = '\n۱ گرم ۱۸عیار:        ' + str(price[0])
    ret += '\n۰٫۱ گرم شمش ۲۴عیار:        ' + str(price[1])
    ret += '\n۰٫۱۵ گرم شمش ۲۴ عیار:        ' + str(price[2])
    ret += '\n۰٫۲۵ گرم شمش ۲۴ عیار:        ' + str(price[3])
    ret += '\n۰٫۵ گرم شمش ۲۴ عیار:        ' + str(price[4])
    ret += '\n۰٫۷۵ گرم شمش ۲۴ عیار:        ' + str(price[5])
    ret += '\n۱ گرم شمش ۲۴ عیار:        ' + str(price[6])
    return ret

def parsis():
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
    ret = '\n۱ گرم شمش ۲۴عیار:        ' + str(price[0])
    ret += '\n۰٫۵ گرم شمش ۲۴عیار:        ' + str(price[1])
    ret += '\n۵ گرم شمش ۲۴عیار:        ' + str(price[2])
    ret += '\n۱۰ گرم شمش ۲۴عیار:        ' + str(price[3])
    ret += '\n۱ اونس شمش ۲۴عیار:        ' + str(price[4])
    return ret

if __name__ == '__main__':
    GoldPriceApp().run()
