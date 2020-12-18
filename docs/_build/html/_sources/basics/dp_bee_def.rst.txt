Bee Definition
**************

Defining a bee

=============
Primary Color
=============

Hex Color Code for the primary color of the bee,  and spawn egg.

Required if not using a custom texture.  One of two main key: values
needed to create a bee. (If not using custom texture.)

Value: String (Hex color code)

.. code-block:: javascript

    "primaryColor": "#f2f24f"


===============
Secondary Color
===============

Hex Color Code for the primary color of the bee,  and spawn egg.

Required if not using a custom texture.  One of two main key: values
needed to create a bee. (If not using custom texture.)

Value: String (Hex color code)


.. code-block:: javascript

    "primaryColor": "#f2f24f"


==============
Particle Color
==============

Hex Color Code for the particles the bees emit.

Value: String (Hex color code)

.. code-block:: javascript

    "secondaryColor": "#d0581f"


===========
Bee Texture
===========

If you would like to use a custom texture for your bee,  other wise the default
one with the colors will be used instead.

Value: String (resource location)

.. code-block:: javascript

        "beeTexture": "productivebees:textures/entity/bee/base/bee"


===========
Create Comb
===========

Whether or not to create a comb for your bee.

Value: boolean

.. code-block:: javascript

        "createComb": true


===============
Attack Response
===============

This is for if you would like your bee to use a different attack response.  Valid
options are fire,  and lava.

Values: [ "fire", "lava" ]

.. code-block:: javascript

        "attackResponse": "fire"


=============
Teleportation
=============

If you would like for your bee to be able to teleport. Such as the :ref:`Ender<Ender>` bee for example.
(This could prove to make things interesting lol.)

Value: boolean

.. code-block:: javascript

        "teleporting": true


===========
Fire Proof
===========

Is your bee fireproof?

Value: boolean

.. code-block:: javascript

        "fireproof": true


===========
Translucent
===========

Should your bee be translucent?

Value: boolean

.. code-block:: javascript

        "translucent": false


========
Draconic
========

Allows for your bee to live in egg hives and gives them protection from dragon's breath attack;

Value: boolean

.. code-block:: javascript

        "draconic": true


========
Redstone
========

Should your bee emit a redstone signal?

Value: boolean

.. code-block:: javascript

        "redstoned": true


=====
Slimy
=====

Whether or not your bee drips particles.

Value: boolean

.. code-block:: javascript

        "slimy": true


=========
Withering
=========

Whether or not your bee gives a withered effect.

Value: boolean

.. code-block:: javascript

        "withered": true


===========
Blinding
===========

Whther or not your bee gives a blinding effect.

Value: boolean

.. code-block:: javascript

        "blinding": true


========
Munchies
========

Does your bee give hunger to nearby people?

Value: boolean

.. code-block:: javascript

        "munchies": false


=====================
Additional Attributes
=====================

These are additional attributes for your bee.  Such as weathr tolerance,
productivity,  etc.  Each of these key: value pairs are optional.  You can
include one or all.

Value: boolean

.. code-block:: javascript

        "attributes": {
                "temper": 1,
                "endurance": 2,
                "behavior": 2,
                "productivity": 2,
                "weather_tolerance": 2
        }
