import { get_number} from "../aux_functions.js"

function q17() {
  const n = get_number("n: ")

  let i = 1,
    s = 0

  while (i <= n) {
    s += 1 / i

    i++
  }

  console.log(`\nS = ${s}`)
}

function q18() {
  const n = get_number("n: ")

  let i = 1,
    s = 0

  while (i < n + 1) {
    s += i / (n - i + 1)

    i++
  }

  console.log(`\nS = ${s}`)
}

function q19() {
  const n = get_number("n: ")

  let s = 0,
    i = 1,
    sinal = 1,
    termo

  while (i <= n) {
    termo = (sinal * i) / (n - i + 1)
    s += termo
    sinal *= -1
    i++
  }

  console.log(`\nS = ${s}`)
}

function q20() {
  const n = get_number("n: ")

  let i = 1,
    s = 0,
    sinal = 1

  while (i <= n) {
    s += (1 / i) * sinal
    sinal *= -1
    i++
  }

  console.log(`\nS = ${s}`)
}

function q21() {
  let i = 1,
    s = 0,
    j = 1

  while (i <= 99) {
    s += i / j

    i++
    j += 2
  }

  console.log(`\nS = ${s}`)
}

function q22() {
  const n = get_number("número de fichas: ")
  let id,
    peso = 0,
    i = 1,
    id_maior = 0,
    peso_maior = 0,
    id_menor = 0,
    peso_menor = Infinity

  while (i <= n) {
    id = get_number("id: ")
    peso = get_number("peso(kg): ")

    if (peso > peso_maior) {
      peso_maior = peso
      id_maior = id
    }

    if (peso < peso_menor) {
      peso_menor = peso
      id_menor = id
    }

    i++
  }

  console.log(
    `\nBoi mais gordo: ID ${id_maior}, peso = ${peso_maior} kg\nBoi mais magro: ID ${id_menor}, peso = ${peso_menor} kg`
  )
}

function q23() {
  const qtd_funcionarios = get_number("Quantidade de funcionários: ")

  let cod,
    hr_trabalhada,
    n_dependentes,
    i = 1

  while (i <= qtd_funcionarios) {
    cod = get_number("código: ")
    hr_trabalhada = get_number("qtd hrs trabalhadas: ")
    n_dependentes = get_number("qtd de dependentes: ")

    const valor_dependentes = 40 * n_dependentes
    const salario_hr = hr_trabalhada * 12
    const salario_bruto = valor_dependentes + salario_hr
    const inss = salario_bruto * (8.5 / 100)
    const ir = salario_bruto * (5 / 100)
    const salario_liquido = salario_bruto - inss - ir

    console.log(`\nSalário Bruto: R$ ${salario_bruto.toFixed(2)}`)
    console.log(`(-) INSS (8,5%): R$ ${inss.toFixed(2)}`)
    console.log(`(-) IR(5%): R$ ${ir.toFixed(2)}`)
    console.log(`Salário Líquido: R$ ${salario_liquido.toFixed(2)}`)
    console.log()

    i++
  }
}

function q24() {
  const qtd_habitantes = get_number("Quantidade de habitantes: ")

  let salario = 0,
    qtd_filhos = 0,
    i = 1,
    total_salarios = 0,
    total_filhos = 0,
    total_menos_que_1000 = 0

  while (i <= qtd_habitantes) {
    salario = get_number("Sálario: ")
    qtd_filhos = get_number("Quantidade de filhos: ")
    console.log()

    if (salario <= 1000) {
      total_menos_que_1000 += salario
    }
    total_salarios += salario
    total_filhos += qtd_filhos

    i++
  }

  const media_salarial = total_salarios / qtd_habitantes
  const media_filhos = total_filhos / qtd_habitantes
  const percentual = qtd_habitantes * (total_menos_que_1000 / 100)

  console.log(
    `\na) média de salário da população: R$ ${media_salarial.toFixed(2)}`
  )
  console.log(`b) média de números de filhos: ${media_filhos}`)
  console.log(
    `c) percentual de pessoas com salário de até R$ 1000: ${percentual}%`
  )
}

function q25() {
  const qtd_eleitores = get_number("Quantidade de eleitores: ")

  let i = 1,
    qtd_votos_1 = 0,
    qtd_votos_2 = 0,
    qtd_votos_3 = 0,
    qtd_votos_nulos = 0,
    qtd_votos_brancos = 0,
    voto

  const candidato1 = 1
  const candidato2 = 2
  const candidato3 = 3
  const voto_nulo = 9
  const voto_branco = 0

  while (i <= qtd_eleitores) {
    voto = pegar_voto_valido("voto: ")

    if (i < qtd_eleitores) {
      console.log("bip\nproxímo voto.")
    } else {
      console.log("bip\nvotação encerrada.")
    }

    if (voto == candidato1) {
      qtd_votos_1++
    } else if (voto == candidato2) {
      qtd_votos_2++
    } else if (voto == candidato3) {
      qtd_votos_3++
    } else if (voto == voto_nulo) {
      qtd_votos_nulos++
    } else if (voto == voto_branco) {
      qtd_votos_brancos++
    }

    i++
  }

  let resultado

  const recebeu_mais_votos = Math.max(qtd_votos_1, qtd_votos_2, qtd_votos_3)

  const empate = qtd_votos_1 === qtd_votos_2 && qtd_votos_2 === qtd_votos_3

  if (empate) {
    resultado = "Empate"
  } else {
    if (recebeu_mais_votos === qtd_votos_1) {
      resultado = "Candidato 1"
    } else if (recebeu_mais_votos === qtd_votos_2) {
      resultado = "Candidato 2"
    } else {
      resultado = "Candidato 3"
    }
  }

  console.log(
    `\na) total de votos para cada candidato:\ncandidato 1 = ${qtd_votos_1} \ncandidato 2 = ${qtd_votos_2}\ncandidato 3 = ${qtd_votos_3}`
  )
  console.log(`\nb) total de votos nulos: ${qtd_votos_nulos}`)
  console.log(`\nc) total de votos em branco: ${qtd_votos_brancos}`)
  console.log(`\nd) vencedor da eleição: ${resultado}`)
}

const pegar_voto_valido = (text) => {
  let voto = get_number(text)
  const opcoes = [1, 2, 3, 9, 0]

  if (!opcoes.includes(voto)) {
    console.log("Opção inválida\nOpções válidas: 1, 2, 3, 9, 0")

    voto = pegar_voto_valido(text)
  }

  return voto
}

q25()
