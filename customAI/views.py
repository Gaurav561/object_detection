from django.shortcuts import render
import os

# Create your views here.
def index(request):
    return render(request , "main.html")

def create_data(request):
    os.system("python dataset_extraction.py")
    os.system("python dataset_extraction1.py")
    os.system("python generate_tfrecord.py --csv_input=train_labels.csv --image_dir=images/train --output_path=train.record")
    os.system("python generate_tfrecord.py --csv_input=test_labels.csv --image_dir=images/test --output_path=test.record")
    os.system("python model_main_tf2.py --model_dir=training/ --pipeline_config_path=training/ssd_efficientdet_d0_512x512_coco17_tpu-8.config")
    return render(request,"index.html")
