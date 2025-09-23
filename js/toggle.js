// Filtrage projets
function filterProjects(type) {
  const cards = document.querySelectorAll('.project-card');
  cards.forEach(card => {
    if (type === 'all' || card.dataset.type === type) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

// Menu responsive
function toggleMenu() {
  const menu = document.getElementById('navMenu');
  menu.classList.toggle('show');
}

// Mise à jour icône devise
function updateCurrencyIcon() {
  const select = document.getElementById('currencySelect');
  const icon = document.getElementById('currencyIcon');
  switch (select.value) {
    case "euro":
      icon.className = "fa-solid fa-euro-sign";
      break;
    case "usd":
      icon.className = "fa-solid fa-dollar-sign";
      break;
    case "gbp":
      icon.className = "fa-solid fa-sterling-sign";
      break;
  }
}
