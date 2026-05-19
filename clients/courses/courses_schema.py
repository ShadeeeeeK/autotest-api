from pydantic import BaseModel, ConfigDict, Field
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class Course(BaseModel):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field("previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение курсов
    """
    user_id: str = Field(alias="userId")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса
    """
    course: Course


class CoursesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
