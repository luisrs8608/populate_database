import csv

def populate_table(conn, cr, data_record):
    file_name = data_record['file_name']
    table = data_record['table']
    fields = data_record['fields']
    query = '''INSERT INTO {}({}) VALUES '''.format(table, ','.join(field[0] for field in fields))
    file_path = 'data/{}'.format(file_name)

    with open(file_path, 'r') as file:
        csv_file = csv.DictReader(file)
        data_list = []
        values = []
        placeholders = ','.join(['%s' for i in range(len(fields))])
        for row in csv_file:
            items = []
            for field in fields:
                if field[1] == 'int':
                    value = int(row[field[0]])
                elif field[1] == 'char':
                    value = row[field[0]]
                items.append(value)
            values.append('({0})'.format(placeholders))
            data_list.extend(items)
        query += ', '.join(str(data) for data in values)

    cr.execute(query, data_list)
    conn.commit()
    count = cr.rowcount
    print(count, "Record inserted successfully")
