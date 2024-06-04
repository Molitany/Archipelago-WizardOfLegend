from dataclasses import dataclass
from Options import Choice, DeathLink, PerGameCommonOptions, StartInventoryPool

class WoLDeathLink(DeathLink):
    """When you die, everyone dies. The reverse is also true."""

@dataclass
class WoLOptions(PerGameCommonOptions):
    death_link: WoLDeathLink
    start_inventory: StartInventoryPool