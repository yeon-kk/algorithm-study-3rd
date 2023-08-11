function solution(a, b) {
  const month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  daySum = b;
  for (let i = 1; i < a; i += 1) {
    daySum += month[i];
  }
  const date = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];
  return date[daySum % 7];
}
