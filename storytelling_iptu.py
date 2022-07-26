import streamlit as st 
#import plotly.express as px
from PIL import Image
import pandas as pd
import numpy as np
st.cache(suppress_st_warning=True)
df = pd.read_csv('tresanoscorreto.csv')

image1 = Image.open('labfaz.jpg')
st.image(image1)
image = Image.open('rio.jpg')
st.image(image, caption='Rio de Janeiro')

audio_file = open('samba2.mp4', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp4')
st.title('O Rio sob a òtica do IPTU')
st.markdown('Ao olhar para um cartão postal do Rio é possível ver um contraste belo')
st.markdown('entre o verde,mata atlântica, o azul, o mar, e o cinza, as edificações.')
st.markdown('Esta é uma das marcas mais cativantes do Rio.')
st.markdown('Mas como conciliar esses três aspectos? Veremos isso por meio do IPTU do Rio.')
st.header('Você sabe o que é o IPTU?')
st.markdown('O IPTU é a sigla para Imposto Predial e Territorial Urbano. (Fonte: Lei 5.172/66)')
st.markdown(' Conforme a Lei,o imposto é de responsabilidade dos Municípios.')
st.markdown('O IPTU é coordenado pela Secretaria Municipal de Fazenda e Planejamento - SMFP')
st.header('Como é calculado o IPTU?')
st.latex(r'''IPTU\ = Valor_{venal} \ x\ Alíquota''')
st.markdown('**me explica melhor?**')
st.header('Conforme o Rio cresce o IPTU também cresce...')
st.markdown('O Valor venal leva em conta a àrea edificada, isto é, a parte o cinza das fotos')
#st.markdown('_**20 mil novas construções surgiram nos últimos 3 anos no Rio**_')
st.markdown('Vem ver o quanto cresceu da parte cinza nos últimos anos')
st.metric(label='Novos Imóveis nos últimos 3 anos',value='20 mil')
mapa = df[['lat','lon']]
st.map(mapa)
st.header('Quem banca o equilíbrio das cores?')
st.markdown('Não precisa pensar muito... tá na ponta da língua. O carioca,né?')
dtipo2 = pd.read_csv('dtipo2.csv')
#fig = px.bar(dtipo2, x="Dono", y="Participação (%)", color="Dono", title="Divisão das Inscrições do IPTU do Rio")
#st.plotly_chart(fig)
image22 = Image.open('cpf.JPG')
st.image(image22)
st.markdown('Então é o povão que paga? Não é bem assim..')
col1, col2, col3 = st.columns(3)
col1.metric("Alíquota para residencial", "1% ")
col2.metric("Alíquota para não residencial", "2,5%")
col3.metric("Alíquota para terrenos", "3%")
st.markdown('E tem mais, tem uma galera que fica isenta. Só por causa do valor venal')
col1, col2, col3 = st.columns(3)
col1.metric("Isenção para residencial até ", "R$70.322,00")
col2.metric("Isenção para não residencial até ", "R$30.687,00")
col3.metric("Isenção para terrenos até", "R$ 47.308,00")
st.header('Eles que lutem')
st.markdown('5 bairros com mais inscrições no IPTU')
#bairros5 =  pd.read_excel('bairros5.xlsx')
#st.dataframe(bairros5)
image33 = Image.open('bairros.jpg')
st.image(image33)
st.header('A cidade das cores vibrantes não vibra com o lixo nas ruas')
st.markdown('Junto ao IPTU é cobrada a TCL - Taxa de Coleta de Lixo')
st.markdown('A TCL é a responsável por manter o lixo longe da passaigens do Rio')
st.markdown('**Vai passando as abas e veja qual é o valor da TCL no seu bairro**')

tab1, tab2, tab3 = st.tabs(["Grupo 1", "Grupo 2", "Grupo 3"])

with tab1:
    st.markdown("Valor da Taxa da Coleta de Lixo  R$86,00")
    st.image("UM.jpg", width=500)

with tab2:
    st.markdown("Valor da Taxa da Coleta de Lixo R$172,00")
    st.image("UM.jpg", width=500)

with tab3:
    st.markdown("Valor da Taxa da Coleta de Lixo R$258,00")
    st.image("UM.jpg", width=500)

name = st.text_input('Gostou dessa história? Diz aí, deixe um comentário.')
st.markdown('**Este samba é só porque. Rio, eu gosto de você**')
st.markdown('**AGRADECIMENTOS**')
st.markdown('**Secretaria Municipal de Fazenda e Planejamento**')
st.markdown('Pedro Paulo')
st.markdown('**Fundação João Goulart**')
st.markdown('Rafaela Bastos')
st.markdown('**LabFaz**')
st.markdown('Pablo Steiner')
st.markdown('Leolo Lopes')
st.markdown('Leila Santiago')
st.markdown('Pedro Zaidan')
st.markdown('_Música: Samba do Avião - Tom Jobim_')
image3 = Image.open('labfaz.jpg')
st.image(image3)
