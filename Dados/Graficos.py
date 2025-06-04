import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Comparativo de Ônibus Elétricos SP x NY", layout="centered")

st.title("🚍 Comparativo: Ônibus Elétricos em São Paulo vs Nova York")

st.markdown("""
### Introdução
Este painel compara os investimentos, crescimento da frota de ônibus elétricos, redução de CO₂ e o impacto populacional nas cidades de **São Paulo** e **Nova York**.
""")

# MENU LATERAL
with st.sidebar:
    selecionado = option_menu(
        menu_title='Menu',
        options=['Frotas', 'Emissões de gases poluentes'],
        default_index=0
    )
#frotas
if selecionado == "Frotas":
    st.header("Crescimento da Frota Elétrica (Ônibus a Bateria – 2020–2025)")
    crescimento = {
        "Ano": ["2020", "2021", "2022", "2023", "2024", "2025"],
        "São Paulo": [0, 20, 50, 150, 299, 527],
        "Nova York": [10, 15, 15, 60, 81, 81]
    }
    df_crescimento = pd.DataFrame(crescimento).set_index("Ano")
    st.line_chart(df_crescimento)
elif selecionado == "Emissões de gases poluentes":
    st.header("Comparação de Ônibus a Combustão")
    onibus = {
        "Cidade": ["Nova York", "São Paulo"],
        "Ônibus a Combustão": [3000, 12473]
    }
    df_onibus = pd.DataFrame(onibus).set_index("Cidade")
    st.bar_chart(df_onibus)
#co2
    st.header("Toneladas de CO₂ emitidas por ano (2023)")
    combustao = {
        "Cidade": ["São Paulo", "Nova York"],
        "Toneladas de CO₂": [1904000, 430320]
    }
    df_combustao = pd.DataFrame(combustao).set_index("Cidade")
    st.bar_chart(df_combustao)
