from django.utils.translation import ugettext as _

TANK = 'Tank'
HEALER = 'Healer'
RANGED = 'Ranged'
MELEE = 'Melee'

roles = [
    TANK,
    HEALER,
    RANGED,
    MELEE,
]

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

CLASS_FORM_CHOICES = [
    (CLASS_DK, _('Death Knight')),
    (CLASS_DH, _('Demon Hunter')),
    (CLASS_DRUID, _('Druid')),
    (CLASS_HUNTER, _('Hunter')),
    (CLASS_MAGE, _('Mage')),
    (CLASS_MONK, _('Monk')),
    (CLASS_PALADIN, _('Paladin')),
    (CLASS_PRIEST, _('Priest')),
    (CLASS_ROGUE, _('Rogue')),
    (CLASS_SHAMAN, _('Shaman')),
    (CLASS_WARLOCK, _('Warlock')),
    (CLASS_WARRIOR, _('Warrior'))
]

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
