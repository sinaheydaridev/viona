from .base import EnumBase


class ProductStatusEnum(EnumBase):
    available = "available"
    expensive = "expensive"
    inexpensive = "inexpensive"


class CustomerStatusEnum(EnumBase):
    active = "active"
    removed = "removed"
