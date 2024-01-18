import yaml
import pymysql

def connect_to_database(db_name):
    """
    连接到指定名称的数据库。

    :param db_name: 数据库名称
    :return: 数据库连接对象
    """
    try:
        # 读取数据库配置
        with open('db_config.yaml', 'r', encoding='utf8') as file:
            config = yaml.safe_load(file)
            db_config = config[db_name]

        # 建立数据库连接
        connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['name'],
            port=db_config['port']
        )

        print(f"成功连接到 MySQL 数据库 '{db_name}'")
        return connection

    except pymysql.MySQLError as e:
        print(f"连接错误：{e}")
        return None

def main():
    # 指定要连接的数据库名称
    database_name = 'mydatabase'

    # 连接到数据库
    db_connection = connect_to_database(database_name)
    if db_connection:
        # 在这里执行数据库操作
        # ...

        # 关闭数据库连接
        db_connection.close()

if __name__ == "__main__":
    main()
