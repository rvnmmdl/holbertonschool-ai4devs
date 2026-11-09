const assert = require("assert");

function getGrade(score) {
  if (score >= 90) {
    return "A";
  } else if (score >= 70) {
    return "C";
  } else if (score >= 50) {
    return "E";
  }
  return "F";
}

function isPassing(score) {
  // 50 is the minimum passing score
  return score >= 50;
}

function check(label, expected, actual) {
  const status = expected === actual ? "PASS" : "FAIL";
  console.log(`${label} | expected=${expected} | actual=${actual} | ${status}`);
  assert.strictEqual(actual, expected);
}

const gradeCases = [[95, "A"], [90, "A"], [89, "C"], [72, "C"], [70, "C"], [69, "E"], [50, "E"], [49, "F"], [30, "F"]];
for (const [score, grade] of gradeCases) {
  check(`getGrade(${score})`, grade, getGrade(score));
}
check("isPassing(50)", true, isPassing(50));
check("isPassing(49)", false, isPassing(49));
check("isPassing(95)", true, isPassing(95));
console.log("All tests passed");
