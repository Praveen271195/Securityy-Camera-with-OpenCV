# Importing the required libraries
import dash
import dash_html_components as html
import dash_core_components
from  dash.dependencies import Input,Output
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Reading the respective datasets
recovered = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")
confirmed = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
deaths = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")

# Reshaping the "confirmed" dataset
confirmed = pd.melt(confirmed,id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],var_name="Date",value_name="Confirmed_Cases")

# Reshaping the recovered dataset
recovered = pd.melt(recovered,id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],var_name="Date",value_name="Recovered_cases")

# Reshaping the deaths dataset
deaths = pd.melt(deaths,id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],var_name="Date",value_name="Deaths")

# Merging the above two datasets - "Confirmed cases and Deaths"
merge1 = pd.merge(right = deaths, how = 'left',on = ['Province/State', 'Country/Region', 'Lat', 'Long', 'Date'],left = confirmed)

# Merging the above merged data with the "Recovered" dataset
merge2 = pd.merge(left=merge1,right=recovered,on=['Province/State', 'Country/Region', 'Lat', 'Long', 'Date'])

# Renaming the merge2 as "covid_data"
covid_data = merge2

# Converting the string dates into data time format
covid_data["Date"] = pd.to_datetime(covid_data["Date"])

# Adding the active cases information
covid_data["Active_cases"] = covid_data["Confirmed_Cases"]-covid_data["Deaths"]-covid_data["Recovered_cases"]

# Subtotal of all required columns
cum_global_cases = covid_data.groupby(['Date'])[['Confirmed_Cases', 'Deaths', 'Recovered_cases', 'Active_cases']].sum().reset_index()

# Creating a dictionary to contain the latitude and longitudes for creating a dynamic map
dictionary_for_locations = covid_data[["Country/Region", "Lat", "Long"]].set_index("Country/Region")[["Lat", "Long"]].T.to_dict("dict")

# Creating Dash app
app = dash.Dash(__name__, meta_tags=[{"name": "viewpoint", "content": "width=device-width"}])
server = app.server
app.title = "DD's Covid Dashboard"

# App layout

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url("Data Detective Logo.png"),
                     id="Data_Detective_logo-img",
            style={"height": "100px",
                   "width": "auto",
                   "margin-bottom": "25px"})

        ], className="one-third column"),
        html.Div([
            html.Div([
                html.H3("Global Covid-19 Dashboard",
                style ={"margin-bottom":    "50px", "color": "#1f2c56"}),
            ])
        ], className="one-half column", id="title"),

        html.Div([
            html.H5('Source: JHU ' + str(covid_data.Date.iloc[-1].strftime("%dth %B, %Y")),
                    style={"margin-bottom": "40px", 'color': "#1f2c56"})

        ], className='one-third column', id='title1')

    ], className="row flex-display", id="header", style={"margin-bottom": "25px"}),

    html.Div([
        html.Div([
            html.H6(children="Global Cases",
                    style={"textAlign": "center",
                           "color": "#6ce5e8"}),
            html.P(f"{cum_global_cases['Confirmed_Cases'].iloc[-1]:,.0f}",
            style={"textAlign": "center",
                   "color": "#fdbaf8",
                    "fontSize": 30}),
            html.P("% change from previous date: " + str(round(((cum_global_cases['Confirmed_Cases'].iloc[-1]-
                                             cum_global_cases['Confirmed_Cases'].iloc[-2])/
                                             cum_global_cases['Confirmed_Cases'].iloc[-2])*100, 2)) + "%",
                   style={'textAlign': 'center',
                          "color": "#6ce5e8",
                          "fontSize": 13,
                          "margin-top": "-1px"})

        ], className="card_container three columns"),

        html.Div([
            html.H6(children="Global Deaths",
                    style={"textAlign": "center",
                           "color": "#6ce5e8"}),
            html.P(f"{cum_global_cases['Deaths'].iloc[-1]:,.0f}",
                   style={"textAlign": "center",
                          "color": "#ea2c62",
                          "fontSize": 30}),
            html.P("% change from previous date: " + str(round(((cum_global_cases['Deaths'].iloc[-1] -
                                              cum_global_cases['Deaths'].iloc[-2]) /
                                             cum_global_cases['Deaths'].iloc[-2]) * 100, 2)) + "%",
                   style={'textAlign': 'center',
                          "color": "#6ce5e8",
                          "fontSize": 13,
                          "margin-top": "-1px"})

        ], className="card_container three columns"),

        html.Div([
            html.H6(children="Global Recovered",
                    style={"textAlign": "center",
                           "color": "#6ce5e8"}),
            html.P(f"{cum_global_cases['Recovered_cases'].iloc[-1]:,.0f}",
                   style={"textAlign": "center",
                          "color": "#9fe6a0",
                          "fontSize": 30}),
            html.P("% change from previous date: " + str(round(((cum_global_cases['Recovered_cases'].iloc[-1] -
                                              cum_global_cases['Recovered_cases'].iloc[-2]) /
                                             cum_global_cases['Recovered_cases'].iloc[-2]) * 100, 2)) + "%",
                   style={'textAlign': 'center',
                          "color": "#6ce5e8",
                          "fontSize": 13,
                          "margin-top": "-1px"})

        ], className="card_container three columns"),

        html.Div([
            html.H6(children="Global Active",
                    style={"textAlign": "center",
                           "color": "#6ce5e8"}),
            html.P(f"{cum_global_cases['Active_cases'].iloc[-1]:,.0f}",
                   style={"textAlign": "center",
                          "color": "#ffc93c",
                          "fontSize": 30}),
            html.P("% change from previous date: " + str(round(((cum_global_cases['Active_cases'].iloc[-1] -
                                              cum_global_cases['Active_cases'].iloc[-2]) /
                                             cum_global_cases['Active_cases'].iloc[-2]) * 100, 2)) + "%",
                   style={'textAlign': 'center',
                          "color": "#6ce5e8",
                          "fontSize": 13,
                          "margin-top": "-1px"})

        ], className="card_container three columns"),

    ], className="row flex display"),
    html.Div([
        html.Div([
            html.P("Select Country:", className="fix_label", style={"color": "#6ce5e8"}),
            dash_core_components.Dropdown(id="w_countries",
                                          multi=False,
                                          searchable=True,
                                          value='India',
                                          placeholder="Select Country",
                                          options=[{"label": c,  "value": c}
                                                   for c in (covid_data['Country/Region'].unique())], className="dcc_components"),
            html.P("Status Last Updated: " + " " + str(covid_data.Date.iloc[-1].strftime("%dth %B, %Y")),
                   className="fix_label", style={"text-align": "center", "color": "#6ce5e8"}),
            # Graph components for displaying Confirmed cases
            dash_core_components.Graph(id="confirmed", config={"displayModeBar": False}, className="dcc_components",
                                       style={"margin-top": "15px"}),
            # Graph components for displaying Deaths cases
            dash_core_components.Graph(id="death", config={"displayModeBar": False}, className="dcc_components",
                                       style={"margin-top": "10px"}),
            # Graph components for displaying Recovered cases
            dash_core_components.Graph(id="recovered", config={"displayModeBar": False}, className="dcc_components",
                                       style={"margin-top": "10px"}),
            # Graph components for displaying Active cases
            dash_core_components.Graph(id="active", config={"displayModeBar": False}, className="dcc_components",
                                       style={"margin-top": "10px"})
        ], className="create_container three columns"),

        html.Div([
            # Graph components for displaying cases in Donut chart
            dash_core_components.Graph(id="donut_chart", config={"displayModeBar": 'hover'}
                                       )
        ], className='create_container four columns'),

        html.Div([
            # Graph components for displaying cases in line and bar chart
            dash_core_components.Graph(id="line_chart", config={"displayModeBar": 'hover'}
                                       )
        ], className='create_container five columns'),

    ], className="row flex-display"),

    html.Div([
        html.Div([
            # Graph components for displaying cases in a map
            dash_core_components.Graph(id="map_chart", config={"displayModeBar": 'hover'}
                                       )
        ], className='create_container1 twelve columns')

    ],className='row flex-display')

], id="mainContainer", style={"display": "flex", "flex-direction": "column"})
# Using callback for using the info from the Confirmed cases dataset, giving a value as input and getting figure a output
@app.callback(Output("confirmed","figure"),
              [Input("w_countries", "value")])
# Function for the dropdown to work based on the country selected by the user
def update_confirmed(w_countries):
    # New data frame for getting the cumulative data, grouped by date and country
    grouped_by_date_and_country = covid_data.groupby(['Date', 'Country/Region'])[['Confirmed_Cases', 'Deaths', 'Recovered_cases', 'Active_cases']].sum().reset_index()
    # New data frame for knowing difference between the previous and new values of selected country
    value_confirmed = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Confirmed_Cases"].iloc[-1]-grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Confirmed_Cases"].iloc[-2]
    # New data frame for knowing difference between the yesterday's and it's previous day's values of selected country
    delta_confirmed = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Confirmed_Cases"].iloc[-2]-grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Confirmed_Cases"].iloc[-3]

    return{
        'data': [go.Indicator(
            mode='number+delta',
            value = value_confirmed,
            delta={'reference': delta_confirmed,
                   'position': 'right',
                   'valueformat': ',g',
                   'relative': False,
                   'font': {'size': 15}},
            number={'valueformat': ',',
                    'font': {'size': 20}},
            domain={'y': [0, 1], 'x':[0, 1]}
        )],
        'layout': go.Layout(
            title={'text': 'New cases in a day',
                   'y': 0.98,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            font=dict(color="#fdbaf8"),
            paper_bgcolor= "#1f2c56",
            plot_bgcolor= "#1f2c56",
            height = 50,

        )
    }
# App callback for Deaths cases data
@app.callback(Output("death", "figure"),
              [Input("w_countries", "value")])
# Function for the drop down to work based on the country selected by the user
def update_dead(w_countries):
    # New data frame for getting the cumulative data, grouped by date and country
    grouped_by_date_and_country = covid_data.groupby(['Date', 'Country/Region'])[['Confirmed_Cases', 'Deaths', 'Recovered_cases', 'Active_cases']].sum().reset_index()
    # New data frame for knowing difference between the previous and new values of selected country
    value_dead = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Deaths"].iloc[-1]-grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Deaths"].iloc[-2]
    # New data frame for knowing difference between the yesterday's and it's previous day's values of selected country
    delta_dead = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Deaths"].iloc[-2]-grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Deaths"].iloc[-3]

    return{
        'data': [go.Indicator(
            mode='number+delta',
            value = value_dead,
            delta={'reference': delta_dead,
                   'position': 'right',
                   'valueformat': ',g',
                   'relative': False,
                   'font': {'size': 15}},
            number={'valueformat': ',',
                    'font': {'size': 20}},
            domain={'y': [0, 1], 'x':[0, 1]}
        )],
        'layout': go.Layout(
            title={'text': 'New deaths in a day',
                   'y': 0.98,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            font=dict(color="#ea2c62"),
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            height=50,

        )
    }
# App callback for Recovered cases data
@app.callback(Output("recovered", "figure"),
              [Input("w_countries", "value")])
# Function for the drop down to work based on the country selected by the user
def update_recovered(w_countries):
    # New data frame for getting the cumulative data, grouped by date and country
    grouped_by_date_and_country = covid_data.groupby(['Date', 'Country/Region'])[['Confirmed_Cases', 'Deaths', 'Recovered_cases', 'Active_cases']].sum().reset_index()
    # New data frame for knowing difference between the previous and new values of selected country
    value_recovered = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Recovered_cases"].iloc[-1]-grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Recovered_cases"].iloc[-2]
    # New data frame for knowing difference between the yesterday's and it's previous day's values of selected country
    delta_recovered = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Recovered_cases"].iloc[-2]-grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Recovered_cases"].iloc[-3]

    return{
        'data': [go.Indicator(
            mode='number+delta',
            value =value_recovered,
            delta={'reference': delta_recovered,
                   'position': 'right',
                   'valueformat': ',g',
                   'relative': False,
                   'font': {'size': 15}},
            number={'valueformat': ',',
                    'font': {'size': 20}},
            domain={'y': [0, 1], 'x':[0, 1]}
        )],
        'layout': go.Layout(
            title={'text': 'Recoveries in a day',
                   'y': 0.98,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            font=dict(color="#9fe6a0"),
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            height=50,
        )
    }
# App callback for Active cases data
@app.callback(Output("active", "figure"),
              [Input("w_countries", "value")])
# Function for the drop down to work based on the country selected by the user
def update_active(w_countries):
    # New data frame for getting the cumulative data, grouped by date and country
    grouped_by_date_and_country = covid_data.groupby(['Date', 'Country/Region'])[['Confirmed_Cases', 'Deaths', 'Recovered_cases', 'Active_cases']].sum().reset_index()
    # New data frame for knowing difference between the previous and new values of selected country
    value_active = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Active_cases"].iloc[-2]-grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Active_cases"].iloc[-1]
    # New data frame for knowing difference between the yesterday's and it's previous day's values of selected country
    delta_active = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Active_cases"].iloc[-2]-grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Active_cases"].iloc[-3]

    return{
        'data': [go.Indicator(
            #   DELTA TO BE ADDED
            mode='number',
            value =value_active,
            delta={'reference': delta_active,
                   'position': 'right',
                   'valueformat': ',g',
                   'relative': False,
                   'font': {'size': 15}},
            number={'valueformat': ',',
                    'font': {'size': 20}},
            domain={'y': [0, 1], 'x':[0, 1]}
        )],
        'layout': go.Layout(
            title={'text': 'Active cases in a day',
                   'y': 0.98,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            font=dict(color="#ffc93c"),
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            height=50,
        )
    }
# App callback for Donut Chart
@app.callback(Output("donut_chart", "figure"),
              [Input("w_countries", "value")])
# Function for displaying the required data for the selected country
def update_donut_chart(w_countries):
    # New data frame for getting the cumulative data, grouped by date and country
    grouped_by_date_and_country = covid_data.groupby(['Date', 'Country/Region'])[['Confirmed_Cases', 'Deaths', 'Recovered_cases', 'Active_cases']].sum().reset_index()
    # New data frame for displaying confirmed values of selected country
    confirmed_value = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Confirmed_Cases"].iloc[-1]
    # New data frame for displaying deaths values of selected country
    deaths_value = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Deaths"].iloc[-1]
    # New data frame for displaying Recovered values of selected country
    recovered_value = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries]["Recovered_cases"].iloc[-1]
    # New data frame for displaying Active cases of selected country
    active_values =  grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == "India"]["Active_cases"].iloc[-1]

    colors = ["#ea2c62", "#9fe6a0", "#ffc93c"]
    return{
        'data': [go.Pie(
            labels=['Deaths', 'Recoveries', 'Active cases'],
            values=[deaths_value, recovered_value, active_values],
            marker=dict(colors=colors),
            hoverinfo='label+value+percent',
            textinfo='label+value',
            hole=.7,
            rotation=45,
        )],
        'layout': go.Layout(
            title={'text': 'Division of cases in ' + (w_countries) + ': ',
                   'y': 0.95,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont={"color": "#6ce5e8",
                       "size": 20},
            font=dict(family='sans-serif',
                      color="#6ce5e8",
                      size=12),
            hovermode='closest',
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            legend={'orientation': 'h',
                    'bgcolor': '#1f2c56',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.1}
        )
    }
# App callback for Line and bar chart
@app.callback(Output("line_chart", "figure"),
              [Input("w_countries", "value")])
# Function for displaying the required data for the selected country
def update_donut_chart(w_countries):
    # New data frame for getting the cumulative data, grouped by date and country
    grouped_by_date_and_country = covid_data.groupby(['Date', 'Country/Region'])[['Confirmed_Cases', 'Deaths', 'Recovered_cases', 'Active_cases']].sum().reset_index()
    # Dataframe that shows that shows daily confirmed cases for selected country
    daily_confirmed_cases1 = grouped_by_date_and_country[grouped_by_date_and_country["Country/Region"] == w_countries][["Country/Region", "Date", "Confirmed_Cases"]].reset_index()
    # Adding a new column for calculating the daily confirmed cases.
    daily_confirmed_cases1["Daily_confirmed_cases"] = daily_confirmed_cases1["Confirmed_Cases"] - daily_confirmed_cases1["Confirmed_Cases"].shift(1)
    # Rolling average
    daily_confirmed_cases1["Rolling_avg"] = daily_confirmed_cases1["Daily_confirmed_cases"].rolling(window=7).mean()
    return{
        'data': [go.Bar(
            x=daily_confirmed_cases1["Date"].tail(60),
            y=daily_confirmed_cases1["Daily_confirmed_cases"].tail(60),
            name="Daily Confirmed Cases",
            marker=dict(color="#fdbaf8"),
            hoverinfo='text',
            hovertext=
            '<b>Date</b>: '+ daily_confirmed_cases1["Date"].tail(60).astype(str) + '<br>' +
            '<b>Daily Confirmed Cases</b>: ' + [f'{x:,.0f}' for x in daily_confirmed_cases1["Daily_confirmed_cases"].tail(60)] + '<br>' +
            '<b>Country</b>: ' + daily_confirmed_cases1["Country/Region"].tail(60).astype(str) + '<br>'
        ),
            go.Scatter(
                x=daily_confirmed_cases1["Date"].tail(60),
                y=daily_confirmed_cases1["Rolling_avg"].tail(60),
                mode='lines',
                name="Rolling Average of last 7 days",
                line=dict(width=4, color="#6ce5e8"),
                hoverinfo='text',
                hovertext=
                '<b>Date</b>: ' + daily_confirmed_cases1["Date"].tail(60).astype(str) + '<br>' +
                '<b>Daily Confirmed Cases</b>: ' + [f'{x:,.0f}' for x in daily_confirmed_cases1["Rolling_avg"].tail(60)] + '<br>'
            )
],
        'layout': go.Layout(
            title={'text': 'Last 60 days, daily confirmed cases: ' + (w_countries),
                   'y': 0.95,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont={"color": "#6ce5e8",
                       "size": 20},
            font=dict(family='sans-serif',
                      color="#6ce5e8",
                      size=12),
            hovermode='closest',
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            legend={'orientation': 'h',
                    'bgcolor': '#1f2c56',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7},
            margin=dict(r=0),
            xaxis=dict(title="<b>Date</b>",
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor="white",
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family="Aerial",
                           color="white",
                           size=12
                       )),
            yaxis=dict(title="<b>Daily Confirmed Cases</b>",
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor="white",
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family="Aerial",
                           color="white",
                           size=12
                       ))
                       )
    }
# App callback for map chart
@app.callback(Output("map_chart", "figure"),
              [Input("w_countries", "value")])
# Function for displaying the required data for the selected country
def update_map_chart(w_countries):
    # New data frame for getting the cumulative data, grouped by date and country
    data_with_lat_and_long = covid_data.groupby(["Lat", "Long", "Country/Region"])[["Confirmed_Cases", "Deaths", "Recovered_cases","Active_cases"]].max().reset_index()
    # Dataframe specific to filtered/selected country
    data_with_lat_and_long_of_country = data_with_lat_and_long[data_with_lat_and_long["Country/Region"] == w_countries]

    if w_countries:
        zoom=2
        zoom_lat= dictionary_for_locations[w_countries]['Lat']
        zoom_long = dictionary_for_locations[w_countries]['Long']
    return{
        'data': [go.Scattermapbox(
            lon=data_with_lat_and_long_of_country['Long'],
            lat=data_with_lat_and_long_of_country["Lat"],
            mode='markers',
            marker=go.scattermapbox.Marker(size=data_with_lat_and_long_of_country['Confirmed_Cases']/1500,
                                            color=data_with_lat_and_long_of_country['Confirmed_Cases'],
                                            colorscale='HSV',
                                            showscale=False,
                                            sizemode='area',
                                            opacity=0.5),
            hoverinfo='text',
            hovertext=
            '<b>Country</b>: '+ data_with_lat_and_long_of_country['Country/Region'].astype(str) + '<br>' +
            '<b>Confirmed Cases</b>: ' + [f'{x:,.0f}' for x in data_with_lat_and_long_of_country['Confirmed_Cases']]+ '<br>' +
            '<b>Deaths</b>: ' + [f'{x:,.0f}' for x in data_with_lat_and_long_of_country['Deaths']] + '<br>' +
            '<b>Recoveries</b>: ' + [f'{x:,.0f}' for x in data_with_lat_and_long_of_country['Recovered_cases']] + '<br>'
        )],

        'layout': go.Layout(
            hovermode='x',
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            margin=dict(r=0, l=0, b=0, t=0),
            mapbox=dict(
                accesstoken='pk.eyJ1IjoicHJhdmVlbjk1IiwiYSI6ImNrb3Fua25zNTBycGoydXJ4eDI0MTV5ZGwifQ.wFKmQQOlwnUbcGwiJndwkw',
                center=go.layout.mapbox.Center(lat=zoom_lat, lon=zoom_long),
                style="outdoors",
                zoom=zoom,
            ),
            autosize=True
        )
    }

# Creating local server
if __name__ == "__main__":
    app.run_server(debug=True)

