from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhysicalIdFromStackParams(_message.Message):
    __slots__ = ["logical_resource_id", "stack_name", "profile", "region"]
    LOGICAL_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    STACK_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    logical_resource_id: str
    stack_name: str
    profile: str
    region: str
    def __init__(self, logical_resource_id: _Optional[str] = ..., stack_name: _Optional[str] = ..., profile: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ["jsonrpc", "id", "method", "params", "metadata"]
    JSONRPC_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    jsonrpc: str
    id: str
    method: str
    params: PhysicalIdFromStackParams
    metadata: RequestMetadata
    def __init__(self, jsonrpc: _Optional[str] = ..., id: _Optional[str] = ..., method: _Optional[str] = ..., params: _Optional[_Union[PhysicalIdFromStackParams, _Mapping]] = ..., metadata: _Optional[_Union[RequestMetadata, _Mapping]] = ...) -> None: ...

class RequestMetadata(_message.Message):
    __slots__ = ["client", "version", "caller", "client_version"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CALLER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    client: str
    version: str
    caller: str
    client_version: str
    def __init__(self, client: _Optional[str] = ..., version: _Optional[str] = ..., caller: _Optional[str] = ..., client_version: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["jsonrpc", "id", "output"]
    JSONRPC_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    jsonrpc: str
    id: str
    output: PhysicalIdFromStackOutput
    def __init__(self, jsonrpc: _Optional[str] = ..., id: _Optional[str] = ..., output: _Optional[_Union[PhysicalIdFromStackOutput, _Mapping]] = ...) -> None: ...

class PhysicalIdFromStackOutput(_message.Message):
    __slots__ = ["physical_id"]
    PHYSICAL_ID_FIELD_NUMBER: _ClassVar[int]
    physical_id: str
    def __init__(self, physical_id: _Optional[str] = ...) -> None: ...
