function abre_fecha_modal_pronuncia(id){
    modal = document.getElementById('card_verso'+ id)
    if (modal.style.display === 'block') {
        modal.style.display = 'none';
    } else {
        modal.style.display = 'block';
    }
}

function abre_fecha_modal_portugues(id){
    modal = document.getElementById('modal_portugues'+ id)
    if (modal.style.display === 'block') {
        modal.style.display = 'none';
    } else {
        modal.style.display = 'block';
    }

}

function verificaResposta() {
    // Obtenha o valor inserido pelo usuário e a resposta correta
    var respostaDoUsuario = document.getElementById("resposta_usuario").value.trim().toLowerCase();
    var respostaCorreta = document.getElementById("resposta_correta").value.trim().toLowerCase();

    // Verifique se a resposta está correta
    if (respostaDoUsuario === respostaCorreta) {
        console.log("Resposta correta!");
    } else {
        console.log("Resposta incorreta!");
    }

    // Evite que o formulário seja enviado e a página recarregada
    return false;
}

