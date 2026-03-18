import sqlite3
def tao_bang_dulieu():
    conn = sqlite3.connect('quanly_sinhvien.db')
    cur = conn.cursor()
    cur.execute(''' 
                    CREATE TABLE IF NOT EXISTS SinhVien (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ho_ten TEXT NOT NULL,
                tuoi INTEGER,
                nganh_hoc TEXT
                )
            ''')
    conn.commit()
    conn.close()

tao_bang_dulieu()