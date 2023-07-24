//히든 넘버
// match와 matchAll 차이
// flag g, matchAll g flag가 없다면 TypeError, match g flag가 있다면 모든 것 탐색
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const regex = new RegExp(/[\d]+/, "g");

const solution = () => {
  const N = input[0];
  const str = input[1];
  const arr = str.match(regex);
  if (arr === null) {
    console.log(0);
  } else {
    const result = arr.reduce((acc, cur) => {
      return Number(cur) + acc;
    }, 0);
    console.log(result);
  }
};
solution();
