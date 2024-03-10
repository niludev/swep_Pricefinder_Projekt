# from django.http import JsonResponse
# from .forms import CarDetailsForm
# from joblib import load
# import pandas as pd
# from django.http import JsonResponse
# from django.views import View
#
# # Load preprocessor and model
# preprocessor = load('preprocessor.joblib')
# model = load('trained_model.joblib')
#
#
# class PredictView(View):
#     def post(self, request, *args, **kwargs):
#         form = CarDetailsForm(request.POST)
#         if form.is_valid():
#             # Extract form data
#             form_data = form.cleaned_data
#
#             # Preprocess the data
#             df = pd.DataFrame([form_data])
#             X = preprocessor.transform(df)
#
#             # Make prediction
#             prediction = model.predict(X)
#
#             # Return response
#             return JsonResponse({'predicted_price': prediction[0]})
#         else:
#             return JsonResponse({'error': form.errors}, status=400)



from django.http import JsonResponse
from .forms import CarDetailsForm
from joblib import load
import pandas as pd
from django.views import View

# Load preprocessor and model
preprocessor = load('price_prediction/preprocessor.joblib')
model = load('price_prediction/trained_model.joblib')

class PredictView(View):
    def post(self, request, *args, **kwargs):
        form = CarDetailsForm(request.POST)
        if form.is_valid():
            # Extract form data
            form_data = form.cleaned_data

            # Process 'Leather interior' to match training data
            form_data['Leather interior'] = 'Yes' if form_data['leather_interior'] else 'No'
            # Create a DataFrame to match the expected input of the preprocessor
            df = pd.DataFrame([form_data])

            # Preprocess the data
            X = preprocessor.transform(df)

            # Make prediction
            prediction = model.predict(X)

            # Return response
            return JsonResponse({'predicted_price': prediction[0]})
        else:
            return JsonResponse({'error': form.errors}, status=400)