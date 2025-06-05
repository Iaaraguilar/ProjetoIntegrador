import streamlit as st
import pandas as pd
import altair as alt
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Comparativo de Ônibus Elétricos SP x NY", layout="centered")

def pagina_frotas():
 
    st.title("🚍 Comparativo: Ônibus a Bateria em São Paulo vs Nova York")

    with st.container():
       

        # Dados e gráfico
        crescimento = {
            "Ano": ["2020", "2021", "2022", "2023", "2024", "2025"],
            "São Paulo": [0, 20, 50, 150, 299, 527],
            "Nova York": [10, 15, 15, 60, 81, 81]
        }

        df_crescimento = pd.DataFrame(crescimento).melt(id_vars="Ano", var_name="Cidade", value_name="Quantidade")

        chart = alt.Chart(df_crescimento).mark_line(point=True).encode(
            x="Ano",
            y="Quantidade",
            color="Cidade"
        ).properties(
            width=600,
            height=400,
            title="Crescimento da Frota Elétrica (Ônibus a Bateria – 2020–2025)"
        )

        st.altair_chart(chart)

def pagina_emissoes():

 


    with st.container():
        st.title("Comparação de Ônibus a Combustão e Emissões de CO₂")

        # Gráfico 1: Quantidade de ônibus a combustão
        df_onibus = pd.DataFrame({
            "Cidade": ["São Paulo", "Nova York"],
            "Ônibus a Combustão": [12473, 3000]
        })

        chart_onibus = alt.Chart(df_onibus).mark_bar().encode(
            x=alt.X("Cidade:N", title="Cidade"),
            y=alt.Y("Ônibus a Combustão:Q", title="Quantidade"),
            color="Cidade"
        ).properties(
            width=400,
            height=300,
            title="Quantidade de Ônibus a Combustão (2023)"
        )

        st.altair_chart(chart_onibus)

        # Gráfico 2: Emissões de CO₂
        df_co2 = pd.DataFrame({
            "Cidade": ["São Paulo", "Nova York"],
            "Toneladas de CO₂": [1904000, 430320]
        })

        chart_co2 = alt.Chart(df_co2).mark_bar().encode(
            x=alt.X("Cidade:N", title="Cidade"),
            y=alt.Y("Toneladas de CO₂:Q", title="Toneladas"),
            color="Cidade"
        ).properties(
            width=400,
            height=300,
            title="Emissões de CO₂ em toneladas geradas por Ônibus a Combustão (2023)"
        )

        st.altair_chart(chart_co2)

# Menu lateral
with st.sidebar:
    selecionado = option_menu(
        menu_title='Menu',
        options=['Frotas', 'Emissões de gases poluentes'],
        default_index=0
    )

# Controle de navegação
if selecionado == "Frotas":
    pagina_frotas()
elif selecionado == "Emissões de gases poluentes":
    pagina_emissoes()