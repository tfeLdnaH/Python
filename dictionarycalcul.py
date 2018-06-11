stocks = {
    'AAPL': 434,
    'GOOG': 325,
    'F': 54,
    'MSFT': 623,
    'TUNA': 549,
}

#print(min(stocks)) result -> AAPL because key is order by letter

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)

