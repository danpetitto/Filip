from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Konfigurace
app.config['SECRET_KEY'] = 'tvuj-secret-key-tady'
app.config['DEBUG'] = True

@app.route('/')
def index():
    """Hlavní stránka"""
    return render_template('index.html')

@app.route('/foto')
def foto():
    """Fotogalerie stránka"""
    return render_template('foto.html')

# ========== NOVÉ LOKACE ROUTES ==========
@app.route('/hron.html')
def hron_html():
    """Hron Gym & Gauny Team Brno - HTML route"""
    return render_template('hron.html')

@app.route('/hron')
def hron():
    """Hron Gym & Gauny Team Brno - alias route"""
    return render_template('hron.html')

@app.route('/hrusovany.html')
def hrusovany_html():
    """VAPAS Hrušovany - HTML route"""
    return render_template('hrusovany.html')

@app.route('/hrusovany')
def hrusovany():
    """VAPAS Hrušovany - alias route"""
    return render_template('hrusovany.html')

@app.route('/holzova.html')
def holzova_html():
    """Základní škola Holzova - HTML route"""
    return render_template('holzova.html')

@app.route('/holzova')
def holzova():
    """Základní škola Holzova - alias route"""
    return render_template('holzova.html')

# ========== PŮVODNÍ STRÁNKY ROUTES ==========
@app.route('/about')
def about():
    """O nás stránka"""
    return render_template('index.html', section='about')

@app.route('/achievements')
def achievements():
    """Úspěchy stránka"""
    return render_template('index.html', section='achievements')

@app.route('/videos')
def videos():
    """Videa stránka"""
    return render_template('index.html', section='videos')

@app.route('/training-locations')
def training_locations():
    """Tréninkové lokace stránka"""
    return render_template('index.html', section='training-locations')

@app.route('/locations')
def locations():
    """Lokace stránka (alias)"""
    return render_template('index.html', section='locations')

@app.route('/services')
def services():
    """Služby stránka"""
    return render_template('index.html', section='services')

@app.route('/sponsors')
def sponsors():
    """Sponzoři stránka"""
    return render_template('index.html', section='sponsors')

@app.route('/contact')
def contact():
    """Kontakt stránka"""
    return render_template('index.html', section='contact')

# ========== API ENDPOINTY ==========
@app.route('/api/contact', methods=['POST'])
def api_contact():
    """API pro kontaktní formulář"""
    try:
        data = request.get_json()
        email = data.get('email')
        message = data.get('message')
        
        # Tady můžeš přidat logiku pro uložení do DB nebo poslání emailu
        print(f"Nová zpráva od {email}: {message}")
        
        # Základní validace
        if not email or not message:
            return jsonify({
                'status': 'error',
                'message': 'Email a zpráva jsou povinné!'
            }), 400
        
        return jsonify({
            'status': 'success',
            'message': 'Zpráva byla úspěšně odeslána! Ozveme se vám co nejdříve.'
        }), 200
        
    except Exception as e:
        print(f"Chyba při odesílání zprávy: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Chyba při odesílání zprávy. Zkuste to prosím později.'
        }), 500

@app.route('/api/membership', methods=['POST'])
def api_membership():
    """API pro registraci členství"""
    try:
        data = request.get_json()
        plan = data.get('plan')
        email = data.get('email')
        
        # Základní validace
        if not plan or not email:
            return jsonify({
                'status': 'error',
                'message': 'Plán a email jsou povinné!'
            }), 400
        
        # Logika pro registraci
        print(f"Nová registrace: {email} - plán {plan}")
        
        # Mapování plánů pro lepší UX
        plan_names = {
            'beginner': 'Začátečník',
            'advanced': 'Pokročilý', 
            'professional': 'Profesionální',
            'hron-personal': 'Hron Gym - Osobní trénink',
            'hron-group': 'Hron Gym - Skupinový trénink',
            'vapas-personal': 'VAPAS Hrušovany - Osobní trénink',
            'vapas-group': 'VAPAS Hrušovany - Skupinový trénink',
            'holzova-group': 'ZŠ Holzova - Skupinový trénink',
            'holzova-family': 'ZŠ Holzova - Rodinný trénink'
        }
        
        plan_name = plan_names.get(plan, plan)
        
        return jsonify({
            'status': 'success',
            'message': f'Registrace do plánu "{plan_name}" byla úspěšná! Brzy vás kontaktujeme.'
        }), 200
        
    except Exception as e:
        print(f"Chyba při registraci: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Chyba při registraci. Zkuste to prosím později.'
        }), 500

# ========== NOVÉ API PRO LOKACE ==========
@app.route('/api/location-inquiry', methods=['POST'])
def api_location_inquiry():
    """API pro dotazy specifické pro lokace"""
    try:
        data = request.get_json()
        location = data.get('location')
        plan_type = data.get('plan_type')
        email = data.get('email')
        message = data.get('message', '')
        
        # Základní validace
        if not location or not plan_type or not email:
            return jsonify({
                'status': 'error',
                'message': 'Lokace, typ plánu a email jsou povinné!'
            }), 400
        
        # Logika pro zpracování dotazu
        print(f"Nový dotaz pro lokaci {location}: {email} - {plan_type}")
        if message:
            print(f"Zpráva: {message}")
        
        # Mapování lokací
        location_names = {
            'hron': 'Hron Gym & Gauny Team Brno',
            'vapas': 'VAPAS Hrušovany',
            'holzova': 'Základní škola Holzova'
        }
        
        location_name = location_names.get(location, location)
        
        return jsonify({
            'status': 'success',
            'message': f'Váš dotaz pro lokaci "{location_name}" byl úspěšně odeslán! Brzy vás kontaktujeme.'
        }), 200
        
    except Exception as e:
        print(f"Chyba při zpracování dotazu: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Chyba při odesílání dotazu. Zkuste to prosím později.'
        }), 500

# ========== STATIC FILES ==========
@app.route('/static/<path:filename>')
def static_files(filename):
    """Obsluha statických souborů"""
    return app.send_static_file(filename)

# ========== ERROR HANDLERS ==========
@app.errorhandler(404)
def not_found_error(error):
    """404 stránka"""
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """500 stránka"""
    return render_template('index.html'), 500

@app.errorhandler(400)
def bad_request_error(error):
    """400 stránka"""
    return jsonify({
        'status': 'error',
        'message': 'Špatný požadavek'
    }), 400

# ========== UTILITY ROUTES ==========
@app.route('/health')
def health_check():
    """Health check pro monitoring"""
    return jsonify({
        'status': 'ok',
        'message': 'Server běží',
        'locations': ['hron', 'hrusovany', 'holzova'],
        'endpoints': {
            'main': '/',
            'foto': '/foto',
            'hron_gym': '/hron.html',
            'vapas': '/hrusovany.html', 
            'holzova': '/holzova.html'
        }
    }), 200

@app.route('/sitemap')
def sitemap():
    """Jednoduchá sitemap pro všechny stránky"""
    pages = [
        {'url': '/', 'name': 'Hlavní stránka'},
        {'url': '/foto', 'name': 'Fotogalerie'},
        {'url': '/hron.html', 'name': 'Hron Gym & Gauny Team Brno'},
        {'url': '/hrusovany.html', 'name': 'VAPAS Hrušovany'},
        {'url': '/holzova.html', 'name': 'Základní škola Holzova'},
    ]
    
    return jsonify({
        'sitemap': pages,
        'total_pages': len(pages)
    }), 200

if __name__ == '__main__':
    # Vytvoření potřebných složek pokud neexistují
    directories = ['templates', 'static', 'static/images', 'static/logos']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Vytvořena složka: {directory}")
    
    print("🥊 Spouštím Sněhulák web server...")
    print("📍 Server poběží na: http://localhost:5000")
    print("🔥 Debug mode: ZAPNUTÝ")
    print("")
    print("📄 Dostupné stránky:")
    print("   • Hlavní: http://localhost:5000")
    print("   • Fotky: http://localhost:5000/foto")
    print("   • Hron Gym: http://localhost:5000/hron.html")
    print("   • VAPAS: http://localhost:5000/hrusovany.html")
    print("   • ZŠ Holzova: http://localhost:5000/holzova.html")
    print("")
    print("🔍 Utility:")
    print("   • Health check: http://localhost:5000/health")
    print("   • Sitemap: http://localhost:5000/sitemap")
    
    # Spuštění aplikace
    app.run(
        host='0.0.0.0',  # Dostupné z venku
        port=5000,       # Port
        debug=True       # Debug mode
    )