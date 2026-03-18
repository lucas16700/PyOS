from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
import plotly.graph_objects as go
import pandas as pd
# 1. Entrada de dados: Array (Lista de listas)
# A primeira linha é geralmente o cabeçalho
dados = [
    ["Mês", "Vendas"],
    ["Jan", 100],
    ["Fev", 150],
    ["Mar", 120],
    ["Abr", 200],
    ["Mai", 180]
]
def imprime(historico_registradores):
    df = pd.DataFrame(historico_registradores, columns=[f"x{i}" for i in range(32)])
    
    fig = go.Figure()

    # Usamos Scattergl (WebGL) para suportar milhões de pontos sem travar
    for i in range(32):
        fig.add_trace(go.Scattergl(
            y=df[f"x{i}"],
            name=f"x{i}",
            mode='lines',
            visible='legendonly' if i > 10 else True # Começa com apenas alguns visíveis para não poluir
        ))

    fig.update_layout(
        title="Depurador de Registradores RISC-V",
        xaxis=dict(
            title="Ciclo de Instrução",
            rangeslider=dict(visible=True), # Barra inferior para navegação rápida
            type="linear"
        ),
        yaxis_title="Valor do Registrador",
        legend=dict(itemclick="toggleothers", itemdoubleclick="toggle"), # Facilita isolar um reg
        template="plotly_dark" # Tema escuro costuma ser melhor para ver picos de estado
    )

    fig.show()
