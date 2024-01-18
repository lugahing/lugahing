import yaml

# 数据库配置
db_config = {
    'database': {
        'name': 'mydatabase',
        'user': 'username',
        'password': 'password',
        'host': 'localhost',
        'port': 3306
    }
}

# 写入到 YAML 文件
with open('db_config.yaml', 'w', encoding='utf8') as file:
    yaml.dump(db_config, file, allow_unicode=True)
