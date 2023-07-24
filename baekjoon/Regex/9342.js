const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const solution = () => {
  const N = parseInt(input[0]);
  const re = new RegExp(/^(A|B|C|D|E|F)?(A)+(F)+(C)+(A|B|C|D|E|F)?$/, "i");

  for (let i = 1; i < N + 1; i += 1) {
    const str = input[i];
    const result = re.test(str);
    result === true ? console.log("Infected!") : console.log("Good");
  }
};
solution();
