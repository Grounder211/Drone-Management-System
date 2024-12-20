import pandas as pd
import mysql.connector

# MySQL database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '0000',
    'database': 'dss'
}

def insert_port_requirements_data():
    try:
        # Establish connection to MySQL
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # Load port requirements data from CSV
        port_requirements_df = pd.read_csv('port_requirements.csv')

        # Insert each row into port_requirements table
        for index, row in port_requirements_df.iterrows():
            insert_stmt = """
                INSERT INTO port_requirements1 
                (port_name, surveillance_area, operational_hours, environmental_conditions, budget, 
                 security_threat_level, wildlife_interference, flight_path_restrictions, 
                 regulatory_requirements, historical_incident_data)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                row['port_name'], row['surveillance_area'], row['operational_hours'], 
                row['environmental_conditions'], row['budget'], row['security_threat_level'], 
                row['wildlife_interference'], row['flight_path_restrictions'], 
                row['regulatory_requirements'], row['historical_incident_data']
            )
            cursor.execute(insert_stmt, data)

        cnx.commit()
        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        if 'cnx' in locals() and cnx.is_connected():
            cnx.rollback()
            cnx.close()

if __name__ == '__main__':
    insert_port_requirements_data()
