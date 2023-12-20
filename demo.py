import requests
import json

def read_and_parse_json(file_path):
    """从文件中读取每行并将其解析为JSON对象"""
    json_objects = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                json_object = json.loads(line.strip())
                json_objects.append(json_object)
            except json.JSONDecodeError:
                print("解析JSON时出错，行内容: ", line)
    return json_objects

def send_request(url, method, headers, payload):
    """发送HTTP请求并返回响应"""
    try:
        # 根据请求方法发送请求
        if method.lower() == 'get':
            response = requests.get(url, headers=headers, params=payload)
        elif method.lower() == 'post':
            response = requests.post(url, headers=headers, json=payload)
        else:
            print("不支持的请求方法:", method)
            return None
        return response
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return None

def write_response_to_file(response, file_path):
    """将HTTP响应写入文件"""
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"状态码: {response.status_code}\n")
        file.write(f"响应内容: {response.text}\n")

def process_json_objects(json_objects, url, method, headers, output_file):
    """处理JSON对象列表，对每个对象发送请求并记录响应"""
    for json_obj in json_objects:
        response = send_request(url, method, headers, json_obj)
        if response:
            write_response_to_file(response, output_file)

def read_first_line_and_convert_to_dict(file_path):
    """读取文件的第一行并将其转换为字典"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.loads(file.readline().strip())
    except FileNotFoundError:
        return "文件不存在。"
    except json.JSONDecodeError as e:
        return f"转换时出错：{e}"

def main(file_path, output_file):
    """主函数，执行程序的主要逻辑"""
    json_objects = read_and_parse_json(file_path)
    base_url = "https://www.baidu.com"  # 示例URL，应根据实际情况修改
    headers = {}
    method = "post"  # 示例方法，应根据实际情况修改

    # 对读取的每个JSON对象发送请求
    for json_obj in json_objects:
        process_json_objects(json_obj, base_url, method, headers, output_file)

    # 读取文件的第一行并转换为字典，然后打印
    first_line_dict = read_first_line_and_convert_to_dict(file_path)
    print(json.dumps(first_line_dict, ensure_ascii=False))

if __name__ == "__main__":
    file_path = '1.txt'  # 输入文件路径
    output_file = '2.txt'  # 输出文件路径
    main(file_path, output_file)
