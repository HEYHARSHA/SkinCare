import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re

# Load the dataset
def load_data():
    df = pd.read_csv('skincare_products.csv')
    return df

# Function to extract and process package size
def process_package_size(product_name):
    match = re.search(r'(\d+)(ml|g)', str(product_name))
    if match:
        quantity, unit = match.groups()
        quantity = float(quantity)
        if unit == 'g':
            quantity *= 1  # Modify this conversion factor if needed
        return quantity
    else:
        return 100

# Main function to run the Streamlit app
def main():
    # Set page config
    st.set_page_config(page_title="Skincare Products Analysis", layout="wide", initial_sidebar_state="expanded")
    # Custom CSS styling
    custom_css = """
        <style>
            body {
                background-color: silver;
                color: black;
            }
            .stMarkdown {
                background-color: pink;
            }
            .stTitle {
                color: Gold;
            }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Set side panel
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Main Page", "Product Type Analysis","Data Visualization"])

    if page == "Main Page":
        main_page()
    elif page == "Product Type Analysis":
        product_type_analysis()
    elif page == "Data Visualization":
        data_visualization()

def main_page():
    st.title('Skincare Products Analysis')

    # Load the data
    df = load_data()

    # Display the original dataframe
    st.subheader('Original Dataset')
    st.write(df)

    # Process 'Package size' column
    df['Package size(ml)'] = df['product_name'].apply(process_package_size)

    df['price'] = df['price'].str.replace('£','')
    df['price'] = pd.to_numeric(df['price'])
    df['price(Euros)']=df['price']
    df.drop(columns='price', inplace = True)

    # Display the processed dataframe
    st.subheader('Processed Dataset')
    st.write(df)

def product_type_analysis():
    st.title('Product Type Analysis')

    # Load the data
    df = load_data()
    
    # Display product types and insights
    product_type = st.radio("Choose an option", ("Types of Products","Common 3 ingredients in each Product Type", "Number of Products for Each Product Type", "Ingredient with the Highest Count", "Ingredient Counts","Highest Appearance Ingredient and its count in Product Type","Product Category"))

    if product_type == "Types of Products":
        product_types = df['product_type'].unique()
        st.subheader('Types of Products')
        st.write(product_types)
    elif product_type == "Number of Products for Each Product Type":
        product_counts = df['product_type'].value_counts()
        st.subheader('Number of Products for Each Product Type')
        st.write(product_counts)
    elif product_type == "Ingredient with the Highest Count":
        all_ingredients = [ingredient.strip() for sublist in df['ingredients'].str.split(',') for ingredient in sublist]
        ingredient_counts = pd.Series(all_ingredients).value_counts()
        most_common_ingredient = ingredient_counts.idxmax()
        highest_count = ingredient_counts.max()
        st.subheader('Ingredient with the Highest Count:')
        st.write('Ingredient:', most_common_ingredient)
        st.write('Count:', highest_count)
    elif product_type == "Ingredient Counts":
        all_ingredients = [ingredient.strip() for sublist in df['ingredients'].str.split(',') for ingredient in sublist]
        ingredient_counts = pd.Series(all_ingredients).value_counts()
        st.subheader('Ingredient Counts:')
        st.write(ingredient_counts)


    elif product_type == 'Common 3 ingredients in each Product Type':
        select_ingre_key6 = 'select_ingre_key'
        Pro_types = ['Moisturiser', 'Serum', 'Oil', 'Mist', 'Balm', 'Mask', 'Peel', 'Eye Care', 'Cleanser', 'Toner', 'Exfoliator', 'Bath Salts', 'Body Wash', 'Bath Oil']
        selected_pro_type = st.radio('Select the Product category:', Pro_types, key=select_ingre_key6)

        if selected_pro_type:
            product_data = df.loc[df['product_type'] == selected_pro_type]
            ingre_count = product_data['ingredients'].nunique()
            st.subheader(f'{selected_pro_type} Ingredient Count:')
            st.write(ingre_count)
            
            all_ingre = [ingredient.strip() for sublist in product_data['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
            
            common_3_ingredients = ingre_counts.head(3)
            st.subheader('Common 3 Ingredients and Counts:')
            st.write(common_3_ingredients)


    elif product_type == 'Highest Appearance Ingredient and its count in Product Type':
        select_ingre_key = 'select_ingre_key'
        Pro_type = st.selectbox('Select the Product category:',['Moisturiser', 'Serum' ,'Oil' ,'Mist', 'Balm' ,'Mask', 'Peel', 'Eye Care','Cleanser', 'Toner' ,'Exfoliator' ,'Bath Salts', 'Body Wash' ,'Bath Oil'], key='select_ingre_key')
        if Pro_type =='Balm':
            Balm = df.loc[df['product_type']=='Balm']
            ingre_count = Balm['ingredients'].nunique()
            st.subheader('Balm Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Balm['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Moisturiser':
            Moisturiser = df.loc[df['product_type']=='Moisturiser']
            ingre_count = Moisturiser['ingredients'].nunique()
            st.subheader('Moisturiser Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Moisturiser['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Serum':
            Serum = df.loc[df['product_type']=='Serum']
            ingre_count = Serum['ingredients'].nunique()
            st.subheader('Serum Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Serum['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Oil':
            Oil = df.loc[df['product_type']=='Oil']
            ingre_count = Oil['ingredients'].nunique()
            st.subheader('Serum Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Oil['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Mist':
            Mist = df.loc[df['product_type']=='Mist']
            ingre_count = Mist['ingredients'].nunique()
            st.subheader('Mist Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Mist['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Mask':
            Mask = df.loc[df['product_type']=='Mask']
            ingre_count = Mask['ingredients'].nunique()
            st.subheader('Mask Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Mask['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Peel':
            Peel = df.loc[df['product_type']=='Peel']
            ingre_count = Peel['ingredients'].nunique()
            st.subheader('Peel Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Peel['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Eye Care':
            Eye_Care = df.loc[df['product_type']=='Eye Care']
            ingre_count = Eye_Care['ingredients'].nunique()
            st.subheader('Peel Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Eye_Care['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Cleanser':
            Cleanser = df.loc[df['product_type']=='Cleanser']
            ingre_count = Cleanser['ingredients'].nunique()
            st.subheader('Peel Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Cleanser['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Toner':
            Toner = df.loc[df['product_type']=='Toner']
            ingre_count = Toner['ingredients'].nunique()
            st.subheader('Peel Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Toner['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Exfoliator':
            Exfoliator = df.loc[df['product_type']=='Exfoliator']
            ingre_count = Exfoliator['ingredients'].nunique()
            st.subheader('Peel Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Exfoliator['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Bath Salts':
            Bath_Salts = df.loc[df['product_type']=='Bath Salts']
            ingre_count = Bath_Salts['ingredients'].nunique()
            st.subheader('Peel Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Bath_Salts['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        elif Pro_type =='Body Wash':
            Body_Wash = df.loc[df['product_type']=='Body Wash']
            ingre_count = Body_Wash['ingredients'].nunique()
            st.subheader('Peel Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Body_Wash['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)
        else:
            Bath_Oil = df.loc[df['product_type']=='Bath Oil']
            ingre_count = Bath_Oil['ingredients'].nunique()
            st.subheader('Peel Ingredient Count: ')
            st.write(ingre_count)
            all_ingre = [ingredient.strip() for sublist in Bath_Oil['ingredients'].str.split(',') for ingredient in sublist]
            ingre_counts = pd.Series(all_ingre).value_counts()
            st.subheader('Ingredient Counts:')
            st.write(ingre_counts)

    elif product_type=='Product Category':
        st.title("Select Product Type")
        product_types = df['product_type'].unique()
        selected_product_type = st.selectbox('Select Product Type:', product_types)
        selected_products = df[df['product_type'] == selected_product_type]
        st.write(selected_products)

def data_visualization():

    Select_Charts_key = 'Select_Charts_key'
    select  = st.selectbox('Select the Charts:',['Price and Product Type','Package Size (ml)', 'All Product Types','Likart Chart visualization on ingredients vs products','Product Type and Product Count'],key='Select_Charts_key')

    # Load the data and process it
    df = load_data()
    df['price'] = df['price'].str.replace('£','')
    df['price'] = pd.to_numeric(df['price'])
    df['price(Euros)'] = df['price']
    df.drop(columns='price', inplace=True)
    # Process 'Package size' column
    df['Package size(ml)'] = df['product_name'].apply(process_package_size)

    if select =='Price and Product Type':
        st.header("BOX PLOT of Price and Product Type")
        # boxPlot
        fig = px.box(df, x='product_type', y='price(Euros)', title='Price Distribution by Product Type')
        st.plotly_chart(fig)
    elif select =='Package Size (ml)':
        st.header("HISTOGRAM PLOT of Package Size (ml)")
        fig = px.histogram(df, x='Package size(ml)', title='Package Size (ml)',color_discrete_sequence=['Orange'])
        st.plotly_chart(fig)  
    elif select == 'Likart Chart visualization on ingredients vs products':
       # elif select == 'Likart Chart visualization on ingredients vs products':
        df = pd.read_csv('skincare_products.csv')

        # Get top 10 ingredients
        ingredient_columns = [col for col in df.columns if col.startswith('ingredient')]
        top_ingredients = df[ingredient_columns].sum().sort_values(ascending=False).head(10)

        # Set top_labels and colors for Likert scale
        top_labels = ['Strongly<br>Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly<br>Disagree']
        colors = ['rgba(38, 24, 74, 0.8)', 'rgba(71, 58, 131, 0.8)', 'rgba(122, 120, 168, 0.8)',
                'rgba(164, 163, 204, 0.85)', 'rgba(190, 192, 213, 1)']

        # Display selectbox for product type
        select_ingre_key = 'select_ingre_key'
        pro_type = st.selectbox('Select the Product category:', df['product_type'].unique(), key=select_ingre_key)

        if pro_type in df['product_type'].unique():
            selected_products = df[df['product_type'] == pro_type]

            # Set x_data as the total count of each ingredient
            x_data = top_ingredients.values
            # Set y_data as the ingredient names
            y_data = top_ingredients.index

            fig = go.Figure()

            for i in range(len(x_data)):
                fig.add_trace(go.Bar(
                    x=[x_data[i]],
                    y=[y_data[i]],
                    orientation='h',
                    marker=dict(
                        color=colors[i % len(colors)],  # Use modulo to loop over colors if there are more than 5 ingredients
                        line=dict(color='rgb(248,248,249)', width=1)
                    )
                ))

            fig.update_layout(
                xaxis=dict(
                    showgrid=False,
                    showline=False,
                    showticklabels=False,
                    zeroline=False,
                    domain=[0.15, 1]
                ),
                yaxis=dict(
                    showgrid=False,
                    showline=False,
                    showticklabels=True,  # Show tick labels for y-axis (ingredient names)
                    zeroline=False,
                ),
                barmode='stack',
                paper_bgcolor='rgb(248,248,255)',
                plot_bgcolor='rgb(248,248,255)',
                margin=dict(l=120, r=10, t=140, b=80),
                showlegend=False,
            )

            annotations = []
            for yd, xd in zip(y_data, x_data):
                annotations.append(dict(xref='paper', yref='y',
                                        x=0.14, y=yd,
                                        xanchor='right',
                                        text=str(yd),
                                        font=dict(family='Arial', size=14, color='rgb(67,67,67)'),
                                        showarrow=False, align='right'))

                # Check if xd is a numeric value before dividing
                if isinstance(xd, (int, float)):
                    annotations.append(dict(xref='x', yref='y',
                                            x=float(xd) / 2, y=yd,  # Convert xd to float before division
                                            text=str(xd),
                                            font=dict(family='Arial', size=14, color='rgb(248, 248, 255)'),
                                            showarrow=False))
                else:
                    annotations.append(dict(xref='x', yref='y',
                                            x=0, y=yd,
                                            text=str(xd),
                                            font=dict(family='Arial', size=14, color='rgb(248, 248, 255)'),
                                            showarrow=False))

            fig.update_layout(annotations=annotations)

            # Display the plotly chart
            st.plotly_chart(fig)



    elif select == 'All Product Types':
        selected_product_type = st.selectbox('Select Product Type', df['product_type'].unique())

        # Filter the DataFrame based on the selected product type
        filtered_df = df[df['product_type'] == selected_product_type]

        # Plot
        fig = px.scatter(filtered_df, x='product_name', y='price(Euros)', 
                        hover_data={'product_name': False, 'price(Euros)': True, 'Package size(ml)': True}, 
                        title=f'Product Names with Price and Package Size for {selected_product_type}',
                        labels={'price(Euros)': 'Price (Euros)', 'product_name': 'Product Name'},
                        )
        fig.update_traces(marker=dict(size=12))
        fig.update_layout(xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig)
    else:
        st.title('Product Type Analysis')
        # Get product counts for each product type
        product_counts = df['product_type'].value_counts().reset_index()
        product_counts.columns = ['Product Type', 'Product Count']

        # Display the bar plot
        st.header("BAR PLOT of Product Type and Product Count")
        fig = px.bar(product_counts, x='Product Type', y='Product Count', title='Product Type and Product Count',color_discrete_sequence=['green'])
        st.plotly_chart(fig)

    # Streamlit App
if __name__ == '__main__':
    main()
