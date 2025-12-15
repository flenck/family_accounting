import sqlite3

conn = sqlite3.connect("family.db")
cursor = conn.cursor()

# 插入测试数据
cursor.execute("INSERT INTO users (name) VALUES (?)", ("你自己",))
cursor.execute("INSERT INTO households (name) VALUES (?)", ("我的家庭",))
cursor.execute("""
INSERT INTO transactions (household_id, amount_cents, note, occurred_at)
VALUES (?, ?, ?, datetime('now'))
""", (1, 10000, "测试买菜"))

conn.commit()

# 查询
cursor.execute("SELECT * FROM transactions;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()