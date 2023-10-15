from pytrends.request import TrendReq
import seaborn as sns
import matplotlib.pyplot as plt

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Australian Cattle"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
interest_by_region = pytrends.interest_by_region(resolution='COUNTRY')
data = interest_by_region.sort_values(by="Australian Cattle", ascending=False)
data = data.head(10)
print(data)


data.reset_index().plot(x="geoName",
                        y="Australian Cattle",
                        figsize=(15,12), kind="bar")
plt.show()