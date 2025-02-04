import pandas as pd
import random
from datetime import datetime, timedelta

def generate_sample_sales_data():
    """Generate sample sales data for demonstration"""
    products = ['Laptop', 'Smartphone', 'Tablet', 'Desktop', 'Printer']
    regions = ['North', 'South', 'East', 'West']
    
    data = []
    start_date = datetime.now() - timedelta(days=30)
    
    for _ in range(50):
        date = start_date + timedelta(days=random.randint(0, 30))
        product = random.choice(products)
        region = random.choice(regions)
        quantity = random.randint(1, 100)
        price = random.uniform(100, 2000)
        total = quantity * price
        
        data.append({
            'Date': date,
            'Product': product,
            'Region': region,
            'Quantity': quantity,
            'Price': price,
            'Total': total
        })
    
    return pd.DataFrame(data)

def analyze_sales_data(df):
    """Analyze the sales data and return insights"""
    analysis = {
        'total_sales': df['Total'].sum(),
        'avg_quantity': df['Quantity'].mean(),
        'top_product': df.groupby('Product')['Total'].sum().idxmax(),
        'top_region': df.groupby('Region')['Total'].sum().idxmax(),
        'daily_sales': df.groupby('Date')['Total'].sum().to_dict(),
        'product_summary': df.groupby('Product').agg({
            'Quantity': 'sum',
            'Total': 'sum'
        }).reset_index().values.tolist()
    }
    return analysis
