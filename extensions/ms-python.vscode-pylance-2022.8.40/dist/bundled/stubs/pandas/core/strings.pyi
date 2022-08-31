import re
from typing import (
    Any,
    Callable,
    Generic,
    Literal,
    Sequence,
    overload,
)

import numpy as np
import pandas as pd
from pandas import Series
from pandas.core.base import NoNewAttributesMixin as NoNewAttributesMixin

from pandas._typing import (
    F,
    T,
)

def cat_core(list_of_columns: list[np.ndarray], sep: str) -> np.ndarray: ...
def cat_safe(list_of_columns: list[np.ndarray], sep: str) -> np.ndarray: ...
def forbid_nonstring_types(
    forbidden: list[str] | None, name: str | None = ...
) -> Callable[[F], F]: ...

class StringMethods(NoNewAttributesMixin, Generic[T]):
    def __init__(self, data: T) -> None: ...
    def __getitem__(self, key: slice | int) -> T: ...
    def __iter__(self) -> T: ...
    @overload
    def cat(
        self,
        *,
        sep: str,
        na_rep: str | None = ...,
        join: Literal["left", "right", "outer", "inner"] = ...,
    ) -> str: ...
    @overload
    def cat(
        self,
        others: Literal[None] = ...,
        *,
        sep: str,
        na_rep: str | None = ...,
        join: Literal["left", "right", "outer", "inner"] = ...,
    ) -> str: ...
    @overload
    def cat(
        self,
        others: Series | pd.Index | pd.DataFrame | np.ndarray | list[Any],
        sep: str = ...,
        na_rep: str | None = ...,
        join: Literal["left", "right", "outer", "inner"] = ...,
    ) -> T: ...
    def split(
        self, pat: str = ..., n: int = ..., expand: bool = ..., *, regex: bool = ...
    ) -> T: ...
    def rsplit(
        self, pat: str = ..., n: int = ..., expand: bool = ..., *, regex: bool = ...
    ) -> T: ...
    @overload
    def partition(self, sep: str = ...) -> pd.DataFrame: ...
    @overload
    def partition(self, *, expand: Literal[True]) -> pd.DataFrame: ...
    @overload
    def partition(self, sep: str, expand: Literal[True]) -> pd.DataFrame: ...
    @overload
    def partition(self, sep: str, expand: Literal[False]) -> T: ...
    @overload
    def partition(self, *, expand: Literal[False]) -> T: ...
    @overload
    def rpartition(self, sep: str = ...) -> pd.DataFrame: ...
    @overload
    def rpartition(self, *, expand: Literal[True]) -> pd.DataFrame: ...
    @overload
    def rpartition(self, sep: str, expand: Literal[True]) -> pd.DataFrame: ...
    @overload
    def rpartition(self, sep: str, expand: Literal[False]) -> T: ...
    @overload
    def rpartition(self, *, expand: Literal[False]) -> T: ...
    def get(self, i: int) -> T: ...
    def join(self, sep: str) -> T: ...
    def contains(
        self, pat: str, case: bool = ..., flags: int = ..., na=..., regex: bool = ...
    ) -> Series[bool]: ...
    def match(
        self, pat: str, case: bool = ..., flags: int = ..., na: Any = ...
    ) -> T: ...
    def replace(
        self,
        pat: str,
        repl: str | Callable[[re.Match], str],
        n: int = ...,
        case: bool | None = ...,
        flags: int = ...,
        regex: bool = ...,
    ) -> T: ...
    def repeat(self, repeats: int | Sequence[int]) -> T: ...
    def pad(
        self,
        width: int,
        side: Literal["left", "right", "both"] = ...,
        fillchar: str = ...,
    ) -> T: ...
    def center(self, width: int, fillchar: str = ...) -> T: ...
    def ljust(self, width: int, fillchar: str = ...) -> T: ...
    def rjust(self, width: int, fillchar: str = ...) -> T: ...
    def zfill(self, width: int) -> T: ...
    def slice(
        self, start: int | None = ..., stop: int | None = ..., step: int | None = ...
    ) -> T: ...
    def slice_replace(
        self, start: int | None = ..., stop: int | None = ..., repl: str | None = ...
    ) -> T: ...
    def decode(self, encoding: str, errors: str = ...) -> T: ...
    def encode(self, encoding: str, errors: str = ...) -> T: ...
    def strip(self, to_strip: str | None = ...) -> T: ...
    def lstrip(self, to_strip: str | None = ...) -> T: ...
    def rstrip(self, to_strip: str | None = ...) -> T: ...
    def wrap(
        self,
        width: int,
        expand_tabs: bool | None = ...,
        replace_whitespace: bool | None = ...,
        drop_whitespace: bool | None = ...,
        break_long_words: bool | None = ...,
        break_on_hyphens: bool | None = ...,
    ) -> T: ...
    def get_dummies(self, sep: str = ...) -> pd.DataFrame: ...
    def translate(self, table: dict[int, int | str | None] | None) -> T: ...
    def count(self, pat: str, flags: int = ...) -> Series[int]: ...
    def startswith(self, pat: str, na: Any = ...) -> Series[bool]: ...
    def endswith(self, pat: str, na: Any = ...) -> Series[bool]: ...
    def findall(self, pat: str, flags: int = ...) -> Series: ...
    @overload
    def extract(
        self, pat: str, flags: int = ..., *, expand: Literal[True] = ...
    ) -> pd.DataFrame: ...
    @overload
    def extract(self, pat: str, flags: int, expand: Literal[False]) -> T: ...
    @overload
    def extract(self, pat: str, flags: int = ..., *, expand: Literal[False]) -> T: ...
    def extractall(self, pat: str, flags: int = ...) -> pd.DataFrame: ...
    def find(self, sub: str, start: int = ..., end: int | None = ...) -> T: ...
    def rfind(self, sub: str, start: int = ..., end: int | None = ...) -> T: ...
    def normalize(self, form: Literal["NFC", "NFKC", "NFD", "NFKD"]) -> T: ...
    def index(self, sub: str, start: int = ..., end: int | None = ...) -> T: ...
    def rindex(self, sub: str, start: int = ..., end: int | None = ...) -> T: ...
    def len(self) -> Series[int]: ...
    def lower(self) -> T: ...
    def upper(self) -> T: ...
    def title(self) -> T: ...
    def capitalize(self) -> T: ...
    def swapcase(self) -> T: ...
    def casefold(self) -> T: ...
    def isalnum(self) -> Series[bool]: ...
    def isalpha(self) -> Series[bool]: ...
    def isdigit(self) -> Series[bool]: ...
    def isspace(self) -> Series[bool]: ...
    def islower(self) -> Series[bool]: ...
    def isupper(self) -> Series[bool]: ...
    def istitle(self) -> Series[bool]: ...
    def isnumeric(self) -> Series[bool]: ...
    def isdecimal(self) -> Series[bool]: ...
    def fullmatch(
        self, pat: str, case: bool = ..., flags: int = ..., na: Any = ...
    ) -> Series[bool]: ...
    def removeprefix(self, prefix: str) -> T: ...
    def removesuffix(self, suffix: str) -> T: ...
