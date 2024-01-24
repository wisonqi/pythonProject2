import requests
from bs4 import BeautifulSoup
import pymysql

# 连接到MySQL数据库
db = pymysql.connect(host='192.168.200.11', user='root', password='dxJob220322#', db='test')
cursor = db.cursor()

# 获取维基百科页面内容
url = "https://zh.wikipedia.org/zh/%E4%B8%96%E7%95%8C%E6%9C%80%E5%A4%A7%E9%93%B6%E8%A1%8C%E5%88%97%E8%A1%A8"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 定位到“资产规模”标签下的表格
table = soup.find('table', {'class': 'wikitable'})

# 解析表格并提取数据
for row in table.find_all('tr')[1:]:  # 跳过表头
    cols = row.find_all('td')
    if len(cols) > 1:  # 确保行中有数据
        ranking = cols[0].text.strip()
        bank_name = cols[1].text.strip()
        total_assets = cols[2].text.strip()
        total_assets = float(total_assets.replace(',', ''))
        # 插入数据到MySQL
        try:
            query = "INSERT INTO top_bank (ranking, bank_name, total_assets) VALUES (%s, %s, %s)"
            cursor.execute(query, (ranking, bank_name, total_assets))
            db.commit()
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()

# 关闭数据库连接
db.close()
