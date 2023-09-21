import {question} from "readline-sync"


// export function input(texto) {
//     let resposta = question(texto)

//     return resposta
// }

export const input = ((texto) =>  {
    return question(texto)
})

export const getNumber = ((texto) => {
    let n = Number(input(texto))

    while (isNaN(n)) {
        n = Number(input(texto))
    }

    return n
})