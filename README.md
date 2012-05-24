roost
=====

Roost is a python-centric library for Twitter data collection and storage.  The library provides the necessary tools to connect processes that collect content from Twitter directly to storage systems that hold the data in easy-to-access forms.

Release schedule
----------------

The library is based on an internal `networkdynamics <http://www.networkdynamics.org>`_ utility that is now being made public.  To ensure readability and maintainability, the library is being unrolled in several stages.

	#. A module, python class, and command-line utility for making calls to the Twitter API
	#. A framework for storing and retrieving Twitter data in a MySQL database
	#. A command-line tool for collecting Twitter data using the API and storing the data into a MySQL database
	#. A module and class connecting to the firehose in various forms
	#. A command-line tool for collecting Twitter data from the firehose and storing the data into a MySQL database or flatfile

At present, only the first stage has been completed.
	
Contact
-------

Please email the primary author of the tool with any questions: `Derek Ruths <mailto:druths@networkdynamics.org>`_.