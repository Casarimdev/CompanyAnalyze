# 📊 Company Sales Data Analysis

Uma análise visual e estatística das vendas mensais de uma empresa de cosméticos e higiene ao longo de 12 meses, utilizando Python (Pandas, Matplotlib e NumPy).

---

## 🧾 Sobre o Projeto

Este projeto explora o dataset `company_sales_data.csv`, que contém informações sobre unidades vendidas e lucros de diferentes categorias de produtos em uma empresa de varejo.

A análise contempla:

- Geração de gráficos interativos e visuais
- Cálculo de métricas como lucro por unidade
- Extração de insights comerciais para tomada de decisão

---

## 📈 Gráficos Gerados

### 1. Total de Unidades Vendidas por Mês
Mostra o volume de vendas mensais de forma agregada.

### 2. Lucro Total por Mês
Exibe a evolução mensal do lucro bruto da empresa.

### 3. Vendas por Produto
Compara a performance de cada categoria (FaceCream, FaceWash, ToothPaste, etc.) mês a mês.

### 4. Correlação: Unidades x Lucro
Gráfico de dispersão que mostra a relação linear quase perfeita entre volume e lucro.

---

## 📌 Métricas Derivadas

- `ProfitPerUnit`: cálculo automático da média de lucro por unidade vendida em cada mês.

---

## 🧠 Principais Insights

| Tema                        | O que o dado mostra?                                                                 | Por que importa?                                                                                                                  |
|-----------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Produto-estrela**         | *Bathing Soap* representa **~52%** do total de unidades vendidas.                      | Principal motor de volume – foco em estoque, margem e campanhas específicas.                                                     |
| **Lucro acompanha volume**  | Relação linear entre unidades e lucro (R² ≈ 1).                                        | Estratégias que aumentam volume tendem a aumentar lucro na mesma proporção.                                                      |
| **Sazonalidade**            | Pico em Agosto (Mês 8) e Novembro (Mês 11); queda em Fevereiro (Mês 2) e Junho (Mês 6).| Sugerem meses para ações promocionais ou campanhas de marketing específicas.                                                     |
| **Produtos de baixo giro**  | *FaceWash* e *Moisturizer* juntos < 15% das vendas.                                   | Podem ser reposicionados ou vendidos em pacotes para melhorar giro.                                                              |
| **Lucro por unidade estável** | *Profit per Unit* manteve-se ~10 ao longo do ano.                                    | Sinal de pricing consistente, mas pode indicar espaço para otimizações sazonais e segmentação de preço.                         |

---

## 🔄 Recomendações Estratégicas

### 🎯 Estoque e Operações
- Manter níveis de serviço elevados para Bathing Soap e ToothPaste.
- Implementar **safety stock** específico para os meses de pico (Jul-Set e Nov-Dez).

### 📣 Marketing Direcionado
- Criar campanhas específicas para os meses de baixa (Fev, Jun) com promoções como **"Leve 2, Pague 1"**.
- Bundles sugeridos: *FaceWash + FaceCream* com leve desconto para estimular cross-sell.

### 💰 Pricing Dinâmico
- Testar aumento de preços controlado (1-2%) em períodos de alta demanda, medindo elasticidade de preço.

### 📊 Dashboards e Monitoramento
- Transformar os gráficos gerados em um dashboard contínuo (Power BI, Looker, etc.).
- Implementar alertas automáticos de performance quando volume ou lucro ficarem >1 desvio-padrão abaixo da média.

---

## 🧮 Estatísticas Descritivas

| Métrica         | Descrição                             |
|-----------------|----------------------------------------|
| `count`         | Número de registros por coluna         |
| `mean`          | Média das vendas e lucros              |
| `std`           | Desvio padrão                          |
| `min`, `max`    | Valores mínimo e máximo                |
| `25%`, `50%`, `75%` | Quartis para análise de dispersão |

---

## 📦 Dataset

O arquivo `company_sales_data.csv` contém:

- Vendas mensais (jan-dez)
- Unidades vendidas por categoria de produto
- Total de unidades e lucro bruto mensal

---

## 🚀 Próximos Passos

- ➕ Integrar dados de **custos logísticos** para cálculo de lucro líquido.
- 📣 Adicionar **informações de marketing** para análise de atribuição.
- 📦 Monitorar **giro de estoque (days-on-hand)** por produto.

---

## 🛠️ Tecnologias Utilizadas

- `pandas`
- `matplotlib`
- `numpy`
- `Python 3`
- `Jupyter / VS Code`

---

## 📬 Feedback e Sugestões

Fique à vontade para abrir uma *issue* ou enviar um *pull request* com sugestões, melhorias ou ideias de análise!

---

### 👨‍💻 Autor

> Desenvolvido por [Seu Nome Aqui]  
> 💼 Data Analyst | Python & Business Intelligence  
> 📧 contato@seudominio.com  
