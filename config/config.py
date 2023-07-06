from dotenv import load_dotenv
from pathlib import Path

application_env = 'development' # 'development', 'testing' or 'deployment'

from .settings import Config
Config(application_env)

from dotenv import load_dotenv
from pathlib import Path

## LOAD AWS CONFIGURATION FROM .AWSENV FILE
env_path = Path('.') / '.awsenv'
load_dotenv(dotenv_path=env_path)

