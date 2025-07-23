# Create paint observation database
from modules.mysql_connection import MySQLConnector

config = {
    'host': 'localhost',
    'user': 'shinleonhardt',
    'password': '12345678',
    'database': 'paint_observe_db',
    'auth_plugin':'mysql_native_password'
}

conn = MySQLConnector(config['host'], config['user'],config['password'], config['database'], config['auth_plugin'])

create_table_query = """
CREATE TABLE IF NOT EXISTS paint_process_logs (
    ngay VARCHAR(50), 
    phong_son VARCHAR(50),
    ten_san_pham VARCHAR(50),
    ma_san_pham VARCHAR(50),
    vat_lieu VARCHAR(50),
    ten_chi_tiet VARCHAR(50),
    loai_hang VARCHAR(50),
    lenh_san_xuat INT,
    dien_tich_chi_tiet FLOAT,
    mau_son VARCHAR(50),
    ma_mau_son VARCHAR(50),
    van_toc_bang_tai FLOAT,
    ap_suat_bot FLOAT,
    ap_suat_gio FLOAT,
    do_day_son VARCHAR(50),
    do_bam_son VARCHAR(50),
    so_luong INT,
    thung_son_moi FLOAT,
    thung_son_thu_hoi FLOAT,
    thung_son_tra_ve FLOAT,
    thung_son_tieu_hao FLOAT
)
"""

if __name__ == "__main__":
    conn.create_connection(create_table_query)

