Bee Breeding Recipes
********************

Defining recipes for bee breeding.
==================================



Type
====

Required. This will always be this value.

.. code-block:: javascript

        "type": "productivebees:bee_breeding"

Parents
=======

Required.  The two parents for creating your bee.

.. code-block:: javascript

        "parent1": "productivebees:glowing",
        "parent2": "productivebees:blazing"

Offspring
=========

Required.  The bee offspring. The name of the bee is the filename used for the bee definition.

.. code-block:: javascript

        "offspring": [
            "productivebees:your_bee_name"
        ]

Breeding Items
==============

Required.  An array (list) of usable items for breeding. While they are not used at the moment, it's a planned feature so it's better to include them now.
First item will be for parent1, second item in the list will be for parent2.

.. code-block:: javascript

        "breeding_items": [
            {
                "item": "minecraft:dirt"
            },
            {
                "tag": "minecraft:flowers"
            }
        ]

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