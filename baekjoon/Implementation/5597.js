const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const student = [];
for (let i = 1; i < 31; i += 1) {
  student.push(i.toString());
}
const result = student.reduce((acc, cur) => {
  const hasNumber = input.filter((value) => value === cur);
  if (hasNumber.length !== 0) {
    return acc;
  } else {
    return [...acc, cur];
  }
}, []);
a = Number(result[0]);
b = Number(result[1]);
if (a > b) {
  console.log(b);
  console.log(a);
} else {
  console.log(a);
  console.log(b);
}
