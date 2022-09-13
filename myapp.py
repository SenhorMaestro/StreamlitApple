import pandas as pd
import yfinance as yf
import streamlit as st 

st.write("""
# Котировки компании Apple

Стоимость акций за период c 1 января 2000 года по 12 сентября 2022
""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2000-1-1', end='2022-9-12')

st.line_chart(tickerDf.Close)

st.write("""
Объём торгов за период c 1 января 2000 года по 12 сентября 2022
""")

st.line_chart(tickerDf.Volume)