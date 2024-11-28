"""This notebook contains helper classes and types for loading data from media datasets."""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/utils/00_data_loading.ipynb.

# %% ../../nbs/utils/00_data_loading.ipynb 3
from __future__ import annotations

import xarray as xr
import pandas as pd
import numpy as np

from typing import (
    Dict, Union, Literal, 
    Optional, Set, Tuple, 
    List, Callable)
import warnings
import os
import json
from pathlib import Path


# %% auto 0
__all__ = ['DataLoader']

# %% ../../nbs/utils/00_data_loading.ipynb 5
class DataLoader:
    """Load data from a file or a directory of files, while keeping track of the metadata."""
    def __init__(
        self, 
        path: Union[str, Path], # path to the file or directory
        metadata_file_name: Optional[str] = None, # name of the metadata file
        custom_data_loader: Optional[Union[Callable, str]] = None # custom data loader function or name of module with custom data loader
        ) -> DataLoader:
        ...
