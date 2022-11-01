# Generated by Django 3.1 on 2022-11-01 14:07

from django.db import migrations, models


TANK = 'Tank'
HEALER = 'Healer'
RANGED = 'Ranged'
MELEE = 'Melee'
CLASS_DK = 'death_knight'
CLASS_DH = 'demon_hunter'
CLASS_DRUID = 'druid'
CLASS_HUNTER = 'hunter'
CLASS_MAGE = 'mage'
CLASS_MONK = 'monk'
CLASS_PALADIN = 'paladin'
CLASS_PRIEST = 'priest'
CLASS_ROGUE = 'rogue'
CLASS_SHAMAN = 'shaman'
CLASS_WARLOCK = 'warlock'
CLASS_WARRIOR = 'warrior'

CLASS_ROLE_MAPPING = {
    CLASS_DK: (TANK, MELEE),
    CLASS_DH: (TANK, MELEE),
    CLASS_DRUID: (TANK, HEALER, MELEE, RANGED),
    CLASS_HUNTER: (RANGED,),
    CLASS_MAGE: (RANGED,),
    CLASS_MONK: (TANK, HEALER, MELEE),
    CLASS_PALADIN: (TANK, HEALER, MELEE),
    CLASS_PRIEST: (HEALER, RANGED),
    CLASS_ROGUE: (MELEE,),
    CLASS_SHAMAN: (HEALER, MELEE, RANGED),
    CLASS_WARLOCK: (RANGED,),
    CLASS_WARRIOR: (TANK, MELEE),
}

CLASS_COLOURS = {
    CLASS_DK: '#C41F3B',
    CLASS_DH: '#A330C9',
    CLASS_DRUID: '#FF7D0A',
    CLASS_HUNTER: '#A9D271',
    CLASS_MAGE: '#40C7EB',
    CLASS_MONK: '#00FF96',
    CLASS_PALADIN: '#F58CBA',
    CLASS_PRIEST: '#FFFFFF',
    CLASS_ROGUE: '#FFF569',
    CLASS_SHAMAN: '#0070DE',
    CLASS_WARLOCK: '#8787ED',
    CLASS_WARRIOR: '#C79C6E',
}


def forward(apps, schema_editor):
    role_model = apps.get_model('raid_roster_drf', 'Role')
    class_model = apps.get_model('raid_roster_drf', 'GameClass')

    for class_name in CLASS_ROLE_MAPPING:
        game_class_obj = class_model.objects.get(name=class_name)
        for role_name in CLASS_ROLE_MAPPING[class_name]:
            role_obj = role_model.objects.get(name=role_name)
            game_class_obj.specializations.add(role_obj)

        game_class_obj.colour = CLASS_COLOURS[class_name]
        game_class_obj.save()


def reverse(apps, schema_editor):
    # reversing deletes fields affected here
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('raid_roster_drf', '0005_cleanup_character_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameclass',
            name='colour',
            field=models.CharField(default='#FFFFFF', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameclass',
            name='specializations',
            field=models.ManyToManyField(blank=True, related_name='class_specialization', to='raid_roster_drf.Role'),
        ),
        migrations.AlterField(
            model_name='character',
            name='off_spec_roles',
            field=models.ManyToManyField(blank=True, related_name='off_spec_characters', to='raid_roster_drf.Role'),
        ),
        migrations.RunPython(
            forward, reverse_code=reverse
        ),
        migrations.AlterField(
            model_name='gameclass',
            name='specializations',
            field=models.ManyToManyField(related_name='class_specialization', to='raid_roster_drf.Role'),
        ),
    ]
