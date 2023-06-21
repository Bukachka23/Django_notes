from ninja import Schema, ModelSchema
from datetime import date
from .models import Note

# Define a schema for input data for a Category instance
class CategoryIn(Schema):
    title: str
    description: str

# Define a schema for output data for a Category instance
class CategoryOut(Schema):
    id: int
    title: str
    description: str
    created: date

# Define a schema for input data for a Note instance
class NoteIn(ModelSchema):
    class Config:
        model = Note
        model_fields = ['title', 'category']

# Define a schema for updating a Note instance
class NoteUpd(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id', 'completed']

# Define a schema for output data for a Note instance
class NoteOut(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id', 'title', 'category', 'created', 'completed']