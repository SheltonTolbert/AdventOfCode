const fs = require("fs");

function isUppercase(char) {
  return char.toUpperCase() === char;
}

function solve(data) {
  let result = 0;
  data.split("\n").forEach((rucksack) => {
    const set = new Set();
    const duplicate = rucksack.split("").reduce((acc, item, index) => {
      if (index < rucksack.length / 2) {
        set.add(item);
      } else {
        if (set.has(item)) return item;
      }
      return acc;
    }, "");

    result += !!duplicate
      ? duplicate.toLowerCase().charCodeAt(0) -
        96 +
        (isUppercase(duplicate) ? 26 : 0)
      : 0;
  });
  return result;
}

const filename = process.argv[2];
fs.readFile(filename, "utf8", function (err, data) {
  if (err) throw err;
  console.log(solve(data));
});
