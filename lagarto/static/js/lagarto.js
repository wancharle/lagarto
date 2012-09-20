
// transforma um item de menu clicavel para mostrar blocos de conteudos 
// o item do menu (menu_tag) tem que ter um atributo "data-bloco" com valor igual ao do bloco que deve aparecer"/
function menu_com_fade(container_id,menu_tag){
    
    $("#"+container_id + " " + menu_tag).click(function (){
    $("#"+container_id + " " + menu_tag).removeClass("ativo");

            var bloco = $(this).attr("data-bloco");
            var menu = $(this);
            menu.addClass("ativo");
            $("#" + container_id +" div.bloco.ativo").fadeOut(function (){
                $("#" + container_id + " div.bloco.ativo").removeClass('ativo');
                $("#"+bloco).fadeIn();
                $("#"+bloco).addClass("ativo");
            });
        });
}
 
