import yaml

# 先切割，根据字典切割，切割成不同的列表，
# 之后把所有列表转成元祖
# 然后把元祖拼接起来
# 之后转成列表
def get_yaml_data(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    res = yaml.load(file, Loader=yaml.FullLoader)
    temp = []
    for i in res:
        temp.append(tuple(i.values()))
    return temp

def get_one_yaml_data(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    res = yaml.load(file, Loader=yaml.FullLoader)
    temp = res[0].get('url')
    return temp


if __name__ == '__main__':
    resp1 = get_yaml_data("../data/home_project/cases/test002_try_test_api.yaml")
    resp2 = get_one_yaml_data("../data/home_project/apis/test002_try_test_api.yaml")
    # print(resp)
    print(resp1)
    print(resp2)