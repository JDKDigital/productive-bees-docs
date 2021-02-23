Bee Spawning Recipes
********************

Bees can be set to spawn from nests in the world, both on world-gen and from crafted nests.

Type
====

Required. This will always be one of these values. Use the big version if you have more than 3 bees in the recipe

.. code-block:: javascript

        "type": "productivebees:bee_spawning"
        "type": "productivebees:bee_spawning_big"

Nest
====

Required. The nest these spawn rules should apply to. Available nests are:
    "productivebees:coarse_dirt_nest"
    "productivebees:gravel_nest"
    "productivebees:sand_nest"
    "productivebees:snow_nest"
    "productivebees:stone_nest"
    "productivebees:soul_sand_nest"
    "productivebees:sugar_cane_nest"
    "productivebees:slimy_nest"
    "productivebees:obsidian_nest"
    "productivebees:glowstone_nest"
    "productivebees:nether_brick_nest"
    "productivebees:nether_quartz_nest"
    "productivebees:end_stone_nest"
    "productivebees:oak_wood_nest"
    "productivebees:acaia_wood_nest"
    "productivebees:birch_wood_nest"
    "productivebees:dark_oak_wood_nest"
    "productivebees:spruce_wood_nest"
    "productivebees:jungle_wood_nest"

.. code-block:: javascript

      "ingredient": {
          "item": "productivebees:coarse_dirt_nest"
      },


Bees
====

Required. A list of bees, 5 max.

.. code-block:: javascript

    "results": [
        {
            "bee": "productivebees:ashy_mining_bee"
        },
        {
            "bee": "productivebees:chocolate_mining_bee"
        },
        {
            "bee": "productivebees:leafcutter_bee"
        }
    ],


Biome requirements
==================

Optional. A list of biome categories required for the recipe to take effect

.. code-block:: javascript

    "biomes": [
        "desert", "beach"
    ],


Biome requirements
==================

Optional. The number of ticks it takes for a bee from this recipe to spawn when a honey treat is used on the nest.

.. code-block:: javascript

    "repopulation_cooldown": 24000


Conditions
==========

Optional.  Typically used as a check for a mod being loaded / available. Conditions should match that of the bees used.

.. code-block:: javascript

        "conditions": [
                {
                        "type": "forge:mod_loaded",
                        "modid": "simplefarming"
                }
        ]