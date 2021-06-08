import numpy as np
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def ratio_charting(asset1, asset2, log, avg):

    pd.set_option('display.max_columns', None)

    master_df = pd.DataFrame()

    # Gather Tickers
    from config import ticker_dictionary

    # check if input is valid
    tickers = list(ticker_dictionary.values())
    valid_input_list = list(ticker_dictionary.keys())

    # convert input to yfinance ticker
    asset1_ticker = ticker_dictionary.get(asset1)
    df_asset1 = yf.Ticker(asset1_ticker).history(period="max")
    # asset2 conversion only if performing ratio analysis

    asset2_ticker = ticker_dictionary.get(asset2)
    df_asset2 = yf.Ticker(asset2_ticker).history(period="max")

    # calculate ratio
    ratio = df_asset1["Close"]/df_asset2["Close"]
    # drop the incompatible dates
    ratio = ratio.dropna()
    # create date column for plotly
    dates = ratio.index
    # convert to list to append to summary df
    ratio_list = list(ratio)
    # creating master df for ratio and analysis
    master_df["Date"] = dates
    master_df["Ratio"] = ratio_list

    print(master_df)
    fig = px.line(master_df, x="Date", y="Ratio",
                  title=asset1+"/"+asset2 + "Ratio")

    # add slider and quick range buttons to chart
    fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=5, label="5y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    ))
    mean = np.mean(ratio_list)

    if avg == True:
        fig.add_shape(type="line", x0=dates[0], y0=mean,
                      x1=dates[-1], y1=mean, line=dict(color="Black",))
    else:
        pass
    if log == True:
        fig.update_yaxes(type='log')
    else:
        pass

    return fig
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################

# second funtion to show an external chart that allows annotations


def ratio_charting_annotate(asset1, asset2, log, avg):

    pd.set_option('display.max_columns', None)

    master_df = pd.DataFrame()

    # Gather Tickers
    from config import ticker_dictionary

    # check if input is valid
    tickers = list(ticker_dictionary.values())
    valid_input_list = list(ticker_dictionary.keys())

    # convert input to yfinance ticker
    asset1_ticker = ticker_dictionary.get(asset1)
    df_asset1 = yf.Ticker(asset1_ticker).history(period="max")
    # asset2 conversion only if performing ratio analysis

    asset2_ticker = ticker_dictionary.get(asset2)
    df_asset2 = yf.Ticker(asset2_ticker).history(period="max")

    # calculate ratio
    ratio = df_asset1["Close"]/df_asset2["Close"]
    # drop the incompatible dates
    ratio = ratio.dropna()
    # create date column for plotly
    dates = ratio.index
    # convert to list to append to summary df
    ratio_list = list(ratio)
    # creating master df for ratio and analysis
    master_df["Date"] = dates
    master_df["Ratio"] = ratio_list

    print(master_df)
    fig = px.line(master_df, x="Date", y="Ratio",
                  title=asset1+"/"+asset2 + "Ratio")

    # add slider and quick range buttons to chart
    fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=5, label="5y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    ))
    fig.update_layout(
        dragmode='drawopenpath',
        newshape_line_color='orange')

    mean = np.mean(ratio_list)

    if avg == True:
        fig.add_shape(type="line", x0=dates[0], y0=mean,
                      x1=dates[-1], y1=mean, line=dict(color="Black",))
    else:
        pass
    if log == True:
        fig.update_yaxes(type='log')
    else:
        pass

    return fig.show(config={'modeBarButtonsToAdd': ['drawline',
                                                    'drawopenpath',
                                                    'drawclosedpath',
                                                    'drawcircle',
                                                    'drawrect',
                                                    'eraseshape'
                                                    ]})
