from datetime import date
from typing import List
from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from .models import Note, Category
from .schemas import NoteIn, NoteOut, NoteUpd, CategoryIn, CategoryOut

# Initialize a NinjaAPI instance
api = NinjaAPI()

# Define an endpoint for creating a note
@api.post("/notes", tags=['Заметки'])
def create_note(request, payload: NoteIn):
    data = payload.dict()
    category = Category.objects.get(id=data['category'])
    del data['category']
    note = Note.objects.create(category=category, **data)
    return {"id": note.id}

# Define an endpoint for creating a category
@api.post("/category", tags=['Категории'])
def create_category(request, payload: CategoryIn):
    category = Category.objects.create(**payload.dict())
    return {"id":category.id}

# Define an endpoint for getting a note
@api.get("/notes/{note_id}", response=NoteOut, tags=['Заметки'])
def get_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    return note

# Define an endpoint for getting a category
@api.get("/category/{category_id}", response=CategoryOut, tags=['Категории'])
def get_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    return category

# Define an endpoint for listing all categories
@api.get("/category", response=List[CategoryOut], tags=['Категории'])
def list_categories(request):
    categories = Category.objects.all()
    return categories

# Define an endpoint for listing all notes
@api.get("/notes", response=List[NoteOut], tags=['Заметки'])
def list_notes(request):
    notes = Note.objects.all()
    return notes

# Define an endpoint for updating a note
@api.patch("/notes/{note_id}", tags=['Заметки'])
def update_note(request, note_id: int, payload: NoteUpd):
    note = get_object_or_404(Note, id=note_id)
    for attr, value in payload.dict().items():
        setattr(note, attr, value)
    note.save()
    return {"success": True}

# Define an endpoint for updating a category
@api.put("/category/{category_id}", tags=['Категории'])
def update_category(request, category_id: int, payload: CategoryIn):
    category = get_object_or_404(Category, id=category_id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return {"success": True}

# Define an endpoint for deleting a note
@api.delete("/notes/{note_id}", tags=['Заметки'])
def delete_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return {"success": True}

# Define an endpoint for deleting a category
@api.delete("/category/{category_id}", tags=['Категории'])
def delete_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return {"success": True}