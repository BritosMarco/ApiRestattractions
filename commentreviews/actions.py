"""Action implementada para aprovar e reprovar vários comentários
de uma única vez na área administrativa
"""

def disapprove_comments(modeladmin, reques, queryset):
    queryset.update(approved=False)

def approve_comments(modeladmin, reques, queryset):
    queryset.update(approved=True)

disapprove_comments.short_description = "Reprovar comentários"
approve_comments.short_description = "Aprovar comentários"