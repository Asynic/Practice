import pymysql


config = {
    'host': '192.168.0.102',
    'port': 3306,
    'user': 'root',
    'password': 'root'
}
connection = pymysql.connect(**config,
                             database='practice',)

with connection:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "show tables;"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
