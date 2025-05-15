import random

class DisasterData:
    def _init_(self):
        self.data = [
            {'temperature': 40, 'rainfall': 10, 'wind': 5, 'disaster': 'none'},
            {'temperature': 30, 'rainfall': 100, 'wind': 20, 'disaster': 'flood'},
            {'temperature': 45, 'rainfall': 0, 'wind': 50, 'disaster': 'fire'},
            {'temperature': 25, 'rainfall': 60, 'wind': 5, 'disaster': 'none'},
            {'temperature': 20, 'rainfall': 200, 'wind': 30, 'disaster': 'flood'}
        ]

    def get_data(self):
        return self.data

class DisasterPredictor:
    def predict(self, temperature, rainfall, wind):
        if rainfall > 150 and wind > 20:
            return 'flood'
        elif temperature > 44 and wind > 30:
            return 'fire'
        else:
            return 'none'

class DisasterResponse:
    def dispatch(self, disaster_type):
        if disaster_type == 'flood':
            return "Dispatching boats and rescue teams"
        elif disaster_type == 'fire':
            return "Dispatching fire trucks and medical units"
        else:
            return "No action needed"

data = DisasterData().get_data()
predictor = DisasterPredictor()
manager = DisasterResponse()

for entry in data:
    pred = predictor.predict(entry['temperature'], entry['rainfall'], entry['wind'])
    action = manager.dispatch(pred)
    print(f"Data: {entry} => Predicted: {pred} => Action: {action}")