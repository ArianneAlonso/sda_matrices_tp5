const alumno = [
    ['juan', [['matematicas', 8], ['lengua', 9], ['sociales', 7], ['naturales', 7]]],
    ['ana', [['lengua', 9], ['matematicas', 10], ['sociales', 8], ['naturales', 6]]],
    ['luis', [['lengua', 6], ['sociales', 8], ['matematicas', 7], ['naturales', 6]]],
    ['maria', [['lengua', 9], ['sociales', 10], ['naturales', 10], ['matematicas', 9]]]
];

function cargarnotas(nombre, materia, nota) {
    for (const persona of alumno) {
        if (persona[0] === nombre) {
            const materias = persona[1];
            let encontrado = false;
            for (const mat of materias) {
                if (mat[0] === materia) {
                    mat[1] = nota;
                    console.log(`nota de ${materia} actualizada a ${nota} para ${nombre}.`);
                    encontrado = true;
                }
            }
            if (!encontrado) {
                materias.push([materia, nota]);
                console.log(`materia ${materia} añadida con nota ${nota} para ${nombre}.`);
            }
            return;
        }
    }
    alumno.push([nombre, [[materia, nota]]]);
    console.log(`alumno ${nombre} añadido con materia ${materia} y nota ${nota}.`);
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function preguntar() {
    rl.question("¿deseas buscar o agregar un alumno? (s/n): ", function(respuesta) {
        if (respuesta.toLowerCase() === 's') {
            rl.question("introduce el nombre del alumno: ", function(nombre) {
                let encontrado = false;
                for (const persona of alumno) {
                    if (persona[0] === nombre) {
                        console.log(`alumno encontrado: ${persona[0]} con calificaciones:`);
                        persona[1].forEach(materia => {
                            console.log(`${materia[0]}: ${materia[1]}`);
                        });
                        encontrado = true;
                        break;
                    }
                }
                if (!encontrado) {
                    console.log(`el alumno ${nombre} no fue encontrado.`);
                    rl.question("introduce la nota de matemáticas: ", function(matematicas) {
                        rl.question("introduce la nota de lengua: ", function(lengua) {
                            rl.question("introduce la nota de sociales: ", function(sociales) {
                                rl.question("introduce la nota de naturales: ", function(naturales) {
                                    cargarnotas(nombre, 'matematicas', parseInt(matematicas));
                                    cargarnotas(nombre, 'lengua', parseInt(lengua));
                                    cargarnotas(nombre, 'sociales', parseInt(sociales));
                                    cargarnotas(nombre, 'naturales', parseInt(naturales));
                                    preguntar();
                                });
                            });
                        });
                    });
                } else {
                    preguntar();
                }
            });
        } else {
            console.log("saliste del programa");
            rl.close();
        }
    });
}

preguntar();
