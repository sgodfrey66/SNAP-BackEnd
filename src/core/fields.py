from django.db import models


class EnumCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        enum = kwargs.pop("enum", None)
        if enum is not None:
            if kwargs.get("choices", None) is not None:
                raise ValueError("Cannot provide choices for EnumCharField")
            kwargs["choices"] = [(item, item.value) for item in enum]
        super().__init__(*args, **kwargs)
