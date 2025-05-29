# Stores the advice and recommendations for gardening based on season and plant type.
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers."
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}

RECOMMENDED_PLANTS = {
    "summer": ["sunflower", "tomato", "zinnia"],
    "winter": ["pansy", "kale", "holly"]
}


# The functions below will handle user input, generate advice, and recommend plants based on the season and type of plant.
def get_user_input():
    """
    Prompts the user for season and plant type. Returns either (season, plant_type).
    """
    season = input("Enter the season (summer/winter): ").strip().lower()
    plant_type = input("Enter the type of plant (flower/vegetable): ").strip().lower()
    return season, plant_type


def generate_advice(season, plant_type):
    """
    Returns gardening advice based on season and plant type.
    """
    advice = SEASON_ADVICE.get(season, "No advice for this season.")
    advice += "\n"
    advice += PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")
    return advice


def recommend_plants(season):
    """
    Suggests plants based on the entered season.
    """
    plants = RECOMMENDED_PLANTS.get(season)
    if plants:
        return f"Recommended plants for {season}: {', '.join(plants)}"
    else:
        return "No specific plant recommendations for this season."


# Main function to run the gardening advice program.
def main():
    season, plant_type = get_user_input()
    print()
    print(generate_advice(season, plant_type))
    print()
    print(recommend_plants(season))


if __name__ == "__main__":
    main()
