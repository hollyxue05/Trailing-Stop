import yfinance as yf
import smtplib
from email.message import EmailMessage
from datetime import datetime

stopPercent = 0.2    #user defined/inputted

stockDict = {
    # 0 = date purchased, 1 = previous peak price, 2 = current trailing stop
    "HOOD" : [datetime(2025, 7, 14), 109.75, 109.75 * (1-stopPercent)], 
    "FIG" : [datetime(2025, 7, 31), 33, 33 * (1-stopPercent)]
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
        stockDict[stockTicker][2] = (1-stopPercent) * currPeakPrice  
    
    trailingStop = stockDict[stockTicker][2] 
    truncated_currPrice = int(currPrice * 1000) / 1000.0
    truncated_trailingStop = int(trailingStop * 1000) / 1000.0

    if currPrice < trailingStop : 
        alertEmail(stockTicker, truncated_currPrice, truncated_trailingStop) 
        print(stockTicker," now has a price of $", truncated_currPrice,", and has fallen below its trailing stop of $", truncated_trailingStop, sep="")
    else :
        print(stockTicker, " currently has a price of $", truncated_currPrice, ", and a trailing stop of $", truncated_trailingStop, sep="")

def alertEmail(stockTicker, currPrice, trailingStop):
    msg = EmailMessage()
    msg.set_content(stockTicker + ''' now has a price of ''' + str(currPrice) + ''' and has fallen below its trailing stop of ''' + str(trailingStop))
    msg['Subject'] = "Trailing Stop Alert"
    msg['From'] = "sender@email.com"
    msg['To'] = "recipiant@email.com"

    try:
        # For Gmail, use 'smtp.gmail.com' and port 587 for TLS or 465 for SSL
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # Or smtplib.SMTP for TLS and then smtp.starttls()
            smtp.login("sender@email.com", "password") # use an app password for security if sending from gmail  
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

for ticker in stockDict:
    print(ticker,":", sep="")
    calculateTrailingStopPrice(ticker)
    print()