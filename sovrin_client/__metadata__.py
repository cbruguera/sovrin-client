"""
sovrin-client package metadata
"""
__version_info__ = (0, 0, 9)
__version__ = '{}.{}.{}'.format(*__version_info__)
__author__ = "Sovrin Foundation."
__license__ = "Apache 2.0"

__all__ = ['__version_info__', '__version__', '__author__', '__license__']

__dependencies__ = {
    "anoncreds": ">=0.1.11",
    "sovrin_common": ">=0.0.4"
}
