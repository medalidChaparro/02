from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ================================
# 🌐 RUTAS PRINCIPALES
# ================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coleccion')
def coleccion():
    selected_category = request.args.get('category', default=None)
    return render_template('categories.html', selected_category=selected_category)

@app.route('/ofertas')
def ofertas():
    category = request.args.get('category')
    return render_template('ofertas.html', selected_category=category)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/cuenta')
def cuenta():
    return render_template('mi-cuenta.html')

# ================================
# 🛒 RUTAS DE COMPRA / USUARIO
# ================================
@app.route('/carrito')
def carrito():
    return render_template('cart.html')

@app.route('/registro')
def registro():
    return render_template('register.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/confirmacion-compra')
def confirmacion_compra():
    return render_template('purchase_confirmation.html')

@app.route('/estado-pedido')
def estado_pedido():
    return render_template('estado-pedido.html')

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')

# ================================
# 💬 RUTA DEL CHATBOT
# ================================
@app.route('/chat')
def chat_page():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message', '')
    bot_response = f"🤖 Bot: Recibí tu mensaje: '{user_message}'"
    return jsonify({'response': bot_response})

# ================================
# 🧪 INICIO DE LA APP
# ================================
if __name__ == '__main__':
    app.run(debug=True)

