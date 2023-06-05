def insert_data(df, table_name, cursor):
    cols = ", ".join(df.columns)
    insert_query = f"INSERT INTO {table_name} ({cols}) VALUES ({', '.join(['%s'] * len(df.columns))})"

    batch_size = 1000  # Number of rows per batch
    values = [tuple(row) for row in df.values]

    # Insert the DataFrame rows into the MySQL table in batches
    for i in range(0, len(values), batch_size):
        batch = values[i:i+batch_size]
        cursor.executemany(insert_query, batch)