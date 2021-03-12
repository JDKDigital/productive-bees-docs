Bee Definition
**************

JSON file for containing the config for the bee, required for all bees.

=============
Primary Color
=============

Hex Color Code for the primary color of the bee and spawn egg.

*Required*

Value: String (Hex color code)

.. code-block:: javascript

    "primaryColor": "#f2f24f"

===============
Secondary Color
===============

Hex Color Code for the primary color of the bee,  and spawn egg.

*Required*

Value: String (Hex color code)

.. code-block:: javascript

    "primaryColor": "#f2f24f"

==============
Particle Color
==============

*Optional*

Hex Color Code for the particles the bees emit when having nectar. If not provided, the default vanilla particle color will be used.

Value: String (Hex color code)

.. code-block:: javascript

    "secondaryColor": "#d0581f"

===========
Bee Texture
===========

*Optional*

If you would like to use a custom texture for your bee, other wise the default one with the colors will be used instead.
Custom textures can be put in a resource pack.

Value: String (resource location)

.. code-block:: javascript

        "beeTexture": "productivebees:path_to_your_texture_file"

====
Name
====

*Optional*

By default, the filename will be used to create the name. If you want a different name from the filename, you can define it here.

Value: string

.. code-block:: javascript

        "name": "Patrick SwayzBee"

==================
Nesting Preference
==================

*Optional*

This option is used by wild bees to define which nests and hives it can live in. The value is a blocktag resource location.

Value: string (resource location)

.. code-block:: javascript

        "nestingPreference": "productivebees:nests/nether_quartz_nests"

===========
Create Comb
===========

*Optional*

Whether or not to create a comb for your bee. Most of the bees provided by default output comb items from the item registry.
For custom bees you can have the mod make an NBT based comb by setting this to true.

Value: boolean

.. code-block:: javascript

        "createComb": true

===============
Attack Response
===============

*Optional*

This is for if you would like your bee to use a special attack response.
Current options are:
    "fire" - sets the target on fire
    "lava" - drops lava on the target

Value: string

.. code-block:: javascript

        "attackResponse": "fire"

==============
Model renderer
==============

You can pick different models for your bee besides the default.

Available models:
    "default" - the default value giving a normal bee model
    "default_crystal" - default sized bee with glowing crystals growing out of it
    "translucent_with_center" - used for slimy bees, renders the bee with a translucent skin and a blob in the center. Custom texture is required for this model.
    "thicc" - big boi bee
    "small" - smaller size, requires custom texture
    "slim" - smaller size, requires custom texture
    "tiny" - requires custom texture

Value: string

.. code-block:: javascript

    "renderer": "default_crystal"

=========
Flowering
=========

Define what your bee will use as flower. Most bees are set to use a block of the type of resource it's producing, but you can choose any block or tag.
Only one of the two entries should be used. If you have a tag, use the flowerTag, for single blocks use the flowerBlock option.

Value: string

.. code-block:: javascript

        "flowerTag": "forge:storage_blocks/iron"
        "flowerBlock": "minecraft:dirt"

====
Size
====

*Optional*

If the model is not your desired size you can adjust it here.
Don't make the bee too small as it will start going through walls.

Value: float

.. code-block:: javascript

        "size": 1.0

=====================
Additional Attributes
=====================

These are additional attributes for your bee.  Such as weather tolerance, productivity, etc.
Each of these key: value pairs are optional. You can include none or all.
Default values will be applied for the attributes not defined.

Value: boolean

.. code-block:: javascript

        "attributes": {
                "temper": 1,
                "endurance": 2,
                "behavior": 2,
                "productivity": 2,
                "weather_tolerance": 2
        }

==========
Conditions
==========

Bees can be conditionally loaded. Conditions follow the same rules as recipe conditions.
The example value can be used to disable a bee.

Value: array

.. code-block:: javascript

        "conditions": [
            {
                "type": "forge:not",
                "value": {
                    "type": "forge:mod_loaded",
                    "modid": "productivebees"
                }
            }
        ]

============
Translucency
============

*Optional*

Bees can be translucent. A custom translucent texture must be provided as well.

Value: boolean

.. code-block:: javascript

        "translucent": false

=============
Teleportation
=============

*Optional*

If you would like for your bee to be able to teleport. Such as the :ref:`Ender<Ender>` bee for example.
(This could prove to make things interesting lol.)

Value: boolean

.. code-block:: javascript

        "teleporting": true

===========
Fire Proof
===========

*Optional*

Is your bee fireproof? Prevents damage from fire and lava.

Value: boolean

.. code-block:: javascript

        "fireproof": false

===========
Translucent
===========

*Optional*

Should your bee be translucent?

Value: boolean

.. code-block:: javascript

        "translucent": false

========
Draconic
========

*Optional*

Allows for your bee to live in egg hives and gives them protection from dragon's breath attack;

Value: boolean

.. code-block:: javascript

        "draconic": false

=========
Redstoned
=========

*Optional*

Should your bee emit a redstone signal when having nectar, triggering contraptions below it?

Value: boolean

.. code-block:: javascript

        "redstoned": false

=====
Slimy
=====

*Optional*

Randomly emit slime particles

Value: boolean

.. code-block:: javascript

        "slimy": false

=========
Withering
=========

*Optional*

Whether or not your bee gives a withered effect when attacking. Also provides immunity to wither damage.

Value: boolean

.. code-block:: javascript

        "withered": false

===========
Blinding
===========

*Optional*

Whether or not your bee gives a blinding effect when attacking.

Value: boolean

.. code-block:: javascript

        "blinding": false

========
Munchies
========

*Optional*

Does your bee give hunger to targets?

Value: boolean

.. code-block:: javascript

        "munchies": false
