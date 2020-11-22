/*
Author: bluepotato
*/
#include "CvGameCoreDLL.h"
#include "CyRiseFall.h"
#include "CyRFCPlayer.h"
#include "CyRFCProvince.h"
#include "CyRFCCity.h"
#include "CyRFCUnit.h"
#include "CyRFCMercenary.h"

void CyRiseFallInterface()
{
	python::class_<CyRiseFall>("CyRiseFall")
		.def("getRFCPlayer", &CyRiseFall::getRFCPlayer, python::return_value_policy<python::reference_existing_object>(), "(int civType)")
		.def("getNumProvinces", &CyRiseFall::getNumProvinces, "int ()")
		.def("getRFCProvince", &CyRiseFall::getRFCProvinceByName, python::return_value_policy<python::reference_existing_object>(), "(str provinceName)")
		.def("getRFCProvince", &CyRiseFall::getRFCProvince, python::return_value_policy<python::reference_existing_object>(), "(int province)")
		.def("addProvince", &CyRiseFall::addProvince, python::return_value_policy<python::reference_existing_object>(), "(str name, int bottom, int left, int top, int right)")
		.def("setMapFile", &CyRiseFall::setMapFile, "void (str name)")
		.def("getMapFile", &CyRiseFall::getMapFile, "str ()")
		;

	python::class_<CyRFCCity>("CyRFCCity")
		.def("setYear", &CyRFCCity::setYear, "void (int year)")
		.def("setX", &CyRFCCity::setX, "void (int x)")
		.def("setY", &CyRFCCity::setY, "void (int y)")
		.def("setPopulation", &CyRFCCity::setPopulation, "void (int population)")
		.def("setNumBuilding", &CyRFCCity::setNumBuilding, "void (int building, int num)")
		.def("setReligion", &CyRFCCity::setReligion, "void (int religion, bool value)")
		.def("setHolyCityReligion", &CyRFCCity::setHolyCityReligion, "void (int religion, bool value)")
		.def("setCulture", &CyRFCCity::setCulture, "void (int civType, bool value)")
		.def("getYear", &CyRFCCity::getYear, "int ()")
		.def("getX", &CyRFCCity::getX, "int ()")
		.def("getY", &CyRFCCity::getY, "int ()")
		.def("getPopulation", &CyRFCCity::getPopulation, "int ()")
		.def("getNumBuilding", &CyRFCCity::getNumBuilding, "int (int building)")
		.def("getReligion", &CyRFCCity::getReligion, "bool (int religion)")
		.def("getHolyCityReligion", &CyRFCCity::getHolyCityReligion, "bool (int religion)")
		.def("getCulture", &CyRFCCity::getCulture, "int (int civType)")
		;

	python::class_<CyRFCUnit>("CyRFCUnit")
		.def("setYear", &CyRFCUnit::setYear, "void (int year)")
		.def("setX", &CyRFCUnit::setX, "void (int x)")
		.def("setY", &CyRFCUnit::setY, "void (int y)")
		.def("setUnitType", &CyRFCUnit::setUnitType, "void (int unitType)")
		.def("setUnitAIType", &CyRFCUnit::setUnitAIType, "void (int unitAIType)")
		.def("setFacingDirection", &CyRFCUnit::setFacingDirection, "void (int facingDirection)")
		.def("setAmount", &CyRFCUnit::setAmount, "void (int amount)")
		.def("setEndYear", &CyRFCUnit::setEndYear, "void (int endYear)")
		.def("setSpawnFrequency", &CyRFCUnit::setSpawnFrequency, "void (int spawnFrequency)")
		.def("setAIOnly", &CyRFCUnit::setAIOnly, "void (bool aiOnly)")
		.def("setDeclareWar", &CyRFCUnit::setDeclareWar, "void (bool declareWar)")
		.def("getYear", &CyRFCUnit::getYear, "int ()")
		.def("getX", &CyRFCUnit::getX, "int ()")
		.def("getY", &CyRFCUnit::getY, "int ()")
		.def("getUnitType", &CyRFCUnit::getUnitType, "int ()")
		.def("getUnitAIType", &CyRFCUnit::getUnitAIType, "int ()")
		.def("getFacingDirection", &CyRFCUnit::getFacingDirection, "int ()")
		.def("getAmount", &CyRFCUnit::getAmount, "int ()")
		.def("getEndYear", &CyRFCUnit::getEndYear, "int ()")
		.def("getSpawnFrequency", &CyRFCUnit::getSpawnFrequency, "int ()")
		.def("isAIOnly", &CyRFCUnit::isAIOnly, "bool ()")
		.def("isDeclareWar", &CyRFCUnit::isDeclareWar, "bool ()")
		;

	python::class_<CyRFCMercenary>("CyRFCMercenary")
		.def("getHireCost", &CyRFCMercenary::getHireCost, "int ()")
		.def("getUnitType", &CyRFCMercenary::getUnitType, "int ()")
		.def("getNumPromotions", &CyRFCMercenary::getNumPromotions, "int ()")
		.def("getPromotion", &CyRFCMercenary::getPromotion, "int (int i)")
		.def("getExperience", &CyRFCMercenary::getExperience, "int ()")
		.def("getMaintenanceCost", &CyRFCMercenary::getMaintenanceCost, "int ()")
		;

	python::class_<CyRFCPlayer>("CyRFCPlayer")
		.def("setStartingYear", &CyRFCPlayer::setStartingYear, "void (int newStartingYear)")
		.def("getStartingYear", &CyRFCPlayer::getStartingYear, "int ()")
		.def("setStartingCivic", &CyRFCPlayer::setStartingCivic, "void (int category, int civic)")
		.def("setStartingGold", &CyRFCPlayer::setStartingGold, "void (int gold)")
		.def("addStartingTech", &CyRFCPlayer::addStartingTech, "void (int tech)")
		.def("setStartingPlot", &CyRFCPlayer::setStartingPlot, "void (int x, int y)")
		.def("addCoreProvince", &CyRFCPlayer::addCoreProvince, "void (str coreProvince)")
		.def("getStability", &CyRFCPlayer::getStability, "int (int category)")
		.def("getTotalStability", &CyRFCPlayer::getTotalStability, "int ()")
		.def("setEnabled", &CyRFCPlayer::setEnabled, "void (bool enabled)")
		.def("isEnabled", &CyRFCPlayer::isEnabled, "bool ()")
		.def("getStartingCivic", &CyRFCPlayer::getStartingCivic, "int (int civicOptionType)")
		.def("getStartingGold", &CyRFCPlayer::getStartingGold, "int ()")
		.def("isStartingTech", &CyRFCPlayer::isStartingTech, "bool (int startingTech)")
		.def("getStartingPlotX", &CyRFCPlayer::getStartingPlotX, "int ()")
		.def("getStartingPlotY", &CyRFCPlayer::getStartingPlotY, "int ()")
		.def("getNumScheduledUnits", &CyRFCPlayer::getNumScheduledUnits, "int ()")
		.def("getNumScheduledCities", &CyRFCPlayer::getNumScheduledCities, "int ()")
		.def("addScheduledUnit", &CyRFCPlayer::addScheduledUnit, python::return_value_policy<python::reference_existing_object>(), "()")
		.def("getScheduledUnit", &CyRFCPlayer::getScheduledUnit, python::return_value_policy<python::reference_existing_object>(), "(int i)")
		.def("addScheduledCity", &CyRFCPlayer::addScheduledCity, python::return_value_policy<python::reference_existing_object>(), "()")
		.def("getScheduledCity", &CyRFCPlayer::getScheduledCity, python::return_value_policy<python::reference_existing_object>(), "(int i)")
		.def("getNumCoreProvinces", &CyRFCPlayer::getNumCoreProvinces, "int ()")
		.def("getCoreProvince", &CyRFCPlayer::getCoreProvince, "str (int i)")
		.def("addStartingWar", &CyRFCPlayer::addStartingWar, "void (int i)")
		.def("isStartingWar", &CyRFCPlayer::isStartingWar, "bool (int i)")
		.def("addRelatedLanguage", &CyRFCPlayer::addRelatedLanguage, "void (int i)")
		.def("isRelatedLanguage", &CyRFCPlayer::isRelatedLanguage, "bool (int i)")
		.def("isMinor", &CyRFCPlayer::isMinor, "bool ()")
		.def("isSpawned", &CyRFCPlayer::isSpawned, "bool ()")
		.def("setMinorCiv", &CyRFCPlayer::setMinorCiv, "void (bool minor)")
		.def("isFlipped", &CyRFCPlayer::isFlipped, "bool ()")
		.def("setFlipped", &CyRFCPlayer::setFlipped, "void (bool flipped)")
		.def("setCompactEmpireModifier", &CyRFCPlayer::setCompactEmpireModifier, "void (int modifier)")
		.def("getCompactEmpireModifier", &CyRFCPlayer::getCompactEmpireModifier, "int ()")
		.def("setUnitUpkeepModifier", &CyRFCPlayer::setUnitUpkeepModifier, "void (int modifier)")
		.def("getUnitUpkeepModifier", &CyRFCPlayer::getUnitUpkeepModifier, "int ()")
		.def("setResearchModifier", &CyRFCPlayer::setResearchModifier, "void (int modifier)")
		.def("getResearchModifier", &CyRFCPlayer::getResearchModifier, "int ()")
		.def("setDistanceMaintenanceModifier", &CyRFCPlayer::setDistanceMaintenanceModifier, "void (int modifier)")
		.def("getDistanceMaintenanceModifier", &CyRFCPlayer::getDistanceMaintenanceModifier, "int ()")
		.def("setNumCitiesMaintenanceModifier", &CyRFCPlayer::setNumCitiesMaintenanceModifier, "void (int modifier)")
		.def("getNumCitiesMaintenanceModifier", &CyRFCPlayer::getNumCitiesMaintenanceModifier, "int ()")
		.def("setUnitProductionModifier", &CyRFCPlayer::setUnitProductionModifier, "void (int modifier)")
		.def("getUnitProductionModifier", &CyRFCPlayer::getUnitProductionModifier, "int ()")
		.def("setCivicUpkeepModifier", &CyRFCPlayer::setCivicUpkeepModifier, "void (int modifier)")
		.def("getCivicUpkeepModifier", &CyRFCPlayer::getCivicUpkeepModifier, "int ()")
		.def("setHealthBonusModifier", &CyRFCPlayer::setHealthBonusModifier, "void (int modifier)")
		.def("getHealthBonusModifier", &CyRFCPlayer::getHealthBonusModifier, "int ()")
		.def("setBuildingProductionModifier", &CyRFCPlayer::setBuildingProductionModifier, "void (int modifier)")
		.def("getBuildingProductionModifier", &CyRFCPlayer::getBuildingProductionModifier, "int ()")
		.def("setWonderProductionModifier", &CyRFCPlayer::setWonderProductionModifier, "void (int modifier)")
		.def("getWonderProductionModifier", &CyRFCPlayer::getWonderProductionModifier, "int ()")
		.def("setGreatPeopleModifier", &CyRFCPlayer::setGreatPeopleModifier, "void (int modifier)")
		.def("getGreatPeopleModifier", &CyRFCPlayer::getGreatPeopleModifier, "int ()")
		.def("setInflationModifier", &CyRFCPlayer::setInflationModifier, "void (int modifier)")
		.def("getInflationModifier", &CyRFCPlayer::getInflationModifier, "int ()")
		.def("setGrowthModifier", &CyRFCPlayer::setGrowthModifier, "void (int modifier)")
		.def("getGrowthModifier", &CyRFCPlayer::getGrowthModifier, "int ()")
		.def("setStartingReligion", &CyRFCPlayer::setStartingReligion, "void (int religion)")
		.def("getStartingReligion", &CyRFCPlayer::getStartingReligion, "int ()")
		;

	python::class_<CyRFCProvince>("CyRFCProvince")
		.def("getName", &CyRFCProvince::getName, "str ()")
		.def("getBottom", &CyRFCProvince::getBottom, "int ()")
		.def("getLeft", &CyRFCProvince::getLeft, "int ()")
		.def("getTop", &CyRFCProvince::getTop, "int ()")
		.def("getRight", &CyRFCProvince::getRight, "int ()")
		.def("getNumScheduledUnits", &CyRFCProvince::getNumScheduledUnits, "int ()")
		.def("addScheduledUnit", &CyRFCProvince::addScheduledUnit, python::return_value_policy<python::reference_existing_object>(), "()")
		.def("getScheduledUnit", &CyRFCProvince::getScheduledUnit, python::return_value_policy<python::reference_existing_object>(), "(int i)")
		.def("getNumMercenaries", &CyRFCProvince::getNumMercenaries, "int ()")
		.def("getMercenary", &CyRFCProvince::getMercenary, python::return_value_policy<python::reference_existing_object>(), "(int i)")
		.def("getNumCities", &CyRFCProvince::getNumCities, "int (int playerType)")
		.def("hireMercenary", &CyRFCProvince::hireMercenary, "void (int playerType, int mercenaryID)")
		;
}
