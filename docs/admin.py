from django.contrib import admin
from docs.models import Comment, Document, DocumentHistory, Folder


# Register your models here.
admin.site.register(Comment)
admin.site.register(Folder)


class DocumentAdmin(admin.ModelAdmin):

    readonly_fields = [
        "version",
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
    ]

    def save_model(self, request, obj, form, change):

        obj.updated_by = request.user

        if obj.id is None:
            obj.version = 1.0
            obj.created_by = request.user
            obj.updated_by = request.user

        if change:
            obj.version = float(obj.version) + 0.1

        super().save_model(request, obj, form, change)


admin.site.register(Document, DocumentAdmin)


class DocumentHistoryAdmin(admin.ModelAdmin):

    readonly_fields = [
        "folder",
        "name",
        "content",
        "version",
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
        "active",
        "document",
    ]

admin.site.register(DocumentHistory, DocumentHistoryAdmin)
