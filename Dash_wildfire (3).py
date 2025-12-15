############################################################
# 📌 Step 1: Import Required Libraries
# These libraries support data handling, dashboard components,
# user interactions, and visualizations.
############################################################

import pandas as pd                      # For data manipulation and analysis
import dash                              # Dash framework for creating the dashboard
from dash import html, dcc               # Dashboard layout and core UI components
from dash.dependencies import Input, Output, State  # For callback interactions
import plotly.graph_objects as go        # Advanced plotting (Graph Objects)
import plotly.express as px              # Quick, high-level plotting
from dash import no_update               # To prevent updates when needed
import datetime as dt                    # For working with dates


############################################################
# 📌 Step 2: Create Dash App
# This initializes the dashboard application.
############################################################

app = dash.Dash(__name__)


############################################################
# 📌 Step 3: Configure App Settings
# Allows callbacks to reference layout components 
# before they are fully created.
############################################################

app.config.suppress_callback_exceptions = True


############################################################
# 📌 Step 4: Load the Wildfire Dataset
# Reads the CSV file from cloud storage into a dataframe.
############################################################

df = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
    'IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv'
)


############################################################
# 📌 Step 5: Extract Month and Year from Date Column
# Converts date to datetime format and creates new Month & Year columns.
############################################################

df['Month'] = pd.to_datetime(df['Date']).dt.month_name() 
df['Year']  = pd.to_datetime(df['Date']).dt.year


############################################################
# 📌 Step 6: Build Dashboard Layout
# This section creates the structure and components of the dashboard:
# - Title
# - Region selector (RadioItems)
# - Year selector (Dropdown)
# - Divisions to hold the output charts
############################################################

app.layout = html.Div(children=[

    # Dashboard Title
    html.H1(
        'Australia Wildfire Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 26}
    ),

    # Outer division
    html.Div([

        ####################################################
        # 📌 Step 6.1: Region Selector (RadioItems)
        ####################################################
        html.Div([
            html.H2('Select Region:', style={'margin-right': '2em'}),

            dcc.RadioItems(
                [
                    {"label": "New South Wales",      "value": "NSW"},
                    {"label": "Northern Territory",   "value": "NT"},
                    {"label": "Queensland",           "value": "QL"},
                    {"label": "South Australia",      "value": "SA"},
                    {"label": "Tasmania",             "value": "TA"},
                    {"label": "Victoria",             "value": "VI"},
                    {"label": "Western Australia",    "value": "WA"}
                ],
                value="NSW",
                id='region',
                inline=True
            )
        ]),

        ####################################################
        # 📌 Step 6.2: Year Selector (Dropdown)
        ####################################################
        html.Div([
            html.H2('Select Year:', style={'margin-right': '2em'}),

            dcc.Dropdown(
                df.Year.unique(),  # list of available years
                value=2005,        # default
                id='year'
            )
        ]),

        ####################################################
        # 📌 Step 6.3: Output Containers for Graphs
        # Two empty divisions to hold Pie and Bar charts
        ####################################################
        html.Div([
            html.Div([], id='plot1'),
            html.Div([], id='plot2')
        ], style={'display': 'flex'}),

    ])  # end inner division

])  # end outer layout


############################################################
# 📌 Step 7: Define Callback Inputs & Outputs
# This connects the Region and Year selections to the output charts.
############################################################

@app.callback(
    [
        Output(component_id='plot1', component_property='children'),
        Output(component_id='plot2', component_property='children')
    ],
    [
        Input(component_id='region', component_property='value'),
        Input(component_id='year',   component_property='value')
    ]
)


############################################################
# 📌 Step 8: Callback Function to Generate Charts
# This function:
# 1. Filters data by region and year
# 2. Computes monthly averages
# 3. Creates:
#    - Pie chart (Average Estimated Fire Area)
#    - Bar chart (Average Pixel Count)
# 4. Returns both charts to the layout
############################################################

def reg_year_display(input_region, input_year):
    
    # Step 1: Filter by region and year
    region_data = df[df['Region'] == input_region]
    y_r_data = region_data[region_data['Year'] == input_year]

    # Step 2: Monthly Avg Estimated Fire Area (Pie Chart)
    est_data = y_r_data.groupby('Month')['Estimated_fire_area'].mean().reset_index()
    fig1 = px.pie(
        est_data,
        values='Estimated_fire_area',
        names='Month',
        title=f"{input_region} : Monthly Average Estimated Fire Area in {input_year}"
    )

    # Step 3: Monthly Avg Count of Fire Pixels (Bar Chart)
    veg_data = y_r_data.groupby('Month')['Count'].mean().reset_index()
    fig2 = px.bar(
        veg_data,
        x='Month',
        y='Count',
        title=f"{input_region} : Average Count of Pixels for Presumed Vegetation Fires in {input_year}"
    )

    # Step 4: Return graphs to dashboard
    return [
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2)
    ]


############################################################
# 📌 Step 9: Run the Dashboard Application
############################################################

if __name__ == '__main__':
    app.run()
