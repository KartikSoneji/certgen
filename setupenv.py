import os

ENV_FILE = ".env"


def get_data_as_dict(path):
    try:
        with open(path, "r") as f:
            return dict(
                tuple(line.replace("\n", "").split("="))
                for line in f.readlines()
                if len(line.strip()) > 0 and not line.lstrip().startswith("#")
            )
    except FileNotFoundError:
        return {}


for variable, value in get_data_as_dict(ENV_FILE).items():
    os.environ[variable] = value
