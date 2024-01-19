import time
import datetime
import pymysql
import yaml

import yaml
import pymysql

def read_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        return yaml.safe_load(file)


def compare_dicts(dict1, dict2):
    diff = {}
    for key in dict1.keys() | dict2.keys():
        if dict1.get(key) != dict2.get(key):
            diff[key] = (dict1.get(key).__str__(), dict2.get(key).__str__())
    return diff

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
            print(db_config)
            print(type(db_config))

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


# 创建数据库连接

def read_and_writ(dbname,yamldb):
    zidian = {}
    connection = connect_to_database(dbname)

    try:
        with connection.cursor() as cursor:
            # 获取所有表的名称
            # 如果有 'id' 列，则执行查询
            query = f"SELECT TABLE_NAME, UPDATE_TIME FROM information_schema.`TABLES` WHERE TABLE_SCHEMA={dbname} AND UPDATE_TIME is not NULL ORDER BY UPDATE_TIME DESC"
            try:
                cursor.execute(query)
                last_record = cursor.fetchall()
                for table in last_record:
                    zidian[table[0]]=table[1]
                print(last_record)
                # print(f"\"{table_name}\":{last_record[0]},")
            except:
                print()
                # print(table_name + "  pass")


            with open(yamldb, 'w', encoding='utf8') as file:
                yaml.dump(zidian, file, allow_unicode=True)

    finally:
        connection.close()
if __name__ == '__main__':

    read_and_writ("phoenix_c2",'1.yaml')
    input("等等")
    read_and_writ("phoenix_exec_c2",'2.yaml')
    # 读取 YAML 文件
    yaml_dict1 = read_yaml_file('1.yaml')
    yaml_dict2 = read_yaml_file('2.yaml')

    # 比较字典
    differences = compare_dicts(yaml_dict1, yaml_dict2)
    if differences:
        print("在两个 YAML 文件之间找到的差异:", differences)
    else:
        print("两个 YAML 文件内容相同。")
