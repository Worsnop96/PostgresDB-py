import psycopg2

conexion = psycopg2.connect(user='postgres', password='virus', host='localhost', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
           sentencia="select *from persona where id in (1,2)"
           cursor.execute(sentencia, (id,))
           registros = cursor.fetchall()
           for registro in registros:
            print(registro)
except Exception as e:
    print(f'ha ocurrido un error de tipo {e}')
finally:
    conexion.close()