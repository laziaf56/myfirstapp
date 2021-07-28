import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume!
""")

option = st.sidebar.selectbox(
    'Please select',
     ['Google','Mocrosoft','Apple'])

if option=='Google':
    tickerSymbol = 'GOOGL'
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

    st.write("""## Closing Price""")
    st.line_chart(tickerDf.Close)
    st.write("""## Volume Price""")
    st.line_chart(tickerDf.Volume)
    
if option=='Mocrosoft':
    tickerSymbol = 'MSFT'
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)

if option=='Apple':
    tickerSymbol = 'AAPL'
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
        
