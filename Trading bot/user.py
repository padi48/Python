from main import StockInfo

x = StockInfo('')

def user(StockInfo):
        
        choice = input("What info would you like to know? ")

        if choice == 'daily':
                x.daily()
        elif choice == 'daily adjusted':
                x.daily_adjusted()
        elif choice == 'weekly':
                x.weekly()
        elif choice == 'weekly adjusted':
                x.weekly_adjusted()
        elif choice == 'monthly':
                x.monthly()
        elif choice == 'monthly adjusted':
                x.monthly_adjusted()
        elif choice == 'company overview':
                x.companyOverview()
        else:
                print("Incorrect info")
                return

user(StockInfo)
