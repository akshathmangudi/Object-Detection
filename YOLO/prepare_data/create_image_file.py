import os


alpaca_id = '/m/0pcr'

train_boxes = os.path.join('.', './data/oidv6-train-annotations-bbox.csv')
val_boxes = os.path.join('.', './data/validation-annotations-bbox.csv')
test_boxes = os.path.join('.', './data/test-annotations-bbox.csv')

image_list_file_path = os.path.join('.', './dataset/image_list_file')

image_list_file_list = []
for j, filename in enumerate([train_boxes, val_boxes, test_boxes]):
    print(filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name in [alpaca_id] and id not in image_list_file_list:
                image_list_file_list.append(id)
                with open(image_list_file_path, 'a') as fw:
                    fw.write('{}/{}\n'.format(['train', 'validation', 'test'][j], id))
            line = f.readline()

        f.close()
