import yaml
def yml_data_with_file(file_name):
    with open("./data/" + file_name + ".yaml", "r", encoding='utf-8') as f:
        yaml.warnings({'YAMLLoadWarning': False})
        data = yaml.load(f)
        return data
