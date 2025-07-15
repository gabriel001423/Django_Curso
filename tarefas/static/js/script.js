//funçao que pergunta ao usuario se ele quer mesmo excluir
document.querySelectorAll(".delete-btn").forEach((btn) => {
  btn.addEventListener("click", function (e) {
    e.preventDefault();

    const delLink = this.getAttribute("href");

    if (delLink && confirm("Quer deletar esta Tarefa?")) {
      window.location.href = delLink;
    }
  });
});



//Função para Pesquisar
document.getElementById("search-btn").addEventListener("click", function () {
  document.getElementById("search-form").onsubmit();
});