const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().split("\n");
const N = input[0];
const dp = new Array(1001).fill(0);
dp[1] = 1;
dp[2] = 2;

for (let i = 3; i < N + 1; i += 1) {
  dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
}
console.log(dp[N]);
