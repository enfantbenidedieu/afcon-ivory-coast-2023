

var team_url_flag = {
    "Ivory Coast"        : "/static/images/FIF_Côte_d'Ivoire_logo.png",
    "Guinea-Bissau"      : "/static/images/Guinea-Bissau_FF_(logo).png",
    "Nigeria"            : "/static/images/Nigeria_national_football_team.png",
    "Equatorial Guinea"  : "/static/images/Equatorial_Guinea_FA.png",
    "Egypt"              : "/static/images/Egypt_national_football_team.png",
    "Mozambique"         : "/static/images/Mozambique_national_football_team.png",
    "Ghana"              : "/static/images/Ghana_FA.png",
    "Cape Verde"         : "/static/images/Cape_Verde_FA_(2020).png",
    "Senegal"            : "/static/images/Senegalese_Football_Federation_logo.svg.png",
    "Gambia"             : "/static/images/Gambia_Football_Federation_(association_football_federation)_logo.png",
    "Cameroon"           : "/static/images/Cameroon_2010crest.png",
    "Guinea"             : "/static/images/Fgf_guinee_logo_shirt.png",
    "Algeria"            : "/static/images/Algerian_NT_(logo).png",
    "Angola"             : "/static/images/Logo_Federaçao_Angolana_de_Futebol.png",
    "Burkina Faso"       : "/static/images/Burkina_Faso_FA.png",
    "Mauritania"         : "/static/images/Mauritania_national_football_team.png",
    "Tunisia"            : "/static/images/Tunisia_national_football_team_logo.png",
    "Namibia"            : "/static/images/Namibia_FA.png",
    "Mali"               : "/static/images/Mali_FF_(New).png",
    "South Africa"       : "/static/images/South_Africa_Flor.png",
    "Morocco"            : "/static/images/Royal_Moroccan_Football_Federation_logo.svg.png",
    "Tanzanie"           : "/static/images/Tanzania_FF_(logo).png",
    "RDC"                : "/static/images/Congo_DR_FA.png",
    "Zambie"             : "/static/images/Zambia_national_footnall_team.png"
  };


var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
    window.dashAgGridComponentFunctions || {});
  
dagcomponentfuncs.TeamLogoRenderer = function (props) {
    var url = team_url_flag[props.value];
    return React.createElement(
      "span",
      null,
      React.createElement("img", { src: url, style: { width: "25px", height: "auto", filter: "brightness(1.1)" } }),
      React.createElement("span", { style: { paddingLeft: "4px" } }, props.value)
    );
  }