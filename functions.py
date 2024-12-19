from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import torch
import transformers

# Suppress non-critical warnings
transformers.logging.set_verbosity_error()


def detect_objects(image_path):
    """
    Detect objects in an image using DetrForObjectDetection.
    """
    # Load and process the image
    image = Image.open(image_path).convert('RGB')
    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
    model = DetrForObjectDetection.from_pretrained(
        "facebook/detr-resnet-50",
        ignore_mismatched_sizes=True  # Ignore weight mismatch warnings
    )

    # Prepare inputs and run the model
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    # Post-process detections
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(
        outputs, target_sizes=target_sizes, threshold=0.9
    )[0]

    # Format the output
    detections = []
    for score, label, box in zip(results["scores"], results["labels"],
                                 results["boxes"]):
        detections.append({
            "bounding_box": [round(float(coord), 2) for coord in box.tolist()],
            "label": model.config.id2label[int(label)],
            "score": round(float(score), 2),
        })

    return detections


if __name__ == '__main__':
    image_path = r'C:\Users\sarfa\Documents\PythonProject\data\test.jpg'
    detected_objects = detect_objects(image_path)
    for obj in detected_objects:
        print(
            f"Bounding Box: {obj['bounding_box']}, Label: {obj['label']}, Score: {obj['score']}")
