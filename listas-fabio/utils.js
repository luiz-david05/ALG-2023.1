import { question } from "readline-sync";

const input = (text) => question(text);

const getNumber = (text) => Number(input(text));

const getRandomNumber = () => Math.floor(Math.random() * 999)


export { input, getNumber, getRandomNumber };