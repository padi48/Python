from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from pprint import pprint


ts = TimeSeries(key='YOUR_API_KEY')
fd = FundamentalData(key='YOUR_API_KEY')
ti = TechIndicators(key='YOUR_API_KEY')
cc = CryptoCurrencies(key='YOUR_API_KEY')


class StockInfo():
    def __init__(self, stock_symbol):
        self.stock_symbol = input("Stock symbol: ")

    def daily(self):
        self.stock_daily = ts.get_daily(symbol=self.stock_symbol)
        pprint(self.stock_daily)

    def daily_adjusted(self):
        self.stock_daily_adjusted = ts.get_daily_adjusted(symbol=self.stock_symbol)
        pprint(self.stock_daily_adjusted)

    def weekly(self):
        self.stock_weekly = ts.get_weekly(symbol=self.stock_symbol)
        pprint(self.stock_weekly)

    def weekly_adjusted(self):
        self.stock_weekly_adjusted = ts.get_weekly_adjusted(symbol=self.stock_symbol)
        pprint(self.stock_weekly_adjusted)

    def monthly(self):
        self.stock_monthly = ts.get_monthly(symbol=self.stock_symbol)
        pprint(self.stock_monthly)

    def monthly_adjusted(self):
        self.stock_monthly_adjusted = ts.get_monthly_adjusted(symbol=self.stock_symbol)
        pprint(self.stock_monthly_adjusted)

    def companyOverview(self):
        self.company_overview = fd.get_company_overview(symbol=self.stock_symbol)
        print("Company overview of {}:".format(self.stock_symbol))
        pprint(self.company_overview)


        

