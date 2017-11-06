import requests
from collections import namedtuple
from bs4 import BeautifulSoup
from datetime import date

API_URL = "http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php"
DayWeatherData = namedtuple("DayWeatherData",
                            ['date',
                             'atmospheric_pressure',
                             'sea_atmospheric_pressure',
                             'precipitation',
                             'max_hour_precipitation',
                             'max_10minutes_precipitation',
                             'ave_temperature',
                             'max_temperature',
                             'min_temperature',
                             'ave_humidity',
                             'min_humidity',
                             'ave_wind_speed',
                             'max_wind_speed',
                             'max_wind_direction',
                             'max_instantaneous_wind_speed',
                             'max_instantaneous_wind_direction',
                             'sunshine_hours',
                             'total_snowfall',
                             'deepest_snow_cover',
                             'daytime_weather',
                             'night_weather',
                             ])


def convert(value):
    value = value.replace(' )', '')
    if '--' in value:
        return None
    if '.' in value:
        return float(value)
    try:
        return int(value)
    except ValueError:
        return value


def get(prec_no, block_no, year, month):
    r = requests.get(API_URL, params={'prec_no': prec_no, 'block_no': block_no, 'year': year, 'month': month})
    text = r.content.decode('utf8')
    soup = BeautifulSoup(text, 'html.parser')

    for tr in soup.find_all('tr', attrs={'style': 'text-align:right;'}):
        td_list = tr.find_all('td')

        # 日
        day = convert(td_list[0].text)

        # 気圧(hPa)	現地 平均
        atmospheric_pressure = convert(td_list[1].text)

        # 気圧(hPa)	海面 平均
        sea_atmospheric_pressure = convert(td_list[2].text)

        # 降水量(mm) 合計
        precipitation = convert(td_list[3].text)

        # 降水量(mm) 最大 1時間
        max_hour_precipitation = convert(td_list[4].text)

        # 降水量(mm) 最大 10分間
        max_10minutes_precipitation = convert(td_list[5].text)

        # 気温(℃) 平均
        ave_temperature = convert(td_list[6].text)

        # 気温(℃) 最高
        max_temperature = convert(td_list[7].text)

        # 気温(℃) 最低
        min_temperature = convert(td_list[8].text)

        # 湿度(％) 平均
        ave_humidity = convert(td_list[9].text)

        # 湿度(％) 最小
        min_humidity = convert(td_list[10].text)

        # 風向・風速(m/s) 平均風速
        ave_wind_speed = convert(td_list[11].text)

        # 風向・風速(m/s) 最大風速 風速
        max_wind_speed = convert(td_list[12].text)

        # 風向・風速(m/s) 最大風速 風向
        max_wind_direction = convert(td_list[13].text)

        # 風向・風速(m/s) 最大瞬間風速 風速
        max_instantaneous_wind_speed = convert(td_list[14].text)

        # 風向・風速(m/s) 最大瞬間風速 風向
        max_instantaneous_wind_direction = convert(td_list[15].text)

        # 日照時間(h)
        sunshine_hours = convert(td_list[16].text)

        # 雪(cm) 降雪 合計
        total_snowfall = convert(td_list[17].text)

        # 雪(cm) 最深積雪 値
        deepest_snow_cover = convert(td_list[18].text)

        # 天気概況 昼 (06:00-18:00)
        daytime_weather = convert(td_list[19].text)

        # 天気概況 夜 (18:00-翌日06:00)
        night_weather = convert(td_list[20].text)

        day_weather_data = DayWeatherData(
            date=date(year=year, month=month, day=day),
            atmospheric_pressure=atmospheric_pressure,
            sea_atmospheric_pressure=sea_atmospheric_pressure,
            precipitation=precipitation,
            max_hour_precipitation=max_hour_precipitation,
            max_10minutes_precipitation=max_10minutes_precipitation,
            ave_temperature=ave_temperature,
            max_temperature=max_temperature,
            min_temperature=min_temperature,
            ave_humidity=ave_humidity,
            min_humidity=min_humidity,
            ave_wind_speed=ave_wind_speed,
            max_wind_speed=max_wind_speed,
            max_wind_direction=max_wind_direction,
            max_instantaneous_wind_speed=max_instantaneous_wind_speed,
            max_instantaneous_wind_direction=max_instantaneous_wind_direction,
            sunshine_hours=sunshine_hours,
            total_snowfall=total_snowfall,
            deepest_snow_cover=deepest_snow_cover,
            daytime_weather=daytime_weather,
            night_weather=night_weather,
        )
        print(day_weather_data)


get(prec_no=14, block_no=47412, year=2014, month=10)
