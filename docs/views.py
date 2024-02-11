from django.shortcuts import render
from .models import Document, Folder


def flatten_folder_tree(folder):
    result = [(folder, 'open')]
    for subfolder in folder.folder_set.all():
        result.extend(flatten_folder_tree(subfolder))
    result.append((folder, 'close'))
    return result



def list_docs(request, document_id=None):

    print(document_id)

    root_folders = Folder.objects.filter(parent__isnull=True)

    flattened_folders = []
    for root_folder in root_folders:
        flattened_folders.extend(flatten_folder_tree(root_folder))
    
    document = Document.objects.filter(id=document_id).first()

    context = {
        "folders": root_folders,
        "document": document,
        "selected_doc": document_id,
        "flattened_folders": flattened_folders,
    }

    return render(request, "docs/list_docs.html", context)

