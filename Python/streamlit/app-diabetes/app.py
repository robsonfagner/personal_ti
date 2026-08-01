import streamlit as st
import pandas as pd
import numpy as np
import pickle


# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Predição de Diabetes", layout="centered")
st.title("🩺 Inteligência Artificial - Diagnóstico de Diabetes")
st.write("Insira os dados clínicos do paciente abaixo para obter a predição da IA.")

# --- CARREGAR O MODELO E O SCALER SALVOS ---
@st.cache_resource
def carregar_arquivos():
    with open("modelo_arvore.pkl", "rb") as f:
        modelo = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        padronizador = pickle.load(f)
    return modelo, padronizador

modelo, scaler = carregar_arquivos()

# --- ENTRADAS DE DADOS DO USUÁRIO ---
st.subheader("📋 Dados Clínicos")

# Criando campos interativos baseados nas variáveis originais do seu dataset
gravidas = st.number_input("Número de Gravidezes", min_value=0, max_value=20, value=1)
glicose = st.slider("Concentração de Glicose Plasmática (mg/dL)", min_value=0.0, max_value=200.0, value=120.0)
pressao = st.slider("Pressão Arterial Diastólica (mm Hg)", min_value=0.0, max_value=130.0, value=70.0)
espessura_pele = st.slider("Espessura da Pele no Tríceps (mm)", min_value=0.0, max_value=99.0, value=20.0)
insulina = st.slider("Concentração de Insulina Sérica (mu U/ml)", min_value=0.0, max_value=800.0, value=80.0)
imc = st.slider("Índice de Massa Corporal (IMC)", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function (Histórico Familiar)", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
idade = st.number_input("Idade do Paciente (anos)", min_value=1, max_index=120, value=30)

# --- BOTÃO DE PREDIÇÃO ---
if st.button("🔮 Realizar Diagnóstico"):
    # 1. Organizar os dados clínicos exatamente no mesmo formato do X_train
    dados_paciente = pd.DataFrame([[
        gravidas, glicose, pressao, espessura_pele, insulina, imc, dpf, idade
    ]], columns=['Gravidas', 'Glicose', 'Pressao Arterial', 'Espessura da pele', 'Insulina', 'IMC', 'DPF', 'Idade'])
    
    # 2. Aplicar a mesma padronização de escala (obrigatório!)
    dados_padronizados = scaler.transform(dados_paciente)
    
    # 3. Realizar a previsão usando a Árvore de Decisão
    predicao = modelo.predict(dados_padronizados)
    probabilidade = modelo.predict_proba(dados_padronizados)
    
    # 4. Apresentar o resultado visual elegante
    st.subheader("🎯 Resultado do Diagnóstico")
    if predicao == 1:
        st.error(f"⚠️ **Alerta:** O modelo classificou o paciente como **DIABÉTICO**.")
        st.write(f"Probabilidade de acerto da IA: {probabilidade[1]*100:.2f}%")
    else:
        st.success(f"🟢 **Saudável:** O modelo classificou o paciente como **NÃO DIABÉTICO**.")
        st.write(f"Probabilidade de acerto da IA: {probabilidade*100:.2f}%")