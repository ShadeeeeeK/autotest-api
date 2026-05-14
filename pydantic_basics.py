import uuid

from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field()
    def username(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def generate_username(self) -> str:
        return f'{self.first_name} {self.middle_name}'


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(default_factory=lambda: str(uuid.uuid4))
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


course_default_model = CourseSchema(
    id="course-id",
    title="playwright",
    maxScore=100,
    minScore=10,
    description="playwright",
    previewFile=FileSchema(
        id="file-id",
        filename="my_file.txt",
        directory="my-directory",
        url="https://ya.ru"
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="user-id",
        email="user@example.com",
        lastName="string",
        firstName="string",
        middleName="string"
    )
)

print('Course default model:', course_default_model)

course_dict = {
    "id": "course-id",
    "title": "playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "playwright",
    "previewFile": {
        "id": "file-id",
        "filename": "my_file.png",
        "directory": "mydirectory",
        "url": "https://ya.ru",
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
}

course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""

course_dict_model = CourseSchema(**course_dict)

course_json_model = CourseSchema.model_validate_json(course_json)
print('Course json model:', course_json_model)


# class UserTest(BaseModel):
#     user_id: int = Field(alias="userId")
#     name_f: str = Field(alias="nameF")
#
# test1 = UserTest(userId=1, nameF='Sergey')

# model_dump преобразует из объекта Pydantic в обычный словарь
#by_alias=True означает, про преобразовать ключи в название, как у алиасов
#exclude - уберет параметр, include- оставит только указанный
# model_dump_json преобразует из объекта Pydantic сразу в json (строку)
# model_validate_json создает модель из строки
#json_str = '{"id": 1, "name": "Alex"}'
#user = User.model_validate_json(json_str) - Pydantic object
# print(test1)
# print(test1.model_dump_json())
# print(type(test1.model_dump_json()))