import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from fbprophet import Prophet


class TimeSeriesModel:

    def __init__(self, file='Online Retail.csv', item_index=False, future_period=30):
        self.df = pd.read_csv(file)
        self.item_index = item_index
        self.prediction_size = future_period
        self.error_log = {}

    def getData(self):
        #TODO: Finish
        pass

    def data_clean(self):
        raw_df = self.df
        raw_df.Description = pd.Categorical(raw_df.Description)
        raw_df['item'] = raw_df.Description.cat.codes
        raw_df['Date_Time'] = pd.to_datetime(raw_df['Date_Time'])
        mod_df = raw_df.drop(['Description', 'Time', 'InvoiceNo'], axis=1)
        mod_df.rename(columns={'Date_Time': 'ds', 'Quantity': 'y'}, inplace=True)
        pos_df = mod_df[mod_df['y'] > 0]
        if self.item_index:
            pos_df = pos_df[pos_df['item'] == self.item_index]
        final_df = pos_df.drop(['item'], axis=1)
        self.df = final_df.sort_values(by="ds")

    def plot_df(self):
        plt.figure(figsize=(17, 8))
        plt.plot(self.df['ds'], self.df['y'])
        plt.xlabel('Date')
        plt.ylabel('Quantity')
        plt.show()

    def fb_prophet(self, plot=False):
        self.data_clean()
        fbP_model = Prophet()
        fbP_model.fit(self.df)
        future = fbP_model.make_future_dataframe(periods=self.prediction_size)
        forecast = fbP_model.predict(future)

        y_hat = forecast['yhat'][-self.prediction_size:]
        y_hat.reset_index(drop=True, inplace=True)

        if plot:
            plt.plot(forecast['ds'], forecast['yhat'])
            plt.plot(self.df['ds'], self.df['y'], color='red')
            plt.show()


model = TimeSeriesModel('datasets/Online Retail.csv')
model.fb_prophet(plot=True)
