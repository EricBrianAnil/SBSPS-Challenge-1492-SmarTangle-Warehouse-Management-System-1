from datetime import datetime
import pandas as pd
# from influxdb_client import InfluxDBClient, Point, WritePrecision
# from influxdb_client.client.write_api import SYNCHRONOUS

# token = "NCAxa9xp-pPyTDYnCrkKowLETS_RSKY2gsTajAh9GKDmMv9NOTQPyYa6DsuBHEMGgeMDm6mUy9qBK5bUDKuiLQ=="
# org = "1faff460d4557f87"
# bucket = "05d45ac3d810e000"
# client = InfluxDBClient(url="https://us-central1-1.gcp.cloud2.influxdata.com", token=token)
# write_api = client.write_api(write_options=SYNCHRONOUS)


data = pd.read_csv('gfa25.csv', encoding='cp1252')
items_list = ['Production Quantity', 'Food Availability per capita', 'Food Supply']
formatted_data = data[data.Item.isin(items_list) & data.Country.eq('India')]
formatted_data.drop(["Commodity"], axis=1)
series = []
for i in range(len(formatted_data)):
	data_item = formatted_data.iloc[i]
	date_year = datetime(int(data_item.Year) , 1, 1)
	series.append("%s,Unit=%s Amount=%s time=%s"%(data_item.Country, data_item.Unit, data_item.Amount, date_year))

print(series)

# data = "mem,host=host1 used_percent=23.43234543"
# write_api.write(bucket, org, data)