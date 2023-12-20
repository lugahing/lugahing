import yaml
import json

def generate_json_example_for_get(parameters):
    """
    根据GET请求的parameters生成JSON示例
    """
    example = {}
    for param in parameters:
        if param['in'] == 'query':
            # 根据参数类型设置默认值
            param_type = param.get('type', 'string')
            if param_type == 'string':
                example[param['name']] = 'string'
            elif param_type == 'integer':
                example[param['name']] = 0
            else:
                example[param['name']] = 'unknown'
    return example

def generate_json_example_for_post(swagger_data, ref):
    """
    根据POST请求的引用生成JSON示例
    """
    ref_path = ref.replace('#/', '').split('/')
    definition = swagger_data
    for part in ref_path:
        definition = definition.get(part, {})

    if 'properties' in definition:
        example = {}
        for prop, details in definition['properties'].items():
            if details['type'] == 'string':
                example[prop] = 'string'
            elif details['type'] == 'integer':
                example[prop] = 0
            else:
                example[prop] = 'unknown'
        return example
    else:
        return {}

def extract_request_params_example(swagger_doc_content):
    """
    从Swagger文档中提取请求参数的JSON示例，并将结果组合成单条JSON
    """
    try:
        swagger_data = yaml.safe_load(swagger_doc_content)
        for path, methods in swagger_data.get("paths", {}).items():
            for method, details in methods.items():
                if method.lower() == 'get':
                    # 处理GET请求
                    example = generate_json_example_for_get(details.get("parameters", []))
                elif method.lower() == 'post':
                    # 处理POST请求
                    ref = details.get("parameters", [{}])[0].get("schema", {}).get("$ref")
                    if ref:
                        example = generate_json_example_for_post(swagger_data, ref)
                else:
                    continue

                result = {
                    "Path": path,
                    "Method": method.upper(),
                    "ParametersExample": example
                }
                return json.dumps(result)
    except yaml.YAMLError as e:
        return f"解析错误: {e}"

if __name__ == "__main__":
    # 主程序运行区域
    file_path = 'swagger_test.yaml'
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取Swagger文件内容
        swagger_doc_content = file.read()

    # 提取请求参数的JSON示例
    json_result = extract_request_params_example(swagger_doc_content)

    output_file_path = '1.txt'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        # 将结果写入文件
        file.write(json_result)
