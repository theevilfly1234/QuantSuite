def add_strategy_signals(data):
    """
    Add strategy signals to the DataFrame (e.g., Moving Average Crossover).
    """
    data['SMA_10'] = data['Close'].rolling(window=10).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['Signal'] = 0
    data.loc[data['SMA_10'] > data['SMA_50'], 'Signal'] = 1  # Buy
    data.loc[data['SMA_10'] < data['SMA_50'], 'Signal'] = -1  # Sell
    return data
