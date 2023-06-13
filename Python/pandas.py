# 헤더 복수로 불러오기
RAW_DATA = pd.read_excel("/fileName.xlsx",
                         sheet_name="sheetName", header=[0,1,2])
# 헤더 하나 제거
RAW_DATA.columns.droplevel(0)

# 헤더 지정
RAW_DATA.columns = raw_columns

# 조건에 맞는 행 찾기
RAW_DATA.loc[RAW_DATA['FDAgroup1'] == 2]

# 인덱스 0부터 재설정하기
RAW_DATA.reset_index(drop=True)

# 회귀분석 (centered)
sm.OLS(TARGET_DATA['y'], sm.add_constant(TARGET_DATA['x'])).fit()

# 히스토그램
plt.hist(TARGET_DATA['resid'], bins = 30)

# 피어슨 상관계수 구하기
correlation_coefficient = TARGET_DATA['A'].corr(TARGET_DATA['B'])

# 열 기준 병합
MERGED_DATA = pd.merge(DATA1, DATA2, on='열 제목', how='inner')