import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
token = os.environ.get("TOKEN")

if token is None:
    raise FileNotFoundError(".envファイルが読み込まれていないのでエラー")

