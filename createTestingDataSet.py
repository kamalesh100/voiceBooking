import random
import os
from datetime import datetime, timedelta
from data.data_stations import STATIONS
from data.data_command_templates import COMMANDS
from data.data_passenger_label import PASSENGERS_SINGULAR, PASSENGERS_PLURAL

# Define lists of possible values
origins = STATIONS
destinations = STATIONS
templates = COMMANDS
passengersSingular = PASSENGERS_SINGULAR
passengersPlural = PASSENGERS_PLURAL


# Define function to get a random date in the future
def get_random_future_date():
    start_date = datetime.now()
    end_date = start_date + timedelta(days=365)  # change to 90 days
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    day = random_date.day
    if random.choice([True, False]):
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        if random.choice([True, False]):
            return random_date.strftime("%B") + " " + str(day) + suffix
        else:
            return str(day) + suffix + " " + random_date.strftime("%B")

    else:
        if random.choice([True, False]):
            return random_date.strftime("%B") + " " + str(day)
        else:
            return str(day) + " " + random_date.strftime("%B")


def get_passenger_label(passengerCount):
    if passengerCount > 1:
        return random.choice(passengersPlural)
    else:
        return random.choice(passengersSingular)


# Ensure testing_data directory exists
if not os.path.exists("testing_data"):
    os.makedirs("testing_data")

data = []
for i in range(1000):
    origin = random.choice(origins)
    destination = random.choice(destinations)
    while destination == origin:  # Make sure destination is not the same as origin
        destination = random.choice(destinations)
    passengers = random.randint(1, 10)  # change to 10 passengers
    date = get_random_future_date()
    template = random.choice(templates)
    passengers_label = get_passenger_label(passengers)

    template_origin_start = template.index("{origin}")
    template_origin_end = template_origin_start + len("{origin}")
    template_destination_start = template.index("{destination}")
    template_destination_end = template_destination_start + len("{destination}")
    template_passengers_start = template.index("{passengers}")
    template_passengers_end = template_passengers_start + len("{passengers}")
    template_date_start = template.index("{date}")
    template_date_end = template_date_start + len("{date}")

    template_entities_end_sequence = [
        {"label": "Origin", "value": template_origin_end},
        {"label": "Destination", "value": template_destination_end},
        {"label": "Passenger", "value": template_passengers_end},
        {"label": "Date", "value": template_date_end},
    ]

    template_entities_end_sequence_sorted = sorted(
        template_entities_end_sequence, key=lambda k: k["value"]
    )

    sentence = template.format(
        origin=origin,
        destination=destination,
        passengers=passengers,
        passengers_label=passengers_label,
        date=date,
    )

    indexCounter = 0
    # Iterate through the sorted sequence
    for item in template_entities_end_sequence_sorted:
        label = item["label"]

        # Depending on the label, get the correct variable
        if label == "Origin":
            origin_start = sentence.index(origin, indexCounter)
            origin_end = origin_start + len(origin)
            indexCounter = origin_end
        elif label == "Destination":
            destination_start = sentence.index(destination, indexCounter)
            destination_end = destination_start + len(destination)
            indexCounter = destination_end
        elif label == "Passenger":
            passengers_start = sentence.index(str(passengers), indexCounter)
            passengers_end = passengers_start + len(str(passengers))
            indexCounter = passengers_end
        elif label == "Date":
            date_start = sentence.index(date, indexCounter)
            date_end = date_start + len(date)
            indexCounter = date_end

    entities = {
        "entities": [
            (origin_start, origin_end, "Origin"),
            (destination_start, destination_end, "Destination"),
            (passengers_start, passengers_end, "Passenger"),
            (date_start, date_end, "Date"),
        ]
    }

    # Append the sentence and its entities to the data
    data.append((sentence, entities))
    print(f"Dataset {i} created.")

# Create dataset file
with open(f"testing_data/data.py", "w") as file:
    file.write("TEST_DATA = " + str(data))
