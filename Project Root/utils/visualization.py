import cv2
import matplotlib.pyplot as plt

def visualize_objects(image_path, objects_data, output_path):
    image = cv2.imread(image_path)
    for obj in objects_data:
        cv2.rectangle(image, obj['bbox'][0], obj['bbox'][1], (0, 255, 0), 2)
        cv2.putText(image, obj['description'], obj['bbox'][0], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imwrite(output_path, image)

def generate_output_table(objects_data, output_path):
    import pandas as pd
    df = pd.DataFrame(objects_data)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    objects_data = [
        {"bbox": [(10, 10), (50, 50)], "description": "Object 1", "text": "Text 1", "summary": "Summary 1"},
        {"bbox": [(60, 60), (100, 100)], "description": "Object 2", "text": "Text 2", "summary": "Summary 2"}
    ]
    visualize_objects("data/input_images/sample.jpg", objects_data, "data/output/annotated_image.jpg")
    generate_output_table(objects_data, "data/output/summary_table.csv")

