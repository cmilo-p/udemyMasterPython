var nombre = "Camilo Pinzón"
var altura = 163

/* var concatenacion = nombre + " " + altura;

var datos = document.getElementById("datos"); 
datos.innerHTML = `
    <h1>Caja de datos</h1>
    <h2>Nombre: ${nombre}</h2>
    <h3>Altura: ${altura}cm</h3>
`;

if(altura >= 190) {
    datos.innerHTML += `
        <h1>Eres Alto</h1>
    `
}else  {
    datos.innerHTML += `
        <h1>Eres Bajo</h1>
    `
}

for(var i = 2000; i<=2020; i++) {
    // bloque de instrucciones
    datos.innerHTML += "<p>Estamos en el año: <p>" + i;
} */

function MuestraMiNombre(nombre, altura) {
    var datos = `
        <h1>Caja de datos</h1>
        <h2>Nombre: ${nombre}</h2>
        <h3>Altura: ${altura}cm</h3>
    `;

    return datos;
}

function imprimir() {
    var datos = document.getElementById("datos"); 
    datos.innerHTML = MuestraMiNombre("Camilo Pinzón", 163);
}

imprimir();

var nombres = ['Victor', 'Antonio', 'Joaquin'];

document.write('<h1>Listado de nombres</h1>');
/* for(i = 0; i < nombres.length; i++) {
    document.write(nombres[i] + '<br>');
} */

nombres.forEach((nombre ) => {
    document.write(nombre + '<br>');
})