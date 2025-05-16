import requests
import streamlit as st

def buscar_endereco(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(endpoint)
    data = response.json() if response.status_code == 200 else ""
    return data

st.image("https://cdn.codemarket.com.br/image/data/felipo/opencart/2/completar-endereco-cep.png")
st.title("Consulta de Endereço")

cep = st.text_input("Digite o CEP do endereço:", key="CEP")
pesquisar = st.button("Pesquisar")

if pesquisar:
    endereco = buscar_endereco(cep)
    if endereco:
        st.success("Endereço localizado com sucesso!")
        st.text(f"CEP: {endereco["cep"]}")
        st.text(f"Logradouro: {endereco["logradouro"]}")
        st.text(f"Complemento: {endereco["complemento"]}")
        st.text(f"Bairro: {endereco["bairro"]}")
        st.text(f"Estado: {endereco["estado"]}")
        st.text(f"UF: {endereco["uf"]}")
    else:
        st.error("Ops! Endereço não localizado ou inexistente.")





