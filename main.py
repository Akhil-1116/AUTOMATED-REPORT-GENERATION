import os
from datetime import datetime
from report_generator import ReportGenerator
from sample_data import generate_sample_sales_data, analyze_sales_data
from templates import create_sales_report
from utils import setup_logging, validate_data

def main():
    # Setup logging
    logger = setup_logging()
    logger.info("Starting report generation process")
    
    try:
        # Generate sample data
        logger.info("Generating sample data")
        df = generate_sample_sales_data()
        
        # Validate data
        logger.info("Validating data")
        validate_data(df)
        
        # Analyze data
        logger.info("Analyzing data")
        analysis_results = analyze_sales_data(df)
        
        # Create output directory if it doesn't exist
        output_dir = "reports"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Generate report filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = os.path.join(output_dir, f"sales_report_{timestamp}.pdf")
        
        # Initialize report generator
        logger.info(f"Initializing report generator for: {output_filename}")
        report_gen = ReportGenerator(output_filename)
        
        # Create report using template
        logger.info("Creating report using template")
        create_sales_report(report_gen, analysis_results)
        
        # Generate PDF
        logger.info("Generating PDF")
        report_gen.generate_pdf()
        
        logger.info(f"Report generated successfully: {output_filename}")
        print(f"Report generated successfully: {output_filename}")
        
    except Exception as e:
        logger.error(f"Error generating report: {str(e)}")
        print(f"Error generating report: {str(e)}")
        raise

if __name__ == "__main__":
    main()
