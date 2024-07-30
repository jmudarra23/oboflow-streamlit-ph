import streamlit as st
from config import workspaces, MIN_BOXES, MIN_IMAGES
import requests
from datetime import datetime, timedelta


st.title("Wizard Football Images Labeled ⚽")


def get_first_date_week(date):
    dayweek = date.weekday()
    first_date = date - timedelta(days=dayweek)
    return first_date


def get_stats(date, labeler_code, api_key, subdomain):
    def fetch_data(start_date, end_date):
        response = requests.get(f"https://api.roboflow.com/{subdomain}/stats", params={
            "api_key": api_key,
            "userId": labeler_code,
            "startDate": start_date,
            "endDate": end_date
        })
        if response.status_code == 200:
            data = response.json()["data"]
            return sum(entry["boxesDrawn"] for entry in data), sum(entry["imagesLabeled"] for entry in data)
        else:
            st.error("Something is wrong... call Jesús")
            return 0, 0

    first_date_week = get_first_date_week(date)

    col1, col2 = st.columns(2)

    boxes_today, imgs_today = fetch_data(date, date)
    boxes_week, imgs_week = fetch_data(first_date_week, date)

    with col1:
        st.subheader("Labels")
        st.metric(label="Today", value=boxes_today)
        st.metric(label="Total weekly", value=boxes_week)
        if boxes_week <= MIN_BOXES:
            st.progress(boxes_week/MIN_BOXES) # Progreso semanal
            st.write(f"Weekly progress: {round((boxes_week/MIN_BOXES)*100, 2)}%")
        else:
            st.progress(100)
            st.write("Weekly progress: 100.0%")
    with col2:
        st.subheader("Images")
        st.metric(label="Today", value=imgs_today)
        st.metric(label="Total weekly", value=imgs_week)
        if imgs_week <= MIN_IMAGES:
            st.progress(imgs_week/MIN_IMAGES)
            st.write(f"Weekly progress: {round((imgs_week/MIN_IMAGES)*100, 2)}%")
        else:
            st.progress(100)
            st.write("Weekly progress: 100.0%")

    if boxes_week < MIN_BOXES:
        st.warning(f"You have {MIN_BOXES - boxes_week} labels left to reach the weekly target!")
    else:
        st.success(f"Congratulations! You have reached your label goal! 🚀")
        st.balloons()
    if imgs_week < MIN_IMAGES:
        st.warning(f"You have {MIN_IMAGES - imgs_week} images left to reach the weekly target!")
    else:
        st.success(f"Congratulations! You reached the image target! 🚀")
        st.balloons()

# Seleccionar el espacio de trabajo
workspace = st.sidebar.selectbox("**Select workspace**", list(workspaces.keys()))

# Obtener los diccionarios correspondientes al espacio de trabajo seleccionado
api_key = workspaces[workspace]["api_key"]
labelers = workspaces[workspace]["labelers"]
subdomain = workspaces[workspace]["subdomain"]

st.sidebar.markdown("---")

labeler = st.sidebar.selectbox(
    "**Name**", list(labelers.values()), index=None
)
if labeler:
    labeler_code = [code for code, name in labelers.items() if name == labeler][0]

st.sidebar.markdown("---")

# Crear el selector de fechas
date = st.sidebar.date_input(
    "**Select a date**",
    datetime.now()
)

if labeler:

    # Llamar a la función para obtener estadísticas al iniciar la aplicación
    get_stats(date, labeler_code, api_key, subdomain)

    # Botón para actualizar estadísticas
    if st.button("Update"):
        
        get_stats(date, labeler_code, api_key, subdomain)
        st.empty()

else:
    st.info("Please 🙏, select the Workspace you belong to and your name.")