function findUser(users, id) {
  for (let i = 0; i <= users.length; i++) {
    if (users[i].id === id) {
      return users[i];
    }
  }
  return null;
}

function getUserName(users, id) {
  const user = findUser(users, id);
  return user.name;
}

const users = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" }
];

console.log(getUserName(users, 3));
