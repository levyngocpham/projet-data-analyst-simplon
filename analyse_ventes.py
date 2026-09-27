
import pandas as pd
import plotly.express as px

# 1. Chargement des données (en supposant que le fichier s'appelle ventes.csv)
df = pd.read_csv('/content/sample_data/ventes.csv')

# Ajustement des noms de colonnes si nécessaire (c1, c2, c3, c4, c5 ou noms classiques)
# Si vos colonnes s'appellent date, produit, prix, qte, region :
df['ca'] = df['prix'] * df['qte']

# 2. Graphique a : Les ventes (quantité) par produit
sales_by_prod = df.groupby('produit')['qte'].sum().reset_index()
fig1 = px.bar(sales_by_prod, x='produit', y='qte',
              title='Quantité des ventes par produit',
              labels={'produit': 'Produit', 'qte': 'Quantité totale'})
fig1.show()

# 3. Graphique b : Le chiffre d'affaires par produit
ca_by_prod = df.groupby('produit')['ca'].sum().reset_index()
fig2 = px.bar(ca_by_prod, x='produit', y='ca',
              title='Chiffre d'affaires total par produit',
              labels={'produit': 'Produit', 'ca': 'Chiffre d'affaires (€)'})
fig2.show()
