const assert = require("assert");

const users = [
  { id: 1, name: "Aysel", address: { city: "Baku" } },
  { id: 2, name: "Murad" },
  { id: 3, name: "Leyla", address: { city: "Ganja" } },
];

function findUserById(id) {
  return users.find((u) => u.id === id);
}

function getCity(id) {
  const user = findUserById(id);
  return user?.address?.city?.toUpperCase() ?? "UNKNOWN";
}

function check(id, expected) {
  const actual = getCity(id);
  const status = actual === expected ? "PASS" : "FAIL";
  console.log(`input id=${id} | expected=${expected} | actual=${actual} | ${status}`);
  assert.strictEqual(actual, expected);
}

check(1, "BAKU");
check(2, "UNKNOWN");   // user without address
check(3, "GANJA");
check(4, "UNKNOWN");   // user does not exist
console.log("All tests passed");
