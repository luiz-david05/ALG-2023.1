import * as lista1 from  './q1_q46.js'
import * as funcoesUteis from '../../input_utils.js'

const converteMs = function converterMsParaKm() {
    const vMs = funcoesUteis.getNumber("Velocidade m/s: ")

    const vKm = lista1.q1(vMs)

    console.log(`\nVelocidade km/h: ${vKm.toFixed(1)}`)
}

converteMs()

