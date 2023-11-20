import {getNumber, getRandomNumber, input} from '../utils.js'

function q1(vMs) {
    return vMs * 3.6
}

function q2(hr, min) {
    return hr * 60 + min
}

function q3(min) {
    const hr = Math.floor(min / 60)
    const mins = min % 60

    return [hr, mins]
}

function q4(valor, cotacao) {
    return valor * cotacao
}

function q5(n) {
    const elementos = n.split('').map(Number)

    let soma = 0

    return elementos.reduce((acc, cur) => soma + acc + cur)

    // let soma = 0
    // elementos.forEach(element => {
    //     soma += element
    // });

    // return soma
}

function q6(vKm) {
    return vKm / 3.6
}

function q7(numeros) {
    const [n1, n2, n3] = numeros.split(' ').map(Number)

    const soma = n1 + n2
    const diff = n2 - n3

    return [soma, diff]
}

function q8(numeros) {
    const [n1, n2] = numeros.split(' ').map(Number)

    const soma = n1 + n2
    const diff = n1 - n2

    if (diff == 0) {
        return ('Divisão por 0, impossível!')
    }

    return soma / diff
}

function q9(numeros) {
    return numeros.split(' ').reverse()
}

function q10(numeros) {
    const [n1, n2] = numeros.split(' ').map(Number)
    
    if (n2 == 0) {
        return ('Divisão por 0, impossível!')
    }
    
    const quo = n1 / n2
    const resto = n1 % n2

    return [quo, resto]
}

function q11(n) {
    return n.split('').reverse().join('')
}

function q12(valor) {
    return valor *  0.25 + valor
}

function q13(valor) {
    return valor * 0.7 
}

// revisar
function q14(notas, pesos) {
    const [n1, n2, n3] = notas.split(' ').map(Number)
    const [p1, p2, p3] = pesos.split(' ').map(Number)

    return (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)
}

function q15(base, altura) {
    return (base * altura) / 2
}

function q16(lado) {
    return lado * lado
}

function q17(base, altura) {
    return base * altura
}

function q18(raio) {
    return 2 * Math.PI * raio
}

function q19(raio) {
    return (4 * Math.PI * Math.pow(raio, 3)) / 3
}

function q20(celsius) {
    return celsius * 1.8 + 32
}

function q21(fahrenheit) {
    return (fahrenheit - 32) / 1.8
}

function q22(distancia) {
    return km * 1000
}

function q23(peso) {
    return peso * 1000
}

function main() {
    const n = getNumber("numero: ")

    console.log(q13(n))
}

main()