# 헤더 복수로 불러오기
RAW_DATA = pd.read_excel("/fileName.xlsx",
                         sheet_name="sheetName", header=[0,1,2])
# 헤더 하나 제거
RAW_DATA.columns.droplevel(0)

# 조건에 맞는 행 찾기
RAW_DATA.loc[RAW_DATA['FDAgroup1'] == 2]

# 인덱스 0부터 재설정하기
RAW_DATA.reset_index(drop=True)