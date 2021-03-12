Bee Conversion Recipes
**********************

Bee conversion is the second way available for providing a means to create your bee.

Type
====

Required. This will always be this value.

.. code-block:: javascript

        "type": "productivebees:bee_conversion"

Source Bee
==========

Required.  The bee to bee used for the conversion recipe.

.. code-block:: javascript

      "source": "minecraft:bee"


Result
======

Required.  The bee produced from the conversion recipe.

.. code-block:: javascript

      "result": "productivebees:bacon"


Conversion Item
===============

Required.  The item or itemtag used for the bee conversion.

.. code-block:: javascript

        "item": {
                "tag": "forge:rawpork"
        }

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