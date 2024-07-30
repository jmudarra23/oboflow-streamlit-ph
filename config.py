import streamlit as st

workspaces = {
    "socceranalytics": {
        "subdomain": "socceranalytics",
        "api_key": st.secrets['API_KEY'],
        "labelers": {
            "6yAuyZQBi3fGWKmbHSAUfFy8Q323": "IATeam Filipinas",
            "CBHqHc8z52NPBgdM4dMzIs4HQYs1": "Rustic Orcullo",
            "DMrDw1BIeRYLlQQ9fz47x58NNXl1": "Daniel Cordez",
        }
    },
    "socceranalytics2": {
        "subdomain": "socceranalytics-2-6tmzm",
        "api_key": st.secrets['API_KEY2'],
        "labelers": {
            "6yAuyZQBi3fGWKmbHSAUfFy8Q323": "IATeam Filipinas",
            "ju99fv4CVLhoAdqWNeUaYZ3t6822": "Noie More",
            "OFaT6Z9tDzQw3OnobHt1IUan2lr1": "Kenneth Cabacungan",
        }
    },
    "socceranalytics3": {
        "subdomain": "socceranalytics-3-0ekyq",
        "api_key": st.secrets['API_KEY3'],
        "labelers": {
            "6yAuyZQBi3fGWKmbHSAUfFy8Q323": "IATeam Filipinas",
            "23l2WlvkaHMeunNVJlq2HYFcS0e2": "Christian Ibo",
        }
    },
}

MIN_BOXES = 6500
MIN_IMAGES = 450