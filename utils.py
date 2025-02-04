import logging
import os
from datetime import datetime

def setup_logging():
    """Setup logging configuration"""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"report_generation_{timestamp}.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

def validate_data(df):
    """Validate input data"""
    required_columns = ['Date', 'Product', 'Region', 'Quantity', 'Price', 'Total']
    
    # Check for required columns
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Check for null values
    null_counts = df.isnull().sum()
    if null_counts.any():
        raise ValueError(f"Found null values in columns: {null_counts[null_counts > 0].index.tolist()}")
    
    # Check for negative values in numeric columns
    numeric_columns = ['Quantity', 'Price', 'Total']
    for col in numeric_columns:
        if (df[col] < 0).any():
            raise ValueError(f"Negative values found in column: {col}")
    
    return True
