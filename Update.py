import psycopg2

conexion = psycopg2.connect(user="postgres", password="virus", host="localhost", port='5432', database="test_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "update persona set nombre=%s, apellido=%s where id=%s"
            valores= ('juan manuel', 'arrecife',4)
            cursor.execute(sentencia, valores)
            registros = cursor.rowcount
            print(f'registros modificados {registros}')

except Exception as e:
    print(f'ha ocurrido un error de tipo {e}')
finally:
    conexion.close()