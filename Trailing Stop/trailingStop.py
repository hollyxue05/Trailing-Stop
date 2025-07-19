import yfinance as yf  # type: ignore
import numpy as np
from datetime import datetime

# def getPortfolioStockList():
#     print("temp")

purchaseDate = datetime(2025, 7, 14)
stockTicker = "CRCL" 
previousPeakValue = 262.97
stopPercent = 0.2

def getCurrPrice():
    myTicker = yf.Ticker(stockTicker)
    currPrice = myTicker.fast_info.last_price
    print(currPrice)
    return currPrice

def getPeakPrice():
    data = yf.download(stockTicker, start=purchaseDate)
    max_high = data["High"].max()
    print(max_high)
    return max_high

def calculateTrailingStopPrice():
#      for each stock in the excel file, do
#     getPeakPrice()
#     If peak value > excelPeakValue
#        update peak price to excel 
#        read "stop%" value, calculate new trailing stop price 
#        update excel file
#    fi
#    if current price < trailing stop price
#      alert()
#    fi
#   done

    trailingStopPrice = 210.376

    currPeakPrice = getPeakPrice()
    currPrice = getCurrPrice()

    if int(currPeakPrice) > int(previousPeakValue) : 
        print("got here")
        #update excel peak price 
        trailingStopPrice = (1-stopPercent) * currPeakPrice  
        #update excel 

    print(trailingStopPrice)
    
    if int(currPrice) < int(trailingStopPrice) : 
        alertCell(currPrice) 


def alertCell(price):
    print("uh oh no money: {price}" )

# getPeakPrice()
calculateTrailingStopPrice()
# getCurrPrice()
