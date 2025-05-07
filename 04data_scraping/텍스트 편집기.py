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

            try:
                # "매각사례" 섹션 찾기
                auction_sections = driver.find_elements(By.CSS_SELECTOR, "#lyCnt_add .sectTitle")
                auction_table = None

                for section in auction_sections:
                    title_element = section.find_element(By.CSS_SELECTOR, "dt")
                    title_text = title_element.text.strip()

                    if "매각사례" in title_text:
                        # 찾으면 바로 다음 테이블
                        auction_table = section.find_element(By.XPATH, "following-sibling::table[1]")
                        break

                if auction_table is None:
                    raise Exception("매각사례 테이블을 찾지 못했습니다.")

                rows = auction_table.find_elements(By.TAG_NAME, "tr")

                if len(rows) > 1:
                    first_row = rows[1]
                    cells = first_row.find_elements(By.TAG_NAME, "td")
                    
                    if len(cells) >= 4:
                        raw_text = cells[3].text.strip()
                        # 정규식으로 "숫자.숫자%" 만 필터
                        import re
                        match = re.search(r"\d+\.\d+%", raw_text)
                        if match:
                            average_sale_rate = match.group()
                        else:
                            average_sale_rate = None
                    else:
                        average_sale_rate = None
                else:
                    average_sale_rate = None

                print(f"✅ 예상 낙찰 비율 추출 성공: {average_sale_rate}")

            except Exception as e:
                print(f"⚠️ 예상 낙찰 비율 추출 실패: {e}")
                average_sale_rate = None
    dtc = DecisionTreeClassifier(class_weight="balanced", random_state=10)
    dtc.fit(X_train, y_train)
    pred = dtc.predict(X_test)
    print(classification_report(y_test,pred))

        tc = RandomForestClassifier(class_weight="balanced", random_state=10)
    dtc.fit(X_train, y_train)
    pred = dtc.predict(X_test)
    print(classification_report(y_test,pred))

        xgb = XGBClassifier(random_state=10)
    xgb.fit(X_train, y_train)
    pred = xgb.predict(X_test)
    print(classification_report(y_test, pred))

        rfc2 = RandomForestClassifier(max_depth=9,n_estimators=100, n_jobs=-1, random_state =10)
    rfc2.fit(smt_X, smt_y)
    rfc2_pred = rfc2.predict(X_test)
    print(classification_report(y_test, rfc2_pred))

                if (end_price + expense + 10000000)< real_price and max_pice/start_price*100 > float(average_sale_rate.replace("%","")):
                            decision = 1 
                else: 
                    decision = 0


    km = KMeans(n_clusters=i, random_state=42)
    km.fit(ss_data)
    result = km.labels_
    df2['cluster']= result