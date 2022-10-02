import os
import argparse
import yaml
import logging


def read_params(config_path):
    """
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def main(config_path, data_source):
    """
    """
    config = read_params(config_path=config_path)
    print(config)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    ROOT_DIR = "/Users/vamsinimmala/PycharmProjects/wafer_project/mlops_main/"

    default_config_path = os.path.join(ROOT_DIR,"config", "params.yaml")
    args.add_argument("--config", default=default_config_path)
    args.add_argument("--datasource", default=None)

    parsed_args = args.parse_args()

    main(config_path=parsed_args.config, data_source=parsed_args.datasource)

