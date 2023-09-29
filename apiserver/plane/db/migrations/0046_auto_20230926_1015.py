# Generated by Django 4.2.5 on 2023-09-26 10:29

from django.db import migrations, models
import plane.db.models.workspace


def update_issue_activity_priority(apps, schema_editor):
    IssueActivity = apps.get_model("db", "IssueActivity")
    updated_issue_activity = []
    for obj in IssueActivity.objects.filter(field="priority"):
        # Set the old and new value to none if it is empty for Priority
        obj.new_value = obj.new_value or "none"
        obj.old_value = obj.old_value or "none"
        updated_issue_activity.append(obj)
    IssueActivity.objects.bulk_update(
        updated_issue_activity,
        ["new_value", "old_value"],
        batch_size=1000,
    )

def update_issue_activity_blocked(apps, schema_editor):
    IssueActivity = apps.get_model("db", "IssueActivity")
    updated_issue_activity = []
    for obj in IssueActivity.objects.filter(field="blocks"):
        # Set the field to blocked_by
        obj.field = "blocked_by"
        updated_issue_activity.append(obj)
    IssueActivity.objects.bulk_update(
        updated_issue_activity,
        ["field"],
        batch_size=1000,
    )



class Migration(migrations.Migration):

    dependencies = [
        ('db', '0045_auto_20230915_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalview',
            name='sort_order',
            field=models.FloatField(default=65535),
        ),
        migrations.AddField(
            model_name='workspacemember',
            name='issue_props',
            field=models.JSONField(default=plane.db.models.workspace.get_issue_props),
        ),
        migrations.RunPython(update_issue_activity_priority),
        migrations.RunPython(update_issue_activity_blocked),
    ]
