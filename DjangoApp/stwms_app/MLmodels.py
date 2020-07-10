import pandas as pd
from matplotlib import pyplot as plt
from fbprophet import Prophet
from time import time
from .models import TransactionHistory
from multiprocessing import Process, Queue


def post_data_clean(temp_df):
    temp_df['ds'] = pd.to_datetime(temp_df['ds']).dt.strftime('%d %b')
    temp_df = temp_df.drop([
        'additive_terms', 'additive_terms_lower', 'additive_terms_upper',
        'multiplicative_terms', 'multiplicative_terms_lower', 'multiplicative_terms_upper'
    ], axis=1)
    labels = temp_df.ds.values
    temp_df = temp_df.round(2)
    indexList = list(temp_df.columns)
    ele = indexList.pop(-1)
    indexList.insert(1, ele)
    temp_df = temp_df[indexList]
    return [labels, temp_df]


class TimeSeriesModel:

    def __init__(self, raw_material_id, store_id, future_period):
        self.df = ''
        self.prediction_size = future_period
        self.error_log = {}
        self.queue = Queue()
        self.fbP_model = Prophet(weekly_seasonality=True, daily_seasonality=True, yearly_seasonality=True)
        self.get_data(raw_material_id, store_id)
        self.pre_data_clean()

    def get_data(self, raw_material_id, store_id):
        self.df = TransactionHistory.objects.filter(rawMaterial_id_id=raw_material_id, storeId_id=store_id) \
            .to_dataframe()

    def pre_data_clean(self, with_time=False):
        raw_df = self.df
        if with_time:
            raw_df['dateTime'] = pd.to_datetime(raw_df['dateTime']).dt.tz_convert('Asia/Kolkata').dt.tz_localize(None)
        else:
            raw_df['dateTime'] = pd.to_datetime(raw_df['dateTime']).dt.date
        final_df = raw_df.drop(['transaction_id', 'rawMaterial_id', 'storeId'], axis=1)
        final_df.rename(columns={'dateTime': 'ds', 'units': 'y'}, inplace=True)
        self.df = final_df.sort_values(by="ds")

    def plot_df(self):
        plt.figure(figsize=(17, 8))
        plt.plot(self.df['ds'], self.df['y'])
        plt.xlabel('Date')
        plt.ylabel('Quantity')
        plt.show()

    def make_forecast(self, var_name, period):
        temp_list = [var_name]
        futureD = self.fbP_model.make_future_dataframe(periods=self.prediction_size, freq=period)
        temp_list.append(self.fbP_model.predict(futureD)[-self.prediction_size:])
        self.queue.put(temp_list)

    def fb_prophet(self, plot=False):
        self.fbP_model.fit(self.df)

        q = Queue()

        # Day Forecast
        day = Process(target=self.make_forecast, args=('forecast_day', 'D'))

        # Hourly Forecast
        hour = Process(target=self.make_forecast, args=('forecast_hour', 'H'))

        # Weekly Forecast
        week = Process(target=self.make_forecast, args=('forecast_hour', 'W'))
        
        # Monthly Forecast
        month = Process(target=self.make_forecast, args=('forecast_hour', 'M'))

        start = time()
        day.start()
        month.start()
        week.start()
        hour.start()
        
        day.join()
        month.join()
        week.join()
        hour.join()
        end = time()
        print(end - start)

        forecasts = {}
        for i in range(4):
            temp_list = self.queue.get()
            forecasts[temp_list[0]] = temp_list[1]

        print(forecasts)

        if plot:
            self.fbP_model.plot_components(forecasts['forecast_day'])
            plt.show()

        forecast_day = post_data_clean(forecasts['forecast_day'])
        forecast_hour = post_data_clean(forecasts['forecast_hour'])
        forecast_week = post_data_clean(forecasts['forecast_week'])
        forecast_month = post_data_clean(forecasts['forecast_month'])

        return forecast_day, forecast_hour, forecast_week, forecast_month
