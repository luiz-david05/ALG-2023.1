import { get_number } from "../aux_functions.js"

function q1() {
  const n = get_number("n: ")

  exibir_numeros_inteiros(n)
}

const exibir_numeros_inteiros = (n) => {
  console.log(`Números inteiros entre 1 e ${n}:`)
  let i = 1

  while (i <= n) {
    console.log(`> ${i}`)
    i++
  }
}

function q2() {
  const n = get_number("n: ")

  console.log(`Números pares entre 1 e ${n}`)
  exibir_numeros_pares(n)
}

const eh_par = (n) => n % 2 === 0

const exibir_numeros_pares = (n) => {
  let i = 1

  while (i <= n) {
    if (eh_par(i)) {
      console.log(`> ${i}`)
    }

    i++
  }
}

function q3() {
  const a0 = get_number("a0: ")
  const limite = get_number("limite: ")
  const r = get_number("razão: ")

  console.log("termos da pa menores que o limite :")
  gerar_pa(a0, limite, r)
}

const gerar_pa = (a0, limite, r) => {
  let i = a0

  while (i < limite) {
    console.log(`> ${i}`)

    i += r
  }
}

function q4() {
  const a0 = get_number("a0: ")
  const limite = get_number("limite: ")
  const r = get_number("razão: ")

  console.log("termos da pg menores que o limite:")
  gerar_pg(a0, limite, r)
}

const gerar_pg = (a0, limite, r) => {
  let i = a0

  while (i < limite) {
    console.log(`> ${i}`)

    i *= r
  }
}

function q5() {
  const n = get_number("n: ")

  const fatorial = calcular_fatorial(n)
  console.log(`${n}! = ${fatorial}`)
}

const calcular_fatorial = (n) => {
  let fatorial = 1,
    i = 1

  while (i < n + 1) {
    fatorial *= i

    i++
  }

  return fatorial
}

function q6() {
  // const n = get_number("n: ")

  console.log("\ntabuada dos números de 1 a 10")
  let j = 1

  while (j <= 10) {
    exibir_tabuada(j)
    console.log()

    j++
  }
}

const exibir_tabuada = (n) => {
  let i = 1

  while (i <= 10) {
    console.log(`${n} x ${i} = ${n * i}`)

    i++
  }
}

function q7() {
  const n = get_number("n: ")

  exibir_numeros_inteiros(n)
  const soma = soma_dos_numeros_inteiros(n)
  console.log(`\nsoma dos números = ${soma}`)
}

const soma_dos_numeros_inteiros = (n) => {
  let i = 1,
    soma = 0

  while (i <= n) {
    i++

    soma += i
  }

  return soma
}

function q8() {
  const n = get_number("n: ")
  const limite_inferior = get_number("limite inferior: ")
  const limite_superior = get_number("limite superior: ")

  exibir_multiplos(n, limite_inferior, limite_superior)
}

const eh_multiplo = (n1, n2) => n1 % n2 === 0

const exibir_multiplos = (n, menor, maior) => {
  let candidato = menor

  console.log(`múltiplos de ${n} entre os limites:`)
  while (candidato <= maior) {
    if (eh_multiplo(candidato, n)) {
      console.log(`> ${candidato}`)
    }

    candidato++
  }
}

function q9() {
  const limite_inferior = get_number("limite inferior: ")
  const limite_superior = get_number("limite superior: ")

  exibir_pares_entre_limites(limite_inferior, limite_superior)

  // questão 10

  exibir_impares_entre_limites(limite_inferior, limite_superior)

  // questão 11

  exibir_primos_entre_limites(limite_inferior, limite_superior)
}

const exibir_pares_entre_limites = (limite_inferior, limite_superior) => {
  let i = limite_inferior

  console.log("Números pares entre os limites:")
  while (i <= limite_superior) {
    if (eh_par(i)) {
      console.log(`> ${i}`)
    }

    i++
  }
}

const exibir_impares_entre_limites = (limite_inferior, limite_superior) => {
  let i = limite_inferior

  console.log("Números impares entre os limites:")
  while (i <= limite_superior) {
    if (!eh_par(i)) {
      console.log(`> ${i}`)
    }

    i++
  }
}

const eh_primo = (n) => {
  if (n <= 1) {
    return false
  }

  let i = 2

  while (i < n) {
    if (eh_multiplo(n, i)) {
      return false
    }

    i++
  }

  return true
}

const exibir_primos_entre_limites = (limite_inferior, limite_superior) => {
  let i = limite_inferior

  console.log("Números primos entre os limites:")
  while (i <= limite_superior) {
    if (eh_primo(i)) {
      console.log(`> ${i}`)
    }

    i++
  }
}

function q12() {
  const qtd_n = get_number("Quantidade de números: ")

  let soma = 0,
    i = 1,
    numero = 0
  while (i <= qtd_n) {
    numero = get_number(`digite o ${i}° número: `)

    soma += numero
    i++
  }

  const media = calcular_media(qtd_n, soma)

  console.log(`\nsoma = ${soma}\nmédia = ${media.toFixed(1)}`)
}

const calcular_media = (qtd, soma) => soma / qtd

function q13() {
  const qtd_n = get_number("Quantidade de números: ")

  let i = 1,
    numero,
    maior = 0

  while (i <= qtd_n) {
    numero = get_number(`digite o ${i}° número: `)

    if (numero > maior) {
      maior = numero
    }

    i++
  }

  console.log(`\nmaior número da lista = ${maior}`)
}

function q14() {
  const n = get_number("n: ")

  let i = 1,
    maior_quadrado

  while (i * i <= n) {
    maior_quadrado = i * i
    i++
  }

  console.log(
    `\nmaior quadrado menor que ${n} = ${maior_quadrado} (quadrado de ${i - 1})`
  )
}

function q15() {
  const n = get_number("n: ")

  let qtd_termos = 0,
    termo = 1,
    i = 2

  console.log(`\n${n} primeiros termos da sequência:`)
  while (qtd_termos < n) {
    console.log(`> ${termo}`)

    termo += i
    i++
    qtd_termos++
  }
}

function q16() {
  const n = get_number("n: ")

  let qtd_termos = 0,
    a = 0,
    b = 1,
    c

  console.log(`${n} primeiros termos da sequência de fibonacci: `)
  while (qtd_termos < n) {
    console.log(`> ${a}`)
    c = a + b

    ;(a = b), (b = c)

    qtd_termos++
  }
}

q16()
