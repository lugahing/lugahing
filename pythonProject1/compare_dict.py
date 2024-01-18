import yaml

def read_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        return yaml.safe_load(file)

def compare_dicts(dict1, dict2):
    diff = {}
    for key in dict1.keys() | dict2.keys():
        if dict1.get(key) != dict2.get(key):
            diff[key] = (dict1.get(key), dict2.get(key))
    return diff

def main():
    # 读取 YAML 文件
    yaml_dict1 = read_yaml_file("YAML_FILE_PATH_1")
    yaml_dict2 = read_yaml_file("YAML_FILE_PATH_2")

    # 比较字典
    differences = compare_dicts(yaml_dict1, yaml_dict2)
    if differences:
        print("在两个 YAML 文件之间找到的差异:", differences)
    else:
        print("两个 YAML 文件内容相同。")

if __name__ == "__main__":
    main()
