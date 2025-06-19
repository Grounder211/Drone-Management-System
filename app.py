from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load datasets
drone_specs_df = pd.read_csv('drone_specs.csv')

# Merge DataFrames based on the correct column names
performance_df = pd.read_csv('performance.csv')
port_requirements_df = pd.read_csv('port_requirements.csv')
merged_df = performance_df.merge(drone_specs_df, left_on='drone_name', right_on='name')
merged_df = merged_df.merge(port_requirements_df, on='port_name')
merged_df.drop(columns=['name'], inplace=True)

# Encode categorical variables
categorical_features = [
    'sensor_capabilities', 'weather_resistance', 'type_of_propulsion', 
    'obstacle_detection', 'environmental_conditions', 'security_threat_level', 
    'wildlife_interference', 'flight_path_restrictions', 'regulatory_requirements', 
    'historical_incident_data'
]
merged_df = pd.get_dummies(merged_df, columns=categorical_features, drop_first=True)

# Normalize numerical features
numerical_features = [
    'flight_radius', 'battery_life', 'payload_capacity', 'camera_resolution', 
    'durability', 'noise_level', 'wind_tolerance', 'range_of_communication', 'gps_accuracy'
]
scaler = StandardScaler()
merged_df[numerical_features] = scaler.fit_transform(merged_df[numerical_features])

# Train model
X = merged_df.drop(columns=['performance_score', 'drone_name', 'port_name'])
y = merged_df['performance_score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)

# Flask routes
@app.route('/')
def index():
    unique_ports = sorted(merged_df['port_name'].unique())  # Get unique port names and sort them
    context = {
        'unique_ports': unique_ports,
        'min_flight_radius_min': drone_specs_df['flight_radius'].min(),
        'min_flight_radius_max': drone_specs_df['flight_radius'].max(),
        'min_battery_life_min': drone_specs_df['battery_life'].min(),
        'min_battery_life_max': drone_specs_df['battery_life'].max(),
        'min_payload_capacity_min': drone_specs_df['payload_capacity'].min(),
        'min_payload_capacity_max': drone_specs_df['payload_capacity'].max(),
        'min_camera_resolution_min': drone_specs_df['camera_resolution'].min(),
        'min_camera_resolution_max': drone_specs_df['camera_resolution'].max()
    }
    return render_template('index.html', **context)

@app.route('/recommend', methods=['POST'])
def recommend():
    port_name = request.form.get('port_name')
    min_flight_radius = float(request.form.get('min_flight_radius', 0))
    min_battery_life = float(request.form.get('min_battery_life', 0))
    min_payload_capacity = float(request.form.get('min_payload_capacity', 0))
    min_camera_resolution = float(request.form.get('min_camera_resolution', 0))

    recommendations = recommend_drone(port_name, min_flight_radius, min_battery_life, min_payload_capacity, min_camera_resolution)
    return render_template('recommendations.html', recommendations=recommendations)

def recommend_drone(port_name, min_flight_radius=0, min_battery_life=0, min_payload_capacity=0, min_camera_resolution=0):
    port_data = port_requirements_df[port_requirements_df['port_name'] == port_name]
    if port_data.empty:
        return []

    potential_drones = merged_df[merged_df['port_name'] == port_name]

    filtered_drones = potential_drones[
        (potential_drones['flight_radius'] >= min_flight_radius) &
        (potential_drones['battery_life'] >= min_battery_life) &
        (potential_drones['payload_capacity'] >= min_payload_capacity) &
        (potential_drones['camera_resolution'] >= min_camera_resolution)
    ]

    if filtered_drones.empty:
        potential_drones_features = potential_drones.drop(columns=['performance_score', 'drone_name', 'port_name'])
        predicted_scores = rf_model.predict(potential_drones_features)
        potential_drones['predicted_performance_score'] = predicted_scores
        ranked_drones = potential_drones.sort_values(by='predicted_performance_score', ascending=False)
        recommendations = ranked_drones[['drone_name', 'predicted_performance_score']].rename(columns={'predicted_performance_score': 'performance_score'}).to_dict(orient='records')
    else:
        ranked_drones = filtered_drones.sort_values(by='performance_score', ascending=False)
        recommendations = ranked_drones[['drone_name', 'performance_score']].to_dict(orient='records')

    return recommendations

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=False)



