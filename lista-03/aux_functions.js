import { question } from "readline-sync"

export const get_number = (texto) => {
  let n = Number(question(texto))

  if (isNaN(n) || n === "") {
    console.log("Digite um número.")

    n = get_number(texto)
  }

  return n
}

export const get_text = (texto) => {
  let input = question(texto)

  if (!isNaN(input)) {
    console.log("Digite um texto sem números.")

    input = get_text(texto)
  }

  return input
}
