import urllib.request
import json
import datetime
import webbrowser



data = input("Codigo País: ")



webbrowser.open('https://timezonedb.com/country-codes')

contents = urllib.request.urlopen("http://api.timezonedb.com/v2/list-time-zone?key=6I35P7039N8L&format=json&country=CR").read().decode('utf8')

wjdata = json.loads(contents)
unix_time = wjdata['zones'][0]['timestamp']




variable = datetime.datetime.utcfromtimestamp(
        int(unix_time)
    ).strftime('%Y-%m-%d %H:%M:%S')



print(variable)



