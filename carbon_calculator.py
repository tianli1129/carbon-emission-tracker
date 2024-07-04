from codecarbon import EmissionsTracker


def calculate_carbon_emissions():
    tracker = EmissionsTracker(output_dir="/Users/Tina/Desktop/carbon-emission-tracker", output_file="emissions_report.json")
    tracker.start()
    try:
        # Compute intensive code goes here
        for number in range(1, 100):
            print(number)
    finally:
        emissions = tracker.stop()
        print('Emission amount in KG:', emissions)


calculate_carbon_emissions()
