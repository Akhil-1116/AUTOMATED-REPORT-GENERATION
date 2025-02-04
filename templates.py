from reportlab.lib import colors
from reportlab.lib.units import inch
import locale

# Set locale for currency formatting
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def create_sales_report(report_generator, data_analysis):
    """Create a sales report template"""
    # Add title
    report_generator.add_title("Sales Performance Report")
    
    # Add summary section
    report_generator.add_header("Executive Summary")
    report_generator.add_paragraph(f"""
    Total Sales: ${locale.currency(data_analysis['total_sales'], grouping=True)[:-3]}
    Average Quantity per Sale: {data_analysis['avg_quantity']:.2f}
    Top Performing Product: {data_analysis['top_product']}
    Best Performing Region: {data_analysis['top_region']}
    """)
    
    # Add product performance table
    report_generator.add_header("Product Performance")
    table_data = [['Product', 'Total Quantity', 'Total Sales']]
    for row in data_analysis['product_summary']:
        table_data.append([
            row[0],
            f"{row[1]:,.0f}",
            f"${row[2]:,.2f}"
        ])
    
    report_generator.add_table(table_data, [2.5*inch, 2*inch, 2*inch])
    
    # Add footer
    report_generator.add_paragraph("""
    Note: This report is automatically generated based on the sales data analysis.
    Please contact the IT department for any questions or concerns.
    """)
