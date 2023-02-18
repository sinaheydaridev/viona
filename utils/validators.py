from uuid import UUID


class ApiValidator:
    def is_uuid4(uuid_string):
        try:
            UUID(uuid_string, version=4)
        except:
            raise ValueError("value must be uuid.")

    def is_enum(valid_enum, enum):
        try:
            include_enum = True
            valid_items = [key[0] for key in valid_enum]
            items = [key[0] for key in enum]
            for item in items:
                include_enum = item in valid_items
            if not include_enum:
                raise ValueError()
        except:
            raise ValueError("value must be enum.")
