from .translaters.achievement import translate_achievement
from .translaters.bodypart import translate_bodypart
from .translaters.clothing_mod import translate_clothing_mod
from .translaters.construction import translate_construction
from .translaters.effect_on_condition import translate_effect_on_condition
from .translaters.effect_type import translate_effect_type
from .translaters.fault import translate_fault
from .translaters.field_type import translate_field_type
from .translaters.gate import translate_gate
from .translaters.gun import translate_gun
from .translaters.gunmod import translate_gunmod
from .translaters.magazine import translate_magazine
from .translaters.mapgen import translate_mapgen
from .translaters.martial_art import translate_martial_art
from .translaters.material import translate_material
from .translaters.missiondef import translate_missiondef
from .translaters.monster_attack import translate_monster_attack
from .translaters.movement_mode import translate_movement_mode
from .translaters.mutation_category import translate_mutation_category
from .translaters.mutation import translate_mutation
from .translaters.palette import translate_palette
from .translaters.profession import translate_profession
from .translaters.recipe_category import translate_recipe_category
from .translaters.recipe_group import translate_recipe_group
from .translaters.recipe import translate_recipe
from .translaters.scenario import translate_scenario
from .translaters.skill_display_type import translate_skill_display_type
from .translaters.snippet import translate_snippet
from .translaters.speed_description import translate_speed_description
from .translaters.sub_bodypart import translate_sub_bodypart
from .translaters.talk_topic import translate_talk_topic
from .translaters.ter_furn_transform import translate_ter_furn_transform
from .translaters.trap import translate_trap
from .translaters.vehicle_part_category import translate_vehicle_part_category
from .translaters.vehicle_spawn import translate_vehicle_spawn
from .translaters.weakpoint_set import translate_weakpoint_set
from .translaters.widget import translate_widget


ignorable = [
    "anatomy",
    "ascii_art",
    "ammo_effect",
    "behavior",
    "butchery_requirement",
    "charge_removal_blacklist",
    "city_building",
    "colordef",
    "disease_type",
    "emit",
    "enchantment",
    "event_transformation",
    "external_option",
    "harvest_drop_type",
    "hit_range",
    "item_blacklist",
    "item_group",
    "migration",
    "mod_tileset",
    "monster_adjustment",
    "monster_blacklist",
    "monster_faction",
    "monstergroup",
    "monster_whitelist",
    "mutation_type",
    "obsolete_terrain",
    "overlay_order",
    "overmap_connection",
    "overmap_location",
    "overmap_special",
    "overmap_special_migration",
    "profession_item_substitutions",
    "region_overlay",
    "region_settings",
    "relic_procgen_data",
    "requirement",
    "rotatable_symbol",
    "scenario_blacklist",
    "scent_type",
    "score",
    "skill_boost",
    "trait_blacklist",
    "trait_group",
    "uncraft",
    "mood_face",
    "vehicle_group",
    "vehicle_placement",
]

# these objects can have their strings automatically extracted.
# insert object "type" here IF AND ONLY IF
# all of their translatable strings are in the following form:
#   "name" member
#   "description" member
#   "text" member
#   "sound" member
#   "messages" member containing an array of translatable strings
automatically_convertible = [
    "activity_type",
    "ammo",
    "ammunition_type",
    "armor",
    "battery",
    "bionic",
    "bionic_item",
    "book",
    "comestible",
    "character_mod",
    "construction_category",
    "construction_group",
    "dream",
    "engine",
    "event_statistic",
    "faction",
    "furniture",
    "generic",
    "harvest",
    "item_action",
    "item_category",
    "json_flag",
    "keybinding",
    "limb_score",
    "loot_zone",
    "map_extra",
    "mod_info",
    "monster",
    "morale_type",
    "npc",
    "proficiency",
    "npc_class",
    "overmap_land_use_code",
    "overmap_terrain",
    "pet_armor",
    "skill",
    "species",
    "speech",
    "spell",
    "start_location",
    "technique",
    "terrain",
    "tool",
    "toolmod",
    "tool_armor",
    "tool_quality",
    "vehicle",
    "vehicle_part",
    "vitamin",
    "weapon_category",
    "wheel",
    "help",
    "weather_type",
]

extract_specials = {
    "achievement": translate_achievement,
    "body_part": translate_bodypart,
    "sub_body_part": translate_sub_bodypart,
    "clothing_mod": translate_clothing_mod,
    "conduct": translate_achievement,
    "construction": translate_construction,
    "effect_on_condition": translate_effect_on_condition,
    "effect_type": translate_effect_type,
    "fault": translate_fault,
    "gun": translate_gun,
    "gunmod": translate_gunmod,
    "magazine": translate_magazine,
    "mapgen": translate_mapgen,
    "martial_art": translate_martial_art,
    "material": translate_material,
    "mission_definition": translate_missiondef,
    "monster_attack": translate_monster_attack,
    "movement_mode": translate_movement_mode,
    "mutation": translate_mutation,
    "mutation_category": translate_mutation_category,
    "palette": translate_palette,
    "practice": translate_recipe,
    "profession": translate_profession,
    "recipe_category": translate_recipe_category,
    "recipe": translate_recipe,
    "recipe_group": translate_recipe_group,
    "scenario": translate_scenario,
    "snippet": translate_snippet,
    "speed_description": translate_speed_description,
    "talk_topic": translate_talk_topic,
    "trap": translate_trap,
    "gate": translate_gate,
    "vehicle_spawn": translate_vehicle_spawn,
    "field_type": translate_field_type,
    "ter_furn_transform": translate_ter_furn_transform,
    "skill_display_type": translate_skill_display_type,
    "vehicle_part_category": translate_vehicle_part_category,
    "weakpoint_set": translate_weakpoint_set,
    "widget": translate_widget,
}
