from pydantic import BaseModel
from typing import List, Union, Optional


class QuestionSchema(BaseModel):
    type: str
    id: str


class CheckboxQuestionSchema(QuestionSchema):
    label: str


class DropdownQuestionSchema(QuestionSchema):
    label: str
    required: bool
    options: List[str]


class FileQuestionSchema(QuestionSchema):
    label: str
    required: bool


class RadioQuestionSchema(QuestionSchema):
    pass


class TelQuestionSchema(QuestionSchema):
    pass


class TextQuestionSchema(QuestionSchema):
    label: str
    placeholder: str
    required: bool


class TextAreaQuestionSchema(QuestionSchema):
    label: str
    placeholder: str
    required: bool
    rows: Optional[str]


class FormSectionSchema(BaseModel):
    title: str
    questions: List[
        Union[
            CheckboxQuestionSchema,
            DropdownQuestionSchema,
            FileQuestionSchema,
            RadioQuestionSchema,
            TelQuestionSchema,
            TextQuestionSchema,
            TextAreaQuestionSchema
        ]
    ]


class CreateFormConfigSchema(BaseModel):
    email: str
    config: List[FormSectionSchema]
