import requests
from django.shortcuts import render
from ..forms import CityForm
from django.conf import settings
from ..weather.api import get_weather_data
from ..ml_model.predict import predict_temperature
from datetime import datetime
import plotly.graph_objects as go
from plotly.offline import plot
from datetime import timedelta
from ..utils.geocode import get_coordinates

future = datetime.now() + timedelta(days=1)

API_KEY = settings.WEATHER_API_KEY

def weather_view(request):
    form = CityForm()
    weather_data = []
    plot_div = None
    # predictions = {}
    pred1 = None
    pred2 = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city1 = form.cleaned_data['city1']
            city2 = form.cleaned_data['city2']

            try:
                data1 = get_weather_data(city1)
            except Exception:
                data1 = {'city': city1, 'error': 'Failed to fetch weather data'}

            try:
                data2 = get_weather_data(city2)
            except Exception:
                data2 = {'city': city2, 'error': 'Failed to fetch weather data'}

            weather_data = [data1, data2]

            # Prediction (dummy lat/lon — replace with real geocoding if needed)
            now = datetime.now()
            lat1, lon1 = get_coordinates(city1)
            lat2, lon2 = get_coordinates(city2)


            if 'error' not in data1:
                pred1 = predict_temperature(lat1, lon1, now.month, future.day, future.hour)
                # predictions[city1.title()] = pred1

            if 'error' not in data2:
                pred2 = predict_temperature(lat2, lon2, now.month, future.day, future.hour)
                # predictions[city2.title()] = pred2

            # Chart if both cities are valid
            if 'error' not in data1 and 'error' not in data2:
                fig = go.Figure()

                fig.add_trace(go.Bar(
                    x=[data1['city'], data2['city']],
                    y=[data1['temperature'], data2['temperature']],
                    name='Temperature (°C)',
                    marker_color='indianred'
                ))

                fig.add_trace(go.Bar(
                    x=[data1['city'], data2['city']],
                    y=[data1['humidity'], data2['humidity']],
                    name='Humidity (%)',
                    marker_color='lightskyblue'
                ))

                fig.update_layout(
                    title='Weather Comparison',
                    xaxis_title='City',
                    yaxis_title='Value',
                    barmode='group',
                    height=270,
                    width=550,
                    font=dict(color="#FFFFFF"),
                    plot_bgcolor='#222222',
                    paper_bgcolor='#111111',
                    margin=dict(l=40, r=40, t=40, b=40)
                )

                plot_div = plot(fig, output_type='div')

    return render(request, 'weather_app/index.html', {
        'form': form,
        'weather_data': weather_data,
        'plot_div': plot_div,
        'pred1' : pred1,
        'pred2' : pred2
        # 'predictions': predictions
    })
