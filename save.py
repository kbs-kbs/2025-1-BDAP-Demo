import requests
import pandas as pd
from datetime import datetime, timedelta

API_KEY = '55546a414d79616735317868654874'  # 본인의 인증키로 교체
BASE_URL = 'http://openapi.seoul.go.kr:8088'
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 12, 31)

date_counts = {}

current_date = START_DATE
while current_date <= END_DATE:
    day = current_date.strftime('%Y-%m-%d')
    daily_count = 0

    for hour in range(24):  # 0~23시까지 루프
        url = f"{BASE_URL}/{API_KEY}/json/tbCycleRentData/1/1/{day}/{hour}"
        response = requests.get(url)
        data = response.json()

        # "rentData"와 "list_total_count"가 있으면 더하기
        try:
            count = int(data['rentData']['list_total_count'])
        except (KeyError, ValueError, TypeError):
            count = 0

        daily_count += count

    date_counts[day] = daily_count
    print(f"{day} 처리 완료 ({daily_count}건)")

    current_date += timedelta(days=1)

# CSV 저장
df = pd.DataFrame(sorted(date_counts.items()), columns=['date', 'rent_count'])
df.to_csv('seoul_bike_rentals_2024.csv', index=False, encoding='utf-8-sig')

print("CSV 파일 저장 완료!")
