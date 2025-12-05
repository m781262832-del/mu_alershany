// ✅ تأثير تحريك بطاقات المشاريع
const projectCards = document.querySelectorAll('.project-card');

projectCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = "scale(1.05)";
        card.style.transition = "0.3s";
        card.style.boxShadow = "4px 4px 15px rgba(0,0,0,0.2)";
    });
    card.addEventListener('mouseleave', () => {
        card.style.transform = "scale(1)";
        card.style.boxShadow = "2px 2px 5px rgba(0,0,0,0.1)";
    });
});


// ✅ لا نمنع التنقل بين الصفحات
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', function() {
        // نترك المتصفح يتصرف طبيعي ✅
    });
});


// ✅ إخفاء رسالة التنبيه بعد 3 ثوانٍ
setTimeout(() => {
    let flash = document.querySelector('.flash');
    if (flash) {
        flash.style.opacity = "0";
        flash.style.transition = "1.5s";
        setTimeout(() => flash.remove(), 1500);
    }
}, 3000);


// ✅ تأثير ضغط الأزرار
const buttons = document.querySelectorAll('button');

buttons.forEach(btn => {
    btn.addEventListener('mousedown', () => {
        btn.style.transform = "scale(0.95)";
    });
    btn.addEventListener('mouseup', () => {
        btn.style.transform = "scale(1)";
    });
});
