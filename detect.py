from ultralytics import YOLO

model = YOLO("best.pt")

# This will run on ALL images inside folder
results = model("test_images/", show=True, save=True)

print("Detection completed!")