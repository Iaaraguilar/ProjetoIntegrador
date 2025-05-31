import streamlit as st
import pandas as pd

st.set_page_config(page_title="Comparativo de Ônibus Elétricos SP x NY", layout="centered")

st.title("🚍 Comparativo: Ônibus Elétricos em São Paulo vs Nova York")

st.markdown("""
### Introdução
Este painel compara os investimentos, crescimento da frota de ônibus elétricos, redução de CO₂ e o impacto populacional nas cidades de **São Paulo** e **Nova York**.
""")

#  1. População 
with st.container():
    st.header("População das Cidades")
    populacao = {
        "Cidade": ["São Paulo", "Nova York"],
        "População": [11895578, 8478000]
    }
    df_populacao = pd.DataFrame(populacao).set_index("Cidade")
    st.bar_chart(df_populacao)

# 2. Investimento Histórico
with st.container():
    st.header("Investimento Histórico em Ônibus Elétricos (2015-2025)")
    investimento = {
        "Ano": list(range(2015, 2026)),
        "São Paulo": [5, 10, 15, 25, 30, 40, 50, 90, 120, 280, 350],
        "Nova York": [3, 8, 12, 20, 28, 35, 45, 85, 100, 310, 370]
    }
    df_investimento = pd.DataFrame(investimento).set_index("Ano")
    st.bar_chart(df_investimento)

# 3. Frota Elétrica Atual
with st.container():
    st.header("Frota Elétrica Atual de Ônibus (2025)")
    frota_atual = {
        "Cidade": ["São Paulo", "Nova York"],
        "Quantidade de Ônibus Elétricos": [789, 265]
    }
    df_frota = pd.DataFrame(frota_atual).set_index("Cidade")
    st.bar_chart(df_frota)

# 4. Crescimento da Frota 
with st.container():
    st.header("Crescimento da Frota Elétrica (2015-2025)")
    crescimento = {
        "Ano": list(range(2015, 2026)),
        "São Paulo": [10, 15, 20, 25, 40, 60, 100, 200, 400, 600, 789],
        "Nova York": [5, 8, 10, 15, 30, 50, 80, 120, 180, 220, 265]
    }
    df_crescimento = pd.DataFrame(crescimento).set_index("Ano")
    st.line_chart(df_crescimento)

# 5. Emissões de CO₂ Evitadas 
with st.container():
    st.header("Emissões Anuais de CO₂ Evitadas (ton)")
    emissoes = {
        "Cidade": ["São Paulo", "Nova York"],
        "Emissões Evitadas": [41300, 90000] 
    }
    df_emissoes = pd.DataFrame(emissoes).set_index("Cidade")
    st.bar_chart(df_emissoes)

#  6. Comparação Elétrico vs Diesel 
with st.container():
    st.header("Comparação: Ônibus Elétrico vs Diesel")

    dados_comparacao = {
        "Aspecto": [
            "Emissão Anual de CO₂ (ton)", 
            "Custo de Manutenção", 
            "Custo de Combustível", 
            "Ruído", 
            "Eficiência Energética (%)", 
            "Vida Útil (anos)"
        ],
        "Ônibus Elétrico": [
            0, 
            "Menor", 
            "Mais barato", 
            "Muito baixo", 
            85, 
            10
        ],
        "Ônibus Diesel": [
            900, 
            "Maior", 
            "Mais caro", 
            "Alto", 
            35, 
            8
        ]
    }
    df_comparacao = pd.DataFrame(dados_comparacao).set_index("Aspecto")
    st.table(df_comparacao)

    st.subheader("Emissões Anuais de CO₂ por Tipo de Ônibus")
    df_emissao_ind = pd.DataFrame({
        "Tipo de Ônibus": ["Elétrico", "Diesel"],
        "Emissão Anual de CO₂ (ton)": [0, 900]
    }).set_index("Tipo de Ônibus")
    st.bar_chart(df_emissao_ind)
