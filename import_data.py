import pg_connection as pg_conn
import populate_table as pt


data = [
    {
        'file_name': 'pais.csv',
        'table': 'shared_app_country',
        'fields': [('id', 'int'), ('name', 'char')]
    },
    {
        'file_name': 'estado.csv',
        'table': 'shared_app_state',
        'fields': [('id', 'int'), ('name', 'char'), ('country_id', 'int')]
    },
    {
        'file_name': 'ciudad.csv',
        'table': 'shared_app_city',
        'fields': [('id', 'int'), ('name', 'char'), ('state_id', 'int')]
    },
]

def import_data():
    conn = pg_conn.connect()
    cr = pg_conn.create_cursor(conn)

    for rec in data:
        pt.populate_table(conn, cr, rec)

    pg_conn.close_connect(conn, cr)

if __name__ == '__main__':
    import_data()