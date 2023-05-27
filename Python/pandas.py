# 헤더 복수로 불러오기
RAW_DATA = pd.read_excel("/fileName.xlsx",
                         sheet_name="sheetName", header=[0,1,2])
# 헤더 하나 제거
RAW_DATA.columns.droplevel(0)