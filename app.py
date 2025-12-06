from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "secret_key_123"

# -----------------------
# إعدادات Gmail
# -----------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'mohammed781262832@gmail.com'
app.config['MAIL_PASSWORD'] = 'nlathaxkqzqqxzjs'

mail = Mail(app)

# -----------------------
# بيانات المشاريع
# -----------------------
projects_data = [
    {
        "id": 1,
        "title": "موقعي الشخصي",
        "short_desc": "موقع شخصي يعرض المشاريع والسيرة الذاتية.",
        "long_desc": "هذا المشروع يوضح خبراتي في تطوير الويب باستخدام Flask وHTML وCSS وJavaScript. يتضمن صفحة رئيسية، صفحة عني، صفحة المشاريع وصفحات تفصيلية لكل مشروع.",
        "image": "project1.jpg"
    },
    {
        "id": 2,
        "title": "تطبيق مهام",
        "short_desc": "تطبيق ويب لإدارة المهام اليومية.",
        "long_desc": "تطبيق ويب لإضافة وحذف وتعديل المهام اليومية باستخدام Python وFlask وقاعدة بيانات SQLite. يتضمن واجهة مستخدم بسيطة وفعالة.",
        "image": "project2.jpg"
    },
    {
        "id": 3,
        "title": "موقع متجر إلكتروني",
        "short_desc": "موقع إلكتروني لبيع المنتجات عبر الإنترنت.",
        "long_desc": "مشروع متجر إلكتروني كامل يشمل عرض المنتجات، سلة التسوق، واجهة الدفع، وصفحات المنتجات التفصيلية. تم تطويره باستخدام Flask وBootstrap وJavaScript.",
        "image": "project3.jpg"
    },
]

# -----------------------
# صفحات الموقع الأساسية
# -----------------------
@app.route('/')
def home():
    return render_template("index.html", active_page="home")

@app.route('/about')
def about():
    return render_template("about.html", active_page="about")

@app.route('/projects')
def projects():
    return render_template("projects.html", projects=projects_data, active_page="projects")
    
@app.route('/project_detail/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects_data if p["id"] == project_id), None)
    if not project:
        return "المشروع غير موجود", 404
    return render_template("project_detail.html", project=project, active_page="projects")

# -----------------------
# صفحة التواصل
# -----------------------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(
            subject="💬 رسالة جديدة من موقعك",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']],
            body=f"""
📩 اسم المرسل: {name}
📧 البريد: {email}

📝 الرسالة:
{message}
            """
        )

        mail.send(msg)
        flash("✔ تم إرسال رسالتك بنجاح وسيتم الرد عليك قريبًا.")
        return redirect(url_for('contact'))

    return render_template("contact.html", active_page="contact")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
