apt_info = []
for info in soup.select('item'):
    # 아파트 이름
    soup.select('item')[0].select_one('aptNm').text
    # 행정동
    soup.select('item')[0].select_one('estateAgentSggNm').text
    # 실거래가
    soup.select('item')[0].select_one('dealAmount').text
    # 층수
    soup.select('item')[0].select_one('floor')[0].text
    # 넓이
    soup.select('item')[0].select('excluUseAr')[0].text