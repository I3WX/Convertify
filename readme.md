

### Convertify API Documentation

**Base URL**: [https://convertify-a8r6.onrender.com](https://convertify-a8r6.onrender.com)

### Overview
The Convertify API allows you to perform various unit conversions, such as length, temperature, area, speed, mass, and data. You can convert from one unit to another by providing the necessary parameters in the URL query.

### API Endpoint
`GET /convert`

### Query Parameters

| Parameter  | Type   | Required | Description                                                                 |
|------------|--------|----------|-----------------------------------------------------------------------------|
| `type`     | string | Yes      | Specifies the conversion type. Options: `length`, `temp`, `area`, `speed`, `mass`, `data`. |
| `value`    | float  | Yes      | The value to be converted.                                                  |
| `from`     | string | Yes      | The unit you want to convert from.                                          |
| `to`       | string | Yes      | The unit you want to convert to.                                            |

### Example Request URL
```
https://convertify-a8r6.onrender.com/convert?type=temp&value=18&from=C&to=F
```

### Supported Conversions

1. **Length Conversion**  
   Converts between different length units.
   - Supported units: `meter`, `kilometer`, `centimeter`, `millimeter`, `micrometer`, `nanometer`

   **Example**:  
   ```
   https://convertify-a8r6.onrender.com/convert?type=length&value=100&from=meter&to=kilometer
   ```

   **Response**:
   ```json
   {
     "result": {
       "converted_value": 0.1,
       "from": "meter",
       "to": "kilometer",
       "value": 100.0
     }
   }
   ```

2. **Temperature Conversion**  
   Converts between Celsius (C), Fahrenheit (F), and Kelvin (K).
   - Supported units: `C`, `F`, `K`

   **Example**:  
   ```
   https://convertify-a8r6.onrender.com/convert?type=temp&value=18&from=C&to=F
   ```

   **Response**:
   ```json
   {
     "result": {
       "converted_value": 64.4,
       "from": "C",
       "to": "F",
       "value": 18.0
     }
   }
   ```

3. **Area Conversion**  
   Converts between different area units.
   - Supported units: `square_meters`, `square_kilometers`, `square_centimeters`, `square_millimeters`, `acres`, `hectares`, `square_yards`, `square_feet`

   **Example**:  
   ```
   https://convertify-a8r6.onrender.com/convert?type=area&value=5000&from=square_meters&to=acres
   ```

   **Response**:
   ```json
   {
     "result": {
       "converted_value": 1.23553,
       "from": "square_meters",
       "to": "acres",
       "value": 5000.0
     }
   }
   ```

4. **Speed Conversion**  
   Converts between different speed units.
   - Supported units: `m/s`, `km/h`, `mph`, `ft/s`, `knots`

   **Example**:  
   ```
   https://convertify-a8r6.onrender.com/convert?type=speed&value=100&from=km/h&to=mph
   ```

   **Response**:
   ```json
   {
     "result": {
       "converted_value": 62.137,
       "from": "km/h",
       "to": "mph",
       "value": 100.0
     }
   }
   ```

5. **Mass Conversion**  
   Converts between different mass units.
   - Supported units: `grams`, `kilograms`, `milligrams`, `micrograms`, `pounds`, `ounces`, `stones`

   **Example**:  
   ```
   https://convertify-a8r6.onrender.com/convert?type=mass&value=2000&from=grams&to=pounds
   ```

   **Response**:
   ```json
   {
     "result": {
       "converted_value": 4.40925,
       "from": "grams",
       "to": "pounds",
       "value": 2000.0
     }
   }
   ```

6. **Data Conversion**  
   Converts between different data units.
   - Supported units: `bytes`, `kilobytes`, `megabytes`, `gigabytes`, `terabytes`, `petabytes`

   **Example**:  
   ```
   https://convertify-a8r6.onrender.com/convert?type=data&value=5000&from=kilobytes&to=megabytes
   ```

   **Response**:
   ```json
   {
     "result": {
       "converted_value": 4.88281,
       "from": "kilobytes",
       "to": "megabytes",
       "value": 5000.0
     }
   }
   ```

### Error Handling
If an invalid unit or conversion type is supplied, the API will return a 400 error with a message:
```json
{
  "error": "Invalid conversion"
}
```

### Use Cases

- Convert lengths like meters to kilometers for scientific calculations.
- Convert temperatures for weather apps or international travel needs.
- Convert areas to understand land sizes in different units.
- Convert speeds for transportation data across different countries.
- Convert mass for weight measurements in different regions.
- Convert data sizes in tech-related tasks.

### Running Locally
To run this API locally, use the following steps:
1. Install Flask and other dependencies:
   ```bash
   pip install flask
   ```
2. Run the application:
   ```bash
   python FlaskApp.py
   ```

Visit the API at `http://localhost:5000`.

### Conclusion
The Convertify API provides a robust and flexible way to convert between various units, with easy-to-use endpoints and support for multiple data types.

---