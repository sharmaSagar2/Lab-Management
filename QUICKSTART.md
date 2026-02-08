# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Open Terminal/PowerShell
Navigate to the project folder:
```powershell
cd c:\Users\sagar\OneDrive\Desktop\web
```

### Step 2: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 3: Generate Sample Data
```powershell
python create_sample_data.py
```

Output should show:
```
✅ Sample Excel file created: data/lab_data.xlsx
📊 Total records: 14
🔬 Labs: Lab A, Lab B, Lab C, Lab D
```

### Step 4: Run the Application
```powershell
python app.py
```

You should see:
```
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

### Step 5: Open in Browser
Click this link or copy-paste in your browser:
👉 **http://localhost:5000**

## 🎯 What You'll See

1. **Lab Dashboard** - 4 lab tiles with assigned riders
2. **Click any lab** → See time slots for that lab
3. **Click any time slot** → Edit rider details
4. **Click Save** → Changes saved automatically to Excel!

## 📝 Sample Data Included

The app comes with 4 labs:
- **Lab A**: 4 time slots, 4 riders
- **Lab B**: 4 time slots, 4 riders  
- **Lab C**: 3 time slots, 3 riders
- **Lab D**: 3 time slots, 3 riders

Total: 14 rider assignments with full test details

## 🔧 Troubleshooting

### Port Already in Use
If port 5000 is in use, modify `app.py` line 81:
```python
app.run(debug=True, port=5001)  # Use port 5001 instead
```

### Excel File Not Found
If you get an error about missing Excel file:
```powershell
python create_sample_data.py
```

### Missing Dependencies
If you see import errors, reinstall requirements:
```powershell
pip install --upgrade -r requirements.txt
```

## 📚 Features Overview

| Feature | Details |
|---------|---------|
| **Home Page** | Grid of 4 lab tiles with rider lists |
| **Lab Details** | Time slots with rider assignments |
| **Rider Form** | Edit test config, fuel type, remarks |
| **Data Storage** | Excel-based (no database needed) |
| **Responsive** | Works on desktop, tablet, mobile |
| **Status Colors** | Green=Active, Red=Inactive |

## 💡 Tips

- **Edit Excel directly**: Add/modify data in `data/lab_data.xlsx`, refresh browser
- **Change status colors**: Edit CSS variables in `static/style.css`
- **Add more dropdowns**: Edit options in `templates/rider_details.html`
- **Custom styling**: All CSS is in `static/style.css`

## 🎨 Customization

Edit the Excel file at `data/lab_data.xlsx` to:
- Add more labs
- Add more riders
- Change test types, fuel types, vehicle classes
- Update status values

Changes will appear immediately when you refresh!

---

**Happy Testing!** 🧪 Questions? Check README.md for detailed documentation.
