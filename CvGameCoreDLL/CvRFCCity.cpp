/*
Author: bluepotato
*/
#include "CvGameCoreDLL.h"
#include "CvRFCCity.h"

CvRFCCity::CvRFCCity() {
	_year = 0;
	_y = 0;
	_x = 0;
	_population = 0;
	_buildings = new int[GC.getNumBuildingInfos()];
	for(int i = 0; i < GC.getNumBuildingInfos(); ++i) {
		_buildings[i] = 0;
	}
	_religions = new bool[GC.getNumReligionInfos()];
	for(int i = 0; i < GC.getNumReligionInfos(); ++i) {
		_religions[i] = 0;
	}
	_holyCityReligions = new bool[GC.getNumReligionInfos()];
	for(int i = 0; i < GC.getNumReligionInfos(); ++i) {
		_holyCityReligions[i] = 0;
	}
}

CvRFCCity::~CvRFCCity() {
	SAFE_DELETE_ARRAY(_buildings);
	SAFE_DELETE_ARRAY(_religions);
	SAFE_DELETE_ARRAY(_holyCityReligions);
}

void CvRFCCity::setYear(int year) {
	_year = year;
}

void CvRFCCity::setX(int x) {
	_x = x;
}

void CvRFCCity::setY(int y) {
	_y = y;
}

void CvRFCCity::setPopulation(int population) {
	_population = population;
}

void CvRFCCity::setNumBuilding(BuildingTypes building, int value) {
	FAssert(building >= 0);
	FAssert(building < GC.getNumBuildingInfos());
	_buildings[building] = value;
}

void CvRFCCity::setReligion(ReligionTypes religion, bool value) {
	FAssert(religion >= 0);
	FAssert(religion < GC.getNumReligionInfos());
	_religions[religion] = value;
}

void CvRFCCity::setHolyCityReligion(ReligionTypes religion, bool value) {
	FAssert(religion >= 0);
	FAssert(religion < GC.getNumReligionInfos());
	_holyCityReligions[religion] = value;
}


int CvRFCCity::getYear() const {
	return _year;
}

int CvRFCCity::getX() const {
	return _x;
}

int CvRFCCity::getY() const {
	return _y;
}

int CvRFCCity::getPopulation() const {
	return _population;
}

int CvRFCCity::getNumBuilding(BuildingTypes building) const {
	FAssert(building >= 0);
	FAssert(building < GC.getNumBuildingInfos());
	return _buildings[building];
}

bool CvRFCCity::getReligion(ReligionTypes religion) const {
	FAssert(religion >= 0);
	FAssert(religion < GC.getNumReligionInfos());
	return _religions[religion];
}

bool CvRFCCity::getHolyCityReligion(ReligionTypes religion) const {
	FAssert(religion >= 0);
	FAssert(religion < GC.getNumReligionInfos());
	return _holyCityReligions[religion];
}


void CvRFCCity::write(FDataStreamBase* stream) {
	stream->Write(_year);
	stream->Write(_x);
	stream->Write(_y);
	stream->Write(_population);
	stream->Write(GC.getNumBuildingInfos(), _buildings);
}

void CvRFCCity::read(FDataStreamBase* stream) {
	stream->Read(&_year);
	stream->Read(&_x);
	stream->Read(&_y);
	stream->Read(&_population);
	stream->Read(GC.getNumBuildingInfos(), _buildings);
}
