from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientRequest(_message.Message):
    __slots__ = ("link",)
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: str
    def __init__(self, link: _Optional[str] = ...) -> None: ...

class CommentRequest(_message.Message):
    __slots__ = ("link",)
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: str
    def __init__(self, link: _Optional[str] = ...) -> None: ...

class ClientResponse(_message.Message):
    __slots__ = ("prod",)
    PROD_FIELD_NUMBER: _ClassVar[int]
    prod: _containers.RepeatedCompositeFieldContainer[ItemProduct]
    def __init__(self, prod: _Optional[_Iterable[_Union[ItemProduct, _Mapping]]] = ...) -> None: ...

class CommentResponse(_message.Message):
    __slots__ = ("comm",)
    COMM_FIELD_NUMBER: _ClassVar[int]
    comm: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, comm: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class ItemProduct(_message.Message):
    __slots__ = ("link", "name", "characteristics", "images", "rating", "price")
    LINK_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    link: str
    name: str
    characteristics: _containers.RepeatedCompositeFieldContainer[Characteristics]
    images: _containers.RepeatedScalarFieldContainer[str]
    rating: str
    price: int
    def __init__(self, link: _Optional[str] = ..., name: _Optional[str] = ..., characteristics: _Optional[_Iterable[_Union[Characteristics, _Mapping]]] = ..., images: _Optional[_Iterable[str]] = ..., rating: _Optional[str] = ..., price: _Optional[int] = ...) -> None: ...

class Characteristics(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ("avatar", "username", "grade", "published_at", "text")
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    avatar: str
    username: str
    grade: str
    published_at: str
    text: str
    def __init__(self, avatar: _Optional[str] = ..., username: _Optional[str] = ..., grade: _Optional[str] = ..., published_at: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
