var id_table = ''
var current_page = 1;
var data = []
var id_pagination = ''
var header = ''
var footer = ''
var division_table = 1
var show_div_id = ''
var entite = ''

function openPageFournisseur() {
    window.location.href = "/dashboard/fournisseur";
}

function openPageFournisseurAdd() {
    window.location.href = "/dashboard/add-fournisseur";
}

function openPageFournisseurUpdate(id_fournisseur) {
    window.location.href = "/dashboard/update-fournisseur/" + id_fournisseur;
}

function openPageSalleBloc() {
    window.location.href = "/dashboard/salle-bloc";
}

function openPageSalleBlocAdd() {
    window.location.href = "/dashboard/add-salle-bloc";
}

function openPageSalleUpdate(id_salle) {
    window.location.href = "/dashboard/update-salle/" + id_salle;
}

function openPageBlocUpdate(id_bloc) {
    window.location.href = "/dashboard/update-bloc/" + id_bloc;
}

function openPageMarque() {
    window.location.href = "/dashboard/marque";
}

function openPageMarqueAdd() {
    window.location.href = "/dashboard/add-marque";
}

function openPageMarqueUpdate(id_marque) {
    window.location.href = "/dashboard/update-marque/" + id_marque;
}

function openPageModele() {
    window.location.href = "/dashboard/modele";
}

function openPageModeleAdd() {
    window.location.href = "/dashboard/add-modele";
}

function openPageModeleUpdate(id_modele) {
    window.location.href = "/dashboard/update-modele/" + id_modele;
}

function openPageMagasin() {
    window.location.href = "/dashboard/magasin";
}

function openPageMagasinAdd() {
    window.location.href = "/dashboard/add-magasin";
}

function openPageMagasinUpdate(id_magasin) {
    window.location.href = "/dashboard/update-magasin/" + id_magasin;
}

function openPageHardware() {
    window.location.href = "/dashboard/hardware";
}

function openPageHardwareAdd() {
    window.location.href = "/dashboard/add-hardware";
}

function openPageHardwareUpdate(id_hardware) {
    window.location.href = "/dashboard/update-hardware/" + id_hardware;
}

function openPageIntervention() {
    window.location.href = "/dashboard/intervention";
}

function openPageLocation() {
    window.location.href = "/dashboard/location";
}

function openPageMessage() {
    window.location.href = "/dashboard/message";
}

function openPageUtilisateur() {
    window.location.href = "/dashboard/utilisateur";
}

function openPageUtilisateurAdd() {
    window.location.href = "/dashboard/add-utilisateur";
}

function openPageUtilisateurUpdate(id_utilisateur) {
    window.location.href = "/dashboard/update-utilisateur/" + id_utilisateur;
}

function openPageReclamation() {
    window.location.href = "/dashboard/reclamation";
}

function get_data_ready_load_table(table_id, table_header, table_footer, table_data, table_division_table){
    id_table = table_id;
    header = table_header;
    footer = table_footer;
    data = table_data;
    division_table = table_division_table;
    console.log(table_division_table, division_table)
    load_table();
}

function load_table() {
    console.log(division_table)
    var table = document.getElementById(id_table);
    table.innerHTML = header;
    var start = (current_page - 1) * division_table;
    var end = current_page * division_table;
    var data_page = data.slice(start, end);
    console.log(start, end)
    console.log(data_page)
    for (var i = 0; i < data_page.length; i++) {
        table.innerHTML += data_page[i];
    }
    table.innerHTML += footer;
}

function get_data_ready_pagination(pagination_id, data_length, division_table, table_show_div_id, table_entite){
    id_pagination = pagination_id;
    show_div_id = table_show_div_id;
    entite = table_entite;
    load_table_navigation(data_length, division_table);
}

function load_table_navigation(data_length, division_table) {
    var pagination = document.getElementById(id_pagination);
    pagination.innerHTML = '';
    page_number = Math.ceil(data_length / division_table);
    pagination.innerHTML += `<li class="page-item disabled"><button onclick="previous_page()" class="page-link" aria-label="Previous"><span aria-hidden="true">«</span></button></li>`
    for (var i = 1; i <= page_number; i++) {
        pagination.innerHTML += `<li id="button-pagination-${i}" class="page-item"><button onclick="get_page(${i})" class="page-link">${i}</button></li>`
    }
    pagination.innerHTML += `<li class="page-item"><button class="page-link" onclick="next_page()" aria-label="Next" ><span aria-hidden="true">»</span></button></li>`
    active_pagination(id_pagination, current_page);
}


function next_page() {
    if (current_page < page_number) {
        current_page++;
        load_table();
        active_pagination(id_pagination, current_page);
    }
}

function previous_page() {
    if (current_page > 1) {
        current_page--;
        load_table();
        active_pagination(id_pagination, current_page);
    }
}

function get_page(page) {
    current_page = page;
    load_table();
    active_pagination(id_pagination, current_page);
}

function active_pagination(id_pagination, current_page) {
    var pagination = document.getElementById(id_pagination);
    for (var i = 1; i <= pagination.children.length - 2; i++) {
        pagination.children[i].classList.remove('active');
    }
    pagination.children[current_page].classList.add('active');
    load_arrow_pagination(current_page);
    load_pagination_show_table(current_page);
}

function load_arrow_pagination(current_page) {
    var pagination = document.getElementById(id_pagination);
    if (current_page === 1) {
        pagination.children[0].classList.add('disabled');
        pagination.children[pagination.children.length - 1].classList.remove('disabled');
    } else if (current_page === page_number) {
        pagination.children[pagination.children.length - 1].classList.add('disabled');
        pagination.children[0].classList.remove('disabled');
    } else {
        pagination.children[0].classList.remove('disabled');
        pagination.children[pagination.children.length - 1].classList.remove('disabled');
    }
}

function load_pagination_show_table(current_page) {
    var show_div = document.getElementById(show_div_id);
    var start = (current_page - 1) * division_table + 1;
    var end = current_page * division_table;
    if (end > data.length) {
        end = data.length;
    }
    show_div.innerHTML = `Affichage de ${start} à ${end} sur ${data.length} ${entite}`
}