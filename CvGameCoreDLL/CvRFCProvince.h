#pragma once
/*
Author: bluepotato
*/

class CvRFCProvince {
	public:
		CvRFCProvince();
		~CvRFCProvince();
		void init(ProvinceTypes provinceType);
		void reset(ProvinceTypes provinceType);
		void uninit();

		void setType(CvString type);
		void setProvinceType(ProvinceTypes provinceType);
		void addMercenary(CvRFCMercenary mercenary);
		void checkMercenaries();
		void hireMercenary(PlayerTypes playerType, int mercenaryID);

		const char* getType() const;
		ProvinceTypes getProvinceType() const;
		const wchar* getName() const;
		int getNumScheduledUnits() const;
		CvRFCUnit* addScheduledUnit();
		CvRFCUnit* getScheduledUnit(int i) const;
		std::vector<CvRFCUnit*>& getScheduledUnits();
		int getNumMercenaries() const;
		CvRFCMercenary& getMercenary(int i);
		std::vector<CvRFCMercenary>& getMercenaries();
		std::vector<CvUnit*> getUnits();
		int getNumCities(PlayerTypes playerType) const;
		CvCity* getFirstCity(PlayerTypes);

		void write(FDataStreamBase* stream);
		void read(FDataStreamBase* stream);

	protected:
		CvString _type;
		CvWString _name;
		ProvinceTypes _provinceType;
		std::vector<CvRFCUnit*> _scheduledUnits; //barbs
		std::vector<CvRFCMercenary> _mercenaries;
};
