
# AI Fertilizer Recommendation System

This project provides an AI-based solution to recommend the optimal type and quantity of fertilizer for farmers based on soil and crop data.
It uses machine learning to analyze soil nutrients and suggest sustainable fertilizer usage.

---

## Features

* Takes inputs such as **soil type**, **crop type**, **farm size**, and **fallow years**.
* Analyzes **soil nutrient data** from Chittoor, Andhra Pradesh.
* Recommends both **type** and **quantity** of fertilizer needed.
* Built with **Gradio** for an easy-to-use web interface.

---

## Project Structure

| File                 | Description                                      |
| -------------------- | ------------------------------------------------ |
| `app.py`             | Main application code with the Gradio interface  |
| `chittor_final1.csv` | Dataset containing soil and nutrient information |
| `requirements.txt`   | Python dependencies                              |
| `README.md`          | Project documentation                            |
| `.gitattributes`     | Git configuration for text file handling         |

---

## Installation and Setup

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

   The Gradio interface will open in your browser.

---

## Usage

1. Enter details such as:

   * Crop type
   * Soil type
   * Size of land
   * Number of years the land has been left fallow
2. Click **Submit** to receive fertilizer recommendations for both type and quantity.

---

## Data

The project uses soil nutrient data specific to Chittoor district, Andhra Pradesh.
It includes values such as pH, EC, organic carbon, and available micronutrients.

* Integrate weather-based recommendations.
* Deploy as a scalable web application for farmers.

---

This README provides clear setup instructions and an overview so that anyone can quickly understand and run the project.
