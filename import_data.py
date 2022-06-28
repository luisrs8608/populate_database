import csv
import pg_connection as pg_conn

def populate_table():
    conn = pg_conn.connect()
    cr = pg_conn.create_cursor(conn)

    query = '''INSERT INTO public.country(id, name) VALUES '''

    with open('.data/pais.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        data_list = []
        for row in csv_file:
            data_list.append((int(row['id']), row['name']))
        query += ', '.join(str(data) for data in data_list)

    cr.execute(query)
    conn.commit()
    count = cr.rowcount
    print(count, "Record inserted successfully")
    pg_conn.close_connect(conn, cr)

if __name__ == '__main__':
    populate_table()