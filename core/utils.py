from django.forms.fields import uuid

def generate_unique_id():
    return str(uuid.uuid4())[:8]
