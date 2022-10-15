import yaml


class Config:
    def __int__(self):
        self.config = None

    def load_config(self):
        with open("./src/config/config.yaml", "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        return data


#
# if __name__== '__main__':
#     cfg = Config()
#     data = cfg.load_config()
#     print(data['topic']['raw'])
#
