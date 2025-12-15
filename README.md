# 🔥 Australia Wildfire Dashboard (Interactive Dash Application)

This project is an interactive **Python Dash dashboard** created to analyse wildfire activity across Australia.  
Users can explore **region-wise** and **year-wise** wildfire patterns using dynamic visualizations powered by **Plotly**.

The dashboard is built entirely using:

- **Pandas** for data processing  
- **Dash** for the web application  
- **Plotly Express** for charts  
- **Callbacks** for interactive filtering  

---

## 📌 Dashboard Features

### ⭐ **1. Region Selection (Radio Buttons)**
Choose from the seven Australian regions:

- New South Wales (NSW)  
- Northern Territory (NT)  
- Queensland (QL)  
- South Australia (SA)  
- Tasmania (TA)  
- Victoria (VI)  
- Western Australia (WA)

### ⭐ **2. Year Selection (Dropdown Menu)**
Pick any available year from the dataset to analyse wildfire trends for that specific year.

---

## 📊 Dynamic Visualizations

When the user selects a region and year, two charts are generated automatically:

### 🔹 **1. Pie Chart — Monthly Average Estimated Fire Area**
Shows how much fire area was recorded across each month of the selected year.

### 🔹 **2. Bar Chart — Monthly Average Pixel Count for Vegetation Fires**
Displays how many fire-detected pixels were captured each month.

These visualizations help identify:

- High-risk fire months  
- Seasonal patterns  
- Region-specific wildfire intensity  

---

## 🧠 What the Application Demonstrates

This project highlights practical skills needed for a **Data Analyst** role:

- Data cleaning and preparation  
- Date extraction (Month, Year)  
- Grouping and aggregations using Pandas  
- Building interactive dashboards  
- Using callbacks to connect UI elements and graphs  
- Creating impactful visualizations for insights  

---

## 📁 File Description

### `Dash_wildfire.py`
This Python script contains:

- Import statements for required libraries  
- Dash app initialization  
- Data loading from the dataset  
- Extraction of Month and Year features  
- Layout design (title, radio buttons, dropdowns, graph containers)  
- Callback function that:
  - Filters data
  - Computes monthly averages
  - Creates Pie and Bar charts
  - Returns charts to the dashboard display  
- App runner code

This file can be executed to launch the dashboard in a browser.

---

## ▶️ How to Run the Application

### Install required libraries:
```bash
pip install pandas dash plotly
_____________________________________________________________________________

Run the Dash app:
python Dash_wildfire.py
_______________________________________
Open the browser and go to:
http://127.0.0.1:8050/
______________________________________
📦 Dataset

The dashboard uses the Historical Wildfires dataset, containing:

Region
Date
Estimated fire area
Fire brightness
Radiative power
Confidence values
Pixel counts

The dataset is loaded directly inside the script.

🙋‍♀️ About This Project

This dashboard was developed as part of hands-on practice in:
Data visualization
Dashboard development
Interactive analytics using Python
_______________________________________
## ✍️ Author Note

This project was developed by **Vidya V. Geetha**, an aspiring **Data Analyst** passionate about transforming raw datasets into meaningful and actionable insights.  
I enjoy working with Python, Pandas, Dash, and visualization tools to build interactive analytical applications that help users understand data intuitively.

This dashboard represents my growing expertise in:

- Data cleaning and preprocessing  
- Exploratory data analysis  
- Interactive dashboard development using Dash  
- Data storytelling through visualizations  

I am continuously learning and excited to take on new challenges in the field of data analytics.  
If you would like to collaborate or discuss opportunities, feel free to connect with me:

**LinkedIn:** https://www.linkedin.com/in/vidyavgk  
**GitHub:** https://github.com/VidyaVGeetha

