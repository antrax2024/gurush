# This is the version of the application.
import os


APP_VERSION = "0.2.6"
# This is the name of the application.
APP_NAME = "gurush"

CONFIG_FILE = os.path.join(
    os.path.expanduser(path="~"), ".config", f"{APP_NAME}", "config.yaml"
)
