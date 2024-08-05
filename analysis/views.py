import io
import numpy as np
import pandas as pd
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

def get_image():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode('utf-8')

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            file_url = fs.url (filename)
            data = pd.read_csv(fs.open(filename))
            head = data.head()
            description = data.describe()
            missing_values = data.isnull().sum()
            missing_values_df = missing_values.to_frame(name='Missing Values')

            histograms = []
            for column in data.select_dtypes(include=[np.number]).columns:
                plt.figure()
                data[column].hist()
                plt.title(column)
                plt.xlabel(column)
                plt.ylabel('Frequency')

                # Save plot to in-memory file
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                # Encode plot to base64
                img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
                histograms.append(img_str)
                plt.close()

            context = {
                'file_url' : file_url,
                'head' : head.to_html(),
                'description' : description.to_html(),
                'missing_values' : missing_values_df.to_html(),
                'histograms' : histograms,
            }
            return render(request, 'analysis/results.html',context)
        else:
            # If the form is not valid, render the form with errors
            return render(request, 'analysis/upload.html', {'form': form})
    else:
        form = UploadFileForm()
        return render(request, 'analysis/upload.html', {'form': form})
