# Plugins for DecoraterBot

Commands are usually *normally* using the `::` prefix unless otherwise set for the plugin itself.

*Documentation on all the things available for plugins is not complete yet.*

*Discord.py normal context code can mostly be used as well.*

Plugins can supply Commands as well.

To start out a plugin be sure to make a ``setup`` function like so:

Note: Do not forget to ``from discord.ext import commands`` after ``import discord`` first.

```py
def setup(bot):
    """
    Example plugin for DecoraterBot.
    """
    bot.add_cog(YourPluginClassHere(bot))
```

To start out the Plugin class after this is like so:

```py
class YourPluginClassHere(object):
    """
    Example Plugin Class.
    """
    def __init__(self, bot):
        self.bot = bot
```

Plugins can also have an ``__load`` and ``__unload`` method in the class you make for the plugin.
This can help make it easier to clean up some things you set locally to that plugin itself.

After that you can use the data on this table exactly the way it is in it.

|   	| Available Plugin Attributes.	|
|:------:	|:-:	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|
| ``...``	| ...	|

## Events

Plugins and all commands inside them can have events to listen to. This can allow someone that can make a plugin that can log information.

For this I plan to rewrite DecoraterBot a bit to have all logging (except for the game command logs) to be loged from a Default plugin to load.
