def GenderMap(Gender: str):
  mapping = {'Female': 0, 'Male': 1}
  return mapping[Gender]

def CALCMap(CALC: str):
  mapping = {'Always': 0, 'Frequently': 1, 'Sometimes': 2, 'no': 3}
  return mapping[CALC]

def FAVCMap(FAVC: str):
  mapping = {'no': 0, 'yes': 1}
  return mapping[FAVC]

def SCCMap(SCC: str):
  mapping = {'no': 0, 'yes': 1}
  return mapping[SCC]

def SMOKEMap(SMOKE: str):
  mapping = {'no': 0, 'yes': 1}
  return mapping[SMOKE]

def FAMILYMap(family: str):
  mapping = {'no': 0, 'yes': 1}
  return mapping[family]

def CAECMap(CAEC: str):
  mapping = {'Always': 0, 'Frequently': 1, 'Sometimes': 2, 'no': 3}
  return mapping[CAEC]

def MTRANSMap(CAEC: str):
  mapping = {'Automobile': 0, 'Bike': 1, 'Motorbike': 2, 'Public_Transportation': 3, 'Walking': 4}
  return mapping[CAEC]

def GetFeatures(Age, Gender, Height, Weight, CALC, FAVC, FCVC, NCP, SCC, SMOKE, CH2O, family, FAF, TUE, CAEC, MTRANS):
  features = [Age, GenderMap(Gender), Height, Weight, CALCMap(CALC), FAVCMap(FAVC), FCVC, NCP, SCCMap(SCC), SMOKEMap(SMOKE), CH2O, FAMILYMap(family), FAF, TUE, CAECMap(CAEC), MTRANSMap(MTRANS)]
  return features