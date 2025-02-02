def GetPredecions(model ,features: list):
  result = {
            0: 'Insufficient_Weight', 
            1: 'Normal_Weight', 
            2: 'Obesity_Type_I',
            3: 'Obesity_Type_II', 
            4: 'Obesity_Type_III', 
            5: 'Overweight_Level_I',
            6: 'Overweight_Level_II'
  }
  
  pred = model.predict([features])[0]
  return result[pred]