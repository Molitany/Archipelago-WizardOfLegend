from enum import Enum
from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List, Set

class ItemType(Enum):
    Relic = 1
    Outfit = 2
    Basic = 3
    Dash = 4
    Optional = 5
    Signature = 6
    BossTier = 7

class ItemDict(TypedDict):
    name: str
    type: ItemType
    classification: ItemClassification

base_id = 16000

group_table: Dict[str, Set[str]] = {
    "relics": [
        "PlayerStart",
        "BuffWithFriendship",
        "WaterChargeFamiliarItem",
        "DamageUp",
        "EmpowerAllArcanaAtMaxHealth",
        "EmpowerArcanaOnStageLoad",
        "DamageUpAtLowHealth",
        "DamageUpWithInventoryCount",
        "DamageUpWithKills",
        "FireDamageUp",
        "AirDamageUp",
        "EarthDamageUp",
        "LightningDamageUp",
        "WaterDamageUp",
        "IceStanza",
        "BlackWolfCoat",
        "DamageUpWithDiffElement",
        "DamageUpWithSameElement",
        "DamageUpWithGold",
        "DamageUpWhenHurt",
        "DamageUpWithMapReveal",
        "DamageUpWithCC",
        "BurnChanceUp",
        "SlowChanceUp",
        "PoisonChanceUp",
        "ShockChanceUp",
        "FreezeChanceUp",
        "BurnLevelUp",
        "PoisonLevelUp",
        "ShockLevelUp",
        "CritChanceUp",
        "CritDamageUp",
        "MeleeCritChanceUp",
        "BasicCancelIncreasesCrit",
        "CritAfterEvade",
        "CritUpAtLowHealth",
        "OutOfCombatCrit",
        "SuperCritChance",
        "BuffWithOverdrive",
        "WanderersFigurine",
        "ODIncreaseOnUse",
        "OverdriveDoubler",
        "FireAura",
        "LightningAura",
        "FrostAura",
        "DoubleAttackChance",
        "ExplosionOnKillChance",
        "FreezeOnKillChance",
        "SevenFlushFire",
        "SevenFlushLightning",
        "HealthUp",
        "MaxHealthUpOnHeal",
        "MaxHealthUpOnTakeDamage",
        "HealDropBoostItem",
        "HealOnCrit",
        "OverdriveToHealth",
        "HealOnPlatPickup",
        "HealWithMapReveal",
        "PotionPack",
        "ResurrectArcanaLoss",
        "DeathProofCrown",
        "ElementalResistanceWithArcana",
        "FireResistanceUp",
        "EarthResistanceUp",
        "WaterResistanceUp",
        "BurnImmune",
        "PoisonImmune",
        "FreezeImmune",
        "ArmorUp",
        "ArmorUpAtLowHealth",
        "ArmorUpWithInventoryCount",
        "SequenceDefense",
        "DefenseUpOnTakeDamage",
        "PaperDefense",
        "EvadeUp",
        "EvadeCrit",
        "EvadeUpAtLowHealth",
        "MoveSpeedUp",
        "HorseMaskItem",
        "MoveSpeedUpPerCD",
        "EnhanceDash",
        "DashInvulnerability",
        "OverhealGrantsShield",
        "OverdriveDefense",
        "ShieldWithOverdriveTimeOut",
        "ParrySidestep",
        "IncreaseBuffDuration",
        "IgnorePits",
        "StatueCamo",
        "ReflectProjectileShield",
        "CapDamageItem",
        "DestroyEnemyProjectilesOnHit",
        "RootShield",
        "ShockShield",
        "MindControlOnHurt",
        "InvulnerableOnMultiHurt",
        "SevenFlushAir",
        "SevenFlushEarth",
        "ReduceCooldown",
        "TozysPocketWatch",
        "DashCancelLowersCD",
        "AltElementLowersCD",
        "ResetCDChance",
        "FreeCooldownsAtLowHealth",
        "KillsLowerCDs",
        "FreeDashChargesOnKillChance",
        "SummonDurationItem",
        "SummonDamageItem",
        "SummonCountItem",
        "FireChargeFamiliarItem",
        "AirChargeFamiliarItem",
        "EarthChargeFamiliarItem",
        "LightningChargeFamiliarItem",
        "KnockbackUp",
        "OverdriveBuildDecayDown",
        "OverdriveDurationUp",
        "HealOverdriveItem",
        "OverdriveMaxAtLowHealth",
        "OverdriveOnTakeDamage",
        "EnemyHPBars",
        "ExtraBasicCombo",
        "AutoBasicCombo",
        "MeleeBasicNegatesProjectiles",
        "AlwaysWinProjectiles",
        "SlowEnemyProjectiles",
        "BuffOnProjectileNegate",
        "ExtraSkillCharge",
        "IgnoreHurtDuringCast",
        "StageMap",
        "GoldUp",
        "GoldOnKillStreak",
        "GoldOnTakeDamage",
        "RelicDiscount",
        "SpellDiscount",
        "FreePurchaseChance",
        "StoreRestock",
        "BuyWithHP",
        "PortableTreasure",
        "PlateEnemyPreventSkills",
        "LeatherEnemyPreventSkills",
        "ClothEnemyPreventSkills",
        "SevenFlushWater",
        "RainbowTrail",
        "PlayerWin",
        "DoctorPrescription",
        "DoctorPlacebo",
        "DoctorDiscount",
        "DoctorVial",
        "FrostFlameStanza",
        "WanderersSet",
        "GlassCannon",
        "Vampiricism",
        "HalfGlass",
        "MaxHPDownRegenAtLowHP",
        "ResurrectRing",
        "DoubleToil",
        "DoubleTrouble",
        "CursedSeal",
        "AttackSpeedItem",
        "IgnoreDashSlide",
        "BasicDamageUpOtherDamageDown",
        "DamageUpNoOverdrive",
        "DamageUpVsBoss",
        "DamageUpStorePriceUp",
        "ArmorUpStorePriceUp",
        "ArmorUpDamageDown",
        "ArmorUpLoseGoldOnHit",
        "EnemyHealthDownEnemyDamageUp",
        "EnemyHealthDownPlayerHealthDown",
        "PlayerEnemyCritChanceUp",
        "EvadeUpEnemyDamageUp",
        "FullHPOnStartNoHeals",
        "HealOnStartZeroGold",
        "BankLoan",
        "NoPlatinumAllGold",
        "FireStanza",
        "WanderersDoll",
        "AoEStatusEffects",
        "DamageCritUpWithCursedRelics",
        "ProjectileDamageUp",
        "DamageUpWithDash",
        "BaseJumpSkillDamageUp",
        "MagicianHat",
        "OnBasicFireArcItem",
        "OnBasicAirTwisterItem",
        "OnBasicEarthDrillItem",
        "OnBasicLightningStrikeItem",
        "OnBasicWaterShotItem",
        "PoisonAura",
        "HealthUpWithMoveArcana",
        "HealthUpWithDefRelics",
        "RetributionHeal",
        "ArmorHPUpWithCursedRelics",
        "AirResistanceUp",
        "ElementalResistanceUpOnHurt",
        "SlowImmune",
        "EvadeUpOnHurt",
        "CritHealChanceUpLow",
        "ParryHeal",
        "StunShield",
        "LimitedGuard",
        "OverdriveToResetCDs",
        "LaserSightItem",
        "GradCap",
        "SpeedBoostOnSurvivalClear",
        "ReduceCDWithCursedRelics",
        "TokenCursed",
        "TokenShuffler",
        "TokenDoctor",
        "TokenTailor",
        "TokenCollector",
        "TokenBanker",
        "TokenPinata",
        "CritHealChanceUp",
        "HealRestock",
        "GradSet",
        "MagicianSet",
        "UnicornMask",
        "ParrySet",
        "GradBouquet",
        "MagicianWand",
        "ParryStun",
        "ArcanaBalancer",
        "ReduceCDReduceDamage",
        "FirstHitDamageUp",
        "DamageUpSkillsCostGold",
        "DamageUpClearInventory",
        "FlatDamage",
        "NoRandomPits",
        "RandomSkillAfterUse",
        "OneHPOneDamage",
        "RandomExplosiveBarrels",
        "LoseArcanaRelicOnHurtChance",
        "ReduceCDPlayerEnemy",
        "EnemyPlayerMoveSpeedUp",
        "RandomElementalEnemies",
        "VampireSoul",
        "RandomDisasters",
        "ExplosionOnKill",
        "DamageUpAtMaxHealth",
        "DamageUpWithBossPerfect",
        "MovementSkillDamageUp",
        "EmpowerBasicItem",
        "DamageUpWithPlatCount",
        "IncreaseWaveSize",
        "WaveDamageUp",
        "WindAuraItem",
        "FireArcanaCountItem",
        "LightningArcanaCountItem",
        "HealthUpWithEmpowered",
        "HealWithPitKill",
        "ArmorUpWithGold",
        "ArmorUpWithPlatCount",
        "ProjectileNegateShield",
        "LightningResistanceUp",
        "ShockImmune",
        "PreventHealDecrease",
        "BurstOnDotItem",
        "IgnoreDeathChance",
        "AirArcanaCountItem",
        "EarthArcanaCountItem",
        "OverdriveGainUp",
        "KeepSigOnDash",
        "ReduceBasicChargeTime",
        "SummonHealthItem",
        "SummonCDItem",
        "SummonVampiricItem",
        "GoldOnBossKillWithWeakness",
        "RandomRelicChest",
        "RandomArcanaChest",
        "ItemStoreLocatorItem",
        "SkillStoreLocatorItem",
        "MiscRoomLocatorItem",
        "PlatFinderItem",
        "WaterArcanaCountItem",
        "DoctorHpDamage",
        "VampireSet",
        "MaxHealthUpRegen",
        "ParryTrio",
        "PerfectRoomLocatorItem",
        "StatusChanceUpGroupItem",
        "OnBasicUseGroupItem",
        "ChargeFamiliarGroupItem",
        "AuraGroupItem",
        "ResistanceUpGroupItem",
        "ImmuneGroupItem",
        "DiscountGroupItem",
        "WithCursedRelicsGroupItem",
        "RoomLocatorGroupItem",
        "GoldGroupItem",
        "ArcanaCountGroupItem",
        "SummonGroupItem",
        "OverdriveUpEmptyOnHurt",
        "DamageUpNoEnemyKnockback",
        "HealthToGold",
        "EmpoweredDamageUp",
        "ReplaceNonCursedRelics",
        "CritChanceDownDamageUp",
        "HalfHammer",
        "EvadeUpCritDown",
        "ExitRoomLocatorItem",
        "ProjDamageUpMeleeDamageDown",
        "BasicChargeTimeUp",
        "MaxHPDownDamageUpPercent",
        "SummonDamageDurationUpCooldownUp",
        "CritDamageUpDamageDown",
        "NoPlatinumDamageUp",
        "BuyWithPlat",
        "DamageOnStageLoad",
        "SignatureOnStageLoad",
        "EnemyCountUp",
        "CurseEveryFloor",
        "PlayerEnemyStatusImmune",
    ],
    "skills_basic": [
        "FlameStrikeBasic",
        "FireOrbBasic",
        "FlameCrossBasic",
        "FireBounceBasic",
        "WindSlashBasic",
        "AirStreakBasic",
        "AirSpinBasic",
        "AirDartBasic",
        "EarthSpikeBasic",
        "VineWhipBasic",
        "EarthAxeBasic",
        "RockThrowBasic",
        "ShockTouchBasic",
        "LightningFistBasic",
        "BoltRailBasic",
        "ThunderOrbBasic",
        "IceDaggerBasic",
        "AquaCrestBasic",
        "IceChargeSwordBasic",
        "WaterArcBasic",
        "ChaosScytheBasic",
        "ChaosBasic",
        "PhantomRoguesBasic",
    ],
    "skills_dash": [
        "FlameShieldDash",
        "FireDash",
        "MagmaBombDash",
        "FireMineDash",
        "Dash",
        "SlicingFieldDash",
        "AirTrapDash",
        "AirChannelDash",
        "EarthDash",
        "PoisonDash",
        "VinePullDash",
        "VineDash",
        "ThunderDash",
        "LightningShadowDash",
        "LightningDash",
        "ChainedDash",
        "WaterDash",
        "IceDash",
        "BubbleDash",
        "FrostWingDash",
        "ChaosDash",
        "ChaosCloneDash",
        "PhantomMageDash",
    ],
    "skills_optionals": [
        "Berserk",
        "CircleBurner",
        "RisingDragon",
        "FlameLeap",
        "ExplosiveCharge",
        "FlamePunch",
        "FlameWolf",
        "FlameSwirl",
        "BlazingBlitz",
        "BlazingCombo",
        "FireBlast",
        "HomingMissiles",
        "FlameReturner",
        "ShootFireArc",
        "ShootFireball",
        "FlakField",
        "FlameSlash",
        "FlameBuster",
        "VacuumFlame",
        "FireBeam",
        "CombustionWave",
        "FireWall",
        "FireBombard",
        "MeteorStrike",
        "FlameTrap",
        "FlameSeekers",
        "FireMinion",
        "FireWard",
        "WindDefense",
        "AeroRing",
        "VortexOrbital",
        "BabylonScales",
        "Tornado",
        "Whirlwind",
        "HeroicLeap",
        "WindSlam",
        "TornadoKick",
        "AeroRipple",
        "SlicingBarrage",
        "TumbleFist",
        "DragonBreath",
        "VortexWave",
        "ShootArrow",
        "ShootVacuumShot",
        "SwordThrow",
        "MindControlCloud",
        "WindFalcon",
        "Twister",
        "AirSentry",
        "WindBall",
        "MultiShot",
        "SonicBoom",
        "AirWave",
        "WindSeekers",
        "WindMinion",
        "WindWard",
        "EarthEnhance",
        "BoulderShield",
        "SpikeRing",
        "GraspingEarth",
        "EarthJump",
        "ShieldCharge",
        "EarthDrill",
        "StalwartDefenders",
        "ShatterStone",
        "EarthRebound",
        "VineJump",
        "HammerThrow",
        "EarthBoomerang",
        "WhirlingAxe",
        "ThrowBoulder",
        "PoisonBolas",
        "ExplodingBoulder",
        "EarthCascade",
        "DrillFan",
        "EarthWheel",
        "DragonStomp",
        "ChurningEarth",
        "EarthAxe",
        "VineWave",
        "PlantBarrage",
        "EarthSeekers",
        "EarthMinion",
        "EarthWard",
        "ElectricAura",
        "MagSphere",
        "ShockNova",
        "VoltSplinter",
        "ThunderDrop",
        "PiercingShock",
        "TeleStrike",
        "LightningFist",
        "LightningSword",
        "ShockWhip",
        "LightningShuriken",
        "LightningXStrike",
        "CurrentBurst",
        "ShockSpear",
        "ShockBoomerang",
        "ShockDragon",
        "ShootBallLightning",
        "ShockVolley",
        "ShootBoltClaymore",
        "ThunderFan",
        "ThunderWave",
        "ShockLace",
        "IonSpike",
        "ShockLine",
        "ThunderAnchor",
        "ThunderSeekers",
        "LightningMinion",
        "LightningWard",
        "AquaCooling",
        "FrostBlock",
        "CircleStrike",
        "SwordStorm",
        "IceChakram",
        "Whirlpool",
        "WaterSlam",
        "FrostSurf",
        "AquaBlitz",
        "FrostSwing",
        "FreezingLunge",
        "CreepingTendril",
        "WaterBlast",
        "IceBoomerang",
        "AquaPrison",
        "WaterBounce",
        "ThrowIceLance",
        "WaterBall",
        "BubbleBarrage",
        "FrostFan",
        "IceWave",
        "Blizzard",
        "AquaBeam",
        "Shark",
        "AquaDragon",
        "IceSeekers",
        "WaterMinion",
        "WaterWard",
        "ChaosWeapons",
        "VoidShift",
        "ChaosDrop",
        "ChaosLunge",
        "MortalCoil",
        "ChaosBall",
        "ChaosBeam",
        "ChaosSword",
        "ChaosSwordStorm",
        "ChaosCluster",
        "PhantomKnights",
        "PhantomLancers",
        "PhantomArchers",
        "Phantomers",
        "DragonGrade",
        "ChaosMinion",
        "ChaosWard",
        "ChaosEraser",
    ],
    "skills_signatures": [
        "RisingDragon",
        "FlameSwirl",
        "BlazingBlitz",
        "FireBlast",
        "HomingMissiles",
        "FlameReturner",
        "ShootFireArc",
        "ShootFireball",
        "FlameSlash",
        "VacuumFlame",
        "FireBeam",
        "MeteorStrike",
        "Tornado",
        "Whirlwind",
        "WindSlam",
        "AeroRipple",
        "SlicingBarrage",
        "TumbleFist",
        "ShootArrow",
        "ShootVacuumShot",
        "SwordThrow",
        "WindFalcon",
        "MultiShot",
        "SonicBoom",
        "SpikeRing",
        "EarthJump",
        "EarthDrill",
        "ShatterStone",
        "HammerThrow",
        "EarthBoomerang",
        "WhirlingAxe",
        "PoisonBolas",
        "EarthCascade",
        "EarthWheel",
        "EarthAxe",
        "PlantBarrage",
        "ShockNova",
        "VoltSplinter",
        "ThunderDrop",
        "PiercingShock",
        "TeleStrike",
        "LightningFist",
        "LightningSword",
        "LightningXStrike",
        "CurrentBurst",
        "ShockDragon",
        "ShootBallLightning",
        "ThunderFan",
        "IceChakram",
        "Whirlpool",
        "FrostSwing",
        "FreezingLunge",
        "WaterBlast",
        "IceBoomerang",
        "ThrowIceLance",
        "WaterBall",
        "FrostFan",
        "IceWave",
        "AquaBeam",
        "AquaDragon",
        "VoidShift",
        "ChaosDrop",
        "ChaosLunge",
        "MortalCoil",
        "ChaosBall",
        "ChaosBeam",
        "ChaosSword",
        "ChaosSwordStorm",
        "ChaosCluster",
        "PhantomKnights",
        "ChaosMinion",
        "ChaosEraser",
    ],
    "outfits": [
        "Hope",
        "Patience",
        "Vigor",
        "Grit",
        "Greed",
        "Pink",
        "Pace",
        "Tempo",
        "Switch",
        "Awe",
        "Fury",
        "Rule",
        "Level",
        "Venture",
        "Fall",
        "Pride",
    ],
    "progression": [
        "Boss tier 1",
        "Boss tier 2",
        "Boss tier 3",
        "Final boss",
    ]
}

item_table: List[ItemDict] = [
    {
        "name": "FlameStrikeBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFireOrbBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FlameCrossBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FireBounceBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAirStreakBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AirSpinBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AirDartBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EarthSpikeBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "VineWhipBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthAxeBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseRockThrowBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShockTouchBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseLightningFistBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BoltRailBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ThunderOrbBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "IceDaggerBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AquaCrestBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseIceChargeSwordBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "WaterArcBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseChaosScytheBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UsePhantomRoguesBasic",
        "type": "ItemType.Basic",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "FlameShieldDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FireDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MagmaBombDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FireMineDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SlicingFieldDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AirTrapDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AirChannelDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EarthDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PoisonDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "VinePullDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "VineDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ThunderDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "LightningShadowDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "LightningDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ChainedDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "WaterDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "IceDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BubbleDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FrostWingDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ChaosDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "ChaosCloneDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "PhantomMageDash",
        "type": "ItemType.Dash",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "Berserk",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseCircleBurner",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseRisingDragon",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlameLeap",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseExplosiveCharge",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlamePunch",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlameWolf",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlameSwirl",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseBlazingBlitz",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseBlazingCombo",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFireBlast",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonHomingMissiles",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlameReturner",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlakField",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlameSlash",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlameBuster",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseVacuumFlame",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFireBeam",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseCombustionWave",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonFireWall",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFireBombard",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonMeteorStrike",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlameTrap",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlameSeekers",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFireMinion",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFireWard",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWindDefense",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAeroRing",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseVortexOrbital",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseBabylonScales",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonTornado",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWhirlwind",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseHeroicLeap",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWindSlam",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseTornadoKick",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAeroRipple",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseSlicingBarrage",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonTumbleFist",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseDragonBreath",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseVortexWave",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShootArrow",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShootVacuumShot",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SwordThrow",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseMindControlCloud",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWindFalcon",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseTwister",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAirSentry",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWindBall",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MultiShot",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseSonicBoom",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAirWave",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWindSeekers",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWindMinion",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWindWard",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthEnhance",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonBoulderShield",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseSpikeRing",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseGraspingEarth",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthJump",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShieldCharge",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthDrill",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "StalwartDefenders",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShatterStone",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthRebound",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseVineJump",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseHammerThrow",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthBoomerang",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWhirlingAxe",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseThrowBoulder",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UsePoisonBolas",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseExplodingBoulder",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthCascade",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseDrillFan",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthWheel",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseDragonStomp",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonChurningEarth",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthAxe",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseVineWave",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UsePlantBarrage",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthSeekers",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthMinion",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthWard",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseElectricAura",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseMagSphere",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShockNova",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseVoltSplinter",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseThunderDrop",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UsePiercingShock",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "TeleStrike",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseLightningFist",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseLightningSword",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShockWhip",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseLightningShuriken",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseLightningXStrike",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseCurrentBurst",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShockSpear",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShockBoomerang",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShockDragon",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShootBallLightning",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShockVolley",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShootBoltClaymore",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseThunderFan",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonThunderWave",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShockLace",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseIonSpike",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShockLine",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseThunderAnchor",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseThunderSeekers",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseLightningMinion",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseLightningWard",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAquaCooling",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFrostBlock",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CircleStrike",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonSwordStorm",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseIceChakram",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWhirlpool",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWaterSlam",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFrostSurf",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAquaBlitz",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFrostSwing",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FreezingLunge",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseCreepingTendril",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWaterBlast",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseIceBoomerang",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAquaPrison",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWaterBounce",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ThrowIceLance",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWaterBall",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonBubbleBarrage",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonBlizzard",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAquaBeam",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonShark",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAquaDragon",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonIceSeekers",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWaterMinion",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWaterWard",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseChaosWeapons",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseVoidShift",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosDrop",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosLunge",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseMortalCoil",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosBall",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosBeam",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosSwordSummon",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosSwordStorm",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosCluster",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UsePhantomKnights",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UsePhantomLancers",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UsePhantomArchers",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UsePhantomSummoners",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseDragonGrade",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosMinion",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosWard",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosEraser",
        "type": "ItemType.Optional",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseRisingDragon",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlameSwirl",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseBlazingBlitz",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFireBlast",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonHomingMissiles",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlameReturner",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFlameSlash",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseVacuumFlame",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFireBeam",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonMeteorStrike",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonTornado",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWhirlwind",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWindSlam",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAeroRipple",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseSlicingBarrage",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonTumbleFist",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShootArrow",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShootVacuumShot",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SwordThrow",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWindFalcon",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MultiShot",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseSonicBoom",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseSpikeRing",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthJump",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthDrill",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShatterStone",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseHammerThrow",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthBoomerang",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWhirlingAxe",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UsePoisonBolas",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthCascade",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthWheel",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseEarthAxe",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UsePlantBarrage",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShockNova",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseVoltSplinter",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseThunderDrop",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UsePiercingShock",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "TeleStrike",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseLightningFist",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseLightningSword",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseLightningXStrike",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseCurrentBurst",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseShockDragon",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShootBallLightning",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseThunderFan",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseIceChakram",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWhirlpool",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseFrostSwing",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FreezingLunge",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWaterBlast",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseIceBoomerang",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ThrowIceLance",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseWaterBall",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAquaBeam",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseAquaDragon",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UseVoidShift",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosDrop",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosLunge",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseMortalCoil",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosBall",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosBeam",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosSwordSummon",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosSwordStorm",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosCluster",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UsePhantomKnights",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosMinion",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "UseChaosEraser",
        "type": "ItemType.Signature",
        "classification": "ItemClassification.useful"
    },
    {
        "name": "DamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EmpowerAllArcanaAtMaxHealth",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EmpowerArcanaOnStageLoad",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpAtLowHealth",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpWithInventoryCount",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpWithKills",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FireDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AirDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EarthDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "LightningDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "WaterDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "IceStanza",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BlackWolfCoat",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpWithDiffElement",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpWithSameElement",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpWithGold",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpWhenHurt",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpWithMapReveal",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpWithCC",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BurnChanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SlowChanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PoisonChanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShockChanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FreezeChanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BurnLevelUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PoisonLevelUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShockLevelUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CritChanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CritDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MeleeCritChanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BasicCancelIncreasesCrit",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CritAfterEvade",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CritUpAtLowHealth",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OutOfCombatCrit",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SuperCritChance",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BuffWithOverdrive",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "WanderersFigurine",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ODIncreaseOnUse",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OverdriveDoubler",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FireAura",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "LightningAura",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FrostAura",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DoubleAttackChance",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ExplosionOnKillChance",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FreezeOnKillChance",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SevenFlushFire",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SevenFlushLightning",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealthUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MaxHealthUpOnHeal",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MaxHealthUpOnTakeDamage",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealDropBoostItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealOnCrit",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OverdriveToHealth",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealOnPlatPickup",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealWithMapReveal",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PotionPack",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ResurrectArcanaLoss",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DeathProofCrown",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ElementalResistanceWithArcana",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FireResistanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EarthResistanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "WaterResistanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BurnImmune",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PoisonImmune",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FreezeImmune",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ArmorUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ArmorUpAtLowHealth",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ArmorUpWithInventoryCount",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SequenceDefense",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DefenseUpOnTakeDamage",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PaperDefense",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EvadeUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EvadeCrit",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EvadeUpAtLowHealth",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MoveSpeedUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HorseMaskItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MoveSpeedUpPerCD",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EnhanceDash",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DashInvulnerability",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OverhealGrantsShield",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OverdriveDefense",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShieldWithOverdriveTimeOut",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ParrySidestep",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "IncreaseBuffDuration",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "IgnorePits",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "StatueCamo",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ReflectProjectileShield",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CapDamageItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DestroyEnemyProjectilesOnHit",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "RootShield",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShockShield",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MindControlOnHurt",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "InvulnerableOnMultiHurt",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SevenFlushAir",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SevenFlushEarth",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ReduceCooldown",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "TozysPocketWatch",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DashCancelLowersCD",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AltElementLowersCD",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ResetCDChance",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FreeCooldownsAtLowHealth",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "KillsLowerCDs",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FreeDashChargesOnKillChance",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonDurationItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonDamageItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonCountItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FireChargeFamiliarItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AirChargeFamiliarItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EarthChargeFamiliarItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "LightningChargeFamiliarItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "KnockbackUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OverdriveBuildDecayDown",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OverdriveDurationUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealOverdriveItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OverdriveMaxAtLowHealth",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OverdriveOnTakeDamage",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EnemyHPBars",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ExtraBasicCombo",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AutoBasicCombo",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MeleeBasicNegatesProjectiles",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AlwaysWinProjectiles",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SlowEnemyProjectiles",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BuffOnProjectileNegate",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ExtraSkillCharge",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "IgnoreHurtDuringCast",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "StageMap",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "GoldUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "GoldOnKillStreak",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "GoldOnTakeDamage",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "RelicDiscount",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SpellDiscount",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FreePurchaseChance",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "StoreRestock",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BuyWithHP",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PortableTreasure",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PlateEnemyPreventSkills",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "LeatherEnemyPreventSkills",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ClothEnemyPreventSkills",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SevenFlushWater",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "RainbowTrail",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PlayerWin",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DoctorPrescription",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DoctorPlacebo",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DoctorDiscount",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DoctorVial",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FrostFlameStanza",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "WanderersSet",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "GlassCannon",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Vampiricism",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HalfGlass",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MaxHPDownRegenAtLowHP",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ResurrectRing",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DoubleToil",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DoubleTrouble",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CursedSeal",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AttackSpeedItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "IgnoreDashSlide",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BasicDamageUpOtherDamageDown",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpNoOverdrive",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpVsBoss",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpStorePriceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ArmorUpStorePriceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ArmorUpDamageDown",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ArmorUpLoseGoldOnHit",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EnemyHealthDownEnemyDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EnemyHealthDownPlayerHealthDown",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PlayerEnemyCritChanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EvadeUpEnemyDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FullHPOnStartNoHeals",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealOnStartZeroGold",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BankLoan",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "NoPlatinumAllGold",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FireStanza",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "WanderersDoll",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AoEStatusEffects",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageCritUpWithCursedRelics",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ProjectileDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpWithDash",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BaseJumpSkillDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MagicianHat",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OnBasicFireArcItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OnBasicAirTwisterItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OnBasicEarthDrillItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OnBasicLightningStrikeItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OnBasicWaterShotItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PoisonAura",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealthUpWithMoveArcana",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealthUpWithDefRelics",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "RetributionHeal",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ArmorHPUpWithCursedRelics",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AirResistanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ElementalResistanceUpOnHurt",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SlowImmune",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EvadeUpOnHurt",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CritHealChanceUpLow",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ParryHeal",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "StunShield",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "LimitedGuard",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OverdriveToResetCDs",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "LaserSightItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "GradCap",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SpeedBoostOnSurvivalClear",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ReduceCDWithCursedRelics",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "TokenCursed",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "TokenShuffler",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "TokenDoctor",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "TokenTailor",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "TokenCollector",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "TokenBanker",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "TokenPinata",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CritHealChanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealRestock",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "GradSet",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MagicianSet",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "UnicornMask",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ParrySet",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "GradBouquet",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MagicianWand",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ParryStun",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ArcanaBalancer",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ReduceCDReduceDamage",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FirstHitDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpSkillsCostGold",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpClearInventory",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FlatDamage",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "NoRandomPits",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "RandomSkillAfterUse",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OneHPOneDamage",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "RandomExplosiveBarrels",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "LoseArcanaRelicOnHurtChance",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ReduceCDPlayerEnemy",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EnemyPlayerMoveSpeedUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "RandomElementalEnemies",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "VampireSoul",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "RandomDisasters",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ExplosionOnKill",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpAtMaxHealth",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpWithBossPerfect",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MovementSkillDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EmpowerBasicItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpWithPlatCount",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "IncreaseWaveSize",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "WaveDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "WindAuraItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "FireArcanaCountItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "LightningArcanaCountItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealthUpWithEmpowered",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealWithPitKill",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ArmorUpWithGold",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ArmorUpWithPlatCount",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ProjectileNegateShield",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "LightningResistanceUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ShockImmune",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PreventHealDecrease",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BurstOnDotItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "IgnoreDeathChance",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AirArcanaCountItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EarthArcanaCountItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OverdriveGainUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "KeepSigOnDash",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ReduceBasicChargeTime",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonHealthItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonCDItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonVampiricItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "GoldOnBossKillWithWeakness",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "RandomRelicChest",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "RandomArcanaChest",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ItemStoreLocatorItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SkillStoreLocatorItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MiscRoomLocatorItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PlatFinderItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "WaterArcanaCountItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DoctorHpDamage",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "VampireSet",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MaxHealthUpRegen",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ParryTrio",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PerfectRoomLocatorItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "StatusChanceUpGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OnBasicUseGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ChargeFamiliarGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "AuraGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ResistanceUpGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ImmuneGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DiscountGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "WithCursedRelicsGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "RoomLocatorGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "GoldGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ArcanaCountGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonGroupItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "OverdriveUpEmptyOnHurt",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageUpNoEnemyKnockback",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HealthToGold",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EmpoweredDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ReplaceNonCursedRelics",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CritChanceDownDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "HalfHammer",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EvadeUpCritDown",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ExitRoomLocatorItem",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "ProjDamageUpMeleeDamageDown",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BasicChargeTimeUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "MaxHPDownDamageUpPercent",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SummonDamageDurationUpCooldownUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CritDamageUpDamageDown",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "NoPlatinumDamageUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "BuyWithPlat",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "DamageOnStageLoad",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "SignatureOnStageLoad",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "EnemyCountUp",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "CurseEveryFloor",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "PlayerEnemyStatusImmune",
        "type": "ItemType.Relic",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Vigor",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Grit",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Greed",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Pink",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Pace",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Tempo",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Switch",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Awe",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Fury",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Rule",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Level",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Venture",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Fall",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Pride",
        "type": "ItemType.Outfit",
        "classification": "ItemClassification.filler"
    },
    {
        "name": "Boss tier 2",
        "type": "ItemType.BossTier",
        "classification": "ItemClassification.progression"
    },
    {
        "name": "Boss tier 3",
        "type": "ItemType.BossTier",
        "classification": "ItemClassification.progression"
    },
    {
        "name": "Final boss",
        "type": "ItemType.BossTier",
        "classification": "ItemClassification.progression"
    }
]