/*
	Adds pagination for citation listing
*/

document.addEventListener("DOMContentLoaded", function () {
  const list = document.getElementById("citations-list");
  if (!list) return;

  const items = Array.from(list.querySelectorAll(".citation-item"));
  const prevBtn = document.getElementById("citations-prev");
  const nextBtn = document.getElementById("citations-next");
  const info = document.getElementById("citations-page-info");

  const perPage = parseInt(list.dataset.citationsPerPage || "10", 10);
  let currentPage = 1;
  const totalPages = Math.ceil(items.length / perPage);

  function renderPage(page) {
    currentPage = page;

    const start = (page - 1) * perPage;
    const end = start + perPage;

    items.forEach((item, index) => {
      item.style.display = index >= start && index < end ? "" : "none";
    });

    if (info) {
      info.textContent = `Page ${currentPage} of ${totalPages}`;
    }
    if (prevBtn) prevBtn.disabled = currentPage === 1;
    if (nextBtn) nextBtn.disabled = currentPage === totalPages;
  }

  if (prevBtn) {
    prevBtn.addEventListener("click", function () {
      if (currentPage > 1) renderPage(currentPage - 1);
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener("click", function () {
      if (currentPage < totalPages) renderPage(currentPage + 1);
    });
  }

  if (items.length > 0) {
    renderPage(1);
  }
});
