# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionSet

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class Goal(Choice):
    """
    Which goal counts as victory.

    - twisted_rosalia: Unlock and complete FINAL-13 Twisted Rosalia
    - medals: Achieve the specified amount of Medals
    """
    display_name = "Goal"
    option_twisted_rosalia = 0
    option_medals = 1
    default = 0

class MedalPercent(Range):
    """
    If the goal is Medals, what percentage of them are required to goal.
    Some Medals may be on or doable only after FINAL-13.
    44 out of the game's 48 Medals are available. XS clear medals are not counted (yet).
    """
    display_name = "Medal Percentage"
    range_start = 1
    range_end = 100
    default = 50

class AvailCharacters(OptionSet):
    """
    List of characters than can appear in the pool. CR-S01 is mandatory and cannot be defined here.
    To start with specific characters use start_inventory.
    """
    display_name = "Available Characters"
    valid_keys = ['Gabriel','Hank','Maria','Naomi','Tomoe']
    default = ['Gabriel','Hank','Maria','Naomi','Tomoe']

class Toolsanity(Toggle):
    """
    Shuffle each character's tools into the pool.
    For example, no Surgery can be completed without "S Sutures".
    """
    display_name = "Toolsanity"

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    #options["goal"] = Goal
    #options["medal_percentage"] = MedalPercent
    #options["enabled_characters"] = AvailCharacters
    #options["toolsanity"] = Toolsanity
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options