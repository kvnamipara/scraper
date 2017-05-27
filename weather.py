import requests
from bs4 import BeautifulSoup
url1='http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WSkN-BOGMUs'
url2='http://forecast.weather.gov/MapClick.php?lat=44.2503&lon=-85.5003#.WSkSYhOGMUs'
page = requests.get(url1)
soup = BeautifulSoup(page.content,'html.parser')
#general forecast
seven_day_info = soup.find(id='seven-day-forecast')
forecast = seven_day_info.find_all(class_='tombstone-container')
tonight= forecast[0]
location= seven_day_info.find(class_='panel-title').get_text()
period = tonight.find(class_='period-name').get_text()
short_desc = tonight.find(class_='short-desc').get_text()
temp = tonight.find(class_='temp').get_text()
#detailed forecast
detailed_forecast = soup.find(id='detailed-forecast-body')
detailed_today = detailed_forecast.find(class_='forecast-text').get_text()

print 'Location : '+location.strip()
print 'Time : '+period 
print 'Short discription : '+short_desc
print 'Temp : '+temp
print 'Long discription : '+detailed_today
