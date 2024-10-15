from simple_functions.functions1 import my_sum, my_prod  # noqa
from simple_functions.cacu_pi import pi, rsum

try:
    from importlib.metadata import version, PackageNotFoundError  # Python 3.8+
except ImportError:  # For Python < 3.8
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    pass
