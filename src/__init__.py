import os
from pathlib import Path

from pyhocon import ConfigFactory
import matplotlib as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
settings = ConfigFactory.parse_file(os.path.join(dir_path, "config", "settings.conf"))

settings.__setattr__("PROJECT_ROOT", Path(dir_path).parent)
settings.__setattr__("COLORS", plt.rcParams["axes.prop_cycle"].by_key()["color"])
