from config import TEMP_THRESHOLD, WATER_INTAKE_PER_DEGREE

def calculate_water_intake(temperature):
    if temperature > TEMP_THRESHOLD:
        water_need = (temperature - TEMP_THRESHOLD) * WATER_INTAKE_PER_DEGREE
        return water_need
    else:
        return 0
