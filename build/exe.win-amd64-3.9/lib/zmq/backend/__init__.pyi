from typing import Any, ByteString, List, Optional, Set, Tuple, Union

from .select import select_backend

class Frame:
    buffer: Any
    bytes: ByteString
    more: bool
    tracker: Any
    def copy_fast(self) -> Frame: ...
    def get(self, option: int) -> Union[int, ByteString, str]: ...
    def set(self, option: int, value: Union[int, ByteString, str]) -> None: ...

class Socket:
    underlying: int
    def close(self, linger: Optional[int] = ...) -> None: ...
    def get(self, option: int) -> Union[int, ByteString, str]: ...
    def set(self, option: int, value: Union[int, ByteString, str]) -> None: ...
    def connect(self, url: str) -> None: ...
    def disconnect(self, url: str) -> None: ...
    def bind(self, url: str) -> None: ...
    def unbind(self, url: str) -> None: ...
    def send(
        self,
        data: Any,
        flags: Optional[int] = ...,
        copy: Optional[bool] = ...,
        track: Optional[bool] = ...,
    ) -> Optional[Frame]: ...
    def recv(
        self,
        flags: Optional[int] = ...,
        copy: Optional[bool] = ...,
        track: Optional[bool] = ...,
    ) -> Union[Frame, ByteString]: ...

class Context:
    underlying: int
    def get(self, option: int) -> Union[int, ByteString, str]: ...
    def set(self, option: int, value: Union[int, ByteString, str]) -> None: ...
    def socket(self, socket_type: int) -> Socket: ...

IPC_PATH_MAX_LEN: int

def has(capability: str) -> bool: ...
def curve_keypair() -> Tuple[bytes, bytes]: ...
def curve_public(secret_key: bytes) -> bytes: ...
def strerror(errno: Optional[int] = ...) -> str: ...
def zmq_errno() -> int: ...
def zmq_version() -> str: ...
def zmq_version_info() -> Tuple[int, int, int]: ...
def zmq_poll(sockets: List[Any], timeout: Optional[int] = ...): ...
def device(device_type: int, frontend: Socket, backend: Optional[Socket] = ...): ...
def proxy(frontend: Socket, backend: Socket): ...
def proxy_steerable(
    frontend: Socket,
    backend: Socket,
    capture: Optional[Socket] = ...,
    control: Optional[Socket] = ...,
): ...
