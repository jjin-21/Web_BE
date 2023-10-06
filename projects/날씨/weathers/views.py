from django.shortcuts import render

# Create your views here.

import pandas as pd
csv_path = 'example/austin_weather.csv'
def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df': df,
    }
    return render(request, 'weathers/problem1.html', context)


import matplotlib.pyplot as plt
# io : 입출력 연산을 위한  Python 표준 라이브러리
# BytesIO : 이진 데이터를 다루기 위한 버퍼를 제공
# 버퍼 : 임시 저장 공간 / 파일 시스템과 유사하지만, 실제로 파일을 만들지
# 않고 메모리 단에서 작업할 수 있음
from io import BytesIO

# 텍스트 <-> 이진 데이터를 변환할 수 있는 모듈
import base64

# 터미널 에러 해결법
plt.switch_backend('Agg')

# plot => 이진 데이터 => 버퍼(저장) => (저장 주소) => templates
def problem2(request):
    df = pd.read_csv(csv_path)
    
    # Date 열을 날짜 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])
    
    # x 축에 표시할 날짜 범위를 6개월 간격으로 생성
    date_range = pd.date_range(start=df['Date'].min(), end=df['Date'].max(), freq='6M')
    
    date = df['Date']
    tempH = df['TempHighF']
    tempA = df['TempAvgF']
    tempL = df['TempLowF']
    
    plt.figure(figsize=(9,6))

    plt.plot(date, tempH, label='High Temperature')
    plt.plot(date, tempA, label='Average Temperature')
    plt.plot(date, tempL, label='Low Temperature')
    
    plt.title('Temperature Variation')
    
    # x 축에 6개월 단위로 레이블 설정
    plt.xticks(date_range, date_range.strftime('%Y-%m-%d'))
    
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.grid(True)
    plt.legend(loc='lower center')
    
    # 버퍼에 그래프를 저장
    buffer = BytesIO()

    # 버퍼에 그래프를 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64로 인코딩 후 사용할 수 있도록 디코딩 & 다듬기
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    
    # 버퍼를 닫아줌
    buffer.close()
    
    # 이미지를 웹 페이지에 표시하기 위해
    # URL 형식(주소 형식)으로 만들어진 문자열을 생성
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'weathers/problem2.html', context)


def problem3(request):
    df = pd.read_csv(csv_path)

    # 날짜 열을 날짜 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])

    # 온도 열을 숫자 형식으로 변환
    df['TempHighF'] = df['TempHighF'].astype(float)
    df['TempAvgF'] = df['TempAvgF'].astype(float)
    df['TempLowF'] = df['TempLowF'].astype(float)

    plt.figure(figsize=(9,6))

    # 날짜 열을 월로 그룹화하고 월별 최고, 평균, 최저 온도의 평균 계산
    monthly_data = df.groupby(df['Date'].dt.strftime('%Y-%m')).agg({
        'TempHighF': 'mean',
        'TempAvgF': 'mean',
        'TempLowF': 'mean'
    }).reset_index()

    # 원하는 날짜 범위 설정
    start_date = '2014-01'
    filtered_data = monthly_data[(monthly_data['Date'] >= start_date)]

    # 그래프 그리기
    plt.clf()
    plt.plot(filtered_data['Date'], filtered_data['TempHighF'], label='High Temperature')
    plt.plot(filtered_data['Date'], filtered_data['TempAvgF'], label='Average Temperature')
    plt.plot(filtered_data['Date'], filtered_data['TempLowF'], label='Low Temperature')
    plt.title("Temperature Variation")
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend(loc='lower right')

    # 6개월 단위로 그리드 라인 설정
    xticks = filtered_data['Date'][::6]  # 6개월 간격으로 라인 표시
    plt.xticks(xticks)
    
    plt.grid(True)

    buffer_m = BytesIO()

    plt.savefig(buffer_m, format='png')

    image_base64 = base64.b64encode(buffer_m.getvalue()).decode('utf-8').replace('\n','')

    buffer_m.close()
    
    context = {
        'month_chart_image' : f'data:image/png;base64, {image_base64}',
    }
    return render(request, 'weathers/problem3.html', context)



def problem4(request):
    df = pd.read_csv(csv_path)

    # 'Event' 컬럼의 결측치를 빈 문자열로 대체
    df['Events'].fillna('', inplace=True)

    # 'Event' 컬럼의 각 이벤트 종류를 카운트
    event_counts = df['Events'].str.split(',').explode().str.strip().value_counts()

    # 'Event' 컬럼에서 빈 문자열인 경우를 "No Event"로 대체
    event_counts[''] = event_counts.get('', 0)  # 빈 문자열을 "No Event"로 이름 변경
    event_counts.rename(index={'': 'No Events'}, inplace=True)


    plt.figure(figsize=(9,6))
    
    event_counts.plot(kind='bar', color='Blue')
    
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.title('Event Counts')
    
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.grid()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}'
    }

    return render(request, 'weathers/problem4.html', context)