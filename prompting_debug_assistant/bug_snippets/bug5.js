function getGrade(score) {
  if (score >= 50) {
    return "E";
  } else if (score >= 70) {
    return "C";
  } else if (score >= 90) {
    return "A";
  }
  return "F";
}

function isPassing(score) {
  // 50 is the minimum passing score
  return score > 50;
}

const scores = [95, 72, 50, 30];

for (const s of scores) {
  console.log(s, getGrade(s), isPassing(s));
}
