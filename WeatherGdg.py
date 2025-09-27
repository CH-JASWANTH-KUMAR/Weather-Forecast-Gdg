import requests

# -----------------------------
# 1. Setup
# -----------------------------
api_key = "6c48963a05036825745d9e8b208caa12"
city = input("Enter city name: ")

# -----------------------------
# 2. Fetch current weather
# -----------------------------
current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
current_res = requests.get(current_url)

if current_res.status_code != 200:
    print("City not found. Please check the name.")
    exit()

current_data = current_res.json()
temp = current_data['main']['temp']
humidity = current_data['main']['humidity']
feels_like = current_data['main']['feels_like']
wind_speed = current_data['wind']['speed']
condition = current_data['weather'][0]['description']

print(f"\n🌤 Current Weather in {city}, {current_data['sys']['country']}:")
print(f"- Temperature: {temp}°C")
print(f"- Feels Like: {feels_like}°C")
print(f"- Humidity: {humidity}%")
print(f"- Wind Speed: {wind_speed} m/s")
print(f"- Condition: {condition}")

# -----------------------------
# 3. Fetch 5-day forecast
# -----------------------------
forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
forecast_res = requests.get(forecast_url)
forecast_data = forecast_res.json()

daily_temps = {}
for item in forecast_data['list']:
    date = item['dt_txt'].split(" ")[0]
    if date not in daily_temps:
        daily_temps[date] = []
    daily_temps[date].append(item['main']['temp'])

print("\n📅 5-Day Forecast (Daily Avg Temps):")
avg_temps = []
for date, temps in daily_temps.items():
    avg = sum(temps) / len(temps)
    avg_temps.append(avg)
    print(f"- {date}: {avg:.2f}°C")

# -----------------------------
# 4. Trend analysis
# -----------------------------
trend = "Stable"
if len(avg_temps) >= 2:
    if avg_temps[-1] > avg_temps[0]:
        trend = "🌡️ Rising temperatures"
    elif avg_temps[-1] < avg_temps[0]:
        trend = "❄️ Falling temperatures"

print(f"\n🔍 Trend Analysis: {trend}")

# -----------------------------
# 5. Comfort level analysis
# -----------------------------
if temp > 30:
    comfort = "🔥 Hot"
elif temp >= 20:
    comfort = "😎 Pleasant"
else:
    comfort = "❄️ Cold"

if humidity > 70:
    humidity_level = "💦 Humid"
else:
    humidity_level = "✅ Comfortable"

print(f"\nAnalysis:")
print(f"- Comfort Level: {comfort}")
print(f"- Humidity Level: {humidity_level}")
