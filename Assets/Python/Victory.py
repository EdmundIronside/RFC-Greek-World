# Rhye's and Fall of the Greek World - Historical Victory Goals

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Popup
import cPickle as pickle

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer

### Constants ###

tLevantTL = (39, 18)
tLevantBR = (43, 26)
tIranTL = (48, 19)
tIranBR = (54, 28)
tNubiaTL = (24, 0)
tNubiaBR = (35, 4)
tMesopotamiaTL = (44, 18)
tMesopotamiaBR = (49, 27)
tEgyptTL = (26, 5)
tEgyptBR = (35, 17)
tNAfricaTL = (0, 17)
tNAfricaBR = (27, 24)
tCyprusTL = (37, 21)
tCyprusBR = (39, 23)
tIberiaTL = (2, 26)
tIberiaBR = (12, 38)
tAnatoliaTL = (35, 25)
tAnatoliaBR = (40, 32)

#following ids refer to civ types, not slots!
iEgypt = 0
iSumeria = 1
iIndusValley = 2
iElam = 3
iMinoa = 4
iPhoenicia = 5
iBabylonia = 6
iHittites = 7
iMycenae = 8
iAssyria = 9
iIsrael = 10
iAthens = 11
iSparta = 12
iScythia = 13
iCarthage = 14
iCeltia = 15
iEtruria = 16
iNubia = 17
iPersia = 18
iRome = 19
iMacedonia = 20
iIndia = 21
iBactria = 22
iNumidia = 23
iGermania = 24
iSassanid = 25
iByzantium = 26
iHuns = 27
iIndependent = 28
iIndependent2 = 29
iBarbarian = 30

iNumPlayers = gc.getMAX_CIV_PLAYERS() - 2 #-2: independent slots

def tech(techName):
	return CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), "TECH_" + techName.upper())

def building(buildingName):
	return CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), "BUILDING_" + buildingName.upper())

def unit(unitName):
	return CvUtil.findInfoTypeNum(gc.getUnitInfo, gc.getNumUnitInfos(), "UNIT_" + unitName.upper())

def civ2player(civType):
	for i in range(gc.getMAX_CIV_PLAYERS()):
		if gc.getPlayer(i).getCivilizationType() == civType:
			return i
	return None

def player2civ(playerType):
	return gc.getPlayer(playerType).getCivilizationType()

class Victory:
	def initGlobals(self):
		global i4000BC
		global i3000BC
		global i2200BC
		global i2180BC
		global i2000BC
		global i1900BC
		global i1800BC
		global i1690BC
		global i1500BC
		global i1400BC
		global i1300BC
		global i1200BC
		global i1250BC
		global i1100BC
		global i1070BC
		global i1000BC
		global i900BC
		global i600BC
		global i500BC
		global i250BC
		global i100BC
		
		i4000BC = getTurnForYear(-4000)
		i3000BC = getTurnForYear(-3000)
		i2200BC = getTurnForYear(-2200)
		i2180BC = getTurnForYear(-2180)
		i2000BC = getTurnForYear(-2000)
		i1900BC = getTurnForYear(-1900)
		i1800BC = getTurnForYear(-1800)
		i1690BC = getTurnForYear(-1690)
		i1500BC = getTurnForYear(-1500)
		i1400BC = getTurnForYear(-1400)
		i1300BC = getTurnForYear(-1300)
		i1200BC = getTurnForYear(-1200)
		i1250BC = getTurnForYear(-1250)
		i1100BC = getTurnForYear(-1100)
		i1070BC = getTurnForYear(-1070)
		i1000BC = getTurnForYear(-1000)
		i900BC = getTurnForYear(-900)
		i600BC = getTurnForYear(-600)
		i500BC = getTurnForYear(-500)
		i250BC = getTurnForYear(-250)
		i100BC = getTurnForYear(-100)
		
		
		global provPalestine
		global provPhoenicia
		global provUpperEgypt
		global provLowerEgypt
		global provNubia
		global provSumer
		global provAkkad
		global provSubartu
		global provKhuzestan
		
		riseFall = CyRiseFall()
		provPalestine = riseFall.getRFCProvince("Palestine")
		provPhoenicia = riseFall.getRFCProvince("Phoenicia")
		provUpperEgypt = riseFall.getRFCProvince("Upper Egypt")
		provLowerEgypt = riseFall.getRFCProvince("Lower Egypt")
		provNubia = riseFall.getRFCProvince("Nubia")
		provSumer = riseFall.getRFCProvince("Sumer")
		provAkkad = riseFall.getRFCProvince("Akkad")
		provSubartu = riseFall.getRFCProvince("Subartu")
		provKhuzestan = riseFall.getRFCProvince("Khuzestan")

	def getGoal(self, i, j):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lGoals'][i][j]

	def setGoal(self, i, j, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lGoals'][i][j] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))
		if iNewValue == 0:
			return
		if self.getGoal(i, 0) == 1 and self.getGoal(i, 1) == 1 and self.getGoal(i, 2) == 1:
			if gc.getGame().getWinner() == -1:
				for j in range(gc.getMAX_CIV_PLAYERS()):
					if gc.getPlayer(j).getCivilizationType() == i:
						gc.getGame().setWinner(j, 7)

	def getEnslavedUnits(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['iEnslavedUnits']

	def getBabyloniaKilledCivs(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['babyloniaKilledCivs']

	def setBabyloniaKilledCivs(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['babyloniaKilledCivs'] = i
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getMycenaeTombsBuilt(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['mycenaeTombsBuilt']

	def setMycenaeTombsBuilt(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['mycenaeTombsBuilt'] = i
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getHittiteKilledUnits(self):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['hittiteKilledUnits']

	def setHittiteKilledUnits(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['hittiteKilledUnits'] = i
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def get2OutOf3(self, iCiv):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['l2OutOf3'][iCiv]

	def set2OutOf3(self, iCiv, bNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['l2OutOf3'][iCiv] = bNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def getSumerianTechs(self, i):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		return scriptDict['lSumerianTechs'][i]

	def setSumerianTechs(self, i, iNewValue):
		scriptDict = pickle.loads(gc.getGame().getScriptData())
		scriptDict['lSumerianTechs'][i] = iNewValue
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def onLoadGame(self):
		self.initGlobals()

	def onGameStart(self):
		self.initGlobals()

		#init script data
		scriptDict = {
					'lGoals': [[-1 for i in range(iNumPlayers)] for j in range(iNumPlayers)], #bluepotato: [[-1,-1,-1]]*con.iNumPlayers would copy the same array over and over. see https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
					'iEnslavedUnits': 0,
					'lSumerianTechs': [-1, -1, -1],
					'babyloniaKilledCivs': 0,
					'hittiteKilledUnits': 0,
					'mycenaeTombsBuilt': 0,
					'l2OutOf3': [False] * iNumPlayers,
		}
		gc.getGame().setScriptData(pickle.dumps(scriptDict))

	def ownedCityPlots(self, tCoords, result, argsList):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it contains a city belonging to the civ"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if (pCurrent.getOwner() == argsList):
			if (pCurrent.isCity()):
				# this is a good plot, so paint it and continue search
				return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)

	def ownedCityPlotsAdjacentArea(self, tCoords, result, argsList):
		"""Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
		Plot is valid if it contains a city belonging to the civ"""
		bPaint = True
		bContinue = True
		pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
		if (pCurrent.getOwner() == argsList[0] and pCurrent.isAdjacentToArea(gc.getMap().plot(argsList[1][0],argsList[1][1]).area())):
			if (pCurrent.isCity()):
				# this is a good plot, so paint it and continue search
				return (None, bPaint, bContinue)
		# not a good plot, so don't paint it but continue search
		return (None, not bPaint, bContinue)

	def squareSearch(self, tTopLeft, tBottomRight, function, argsList): #by LOQ
		"""Searches all tile in the square from tTopLeft to tBottomRight and calls function for
		every tile, passing argsList. The function called must return a tuple: (1) a result, (2) if
		a plot should be painted and (3) if the search should continue."""
		tPaintedList = []
		result = None
		for x in range(tTopLeft[0], tBottomRight[0]+1):
			for y in range(tTopLeft[1], tBottomRight[1]+1):
				result, bPaintPlot, bContinueSearch = function((x, y), result, argsList)
				if bPaintPlot:			# paint plot
					tPaintedList.append((x, y))
				if not bContinueSearch:		# goal reached, so stop
					return result, tPaintedList
		return result, tPaintedList

	def checkOwnedArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
		dummy1, plotList = self.squareSearch(tTopLeft, tBottomRight, self.ownedCityPlots, iActiveCiv)
		if (len(plotList) >= iThreshold):
			return True
		else:
			return False


	def checkOwnedAreaAdjacentArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold, tPlotArea):
		dummy1, plotList = self.squareSearch(tTopLeft, tBottomRight, self.ownedCityPlotsAdjacentArea, [iActiveCiv, tPlotArea])
		if (len(plotList) >= iThreshold):
			print(len(plotList))
			return True
		else:
			print(len(plotList))
			return False


	def checkFoundedArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
		dummy1, plotList = self.squareSearch(tTopLeft, tBottomRight, self.foundedCityPlots, iActiveCiv)
		if (len(plotList) >= iThreshold):
			return True
		else:
			return False

	def checkNotOwnedArea(self, iActiveCiv, tTopLeft, tBottomRight):
		dummy1, plotList = self.squareSearch(tTopLeft, tBottomRight, self.ownedCityPlots, iActiveCiv)
		if (len(plotList)):
			return False
		else:
			return True

	def checkNotOwnedArea_Skip(self, iActiveCiv, tTopLeft, tBottomRight, tSkipTopLeft, tSkipBottomRight):
		dummy1, plotList = self.squareSearch(tTopLeft, tBottomRight, self.ownedCityPlots, iActiveCiv)
		if (not len(plotList)):
			return True
		else:
			for loopPlot in plotList:
				if not (loopPlot[0] >= tSkipTopLeft[0] and loopPlot[0] <= tSkipBottomRight[0] and \
				    loopPlot[1] >= tSkipTopLeft[1] and loopPlot[1] <= tSkipBottomRight[1]):
					return False
		return True


	def checkOwnedCoastalArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
		dummy1, plotList = self.squareSearch(tTopLeft, tBottomRight, self.ownedCityPlots, iActiveCiv)
		iCounter = 0
		for i in range(len(plotList)):
			x = plotList[i][0]
			y = plotList[i][1]
			plot = gc.getMap().plot(x, y)
			if (plot.isCity()):
			       if (plot.getPlotCity().isCoastalOld()):
				       iCounter += 1
		if (iCounter >= iThreshold):
			return True
		else:
			return False

	def checkOwnedCoastalAreaExceptions(self, iActiveCiv, tTopLeft, tBottomRight, tExceptionList, iThreshold):
		dummy1, plotList = self.squareSearch(tTopLeft, tBottomRight, self.ownedCityPlots, iActiveCiv)
		iCounter = 0
		for i in range(len(plotList)):
			x = plotList[i][0]
			y = plotList[i][1]
			plot = gc.getMap().plot(x, y)
			if (plot.isCity()):
			       if (plot.getPlotCity().isCoastalOld()):
				       bOK = True
				       for j in tExceptionList:
					       if (x == j[0] and y == j[1]):
						       bOK = False
						       break
				       if (bOK):
					       iCounter += 1
		if (iCounter >= iThreshold):
			return True
		else:
			return False

	def checkFoundedCoastalArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
		dummy1, plotList = self.squareSearch(tTopLeft, tBottomRight, self.foundedCityPlots, iActiveCiv)
		iCounter = 0
		for i in range(len(plotList)):
			x = plotList[i][0]
			y = plotList[i][1]
			plot = gc.getMap().plot(x, y)
			if (plot.isCity()):
			       if (plot.getPlotCity().isCoastalOld()):
				       iCounter += 1
		if (iCounter >= iThreshold):
			return True
		else:
			return False

	def checkPlayerTurn(self, iGameTurn, iPlayer):
		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return
		
		pPlayer = gc.getPlayer(iPlayer)
		
		if not pPlayer.isAlive():
			return

		civType = pPlayer.getCivilizationType()

		if (civType == iEgypt):
			if (iGameTurn <= i1070BC):
				if (iGameTurn == i2180BC):
					if (pPlayer.countTotalCulture() >= 1000):
						self.setGoal(iEgypt, 0, 1)
					else:
						self.setGoal(iEgypt, 0, 0)
				elif (iGameTurn == i1690BC):
					if (gc.getGame().getTeamRank(iEgypt) == 0):
						self.setGoal(iEgypt, 1, 1)
					else:
						self.setGoal(iEgypt, 1, 0)
				elif (iGameTurn > i1690BC):
					bPhoenicia = provPhoenicia.getNumCities(iPlayer) >= 2
					bPalestine = provPalestine.getNumCities(iPlayer) >= 2
					bEgypt = provUpperEgypt.getNumCities(iPlayer) + provLowerEgypt.getNumCities(iPlayer) >= 2
					bNubia = provNubia.getNumCities(iPlayer) >= 2
					if (bPhoenicia and bPalestine and bEgypt and bNubia):
						self.setGoal(iEgypt, 2, 1)
					elif iGameTurn > i1070BC:
						self.setGoal(iEgypt, 2, 0)
		elif (civType == iSumeria):
			if (iGameTurn == i2200BC):
				bSumer = provSumer.getNumCities(iPlayer) >= 1
				bAkkad = provAkkad.getNumCities(iPlayer) >= 1
				bSubartu = provSubartu.getNumCities(iPlayer) >= 1
				bKhuzestan = provKhuzestan.getNumCities(iPlayer) >= 1
				if (bSumer and bAkkad and bSubartu and bKhuzestan):
					self.setGoal(iSumeria, 2, 1)
				else:
					self.setGoal(iSumeria, 2, 0)

			if (iGameTurn == i2000BC):
				bestCity = self.calculateTopCityCulture(46, 19)
				if (bestCity != -1):
					if (bestCity.getOwner() == iSumeria and bestCity.getX() == 46 and bestCity.getY() == 19):
						self.setGoal(iSumeria, 1, 1)
					else:
						self.setGoal(iSumeria, 1, 0)
				else:
					self.setGoal(iSumeria, 1, 0)
		elif (civType == iIndusValley):
			if (iGameTurn == i1250BC):
				iIndusValleyResource = 0
				bResources = True
				for iBonus in range(gc.getNumBonusInfos()):
					if (pPlayer.getNumAvailableBonuses(iBonus) > 0):
						iIndusValleyResource += 1
				for iCiv in range(iNumPlayers):
					if (iCiv != iIndusValley):
						pCiv = gc.getPlayer(iCiv)
						iElseResource = 0
						if (pCiv.isAlive()):
							for iBonusA in range(gc.getNumBonusInfos()):
								if (pCiv.getNumAvailableBonuses(iBonusA) > 0):
									iElseResource += 1
							if (iElseResource > iIndusValleyResource):
								bResources = False
								break
				if (bResources):
					self.setGoal(iIndusValley, 1, 1)
				else:
					self.setGoal(iIndusValley, 1, 0)

			if (iGameTurn == i1500BC):
				iPop = pPlayer.getRealPopulation()
				bFirst = True
				for iCiv in range(iNumPlayers):
					if (iPop < gc.getPlayer(iCiv).getRealPopulation()):
						bFirst = False
						break
				if (bFirst):
					self.setGoal(iIndusValley, 0, 1)
				else:
					self.setGoal(iIndusValley, 0, 0)

			if (iGameTurn == i1000BC):
				if (self.getGoal(iIndusValley, 2) == -1): #see onCityAcquired()
					self.setGoal(iIndusValley, 2, 1)

		elif civType == iElam and iGameTurn <= i1000BC:
			if iGameTurn < i1900BC:
				cIndusValley = civ2player(iIndusValley)
				if civ2player(cIndusValley) != None and pPlayer.canContact(cIndusValley) and pPlayer.canTradeNetworkWith(cIndusValley):
					self.setGoal(iElam, 1, 1)
			elif iGameTurn == i1900BC and self.getGoal(iElam, 1) == -1:
				self.setGoal(iElam, 1, 0)
			elif iGameTurn < i1500BC and self.getGoal(iElam, 2) == -1:
				if self.checkOwnedArea(iElam, tIranTL, tIranBR, 5):
					self.setGoal(iElam, 2, 1)
			elif iGameTurn == i1500BC and self.getGoal(iElam, 2) == -1:
				if self.checkOwnedArea(iElam, tIranTL, tIranBR, 5):
					self.setGoal(iElam, 2, 1)
				else:
					self.setGoal(iElam, 2, 0)
		elif (civType == iMinoa):
			if (iGameTurn == i1400BC):
				if (teamMinoa.isHasTech(tech('calendar'))):
					self.setGoal(iMinoa, 0, 1)
				else:
					self.setGoal(iMinoa, 0, 0)

			if (iGameTurn == i1200BC):
				if (gc.getGame().getTeamRank(iMinoa) == 0):
					self.setGoal(iMinoa, 1, 1)
				else:
					self.setGoal(iMinoa, 1, 0)

			if (iGameTurn == i1000BC):
				bestCity = self.calculateTopCityCulture(33, 21)
				if (bestCity != -1):
					if (bestCity.getOwner() == iMinoa and bestCity.getX() == 33 and bestCity.getY() == 21):
						self.setGoal(iMinoa, 2, 1)
					else:
						self.setGoal(iMinoa, 2, 0)
				else:
					self.setGoal(iMinoa, 2, 0)

		elif (civType == iPhoenicia):
			if (iGameTurn == i900BC):
				bLevant = self.checkOwnedArea(iPhoenicia, tLevantTL, tLevantBR, 1)
				bNAfrica = self.checkOwnedArea(iPhoenicia, tNAfricaTL, tNAfricaBR, 1)
				bCyprus = self.checkOwnedArea(iPhoenicia, tCyprusTL, tCyprusBR, 1)
				bIberia = self.checkOwnedArea(iPhoenicia, tIberiaTL, tIberiaBR, 1)
				if (bLevant and bNAfrica and bCyprus and bIberia):
					self.setGoal(iPhoenicia, 0, 1)
				else:
					self.setGoal(iPhoenicia, 0, 0)

			if (iGameTurn == i600BC):
				lRevealedMap = [0] * iNumPlayers
				for iCiv in range(iNumPlayers):
					for x in range(63):
						for y in range(60):
							if (gc.getMap().plot(x, y).isRevealed(iCiv, False)):
							      lRevealedMap[iCiv] += 1
				bBestMap = True
				for iCiv in range(iNumPlayers):
					if (lRevealedMap[iPhoenicia] < lRevealedMap[iCiv]):
						bBestMap = False
						break

				if (bBestMap == True):
					self.setGoal(iPhoenicia, 1, 1)
				else:
					self.setGoal(iPhoenicia, 1, 0)

			if (iGameTurn == i500BC):
				iPhoeniciaResource = 0
				bResources = True
				for iBonus in range(gc.getNumBonusInfos()):
					if (pPlayer.getNumAvailableBonuses(iBonus) > 0):
						iPhoeniciaResource += 1
				for iCiv in range(iNumPlayers):
					if (iCiv != iPhoenicia):
						pCiv = gc.getPlayer(iCiv)
						iElseResource = 0
						if (pCiv.isAlive()):
							for iBonusA in range(gc.getNumBonusInfos()):
								if (pCiv.getNumAvailableBonuses(iBonusA) > 0):
									iElseResource += 1
							if (iElseResource > iPhoeniciaResource):
								bResources = False
								break
				if (bResources):
					self.setGoal(iPhoenicia, 2, 1)
				else:
					self.setGoal(iPhoenicia, 2, 0)

		elif civType == iBabylonia and iGameTurn <= i600BC:
			babylonPlot = gc.getMap().plot(46, 22)
			if iGameTurn < i1000BC:
				if babylonPlot.isCity():
					if babylonPlot.getPlotCity().getNumWorldWonders() >= 6:
						self.setGoal(iBabylonia, 0, 1)
			elif iGameTurn == i1000BC:
				if not babylonPlot.isCity() or babylonPlot.getPlotCity().getNumWorldWonders() < 6:
					self.setGoal(iBabylonia, 0, 0)
				else:
					self.setGoal(iBabylonia, 0, 1)
			if iGameTurn < i600BC:
				if self.getBabyloniaKilledCivs() >= 3:
					self.setGoal(iBabylonia, 2, 1)
			elif iGameTurn == i600BC:
				if self.getBabyloniaKilledCivs() < 3:
					self.setGoal(iBabylonia, 2, 0)
				else:
					self.setGoal(iBabylonia, 2, 1)
		elif civType == iHittites:
			if self.getGoal(iHittites, 0) == -1 and iGameTurn > i1400BC:
				self.setGoal(iHittites, 0, 0)
			if iGameTurn == i1300BC:
				result = True
				for i in range(iNumPlayers):
					if i == iPlayer:
						if not self.checkOwnedArea(i, tLevantTL, tLevantBR, 1):
							result = False
					else:
						if self.checkOwnedArea(i, tLevantTL, tLevantBR, 1):
							result = False
				self.setGoal(iHittites, 1, result)
			elif iGameTurn < i1200BC:
				if self.getHittiteKilledUnits() >= 15:
					self.setGoal(iHittites, 2, 1)
			if self.getGoal(iHittites, 2) == -1 and iGameTurn > i1200BC:
				self.setGoal(iHittites, 2, 0)
		elif civType == iMycenae:
			if self.getGoal(iMycenae, 0) == -1 and iGameTurn > i1300BC:
				self.setGoal(iMycenae, 0, 0)
			if self.getGoal(iMycenae, 1) == -1 and iGameTurn > i1100BC:
				self.setGoal(iMycenae, 1, 0)
			if iGameTurn == i1000BC:
				result = self.checkOwnedArea(iBarbarian, tAnatoliaTL, tAnatoliaBR, 1) or self.checkOwnedArea(iIndependent, tAnatoliaTL, tAnatoliaBR, 1) or self.checkOwnedArea(iIndependent2, tAnatoliaTL, tAnatoliaBR, 1)
				self.setGoal(iMycenae, 2, not result)

	def onCityBuilt(self, city):
		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		iGameTurn = gc.getGame().getGameTurn()

	def onCityAcquired(self, owner, attacker, city, bConquest):
		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		iGameTurn = gc.getGame().getGameTurn()
		cityX = city.getX()
		cityY = city.getY()
		
		ownerType = gc.getPlayer(owner).getCivilizationType()
		attackerType = gc.getPlayer(attacker).getCivilizationType()

		if self.getGoal(iElam, 0) == -1 and cityX == 46 and cityY == 19: #Ur captured by Elam
			if attackerType == iElam:
				self.setGoal(iElam, 0, 1)
			else:
				self.setGoal(iElam, 0, 0)

		if self.getGoal(iHittites, 0) == -1 and cityX == 46 and cityY == 22: #Babylon captured by Hittites
			if attackerType == iHittites:
				self.setGoal(iHittites, 0, 1)

		if (ownerType == iIndusValley):
			if (bConquest):
				if (self.getGoal(iIndusValley, 2) == -1):
					if (iGameTurn <= i1000BC):
						if (attackerType == iBarbarian):
							self.setGoal(iIndusValley, 2, 0)

		if attackerType == iBabylonia:
			if gc.getPlayer(owner).getNumCities() == 0:
				self.setBabyloniaKilledCivs(self.getBabyloniaKilledCivs()+1)

	def onCityRazed(self, city, conqueror, owner):
		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		if self.getGoal(iElam, 0) == -1 and city.getX() == 46 and city.getY() == 19: #Ur captured by Elam
			if gc.getPlayer(conqueror).getCivilizationType() == iElam:
				self.setGoal(iElam, 0, 1)
			else:
				self.setGoal(iElam, 0, 0)

	def onTechAcquired(self, iTech, iPlayer):
		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		iGameTurn = gc.getGame().getGameTurn()
		civType = gc.getPlayer(iPlayer).getCivilizationType()

		if (civType == iSumeria):
			if (self.getGoal(iSumeria, 0) == -1):
				if (iTech == tech('the_wheel')):
					self.setSumerianTechs(0, 1)
					for iCiv in range(iNumPlayers):
						if (iCiv != iSumeria):
							if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
								self.setSumerianTechs(0, 0)
				elif (iTech == tech('masonry')):
					self.setSumerianTechs(1, 1)
					for iCiv in range(iNumPlayers):
						if (iCiv != iSumeria):
							if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
								self.setSumerianTechs(1, 0)
				elif (iTech == tech('cuneiform')):
					self.setSumerianTechs(2, 1)
					for iCiv in range(iNumPlayers):
						if (iCiv != iSumeria):
							if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
								self.setSumerianTechs(2, 0)
				if (self.getSumerianTechs(0) == 1 and self.getSumerianTechs(1) == 1 and self.getSumerianTechs(2) == 1):
					self.setGoal(iSumeria, 0, 1)
				elif (self.getSumerianTechs(0) == 0 or self.getSumerianTechs(1) == 0 or self.getSumerianTechs(2) == 0):
					self.setGoal(iSumeria, 0, 0)
		elif civType == iBabylonia:
			if self.getGoal(iBabylonia, 1) == -1:
				if iTech == tech('code_of_laws'):
					self.setGoal(iBabylonia, 1, 1)
					for iCiv in range(iNumPlayers):
						if iCiv != iBabylonia:
							if gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech):
								self.setGoal(iBabylonia, 1, 0)
								break

	def onBuildingBuilt(self, iPlayer, iBuilding):
		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		iGameTurn = gc.getGame().getGameTurn()
		civType = gc.getPlayer(iPlayer).getCivilizationType()

		if civType == iMycenae:
			if iBuilding == building('mycenae_tholoi'):
				if self.getGoal(iMycenae, 0) == -1:
					self.setMycenaeTombsBuilt(self.getMycenaeTombsBuilt() + 1)
					if self.getMycenaeTombsBuilt() >= 3:
						self.setGoal(iMycenae, 0, 1)
			elif iBuilding == building('lion_gate'):
				if self.getGoal(iMycenae, 1) == -1:
					self.setGoal(iMycenae, 1, 1)

	def onCombatResult(self, argsList):

		if (not gc.getGame().isVictoryValid(7)): #7 == historical
			return

		pWinningUnit,pLosingUnit = argsList
		pWinningPlayer = gc.getPlayer(pWinningUnit.getOwner())
		pLosingPlayer = gc.getPlayer(pLosingUnit.getOwner())
		cLosingUnit = PyHelpers.PyInfo.UnitInfo(pLosingUnit.getUnitType())
		iPlayer = pWinningPlayer.getID()
		civType = gc.getPlayer(iPlayer).getCivilizationType()
		if civType == iHittites:
			if pWinningUnit.getUnitType() == unit('hittite_huluganni'):
				self.setHittiteKilledUnits(self.getHittiteKilledUnits() + 1)

	def calculateTopCityCulture(self, x, y):
		iBestCityValue = 0
		pCurrent = gc.getMap().plot(x, y)
		if (pCurrent.isCity()):
			bestCity = pCurrent.getPlotCity()
			for iPlayerLoop in range(gc.getMAX_PLAYERS()):
				apCityList = PyPlayer(iPlayerLoop).getCityList()

				for pCity in apCityList:
					iTotalCityValue = pCity.GetCy().countTotalCultureTimes100()
					if (iTotalCityValue > iBestCityValue and not pCity.isBarbarian()):
						bestCity = pCity
						iBestCityValue = iTotalCityValue
			return bestCity
		return -1

	def calculateTopCityPopulation(self, x, y):
		iBestCityValue = 0
		pCurrent = gc.getMap().plot(x, y)
		if (pCurrent.isCity()):
			bestCity = pCurrent.getPlotCity()
			for iPlayerLoop in range(gc.getMAX_PLAYERS()):
				apCityList = PyPlayer(iPlayerLoop).getCityList()

				for pCity in apCityList:
					iTotalCityValue = pCity.getPopulation()
					if (iTotalCityValue > iBestCityValue and not pCity.isBarbarian()):
						bestCity = pCity
						iBestCityValue = iTotalCityValue
			return bestCity
		return -1