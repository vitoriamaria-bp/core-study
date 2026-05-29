document.addEventListener("DOMContentLoaded", function() {
    // 1. Fechar Toasts
    setTimeout(function() {
        let toasts = document.querySelectorAll('.alert-toast');
        toasts.forEach(t => { t.style.opacity = '0'; setTimeout(() => t.remove(), 300); });
    }, 4000);

    // 2. Menu Ativo
    const currentPath = window.location.pathname;
    document.querySelectorAll('.sidebar-menu li a').forEach(link => {
        if (currentPath === link.getAttribute('href') || (link.getAttribute('href') !== '/admin' && currentPath.startsWith(link.getAttribute('href')))) {
            link.classList.add('active');
        }
    });

    // 3. Recolher Menu (USANDO CLASSE .mini QUE ESTÁ NO SEU CSS)
    const toggleBtn = document.getElementById('toggle-sidebar');
    const sidebar = document.querySelector('.sidebar');
    const mainWrapper = document.querySelector('.main-wrapper');

    if(toggleBtn && sidebar && mainWrapper) {
        toggleBtn.addEventListener('click', function() {
            sidebar.classList.toggle('mini');
            mainWrapper.classList.toggle('mini');
        });
    }
});

// Máscara
function mascaraTelefone(event) {
    let input = event.target;
    let telefone = input.value.replace(/\D/g, ""); 
    if (telefone.length > 10) telefone = telefone.replace(/^(\d{2})(\d{5})(\d{4}).*/, "($1) $2-$3");
    else if (telefone.length > 5) telefone = telefone.replace(/^(\d{2})(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    else if (telefone.length > 2) telefone = telefone.replace(/^(\d{2})(\d{0,5})/, "($1) $2");
    input.value = telefone;
}