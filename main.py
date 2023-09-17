# INF 601 - Advanced Programming with Python
# Jasmine Irvin
# Mini Project 1
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import copy
import pprint

#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#(5/5 points) Proper import of packages used.

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period='10d')
    closing_list = []
    dates = []

    # ammended to add dates as well as price to list
    for date, price in zip(hist.index, hist['Close']):
        dates.append(date.date())
        closing_list.append(round(price, 2))

    # ammended to add dates
    return closing_list, dates

stocks = ["MSFT", "AAPL", "AMZN", "ADBE", "NVDA"]

# loop through all stocks in list
for stock in stocks:
    stock_closing, dates = np.array(getClosing(stock))
    days = list(range(1, len(stock_closing) + 1))

    # Plots the graph
    plt.plot(days, stock_closing)

    # get our min and max for Y
    prices = getClosing(stock)[0]
    low_price = min(prices)
    high_price = max(prices)
    plt.axis([1, 10, low_price - 2, high_price + 2])

    # Set our xaxis min and max
    # form [xmin, xmax, ymin, ymax]
    plt.xticks(days, dates, rotation=45)

    # Update x-axis label to "Date"
    # Set our labels for the graph
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title("Closing Price for " + stock)

    # Shows the graph
    plt.show()



#(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
#(10/10 points) Store this information in a list that you will convert to an array in NumPy.
#(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum, it just needs to show 10 data points.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this file with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.