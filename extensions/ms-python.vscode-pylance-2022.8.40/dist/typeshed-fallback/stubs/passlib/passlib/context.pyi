from _typeshed import Self, StrOrBytesPath, SupportsItems
from typing import Any

class CryptPolicy:
    @classmethod
    def from_path(cls, path, section: str = ..., encoding: str = ...): ...
    @classmethod
    def from_string(cls, source, section: str = ..., encoding: str = ...): ...
    @classmethod
    def from_source(cls, source, _warn: bool = ...): ...
    @classmethod
    def from_sources(cls, sources, _warn: bool = ...): ...
    def replace(self, *args, **kwds): ...
    def __init__(self, *args, **kwds) -> None: ...
    def has_schemes(self): ...
    def iter_handlers(self): ...
    def schemes(self, resolve: bool = ...): ...
    def get_handler(self, name: Any | None = ..., category: Any | None = ..., required: bool = ...): ...
    def get_min_verify_time(self, category: Any | None = ...): ...
    def get_options(self, name, category: Any | None = ...): ...
    def handler_is_deprecated(self, name, category: Any | None = ...): ...
    def iter_config(self, ini: bool = ..., resolve: bool = ...): ...
    def to_dict(self, resolve: bool = ...): ...
    def to_file(self, stream, section: str = ...) -> None: ...
    def to_string(self, section: str = ..., encoding: Any | None = ...): ...

class CryptContext:
    @classmethod
    def from_string(cls: type[Self], source: str | bytes, section: str = ..., encoding: str = ...) -> Self: ...
    @classmethod
    def from_path(cls: type[Self], path: StrOrBytesPath, section: str = ..., encoding: str = ...) -> Self: ...
    def copy(self, **kwds: Any) -> CryptContext: ...
    def using(self, **kwds: Any) -> CryptContext: ...
    def replace(self, **kwds): ...
    def __init__(self, schemes: Any | None = ..., policy=..., _autoload: bool = ..., **kwds) -> None: ...
    policy: CryptPolicy
    def load_path(self, path: StrOrBytesPath, update: bool = ..., section: str = ..., encoding: str = ...) -> None: ...
    def load(
        self,
        source: str | bytes | SupportsItems[str, Any] | CryptContext,
        update: bool = ...,
        section: str = ...,
        encoding: str = ...,
    ) -> None: ...
    def update(self, *args: Any, **kwds: Any) -> None: ...
    def schemes(self, resolve: bool = ..., category: Any | None = ..., unconfigured: bool = ...): ...
    def default_scheme(self, category: Any | None = ..., resolve: bool = ..., unconfigured: bool = ...): ...
    def handler(self, scheme: Any | None = ..., category: Any | None = ..., unconfigured: bool = ...): ...
    @property
    def context_kwds(self): ...
    def to_dict(self, resolve: bool = ...) -> dict[str, Any]: ...
    def to_string(self, section: str = ...) -> str: ...
    mvt_estimate_max_samples: int
    mvt_estimate_min_samples: int
    mvt_estimate_max_time: int
    mvt_estimate_resolution: float
    harden_verify: Any
    min_verify_time: int
    def reset_min_verify_time(self) -> None: ...
    def needs_update(
        self, hash: str | bytes, scheme: str | None = ..., category: str | None = ..., secret: str | bytes | None = ...
    ) -> bool: ...
    def hash_needs_update(self, hash, scheme: Any | None = ..., category: Any | None = ...): ...
    def genconfig(self, scheme: Any | None = ..., category: Any | None = ..., **settings): ...
    def genhash(self, secret, config, scheme: Any | None = ..., category: Any | None = ..., **kwds): ...
    def identify(self, hash, category: Any | None = ..., resolve: bool = ..., required: bool = ..., unconfigured: bool = ...): ...
    def hash(self, secret: str | bytes, scheme: str | None = ..., category: str | None = ..., **kwds: Any) -> str: ...
    def encrypt(self, *args, **kwds): ...
    def verify(
        self, secret: str | bytes, hash: str | bytes, scheme: str | None = ..., category: str | None = ..., **kwds: Any
    ) -> bool: ...
    def verify_and_update(
        self, secret: str | bytes, hash: str | bytes, scheme: str | None = ..., category: str | None = ..., **kwds: Any
    ) -> tuple[bool, str | None]: ...
    def dummy_verify(self, elapsed: int = ...): ...
    def is_enabled(self, hash: str | bytes) -> bool: ...
    def disable(self, hash: str | bytes | None = ...) -> str: ...
    def enable(self, hash: str | bytes) -> str: ...

class LazyCryptContext(CryptContext):
    def __init__(self, schemes: Any | None = ..., **kwds) -> None: ...
    def __getattribute__(self, attr: str) -> Any: ...
