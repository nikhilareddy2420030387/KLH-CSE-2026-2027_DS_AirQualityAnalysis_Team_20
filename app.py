import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Air Quality Analysis Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background-color: #F4F8F3;
}

[data-testid="stSidebar"] {
    background-color: #123D2B;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #164B35;
    margin-bottom: 0;
}

.subtitle {
    color: #66816F;
    font-size: 15px;
    margin-bottom: 25px;
}

.metric-card {
    background: white;
    padding: 22px;
    border-radius: 15px;
    border-left: 5px solid #3A9D68;
    box-shadow: 0 3px 12px rgba(0,0,0,0.04);
}

.metric-label {
    color: #718477;
    font-size: 14px;
    font-weight: 600;
}

.metric-value {
    color: #164B35;
    font-size: 29px;
    font-weight: 800;
}

.section-title {
    color: #164B35;
    font-size: 23px;
    font-weight: 700;
    margin-top: 20px;
}

.info-card {
    background: #E5F2E8;
    padding: 18px;
    border-radius: 12px;
    color: #164B35;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

@st.cache_data
def load_data():

    possible_paths = [
        Path("data/city_day.csv"),
        Path("city_day.csv")
    ]

    file_path = None

    for path in possible_paths:
        if path.exists():
            file_path = path
            break

    if file_path is None:
        return None

    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip()

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce"
        )

    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    return df


df = load_data()


# --------------------------------------------------
# CHECK DATASET
# --------------------------------------------------

if df is None:

    st.error(
        "Dataset not found. Please place city_day.csv "
        "inside the data folder."
    )

    st.stop()


if "City" not in df.columns:

    st.error("The dataset does not contain a City column.")

    st.stop()


if "Date" not in df.columns:

    st.error("The dataset does not contain a Date column.")

    st.stop()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.markdown("## 🌿 AIR QUALITY")
st.sidebar.markdown("### Analysis Dashboard")

st.sidebar.markdown("---")

st.sidebar.markdown("### Dashboard Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "Overview",
        "City Analysis",
        "Pollutant Analysis",
        "AQI Analysis",
        "Data Explorer"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown("### Filters")

cities = sorted(
    df["City"].dropna().unique().tolist()
)

selected_cities = st.sidebar.multiselect(
    "Select Cities",
    cities,
    default=cities[:min(5, len(cities))]
)

if not selected_cities:
    selected_cities = cities

filtered_df = df[
    df["City"].isin(selected_cities)
].copy()

if not filtered_df.empty:

    min_date = filtered_df["Date"].min().date()
    max_date = filtered_df["Date"].max().date()

    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if isinstance(date_range, tuple) and len(date_range) == 2:

        start_date, end_date = date_range

        filtered_df = filtered_df[
            (filtered_df["Date"].dt.date >= start_date) &
            (filtered_df["Date"].dt.date <= end_date)
        ]

st.sidebar.markdown("---")

st.sidebar.caption(
    "Air Quality Analysis and Visualisation | 2026–2027"
)


# --------------------------------------------------
# COMMON FUNCTIONS
# --------------------------------------------------

pollutants = [
    "PM2.5",
    "PM10",
    "NO",
    "NO2",
    "NOx",
    "NH3",
    "CO",
    "SO2",
    "O3"
]

available_pollutants = [
    col for col in pollutants
    if col in filtered_df.columns
]


def metric_card(label, value):

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def section_heading(title):

    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True
    )


def green_chart(fig):

    fig.update_layout(
        template="plotly_white",
        font=dict(
            family="DM Sans",
            color="#164B35"
        ),
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🌿 Air Quality Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Explore air pollution patterns, pollutant concentrations '
    'and Air Quality Index across Indian cities.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# OVERVIEW PAGE
# --------------------------------------------------

if page == "Overview":

    section_heading("Environmental Overview")

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()

    total_records = len(filtered_df)

    total_cities = filtered_df["City"].nunique()

    avg_aqi = (
        filtered_df["AQI"].mean()
        if "AQI" in filtered_df.columns
        else np.nan
    )

    avg_pm25 = (
        filtered_df["PM2.5"].mean()
        if "PM2.5" in filtered_df.columns
        else np.nan
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "Total Records",
            f"{total_records:,}"
        )

    with col2:
        metric_card(
            "Cities Covered",
            f"{total_cities}"
        )

    with col3:
        metric_card(
            "Average AQI",
            f"{avg_aqi:.1f}" if pd.notna(avg_aqi) else "N/A"
        )

    with col4:
        metric_card(
            "Average PM2.5",
            f"{avg_pm25:.1f}" if pd.notna(avg_pm25) else "N/A"
        )

    section_heading("Air Quality Trends")

    if "AQI" in filtered_df.columns:

        trend_data = (
            filtered_df
            .dropna(subset=["Date", "AQI"])
            .groupby("Date")["AQI"]
            .mean()
            .reset_index()
        )

        fig = px.line(
            trend_data,
            x="Date",
            y="AQI",
            title="Average AQI Over Time",
            markers=True
        )

        fig.update_traces(
            line=dict(color="#258653", width=3)
        )

        green_chart(fig)

    col1, col2 = st.columns(2)

    with col1:

        if "City" in filtered_df.columns and "AQI" in filtered_df.columns:

            city_aqi = (
                filtered_df
                .groupby("City")["AQI"]
                .mean()
                .reset_index()
                .sort_values("AQI", ascending=False)
            )

            fig = px.bar(
                city_aqi,
                x="City",
                y="AQI",
                title="Average AQI by City",
                color="AQI",
                color_continuous_scale="Greens"
            )

            green_chart(fig)

    with col2:

        if "AQI_Bucket" in filtered_df.columns:

            bucket_data = (
                filtered_df["AQI_Bucket"]
                .value_counts()
                .reset_index()
            )

            bucket_data.columns = [
                "AQI Category",
                "Count"
            ]

            fig = px.pie(
                bucket_data,
                names="AQI Category",
                values="Count",
                title="AQI Category Distribution",
                hole=0.45,
                color_discrete_sequence=px.colors.sequential.Greens
            )

            green_chart(fig)


# --------------------------------------------------
# CITY ANALYSIS
# --------------------------------------------------

elif page == "City Analysis":

    section_heading("City-wise Air Quality Analysis")

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()

    if "AQI" in filtered_df.columns:

        city_data = (
            filtered_df
            .groupby("City")["AQI"]
            .mean()
            .reset_index()
            .sort_values("AQI", ascending=False)
        )

        fig = px.bar(
            city_data,
            x="City",
            y="AQI",
            color="AQI",
            title="Average AQI Comparison Across Cities",
            color_continuous_scale="Greens",
            text_auto=".1f"
        )

        green_chart(fig)

        section_heading("City AQI Statistics")

        st.dataframe(
            city_data,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning("AQI column is not available in the dataset.")


# --------------------------------------------------
# POLLUTANT ANALYSIS
# --------------------------------------------------

elif page == "Pollutant Analysis":

    section_heading("Pollutant Concentration Analysis")

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()

    if not available_pollutants:

        st.warning("No pollutant columns found.")

    else:

        selected_pollutant = st.selectbox(
            "Choose Pollutant",
            available_pollutants
        )

        pollutant_data = filtered_df[
            ["Date", "City", selected_pollutant]
        ].dropna()

        avg_value = pollutant_data[
            selected_pollutant
        ].mean()

        max_value = pollutant_data[
            selected_pollutant
        ].max()

        col1, col2 = st.columns(2)

        with col1:
            metric_card(
                "Average Concentration",
                f"{avg_value:.2f}"
            )

        with col2:
            metric_card(
                "Maximum Concentration",
                f"{max_value:.2f}"
            )

        daily_data = (
            pollutant_data
            .groupby("Date")[selected_pollutant]
            .mean()
            .reset_index()
        )

        fig = px.line(
            daily_data,
            x="Date",
            y=selected_pollutant,
            title=f"{selected_pollutant} Concentration Over Time",
            markers=True
        )

        fig.update_traces(
            line=dict(color="#258653", width=3)
        )

        green_chart(fig)

        city_pollutant = (
            pollutant_data
            .groupby("City")[selected_pollutant]
            .mean()
            .reset_index()
            .sort_values(
                selected_pollutant,
                ascending=False
            )
        )

        fig = px.bar(
            city_pollutant,
            x="City",
            y=selected_pollutant,
            title=f"Average {selected_pollutant} by City",
            color=selected_pollutant,
            color_continuous_scale="Greens"
        )

        green_chart(fig)


# --------------------------------------------------
# AQI ANALYSIS
# --------------------------------------------------

elif page == "AQI Analysis":

    section_heading("Air Quality Index Analysis")

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()

    if "AQI" not in filtered_df.columns:

        st.warning("AQI column is unavailable.")

    else:

        aqi_data = filtered_df.dropna(
            subset=["AQI"]
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            metric_card(
                "Average AQI",
                f"{aqi_data['AQI'].mean():.2f}"
            )

        with col2:
            metric_card(
                "Maximum AQI",
                f"{aqi_data['AQI'].max():.2f}"
            )

        with col3:
            metric_card(
                "Minimum AQI",
                f"{aqi_data['AQI'].min():.2f}"
            )

        fig = px.histogram(
            aqi_data,
            x="AQI",
            nbins=30,
            title="Distribution of Air Quality Index",
            color_discrete_sequence=["#3A9D68"]
        )

        green_chart(fig)

        if "AQI_Bucket" in aqi_data.columns:

            bucket_data = (
                aqi_data["AQI_Bucket"]
                .value_counts()
                .reset_index()
            )

            bucket_data.columns = [
                "AQI Category",
                "Number of Records"
            ]

            fig = px.bar(
                bucket_data,
                x="AQI Category",
                y="Number of Records",
                title="Air Quality Category Distribution",
                color="AQI Category",
                color_discrete_sequence=px.colors.sequential.Greens
            )

            green_chart(fig)

        section_heading("AQI by City")

        city_aqi = (
            aqi_data
            .groupby("City")["AQI"]
            .mean()
            .reset_index()
            .sort_values("AQI", ascending=False)
        )

        fig = px.bar(
            city_aqi,
            x="City",
            y="AQI",
            title="Average AQI Across Selected Cities",
            color="AQI",
            color_continuous_scale="Greens"
        )

        green_chart(fig)


# --------------------------------------------------
# DATA EXPLORER
# --------------------------------------------------

elif page == "Data Explorer":

    section_heading("Dataset Explorer")

    st.markdown(
        '<div class="info-card">'
        'Explore the selected air quality records and '
        'understand the structure of the dataset.'
        '</div>',
        unsafe_allow_html=True
    )

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()

    col1, col2 = st.columns(2)

    with col1:
        metric_card(
            "Rows",
            f"{filtered_df.shape[0]:,}"
        )

    with col2:
        metric_card(
            "Columns",
            f"{filtered_df.shape[1]}"
        )

    section_heading("Dataset Preview")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=400
    )

    section_heading("Missing Values")

    missing = (
        filtered_df.isnull()
        .sum()
        .reset_index()
    )

    missing.columns = [
        "Column",
        "Missing Values"
    ]

    fig = px.bar(
        missing,
        x="Column",
        y="Missing Values",
        title="Missing Values in Dataset",
        color="Missing Values",
        color_continuous_scale="Greens"
    )

    green_chart(fig)

    section_heading("Descriptive Statistics")

    st.dataframe(
        filtered_df.describe(
            include="all"
        ),
        use_container_width=True
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#66816F; padding:15px;">
        🌿 <b>Air Quality Analysis and Visualisation</b><br>
        Data Science Project | 2026–2027<br>
        Built using Python, Pandas, Plotly and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)