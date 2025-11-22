from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    html = """
    <h1>University Search</h1>
    <form method="POST">
        Country: <input type="text" name="country" required>
        Filter: <input type="text" name="filter">
        <input type="submit" value="Search">
    </form>
    """
    
    if request.method == 'POST':
        country = request.form.get('country')
        filter_txt = request.form.get('filter', '').lower()
        url = "http://universities.hipolabs.com/search?country=" + country
        
        try:
            data = requests.get(url).json()
            results = [u for u in data if filter_txt in u['name'].lower()]
            
            html += f"<h3>Found {len(results)}:</h3><ul>"
            for uni in results:
                html += f"<li>{uni['name']}</li>"
            html += "</ul>"
        except:
            html += "<p>Error loading data.</p>"
            
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)