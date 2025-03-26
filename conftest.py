import os


def pytest_addoption(parser):
    parser.addoption("--api", dest="api", action="store", default="", help="Параметр API_ID")
    parser.addoption("--hash", dest="hash", action="store", default="", help="Параметр HASH_ID")


def pytest_configure(config):
    os.environ["api"] = config.getoption('api')
    os.environ["hash"] = config.getoption('hash')
