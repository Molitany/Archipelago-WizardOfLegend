from typing import Dict
from BaseClasses import Item, ItemClassification, Location, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule
from .Items import ItemDict, ItemType, item_table, group_table, base_id
from .Locations import location_names
from .Options import WoLOptions


class WizardOfLegendWeb(WebWorld):
    theme = "partytime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Wizard of Legend",
        "English",
        "setup_en.md",
        "setup/en",
        ["Molitany"]
    )]


class WizardOfLegendWorld(World):
    """
    asd
    """
    game: str = "Wizard of Legend"
    web = WizardOfLegendWeb()
    data_version = 2

    item_name_to_id = {item["name"]: base_id +
                       index for index, item in enumerate(item_table)}
    location_name_to_id = {loc: base_id +
                           index for index, loc in enumerate(location_names)}

    item_name_groups = group_table
    options_dataclass = WoLOptions
    options: WoLOptions

    required_client_version = (0, 4, 6)

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        game_region = Region("InGame", self.player, self.multiworld)
        self.multiworld.regions += [menu_region, game_region]
        menu_region.connect(game_region)

        locations = [WizardOfLegendLocation(
            self.player, loc_name, self.location_name_to_id[loc_name], game_region) for loc_name in location_names]
        game_region.locations.extend(locations)

        victory = WizardOfLegendLocation(
            self.player, "Master Sura", None, game_region)
        victory.place_locked_item(self.create_event("Victory"))
        set_rule(victory, lambda state: state.has("Master Sura"))
        game_region.locations.append(victory)
        
        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            "Victory", self.player)

    def create_items(self) -> None:
        exclude = [
            item for item in self.multiworld.precollected_items[self.player]]

        pool = []
        for item in item_table:
            if item in exclude:
                self.multiworld.itempool.append(self.create_item("nothing"))
            else:
                pool.append(self.create_item(item["name"]))
        self.multiworld.itempool += pool

    def set_rules(self) -> None:
        set_rule(self.multiworld.get_location("Boss tier 2", self.player),
                 lambda state: state.has("Boss tier 1", self.player))

        set_rule(self.multiworld.get_location("Boss tier 3", self.player),
                 lambda state: state.has("Boss tier 2", self.player))

        set_rule(self.multiworld.get_location("Master Sura", self.player),
                 lambda state: state.has("Boss tier 3", self.player))

    def create_item(self, name: str) -> "WizardOfLegendItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id
        return WizardOfLegendItem(name, item_table[id]["classification"], item_id, player=self.player)

    def create_event(self, event: str):
        return WizardOfLegendItem(event, ItemClassification.progression_skip_balancing, None, self.player)


class WizardOfLegendItem(Item):
    game: str = "Wizard of Legend"


class WizardOfLegendLocation(Location):
    game: str = "Wizard of Legend"
