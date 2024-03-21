# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from typing import Dict, List

from pydantic import BaseModel
from pydantic.fields import FieldInfo


class ModelView:
    def __init__(self, model: BaseModel) -> None:
        self.model: BaseModel = model
        self.model_fields: Dict[str, FieldInfo] = self.model.model_fields

    def definitions(self) -> List[tuple[str, dict]]:
        definitions: List[tuple[str, dict]] = []
        for k, v in self.model_fields.items():
            data = v.json_schema_extra or {}
            data.update(
                {
                    "required": v.is_required(),
                    "description": v.description,
                    "annotation": v.annotation,
                }
            )
            definitions.append((k, data))
        return definitions
