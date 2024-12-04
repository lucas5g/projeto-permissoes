import streamlit as st 
st.title('Projeto e Permissões')
with st.form('form-projeto-permissoes'):
    projeto = st.text_input('Sigla do Projeto', placeholder='Ex: PROJETOSIGLA', )
    funcionalidades = st.text_input('Siglas das Funcionalidades', placeholder='Ex: "FUNCIONALIDADE1, FUNCIONALIDADE2')
    acoes = st.text_input('Siglas das Ações', placeholder='Ex: "ACAO1, ACAO2')

    submit = st.form_submit_button('Cadastrar')

def validarCampos():
    for campo, valor in [projeto, funcionalidades, acoes]:
        if campo == '':
            st.warning('Preencha todos os campos')

        print(campo, valor )
if submit:
    validarCampos()

