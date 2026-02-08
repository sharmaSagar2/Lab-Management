# Configuration & Customization Guide

## 📋 Excel File Structure

Your Excel file (`data/lab_data.xlsx`) should have these columns:

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| Lab Name | Text | Name of the laboratory | Lab A, Lab B |
| Rider Name | Text | Name of the rider/test personnel | John Smith |
| Time Slot | Text | Time duration for testing | 09:00–11:00 |
| Test Type | Text | Type of test being performed | Emission Test |
| Fuel Type | Text | Type of fuel | Petrol, Diesel, CNG |
| Vehicle Class | Text | Classification of vehicle | Two-Wheeler, Four-Wheeler |
| Remarks | Text | Additional notes | Standard test, Pre-delivery |
| Status | Text | Active or Inactive | Active, Inactive |

## 🎨 Customizing Colors

Edit `static/style.css` to change colors. Find the `:root` section:

```css
:root {
    --primary-color: #2563eb;        /* Main blue */
    --secondary-color: #1e40af;      /* Darker blue */
    --danger-color: #dc2626;         /* Red for Inactive */
    --success-color: #16a34a;        /* Green for Active */
    --warning-color: #ea580c;        /* Orange */
    --light-bg: #f8fafc;             /* Light background */
    --card-bg: #ffffff;              /* Card white */
    --text-dark: #1e293b;            /* Dark text */
    --text-light: #64748b;           /* Light gray text */
    --border-color: #e2e8f0;         /* Border color */
}
```

### Example: Change Primary Color to Purple
```css
--primary-color: #9333ea;
--secondary-color: #7e22ce;
```

## 📝 Dropdown Options

### Test Types
Edit in `templates/rider_details.html`, find the Test Type dropdown:

```html
<select id="testType" name="testType" class="form-input" required>
    <option value="Emission Test">Emission Test</option>
    <option value="Performance Test">Performance Test</option>
    <!-- Add more options here -->
</select>
```

### Fuel Types
Find the Fuel Type dropdown in the same file:

```html
<select id="fuelType" name="fuelType" class="form-input" required>
    <option value="Petrol">Petrol</option>
    <option value="Diesel">Diesel</option>
    <!-- Add more options here -->
</select>
```

### Vehicle Classes
Find the Vehicle Class dropdown:

```html
<select id="vehicleClass" name="vehicleClass" class="form-input" required>
    <option value="Two-Wheeler">Two-Wheeler</option>
    <option value="Four-Wheeler">Four-Wheeler</option>
    <!-- Add more options here -->
</select>
```

## 🔌 Flask Configuration

Edit `app.py` to customize Flask settings:

### Change Debug Mode
```python
if __name__ == '__main__':
    app.run(debug=False)  # Change True to False for production
```

### Change Port
```python
if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Use port 8000 instead of 5000
```

### Change Excel File Location
```python
EXCEL_FILE = os.path.join(app.config['UPLOAD_FOLDER'], 'lab_data.xlsx')
# Change to:
EXCEL_FILE = r'C:\path\to\your\custom\data.xlsx'
```

## 📱 Responsive Design

The application automatically adapts to different screen sizes:

- **Desktop (> 768px)**: 4-column grid for labs, multi-column for time slots
- **Tablet (768px)**: 2-column grid
- **Mobile (< 480px)**: 1-column grid, simplified breadcrumbs

To modify breakpoints, edit `static/style.css`:

```css
@media (max-width: 768px) {
    .labs-grid {
        grid-template-columns: 1fr;  /* Change to auto-fill for 2 columns */
    }
}
```

## 🎯 Grid Layout Customization

### Customize Lab Tile Grid

In `static/style.css`, find:
```css
.labs-grid {
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
}
```

- **2 columns**: `repeat(2, 1fr)`
- **3 columns**: `repeat(3, 1fr)`
- **4 columns**: `repeat(4, 1fr)`
- **Auto-fill**: `repeat(auto-fill, minmax(280px, 1fr))`

## 🔐 Security Considerations

For production use:

1. **Set Flask debug to False**
   ```python
   app.run(debug=False)
   ```

2. **Add input validation** in `app.py`
   ```python
   def update_rider_details(lab_name, rider_name, time_slot, data):
       # Add validation for incoming data
       if not all([lab_name, rider_name, time_slot]):
           return False
   ```

3. **Protect Excel file** - Use secure folder permissions

4. **Add authentication** (optional) - For restricted access

## 📊 Adding More Columns to Excel

To add a custom column:

1. **Add column to Excel** (`data/lab_data.xlsx`)
2. **Update Flask code** in `app.py`:
   ```python
   def get_rider_details(lab_name, rider_name, time_slot):
       # Add your custom field
       'custom_field': row['Custom Field Name']
   ```
3. **Update template** in `templates/rider_details.html`:
   ```html
   <div class="form-group">
       <label for="customField">Custom Field</label>
       <input type="text" id="customField" name="customField" 
              value="{{ rider.custom_field }}" class="form-input">
   </div>
   ```

## 🚀 Performance Tips

1. **Large Excel files**: Consider converting to database (SQLite/PostgreSQL)
2. **Caching**: Add Flask caching for frequently accessed data
3. **Pagination**: Add pagination for many labs/time slots

## 🎓 Common Modifications

### Change Application Title
In `templates/base.html`:
```html
<h1 class="navbar-title">🔬 My Custom Title</h1>
```

### Remove Grid Layout (Display as List)
In `static/style.css`:
```css
.labs-grid {
    display: flex;
    flex-direction: column;
}
```

### Change Status Display
In `templates/home.html`:
```html
<span class="status-badge">
    {% if lab.status == 'Active' %}🟢 Active{% else %}🔴 Inactive{% endif %}
</span>
```

### Add Required Field Indicator
In `templates/rider_details.html`:
```html
<label for="testType">Test Type <span style="color: red;">*</span></label>
```

## 📞 Support

For detailed help on:
- **Flask**: https://flask.palletsprojects.com/
- **Pandas**: https://pandas.pydata.org/docs/
- **HTML/CSS**: https://developer.mozilla.org/

---

**Remember**: Always backup your Excel file before making major changes!
