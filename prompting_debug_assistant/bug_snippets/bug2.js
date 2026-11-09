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
  return user.address.city.toUpperCase();
}

console.log(getCity(1));
console.log(getCity(2));
console.log(getCity(4));
