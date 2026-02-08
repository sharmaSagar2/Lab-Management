import pandas as pd
import os

# Create sample data
data = {
    'Lab Name': [
        'Lab A', 'Lab A', 'Lab A', 'Lab A',
        'Lab B', 'Lab B', 'Lab B', 'Lab B',
        'Lab C', 'Lab C', 'Lab C',
        'Lab D', 'Lab D', 'Lab D'
    ],
    'Rider Name': [
        'John Smith', 'Sarah Johnson', 'Mike Davis', 'Emma Wilson',
        'David Brown', 'Lisa Anderson', 'Robert Taylor', 'Jennifer Lee',
        'Christopher White', 'Michelle Martin', 'Daniel Jackson',
        'Andrew Garcia', 'Lauren Rodriguez', 'Matthew Martinez'
    ],
    'Time Slot': [
        '09:00–11:00', '11:00–13:00', '13:00–15:00', '15:00–17:00',
        '09:00–11:00', '11:00–13:00', '13:00–15:00', '15:00–17:00',
        '09:00–11:00', '11:00–13:00', '13:00–15:00',
        '10:00–12:00', '12:00–14:00', '14:00–16:00'
    ],
    'Test Type': [
        'Emission Test', 'Performance Test', 'Safety Test', 'Durability Test',
        'Noise Test', 'Emission Test', 'Performance Test', 'Safety Test',
        'Emission Test', 'Durability Test', 'Performance Test',
        'Safety Test', 'Noise Test', 'Emission Test'
    ],
    'Fuel Type': [
        'Petrol', 'Diesel', 'CNG', 'LPG',
        'Electric', 'Hybrid', 'Petrol', 'Diesel',
        'CNG', 'Petrol', 'Diesel',
        'Electric', 'Hybrid', 'Petrol'
    ],
    'Vehicle Class': [
        'Two-Wheeler', 'Three-Wheeler', 'Four-Wheeler', 'Light Commercial',
        'Heavy-Duty', 'Two-Wheeler', 'Three-Wheeler', 'Four-Wheeler',
        'Light Commercial', 'Heavy-Duty', 'Four-Wheeler',
        'Two-Wheeler', 'Three-Wheeler', 'Four-Wheeler'
    ],
    'Remarks': [
        'Standard test', 'Pre-delivery inspection', 'High-speed test', 'Extended durability',
        'Silent operation', 'Optimal emissions', 'Highway performance', 'Urban safety',
        'Emissions control', 'Long-term reliability', 'Acceleration test',
        'Brake system check', 'Noise reduction', 'Cold start test'
    ],
    'Status': [
        'Active', 'Active', 'Active', 'Inactive',
        'Active', 'Active', 'Inactive', 'Active',
        'Active', 'Active', 'Active',
        'Inactive', 'Active', 'Active'
    ]
}

df = pd.DataFrame(data)

# Create data folder if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save to Excel
excel_file = 'data/lab_data.xlsx'
df.to_excel(excel_file, index=False)

print(f"✅ Sample Excel file created: {excel_file}")
print(f"📊 Total records: {len(df)}")
print(f"🔬 Labs: {', '.join(df['Lab Name'].unique())}")
