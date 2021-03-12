Bee Production Recipes
**********************

Recipe defining what a bee produces inside an advanced hive.

Type
====

Required. This will always be this value.

.. code-block:: javascript

        "type": "productivebees:advanced_beehive"

Bee Ingredient
==============

Required. The id of the bee.

.. code-block:: javascript

      "ingredient": "productivebees:coal"


Results
=======

Required. The array of output items. min, max and chance are optional.

.. code-block:: javascript

      "results": [
          {
              "item": {
                  "tag": "forge:honeycombs/fossilised"
              }
          },
          {
              "item": {
                  "item": "minecraft:coal"
              },
              "min": 1.0,
              "max": 2.0,
              "chance": 30
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