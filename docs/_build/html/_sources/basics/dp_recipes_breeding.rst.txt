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

Required.  The bee offspring or array (list) of potential bees as a result of breeding.

.. code-block:: javascript

        "offspring": [
                "productivebees:yellorium"
        ]

Breeding Items
==============

Required.  An array (list) of usable items for breeding. 

.. code-block:: javascript

        "breeding_items": [
                {
                        "item": "minecraft:flowers"
                }
        ]