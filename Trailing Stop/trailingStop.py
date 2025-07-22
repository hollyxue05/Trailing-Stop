import yfinance as yf  
import numpy as np
import pandas as pd
from datetime import datetime

purchaseDate = datetime(2025, 7, 14)
stockTicker = "CRCL" #given from the user's spreadsheet or input 
stopPercent = 0.2    #user inputted
previousPeakValue = 262.97  #given from the user's spreadsheet or input  
trailingStopPrice = previousPeakValue * (1-stopPercent)
    
def getCurrPrice():
    myTicker = yf.Ticker(stockTicker)
    currPrice = myTicker.fast_info.last_price
    return currPrice

def getPeakPrice():
    data = yf.Ticker(stockTicker).history(start = purchaseDate)
    max_high = data['High'].max()
    return float(max_high)

def calculateTrailingStopPrice():
    currPeakPrice = getPeakPrice() 
    currPrice = getCurrPrice() 

    # currPeakPrice is ambiguous rn 
    if currPeakPrice > previousPeakValue : 
        #update excel peak price 
        global trailingStopPrice 
        trailingStopPrice = (1-stopPercent) * currPeakPrice  
        # update excel 
    
    if int(currPrice) < int(trailingStopPrice) : 
        alertCell(currPrice) 
    else :
        print("current trailing stop =", trailingStopPrice)
        print("current price = ", currPrice)


def alertCell(price):
    print("uh oh no money: {price}" )

# getPeakPrice()
calculateTrailingStopPrice()
# getCurrPrice()
