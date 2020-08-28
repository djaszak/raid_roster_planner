# Generated by Django 3.1 on 2020-08-28 19:21

from django.db import migrations

from raid_roster_planner.raid_roster_drf import constants


roles = [
    'Tank',
    'Healer',
    'Ranged',
    'Melee',
]


classes = [
    constants.CLASS_DK,
    constants.CLASS_DH,
    constants.CLASS_DRUID,
    constants.CLASS_HUNTER,
    constants.CLASS_MAGE,
    constants.CLASS_MONK,
    constants.CLASS_PALADIN,
    constants.CLASS_PRIEST,
    constants.CLASS_ROGUE,
    constants.CLASS_SHAMAN,
    constants.CLASS_WARLOCK,
    constants.CLASS_WARRIOR,
]


# forward function
def add_data(apps, schema_editor):
    role_model = apps.get_model('raid_roster_drf', 'Role')
    game_class_model = apps.get_model('raid_roster_drf', 'GameClass')

    for rl in roles:
        role_model.objects.get_or_create(name=rl)

    for cl in classes:
        game_class_model.objects.get_or_create(name=cl)


# forward function
def remove_data(apps, schema_editor):
    role_model = apps.get_model('raid_roster_drf', 'Role')
    game_class_model = apps.get_model('raid_roster_drf', 'GameClass')

    role_model.objects.filter(name__in=roles).delete()
    game_class_model.objects.filter(name__in=classes).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('raid_roster_drf', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_data,
            remove_data
        )
    ]
