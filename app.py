import pandas as pd
from sklearn.preprocessing import LabelEncoder
import gradio as gr
import json

# Load data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Encode soil and crop types
def encode_soil_crop(data):
    encode_soil = LabelEncoder()
    data['Soil_Type'] = encode_soil.fit_transform(data['Soil_type'])
    encode_crop = LabelEncoder()
    data['Crop_Type'] = encode_crop.fit_transform(data['Crop_type'])
    return data

# Define nutrient thresholds and application rates
def define_thresholds_application_rates():
    thresholds = {
        'Avail_P': 10,
        'Exch_K': 50,
        'Avail_Ca': 200,
        'Avail_Mg': 50,
        'Avail_S': 10,
        'Avail_Zn': 1,
        'Avail_B': 0.5,
        'Avail_Fe': 4,
        'Avail_Cu': 0.3,
        'Avail_N': 5
    }
    application_rates = {
        'P': 30,
        'K': 50,
        'Ca': 40,
        'Mg': 20,
        'S': 25,
        'Zn': 5,
        'B': 2,
        'Fe': 10,
        'Cu': 1,
        'N': 4
    }
    return thresholds, application_rates

# Define soil density and depth
def define_soil_density_depth():
    soil_density = 1800
    soil_depth = 0.2
    return soil_density, soil_depth

# Function to get fertilizer recommendation
def get_fertilizer_recommendation(row, land_size_m2, fallow_years, thresholds, application_rates):
    deficiencies = []
    fertilizer_amounts = {}
    for nutrient, threshold in thresholds.items():
        if row[nutrient] < threshold:
            nutrient_name = nutrient.split('_')[-1]
            full_nutrient_name = {
                'P': 'Phosphorus',
                'K': 'Potassium',
                'Ca': 'Calcium',
                'Mg': 'Magnesium',
                'S': 'Sulphur',
                'Zn': 'Zinc',
                'B': 'Boron',
                'Fe': 'Iron',
                'Cu': 'Copper',
                'N': 'Nitrogen'
            }[nutrient_name]
            deficiencies.append(full_nutrient_name)
            base_amount_per_m2 = application_rates[nutrient_name] / 10000
            total_amount = base_amount_per_m2 * land_size_m2 * (1 + 0.1 * fallow_years)
            fertilizer_amounts[full_nutrient_name] = round(total_amount, 2)
    if deficiencies:
        return {'recommendation': f'fertilizer needed for {", ".join(deficiencies)}', 'fertilizer_amounts': fertilizer_amounts}
    else:
        return {'recommendation': 'no deficiency, Manure Recommended', 'fertilizer_amounts': {}}

# Gradio application
def gradio_application():
    file_path = 'chittor_final1.csv'
    data = load_data(file_path)
    if data is not None:
        data = encode_soil_crop(data)
        thresholds, application_rates = define_thresholds_application_rates()
        soil_density, soil_depth = define_soil_density_depth()

        def fertilizer_recommendation(soil_type_input, crop_type_input, land_size_m2, fallow_years):
            filtered_data = data[(data['Soil_type'] == soil_type_input) & (data['Crop_type'] == crop_type_input)]
            if filtered_data.empty:
                return json.dumps({'error': 'No data available for the given soil type and crop type.'})
            else:
                row = filtered_data.iloc[0]
                recommendation = get_fertilizer_recommendation(row, land_size_m2, fallow_years, thresholds, application_rates)
                return json.dumps(recommendation)

        demo = gr.Interface(
            fn=fertilizer_recommendation,
            inputs=[
                gr.Dropdown(label="Soil Type", choices=list(data['Soil_type'].unique())),
                gr.Dropdown(label="Crop Type", choices=list(data['Crop_type'].unique())),
                gr.Number(label="Land Size (m2)"),
                gr.Number(label="Fallow Years")
            ],
            outputs="json",
            title="Fertilizer Recommendation App",
            description="Enter the soil type, crop type, land size, and fallow years to get a fertilizer recommendation."
        )

        demo.launch()

if __name__ == "__main__":
    gradio_application()
