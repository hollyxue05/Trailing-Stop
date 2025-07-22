import yfinance as yf  
import numpy as np
import pandas as pd
from datetime import datetime

stopPercent = 0.2    #user inputted

stockDict = {
    # 0 = date purchased, 1 = previous peak price, 2 = current trailing stop
    "CRCL" : [datetime(2025, 7, 14), 262.97, 262.97 * (1-stopPercent)]
}


def getCurrPrice(stockTicker):
    myTicker = yf.Ticker(stockTicker)
    currPrice = myTicker.fast_info.last_price
    return currPrice

def getPeakPrice(stockTicker):
    global stockDict 
    data = yf.Ticker(stockTicker).history(start = stockDict[stockTicker][0])
    max_high = data['High'].max()
    return float(max_high)

def calculateTrailingStopPrice(stockTicker):
    currPrice = getCurrPrice(stockTicker) 
    currPeakPrice = getPeakPrice(stockTicker) 

    global stockDict

    if currPeakPrice > stockDict[stockTicker][1] : 
        #update excel peak price 
        global trailingStopPrice 
        trailingStopPrice = (1-stopPercent) * currPeakPrice  
        # update excel 
    
    if int(currPrice) < int(trailingStopPrice) : 
        alertCell(currPrice) 
        print("current trailing stop =", trailingStopPrice)
        print("current price = ", currPrice)
    else :
        print("current trailing stop =", trailingStopPrice)
        print("current price = ", currPrice)

def alertCell(price):
    print("uh oh no money: " )

# print(getCurrPrice("CRCL"))
# print(getPeakPrice("CRCL"))

calculateTrailingStopPrice("CRCL")
