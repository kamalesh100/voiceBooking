from dataset import TRAIN_DATA

output = []
for item in TRAIN_DATA:
    entities = item[1]["entities"]
    entity_dict = {}
    entity_dict["text"] = item[0]
    for start, end, label in entities:
        value = item[0][start:end]
        entity_dict[label] = value
    output.append(entity_dict)

print(output)

