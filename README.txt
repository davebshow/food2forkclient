================
Food2ForkClient
================

Getting Started
---------------

Use the Food2ForkClient object::

	from food2forkclient import Food2ForkClient

	food = Food2ForkClient()

Search for the most popular recipes::

	food.search()

Use query parameter to search for ingredients::

	food.search(q='chicken')

Use Food2Fork's builtin pagination::

	food.search(q='chicken', page=2)

Control number of results::

	food.search(q='chicken', page=2, count=20)

Search for multiple ingredient::

	food.search(q='chicken,pesto', page=1, count=20)

Get the recipes ingredients::

	food.get('26851')




