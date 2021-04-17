import requests
from datetime import datetime
import matplotlib.pyplot as plt

def getDate(timestamp: str):
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%d-%m-%y')


r = requests.get("https://api.alternative.me/fng/?limit=300").json()

dates = []
values = []
for index, day in enumerate(r['data']):
    dates.append(getDate(day['timestamp']))
    values.append(day['value'])

data = {'value' : values, 
        'date' : dates}

fig, ax = plt.subplots()
plt.plot(data['value'])
plt.xticks(range(len(data['date'])), data['date'])
[l.set_visible(False) for (i,l) in enumerate(ax.axes.xaxis.get_ticklabels()) if i % 20 != 0] #label every 20 days
plt.gca().invert_yaxis()
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()
