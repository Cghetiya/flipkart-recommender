import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="AI Product Recommender", page_icon="✨")

# --- Advanced CSS for a sleek, modern look with animations and new color palette ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body {
        font-family: 'Inter', sans-serif;
        color: #333;
    }

    /* --- NEW BACKGROUND COLOR (Pure White) --- */
    html, body,
    [data-testid="stAppViewContainer"],
    section.main {
        background: #ffffff !important; /* Pure white background */
        background-attachment: fixed !important; /* Ensures background stays fixed during scroll */
    }

    /* Apply font to all streamlit elements *after* background is set (no background on this one) */
    [class*="st-emotion-cache"] {
        font-family: 'Inter', sans-serif;
        color: #333;
    }


    /* --- Main Header - More vibrant gradient --- */
    .big-header {
        font-family: 'Montserrat', sans-serif; /* Impactful header font */
        font-size: 4.5rem !important; /* Slightly larger for presence */
        font-weight: 800 !important;
        margin-bottom: 0.5em;
        margin-top: -0.1em;
        text-align: center;
        background: linear-gradient(90deg, #1a73e8 20%, #00bcd4 80%); /* Deeper blue to bright teal */
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.04em;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.08); /* More pronounced shadow */
        animation: fadeInDown 1.2s ease-out; /* Slightly longer animation */
    }

    /* --- Section Titles - Cohesive color --- */
    .section-title {
        font-size: 1.25rem !important; /* Prominent */
        font-weight: 700 !important;
        color: #2c7ac7; /* A solid mid-blue from the palette */
        margin-bottom: 0.8em;
        margin-top: 1.5em;
        letter-spacing: 0.03em;
        text-transform: uppercase;
        border-bottom: 2px solid rgba(44, 122, 199, 0.2); /* Matches section title blue with transparency */
        padding-bottom: 0.3em;
        animation: fadeInLeft 1s ease-out;
    }

    /* --- FILTER CARD CONTAINER - APPLE-LIKE STYLING --- */
    section.main > div > div > div:nth-child(2) > div {
        background: #ffffff; /* Pure white */
        border-radius: 28px; /* More rounded corners */
        /* Layered, soft shadows for a floating effect */
        box-shadow: 
            0 8px 25px rgba(0, 0, 0, 0.06), /* Main, diffused shadow */
            0 2px 8px rgba(0, 0, 0, 0.04); /* Closer, sharper shadow for definition */
        border: none; /* No visible border, let shadow define shape */
        padding: 2.5em 2.5em 2em 2.5em; /* Generous padding */
        margin-bottom: 2.5em; /* More space below */
        margin-top: 0.8em;
        transition: all 0.3s ease-in-out;
        animation: fadeInUp 0.9s ease-out;
    }
    section.main > div > div > div:nth-child(2) > div:hover {
        /* Enhanced shadow and slight lift on hover */
        box-shadow: 
            0 12px 35px rgba(0, 0, 0, 0.08), 
            0 4px 12px rgba(0, 0, 0, 0.06);
        transform: translateY(-5px); /* Noticeable lift */
    }


    /* --- Selectboxes Styling --- */
    .stSelectbox > div > div {
        background-color: #f7fafd;
        border-radius: 12px;
        border: 1px solid #dbe6ef;
        padding: 0.5rem 1rem;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.03);
        transition: all 0.2s ease-in-out;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .stSelectbox > div > div:hover {
        border-color: #8ac0e2;
        box-shadow: inset 0 1px 5px rgba(0,0,0,0.07);
    }
    .stSelectbox > div > div > div:first-child > div:first-child > div {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        flex-grow: 1;
        min-width: 0;
        padding-right: 0.5rem;
        color: #333;
        font-weight: 500;
    }
    .stSelectbox > div > div > div:first-child > div:last-child {
        flex-shrink: 0;
    }
    .stSelectbox > label {
        font-size: 0.95rem;
        font-weight: 600;
        color: #555;
        margin-bottom: 0.3em;
    }

    /* --- SLIDER STYLING --- */
    .stSlider > div > div {
        background-color: transparent;
        border: none;
        box-shadow: none;
        padding: 0.5rem 0.2rem;
    }

    .stSlider .st-emotion-cache-1ajxajb {
        background-color: #e0eaf2 !important;
        border-radius: 5px;
        height: 6px;
        margin: 0;
    }

    .stSlider .st-emotion-cache-qtb0lq {
        background: linear-gradient(90deg, #1a73e8, #00bcd4) !important;
        border-radius: 5px;
        height: 6px;
        transition: width 0.2s ease-out;
    }

    .stSlider .st-emotion-cache-1o02p14 {
        background-color: #1a73e8 !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        width: 18px;
        height: 18px;
        border-radius: 50% !important;
        top: -6px;
        transform: scale(1);
        transition: background-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease;
    }

    .stSlider .st-emotion-cache-1o02p14:hover {
        background-color: #00bcd4 !important;
        transform: scale(1.1);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }

    .stSlider > label {
        font-size: 0.95rem;
        font-weight: 600;
        color: #555;
        margin-bottom: 0.5em;
        display: block;
    }

    .stSlider .st-emotion-cache-1gjn1l > span {
        font-size: 0.85rem;
        font-weight: 500;
        color: #777;
        padding: 0.2em 0.5em;
        background-color: #f0f4f7;
        border-radius: 8px;
        margin: 0 0.2em;
    }

    .stSlider .st-emotion-cache-1mngp60 {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1a73e8;
        margin-top: -1.5em;
        margin-bottom: 0.5em;
        text-align: center;
        position: relative;
        left: 0;
        transform: none;
    }


    /* --- DataFrame Styling (Beautiful Table) --- */
    .beautiful-table .stDataFrame {
        border-radius: 16px !important; /* Consistent roundedness */
        box-shadow: 0 12px 35px rgba(0,0,0,0.08), 0 5px 15px rgba(0,0,0,0.05); /* Clean, visible shadow */
        border: none !important;
        overflow: hidden;
        margin-bottom: 2.5em;
        margin-top: 0.8em;
        background: #ffffff !important; /* Pure white background */
        transition: all 0.3s ease-in-out;
        animation: fadeIn 1s ease-out;
    }
    .beautiful-table .stDataFrame:hover {
        box-shadow: 0 18px 50px rgba(0,0,0,0.12), 0 8px 20px rgba(0,0,0,0.08);
        transform: translateY(-3px); /* Subtle lift */
    }

    /* --- Expander Styling --- */
    .stExpander > div > div {
        border-radius: 14px;
        border: 1px solid #dbe6ef; /* Matches input border */
        background-color: #fcfdfe; /* Very light background for content */
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        padding: 1em 1.2em;
    }
    .stExpander > div > div > div:first-child > div > p {
        font-weight: 600;
        color: #2c7ac7; /* Matches section title blue */
        font-size: 1.05rem;
    }

    /* --- Info message styling --- */
    .stAlert {
        border-radius: 12px !important;
        background-color: #e6f7ff !important; /* Light blue background */
        color: #007bff !important; /* Standard blue text */
        border: 1px solid #99d6ff !important; /* Slightly darker blue border */
        padding: 1.2rem !important;
        animation: fadeIn 0.6s ease-out;
        margin-top: 1.5em; /* Add some space above the alert */
    }

    /* --- Overall page padding --- */
    /* This class likely controls padding within the main app container, keep it separate from background */
    .st-emotion-cache-z5fcl4 {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    /* --- Keyframe Animations --- */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInLeft {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Horizontal line for separation */
    hr {
        border: none;
        border-top: 1px solid #e0e6ed;
        margin: 1.8em 0;
    }

    /* Adjust Streamlit's default gap between columns if necessary */
    .st-emotion-cache-1ujr3b7 {
        gap: 1.2rem;
    }

    </style>
""", unsafe_allow_html=True)

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv('ml_predictions_for_streamlit.csv')
    df['Who'] = df['Who'].astype(str).str.strip().str.lower()
    df['Brand'] = df['Brand'].astype(str).str.strip()
    df['Product Type'] = df['Product Type'].astype(str).str.strip()
    return df

df = load_data()

# --- Title and Header ---
st.markdown('<div class="big-header">Flipkart Product Recommender</div>', unsafe_allow_html=True)

# --- Filter and Search Section ---
with st.container():
    st.markdown('<div class="section-title">Filter & Search</div>', unsafe_allow_html=True)

    with st.expander("Adjust your product filters", expanded=True):
        col1, col2, col3, col4 = st.columns([1.5, 1.5, 1.5, 1])
        with col1:
            who_values = set(x.strip().lower() for x in df['Who'].unique())
            if 'kid' in who_values or 'kids' in who_values:
                who_options = ['All', 'kid', 'men', 'women']
            else:
                who_options = ['All'] + sorted(who_values)
            who = st.selectbox('Who is it for?', who_options, key="who_select")
        with col2:
            brand_options = ['All'] + sorted(df['Brand'].unique())
            brand = st.selectbox('Select Brand', brand_options, key="brand_select")
        with col3:
            product_type_options = ['All'] + sorted(df['Product Type'].unique())
            product_type = st.selectbox('Product Type', product_type_options, key="product_type_select")
        with col4:
            rating_options = ['All'] + sorted(df['Rating'].unique())
            rating = st.selectbox('Minimum Rating', rating_options, key="rating_select")

        st.markdown("---")

        col_slider_left, col_slider_center, col_slider_right = st.columns([1, 2, 1])
        with col_slider_center:
            top_n = st.slider('How many recommendations?', 1, 20, 10, key="top_n_slider")

# --- Filtering Logic (Unchanged) ---
filtered = df.copy()
if who and who.lower() != 'all':
    filtered = filtered[filtered['Who'] == who]
if brand and brand.lower() != 'all':
    filtered = filtered[filtered['Brand'] == brand]
if product_type and product_type.lower() != 'all':
    filtered = filtered[filtered['Product Type'] == product_type]
if rating and rating != 'All':
    filtered = filtered[filtered['Rating'] >= float(rating)]

if 'predicted_rating' in filtered.columns:
    sort_cols = ['predicted_rating', 'Rating']
elif 'Rating' in filtered.columns:
    sort_cols = ['Rating']
else:
    sort_cols = filtered.columns.tolist()[:1]

filtered = filtered.sort_values(sort_cols, ascending=[False]*len(sort_cols))
cols_to_show = ['Brand', 'Title', 'Product Type', 'Who', 'Rating', 'Total Ratings Given']
if 'predicted_rating' in filtered.columns:
    cols_to_show.append('predicted_rating')
result = filtered[cols_to_show].head(top_n)

# --- Display Results Section ---
st.markdown('<div class="section-title">Recommended Products</div>', unsafe_allow_html=True)
if not result.empty:
    st.markdown('<div class="beautiful-table">', unsafe_allow_html=True)
    st.dataframe(result, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("No products match your current filter criteria. Try adjusting your selections!")

# --- Footer (Optional) ---
st.markdown("""
    <style>
        .footer {
            text-align: center;
            padding-top: 40px; /* More space above footer */
            font-size: 0.85em;
            color: #777; /* Softer gray */
        }
    </style>
    <div class="footer">
        Powered by AI & Streamlit | 2025
    </div>
""", unsafe_allow_html=True)