
// transforma um item de menu clicavel para mostrar blocos de conteudos 
// o item do menu (menu_tag) tem que ter um atributo "data-bloco" com valor igual ao do bloco que deve aparecer"/
function menu_com_fade(container_id,menu_tag){
    
    $("#"+container_id + " " + menu_tag).click(function (){

        $("#"+container_id + " " + menu_tag).removeClass("ativo");

        var bloco = $(this).attr("data-bloco");
        var menu = $(this);
        menu.addClass("ativo");
        $("#" + container_id +" div.bloco.ativo").hide();
        $("#" + container_id + " div.bloco.ativo").removeClass('ativo');
        $("#"+bloco).fadeIn();
        $("#"+bloco).addClass("ativo");
           
    });
}
 
function menu_com_fade_suites(container_id,menu_tag){
    
    $("#"+container_id + " " + menu_tag).click(function (){

        $("#"+container_id + " " + menu_tag).removeClass("ativo");
        $("#"+container_id + " h2").removeClass("ativo");
        $("#"+container_id + " li").removeClass("ativo");

        if (menu_tag == "li"){
            $(this).parent().prev("h2").addClass("ativo");    
        }
        if (menu_tag =="h2"){

            $(this).next().children().first().addClass("ativo");    
        }
        var bloco = $(this).attr("data-bloco");
        var menu = $(this);
        menu.addClass("ativo");
        $("#" + container_id +" div.bloco.ativo").hide();
        $("#" + container_id + " div.bloco.ativo").removeClass('ativo');
        $("#"+bloco).fadeIn();
        $("#"+bloco).addClass("ativo");
           
    });
}

function parseURLParams(url) {
  var queryStart = url.indexOf("?") + 1;
  var queryEnd   = url.indexOf("#") + 1 || url.length + 1;
  var query      = url.slice(queryStart, queryEnd - 1);

  if (query === url || query === "") return;

  var params  = {};
  var nvPairs = query.replace(/\+/g, " ").split("&");

  for (var i=0; i<nvPairs.length; i++) {
    var nv = nvPairs[i].split("=");
    var n  = decodeURIComponent(nv[0]);
    var v  = decodeURIComponent(nv[1]);
    if ( !(n in params) ) {
      params[n] = [];
    }
    params[n].push(nv.length === 2 ? v : null);
  }
  return params;
}
