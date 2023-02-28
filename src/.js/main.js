import "../css/style.css";
import { ENV } from "./env";
document.querySelector("#app").innerHTML = "<h1>Hello RubyJS</h1>";
console.log(`Token A: ${ENV.VITE_TOKEN_A}`);
console.log(`Token B: ${ENV.TOKEN_B}`)