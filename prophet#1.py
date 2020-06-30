import logging
import pandas as pd 
import matplotlib.pyplot as plt
from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot

#df = pd.read_csv('/home/euijin/dev/ml/data/example_wp_log_peyton_manning.csv')
#df.head()

# prophet의 로그 기능 끄기
logging.getLogger('fbprophet').setLevel(logging.WARNING)

url = "https://raw.githubusercontent.com/facebook/prophet/master/examples/example_wp_log_peyton_manning.csv"
df = pd.read_csv(url)
df.tail()

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=365)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = m.plot(forecast)
# plt.show(fig1)

#fig2 = m.plot_components(forecast)
# plt.show(fig2)

a = add_changepoints_to_plot(fig1.gca(), m, forecast, threshold=0)
plt.show()


