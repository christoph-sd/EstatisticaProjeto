from functions.data import download_history
from plotly.graph_objects import Figure
import plotly.express as px

def plot_history(ticker:str) -> Figure:
    """
        Plot historical data from yahoo finance.
            Args:
        ticker (str): Ticker name.
    """


    df = download_history('BBAS3.SA')
    fig = px.line (
        df,
        x = 'Date',
        y = 'Close',
        title = f'{ticker} stock price.' 
    )
    return fig