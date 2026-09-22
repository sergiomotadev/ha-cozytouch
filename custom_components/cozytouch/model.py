"""Atlantic Cozytouch device model mapping.

Mandatory :
    * modelId : modelId of the device
    * name : commercial name of the device.
    * type : device type from CozytouchDeviceType enum.
    * HVACModes : list of available HVAC value/mode pairs

Optional :
    * currentTemperatureAvailable : enable current temperature availability (default : True)
    * currentTemperatureAvailableZ1 : enable current temperature availability for Z1 (used for HEAT_PUMP, default : True)
    * currentTemperatureAvailableZ2 : enable current temperature availability for Z2 (used for HEAT_PUMP, default : True)
    * exhaustTemperatureAvailable : enable exhaust temperature availability (default : True)
    * fanModes : list of value/mode pairs
    * swingModes : list of value/mode pairs
    * quietModeAvailable : enable quiet mode availability (default : False)

"""  # noqa: D205

from enum import StrEnum

from homeassistant.components.climate import HVACMode
from homeassistant.components.climate.const import (
    FAN_AUTO,
    FAN_HIGH,
    FAN_LOW,
    FAN_MEDIUM,
    FAN_OFF,
    FAN_ON,
)

from .const import (
    HEATING_MODE_COMFORT,
    HEATING_MODE_ECO,
    HEATING_MODE_ECO_PLUS,
    HEATING_MODE_MANUAL,
    HEATING_MODE_PROG,
    SWING_MODE_DOWN,
    SWING_MODE_MIDDLE_DOWN,
    SWING_MODE_MIDDLE_UP,
    SWING_MODE_UP,
)


class CozytouchDeviceType(StrEnum):
    """Device types enum."""

    UNKNOWN = "unknown"
    THERMOSTAT = "thermostat"
    GAZ_BOILER = "gaz_boiler"
    HEAT_PUMP = "heat_pump"
    WATER_HEATER = "water_heater"
    TOWEL_RACK = "towel_rack"
    AC = "ac"
    AC_CONTROLLER = "ac_controller"
    HUB = "hub"


def get_model_infos(
    modelId: int, zoneName: str | None = None, productId: int | None = None
):
    """Return infos from model ID.

    Some modelIds are reused by Atlantic across different product families
    (e.g. modelId 557 is used both for a Takao air conditioner and for the
    heating circuit of an Áurea Duo heat pump). When that happens the
    productId is used to disambiguate them.
    """
    modelInfos = {"modelId": modelId, "HVACModesCapabilityId": {7, 8}}

    if modelId == 56:
        modelInfos["name"] = "Naema 2 Micro 25"
        modelInfos["type"] = CozytouchDeviceType.GAZ_BOILER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 61:
        modelInfos["name"] = "Naia 2 Micro 25"
        modelInfos["type"] = CozytouchDeviceType.GAZ_BOILER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 65:
        modelInfos["name"] = "Naema 2 Duo 25"
        modelInfos["type"] = CozytouchDeviceType.GAZ_BOILER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 76:
        modelInfos["name"] = "Alfea Extensa Duo AI UE"
        modelInfos["type"] = CozytouchDeviceType.HEAT_PUMP
        modelInfos["currentTemperatureAvailableZ1"] = False
        modelInfos["currentTemperatureAvailableZ2"] = True
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
        }

        modelInfos["exhaustTemperatureAvailable"] = False

    elif modelId == 211:
        modelInfos["name"] = "Alfea Extensa Duo A.I. 3 R32"
        modelInfos["type"] = CozytouchDeviceType.HEAT_PUMP
        modelInfos["currentTemperatureAvailableZ1"] = True
        modelInfos["currentTemperatureAvailableZ2"] = True

        modelInfos["HVACModesCapabilityId"] = {1, 2}

        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            1: HVACMode.HEAT,
            2: HVACMode.AUTO,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
        }

        modelInfos["exhaustTemperatureAvailable"] = False

    elif modelId == 235:
        modelInfos["name"] = "Thermostat Navilink Connect"
        modelInfos["type"] = CozytouchDeviceType.THERMOSTAT
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 236:
        modelInfos["name"] = "Sauter Phazy"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }
        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }

    elif modelId == 389:
        modelInfos["name"] = "AQUEO ACI HYB VS 300L 3000M"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }
        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }

    elif modelId == 390:
        modelInfos["name"] = "AQUEO ACI HYB VM 150L 2200M"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }
        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }

    elif modelId == 418:
        modelInfos["name"] = "Atlantic Loria Duo 6006"
        modelInfos["type"] = CozytouchDeviceType.THERMOSTAT
        modelInfos["exhaustTemperatureAvailable"] = True
        modelInfos["currentTemperatureAvailableZ1"] = True
        modelInfos["currentTemperatureAvailableZ2"] = False
        modelInfos["overrideModeAvailable"] = True

        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 556:
        modelInfos["name"] = "Naviclim Hub"
        modelInfos["type"] = CozytouchDeviceType.HUB
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
        }

    elif modelId == 1457:
        modelInfos["name"] = "HUB Cozytouch"
        modelInfos["type"] = CozytouchDeviceType.HUB
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
        }
        
    elif modelId == 557 and productId == 26:
        # Áurea Duo heating circuit (room controller / thermostat).
        # This shares modelId 557 with the Takao air conditioner, so it is
        # disambiguated using productId 26.
        name = "Áurea Duo - "
        if zoneName is not None:
            modelInfos["name"] = name + zoneName
        else:
            modelInfos["name"] = name + "Circuito"

        modelInfos["type"] = CozytouchDeviceType.HEAT_PUMP
        modelInfos["currentTemperatureAvailableZ1"] = True
        modelInfos["currentTemperatureAvailableZ2"] = False
        modelInfos["exhaustTemperatureAvailable"] = False

        # The operating mode is carried by capability 7 for this circuit.
        modelInfos["HVACModesCapabilityId"] = {7}
        # NOTE: the exact enumeration of capability 7 for this device is not
        # fully documented. The values below follow the same space used by the
        # Atlantic air conditioners (which also use capability 7). If a mode is
        # displayed incorrectly, adjust this mapping.
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            1: HVACMode.AUTO,
            3: HVACMode.COOL,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
        }

    elif (modelId >= 557 and modelId <= 561) or modelId == 1734:
        name = "Air Conditioner "
        if zoneName is not None:
            modelInfos["name"] = name + "(" + zoneName + ")"
        elif modelId <= 561:
            modelInfos["name"] = name + "(#" + str(modelId - 556) + ")"
        else:
            modelInfos["name"] = name + "(#" + str(modelId - 1733) + ")"

        modelInfos["type"] = CozytouchDeviceType.AC
        modelInfos["currentTemperatureAvailable"] = False
        modelInfos["quietModeAvailable"] = True

        modelInfos["fanModes"] = {
            1: FAN_LOW,
            2: FAN_MEDIUM,
            3: FAN_HIGH,
            5: FAN_AUTO,
        }

        modelInfos["swingModes"] = {
            1: SWING_MODE_UP,
            2: SWING_MODE_MIDDLE_UP,
            3: SWING_MODE_MIDDLE_DOWN,
            4: SWING_MODE_DOWN,
        }

        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            1: HVACMode.AUTO,
            3: HVACMode.COOL,
            4: HVACMode.HEAT,
            7: HVACMode.FAN_ONLY,
            8: HVACMode.DRY,
        }

    elif modelId >= 562 and modelId <= 570:
        name = "Air Conditioner User Interface "
        if zoneName is not None:
            modelInfos["name"] = name + "(" + zoneName + ")"
        else:
            modelInfos["name"] = name + "(#" + str(modelId - 561) + ")"

        modelInfos["type"] = CozytouchDeviceType.AC_CONTROLLER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
        }

    elif modelId == 1353:
        modelInfos["name"] = "Calypso Split Interface"
        modelInfos["type"] = CozytouchDeviceType.HUB
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
        }

    elif modelId == 1376 and productId == 47:
        # Áurea Duo domestic hot water tank (shares modelId 1376 with the
        # Calypso Split, disambiguated using productId 47).
        modelInfos["name"] = "Áurea Duo - ACS"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        # According to the Áurea Duo manual the DHW only has two modes:
        # Confort and Eco. The observed value for capability 87 is 2.
        # NOTE: the exact value <-> mode mapping is a best guess (2 = Comfort).
        # Switch the mode from the Cozytouch app and check capability 87 to
        # confirm/adjust if needed.
        modelInfos["HeatingModes"] = {
            2: HEATING_MODE_COMFORT,
            3: HEATING_MODE_ECO,
        }

    elif modelId in (1369, 1376):
        modelInfos["name"] = "Calypso Split"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }

    elif modelId in (1371, 1372):
        modelInfos["name"] = "Aeromax SPLIT 3"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }

    elif modelId == 1381:
        modelInfos["name"] = "KELUD 1750W BLC"
        modelInfos["type"] = CozytouchDeviceType.TOWEL_RACK
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 1382:
        modelInfos["name"] = "KELUD 1750W Anthracite Standard"
        modelInfos["type"] = CozytouchDeviceType.TOWEL_RACK
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 1388 and productId == 55:
        # Áurea Duo temperature probe (shares modelId 1388 with the Doris
        # towel rack, disambiguated using productId 55).
        modelInfos["name"] = "Áurea Duo - Sonda de temperatura"
        modelInfos["type"] = CozytouchDeviceType.THERMOSTAT
        modelInfos["HVACModesCapabilityId"] = set()
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 1388:
        modelInfos["name"] = "Doris étroit 1500W BLC"
        modelInfos["type"] = CozytouchDeviceType.TOWEL_RACK
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 1444:
        modelInfos["name"] = "Naema 3 Micro 25"
        modelInfos["type"] = CozytouchDeviceType.GAZ_BOILER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 1543:
        modelInfos["name"] = "Asama Connecté II Ventilo 1750W Blanc"
        modelInfos["type"] = CozytouchDeviceType.TOWEL_RACK
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }
    elif modelId == 1546:  # Asama Connecté II Ventilo 1500W
        modelInfos["name"] = "Asama Connecté II Ventilo 1500W ANTH"
        modelInfos["type"] = CozytouchDeviceType.TOWEL_RACK
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 1547:  # Asama Connecté II Ventilo 1750W
        modelInfos["name"] = "Asama Connecté II Ventilo 1750W ANTH"
        modelInfos["type"] = CozytouchDeviceType.TOWEL_RACK
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 1551:
        modelInfos["name"] = "Asama Connecté II Ventilo 1750W Noir"
        modelInfos["type"] = CozytouchDeviceType.TOWEL_RACK
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 1622:
        modelInfos["name"] = "Thermor Riva 5"
        modelInfos["type"] = CozytouchDeviceType.TOWEL_RACK
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }
       
    elif modelId == 1641:
        modelInfos["name"] = "Atlantic Explorer V5 (200L)"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }
       
    elif modelId == 1642:
        modelInfos["name"] = "Atlantic Explorer V5 (270L)"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }

    elif modelId == 1644:
        modelInfos["name"] = "Atlantic Explorer V5 (240L)"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }

    elif modelId == 1645:
        modelInfos["name"] = "Atlantic Explorer V5 (270L with coil)"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }
   
    elif modelId == 1656:
        modelInfos["name"] = "Aeromax 6"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }

    elif modelId == 1657:
        modelInfos["name"] = "Calypso 200L"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }

    elif modelId == 1966:
        modelInfos["name"] = "Thermor Malicio 3 120L"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
            4: HEATING_MODE_PROG,
        }
       
    elif modelId == 1957:
        modelInfos["name"] = "LINEO CONNECTE MP 100L 2250W"
        modelInfos["type"] = CozytouchDeviceType.WATER_HEATER
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

        modelInfos["HeatingModes"] = {
            0: HEATING_MODE_MANUAL,
            3: HEATING_MODE_ECO_PLUS,
        }

    elif modelId == 1720:
        # Áurea Duo main unit (aerothermal heat pump + DHW).
        # The heating/DHW controls live on the child devices (circuit, DHW,
        # generator); this main device mainly exposes energy consumption,
        # outside temperature, away mode and diagnostic sensors. Capability 8
        # of this device is not an HVAC mode, so climate creation is disabled
        # by leaving HVACModesCapabilityId empty.
        modelInfos["name"] = "Atlantic Áurea Duo"
        modelInfos["type"] = CozytouchDeviceType.HEAT_PUMP
        modelInfos["HVACModesCapabilityId"] = set()
        modelInfos["exhaustTemperatureAvailable"] = False
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    elif modelId == 1391:
        # Áurea Duo outdoor/generator unit (compressor + hydraulic module).
        # Exposes water pressure, water temperatures, exhaust temperature and
        # pump statistics. No climate entity.
        modelInfos["name"] = "Áurea Duo - Grupo exterior"
        modelInfos["type"] = CozytouchDeviceType.HEAT_PUMP
        modelInfos["HVACModesCapabilityId"] = set()
        modelInfos["exhaustTemperatureAvailable"] = True
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    else:
        modelInfos["name"] = "Unknown product (" + str(modelId) + ")"
        modelInfos["type"] = CozytouchDeviceType.UNKNOWN
        modelInfos["HVACModes"] = {
            0: HVACMode.OFF,
            4: HVACMode.HEAT,
        }

    return modelInfos
